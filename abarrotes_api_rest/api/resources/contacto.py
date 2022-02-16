from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from abarrotes_api_rest.models import Contacto


class ContactoResource(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.contacto = Contacto()

    def get(self, id_contacto):
        self.contacto.id_contacto = id_contacto
        contacto = self.contacto.seleccionar()
        print(contacto.json)
        return contacto

    def delete(self, id_contacto):
        self.contacto.id_contacto = id_contacto
        self.contacto.eliminar()

        return {"mensaje": "contacto eliminado correctamente"}


class ContactoList(Resource):
    """Creation and get_all
    """

    method_decorators = [jwt_required()]

    def __init__(self):
        self.contacto = Contacto()

    def get(self):
        return self.contacto.listar()

    def post(self):
        print(f'post user endpoint; request: {request.json}')
        self.contacto.id_entidad = request.json['id_entidad']
        self.contacto.usuario_registro = request.json['usuario_registro']

        self.contacto.insertar()
        return {"mensaje": "contacto agregado correctamente"}, 201
