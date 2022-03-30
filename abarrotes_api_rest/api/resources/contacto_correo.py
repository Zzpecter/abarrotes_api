from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from abarrotes_api_rest.models import ContactoCorreo


class ContactoCorreoResource(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.contacto_correo = ContactoCorreo()

    def get(self, id_contacto_correo):
        self.contacto_correo.id_contacto_correo = id_contacto_correo
        contacto_correo = self.contacto_correo.seleccionar()
        print(contacto_correo.json)
        return contacto_correo

    def put(self, id_contacto_correo):
        self.contacto_correo.id_contacto_correo = id_contacto_correo
        print(f'put user endpoint; request: {request.json}')

        self.contacto_correo.id_contacto = request.json['id_contacto']
        self.contacto_correo.correo = request.json['correo']
        self.contacto_correo.usuario_registro = request.json['usuario_registro']

        self.contacto_correo.actualizar()
        return {"mensaje": "correo de contacto actualizado correctamente"}

    def delete(self, id_contacto_correo):
        self.contacto_correo.id_contacto_correo = id_contacto_correo
        self.contacto_correo.eliminar()

        return {"mensaje": "correo de contacto eliminado correctamente"}


class ContactoCorreoList(Resource):
    """Creation and get_all
    """

    method_decorators = [jwt_required()]

    def __init__(self):
        self.contacto_correo = ContactoCorreo()

    def get(self):
        return self.contacto_correo.listar()

    def post(self):
        print(f'post endpoint; request: {request.json}')
        self.contacto_correo.id_contacto = request.json['id_contacto']
        self.contacto_correo.correo = request.json['correo']
        self.contacto_correo.usuario_registro = request.json['usuario_registro']

        self.contacto_correo.insertar()
        return {"mensaje": "correo de contacto  agregado correctamente"}, 201


class ContactoCorreoByContactoResource(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.contacto_correo = ContactoCorreo()

    def get(self, id_contacto):
        self.contacto_correo.id_contacto = id_contacto
        contacto_correo = self.contacto_correo.listar_por_contacto()
        print(contacto_correo.json)
        return contacto_correo