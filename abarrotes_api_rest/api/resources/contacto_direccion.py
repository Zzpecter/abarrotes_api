from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from abarrotes_api_rest.models import ContactoDireccion


class ContactoDireccionResource(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.contacto_direccion = ContactoDireccion()

    def get(self, id_contacto_direccion):
        self.contacto_direccion.id_contacto_direccion = id_contacto_direccion
        contacto = self.contacto_direccion.seleccionar()
        print(contacto.json)
        return contacto

    def put(self, id_contacto_direccion):
        self.contacto_direccion.id_contacto_direccion = id_contacto_direccion
        print(f'put contactoDireccion endpoint; request: {request.json}')
        self.contacto_direccion.id_contacto = request.json['id_contacto']
        self.contacto_direccion.id_localidad = request.json['id_localidad']
        self.contacto_direccion.calle = request.json['calle']
        self.contacto_direccion.numero_casa = request.json['numero_casa']
        self.contacto_direccion.zona = request.json['zona']
        self.contacto_direccion.detalles = request.json['detalles']
        self.contacto_direccion.usuario_registro = request.json['usuario_registro']

        self.contacto_direccion.actualizar()
        return {"mensaje": "direccion de contacto actualizado correctamente"}

    def delete(self, id_contacto_direccion):
        self.contacto_direccion.id_contacto_direccion = id_contacto_direccion
        self.contacto_direccion.eliminar()

        return {"mensaje": "direccion de contacto eliminado correctamente"}


class ContactoDireccionList(Resource):
    """Creation and get_all
    """

    method_decorators = [jwt_required()]

    def __init__(self):
        self.contacto_direccion = ContactoDireccion()

    def get(self):
        return self.contacto_direccion.listar()

    def post(self):
        print(f'post endpoint; request: {request.json}')
        self.contacto_direccion.id_contacto = request.json['id_contacto']
        self.contacto_direccion.id_localidad = request.json['id_localidad']
        self.contacto_direccion.calle = request.json['calle']
        self.contacto_direccion.numero_casa = request.json['numero_casa']
        self.contacto_direccion.zona = request.json['zona']
        self.contacto_direccion.detalles = request.json['detalles']
        self.contacto_direccion.usuario_registro = request.json['usuario_registro']
        self.contacto_direccion.insertar()
        return {"mensaje": "direccion de contacto  agregado correctamente"}, 201
