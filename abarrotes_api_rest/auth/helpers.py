"""Various helpers for auth. Mainly about tokens blocklisting

Heavily inspired by
https://github.com/vimalloc/flask-jwt-extended/blob/master/examples/blocklist_database.py
"""
from datetime import datetime
from flask_jwt_extended import decode_token
from abarrotes_api_rest.extensions import db
from abarrotes_api_rest.models.api_tokens import ApiTokens


def add_token_to_database(encoded_token, identity_claim):
    decoded_token = decode_token(encoded_token)

    db_token = ApiTokens(
        jti=decoded_token["jti"],
        tipo_token=decoded_token["type"],
        id_entidad = decoded_token[identity_claim],
        fecha_expiracion= datetime.fromtimestamp(decoded_token["exp"]),
        revocado= False,
    )
    db_token.insertar()


def is_token_revoked(jwt_payload):
    """
    Checks if the given token is revoked or not. Because we are adding all the
    tokens that we create into this database, if the token is not present
    in the database we are going to consider it revoked, as we don't know where
    it was created.
    """
    jti = jwt_payload["jti"]
    try:
        token = TokenBlocklist.query.filter_by(jti=jti).one()
        return token.revoked
    except NoResultFound:
        return True


def revoke_token(token_jti, user):
    """Revokes the given token

    Since we use it only on logout that already require a valid access token,
    if token is not found we raise an exception
    """
    try:
        token = TokenBlocklist.query.filter_by(jti=token_jti, user_id=user).one()
        token.revoked = True
        db.session.commit()
    except NoResultFound:
        raise Exception("Could not find the token {}".format(token_jti))
