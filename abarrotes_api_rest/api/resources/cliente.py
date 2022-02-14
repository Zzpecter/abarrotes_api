from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from abarrotes_api_rest.models import Cliente


class ClienteResource(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.cliente = Cliente()

    def get(self, id_entidad):
        self.cliente.id_entidad = id_entidad
        cliente = self.cliente.seleccionar()
        print(cliente.json)
        return cliente

    def put(self, id_entidad):
        self.cliente.id_entidad = id_entidad
        print(f'put cliente endpoint; request: {request.json}')

        self.cliente.razon_social = request.json['razon_social']
        self.cliente.nit_ci = request.json['nit_ci']
        self.cliente.usuario_registro = request.json['usuario_registro']

        self.cliente.actualizar()
        return {"mensaje": "cliente actualizado correctamente"}

    def delete(self, id_entidad):
        self.cliente.id_entidad = id_entidad
        self.cliente.eliminar()

        return {"mensaje": "cliente eliminado correctamente"}


class ClienteList(Resource):
    """Creation and get_all
    """

    method_decorators = [jwt_required()]

    def __init__(self):
        self.cliente = Cliente()

    def get(self):
        return self.cliente.listar()

    def post(self):
        print(f'post cliente endpoint; request: {request.json}')
        self.cliente.id_entidad = request.json['id_entidad']
        self.cliente.razon_social = request.json['razon_social']
        self.cliente.nit_ci = request.json['nit_ci']
        self.cliente.usuario_registro = request.json['usuario_registro']

        self.cliente.insertar()
        return {"mensaje": "cliente agregado correctamente"}, 201
