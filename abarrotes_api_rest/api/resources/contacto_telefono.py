from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from abarrotes_api_rest.models import ContactoTelefono


class ContactoTelefonoResource(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.contacto_telefono = ContactoTelefono()

    def get(self, id_contacto_telefono):
        self.contacto_telefono.id_contacto_telefono = id_contacto_telefono
        localidad = self.contacto_telefono.seleccionar()
        print(localidad.json)
        return localidad

    def put(self, id_contacto_telefono):
        self.contacto_telefono.id_contacto_telefono = id_contacto_telefono
        print(f'put contactoTelefono endpoint; request: {request.json}')

        self.contacto_telefono.id_contacto = request.json['id_contacto']
        self.contacto_telefono.codigo_pais = request.json['codigo_pais']
        self.contacto_telefono.numero = request.json['numero']
        self.contacto_telefono.usuario_registro = request.json['usuario_registro']

        self.contacto_telefono.actualizar()
        return {"mensaje": "telefono de contacto actualizado correctamente"}

    def delete(self, id_contacto_telefono):
        self.contacto_telefono.id_contacto_telefono = id_contacto_telefono
        self.contacto_telefono.eliminar()

        return {"mensaje": "telefono de contacto eliminado correctamente"}


class ContactoTelefonoList(Resource):
    """Creation and get_all
    """

    method_decorators = [jwt_required()]

    def __init__(self):
        self.contacto_telefono = ContactoTelefono()

    def get(self):
        return self.contacto_telefono.listar()

    def post(self):
        print(f'post endpoint; request: {request.json}')
        self.contacto_telefono.id_contacto = request.json['id_contacto']
        self.contacto_telefono.codigo_pais = request.json['codigo_pais']
        self.contacto_telefono.numero = request.json['numero']
        self.contacto_telefono.usuario_registro = request.json['usuario_registro']

        self.contacto_telefono.insertar()
        return {"mensaje": "telefono de contacto  agregado correctamente"}, 201
