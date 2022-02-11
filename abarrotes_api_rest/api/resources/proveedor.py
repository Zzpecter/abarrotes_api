from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from abarrotes_api_rest.models import Proveedor


class ProveedorResource(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.proveedor = Proveedor()

    def get(self, id_entidad):
        self.proveedor.id_entidad = id_entidad
        proveedor = self.proveedor.seleccionar()
        print(proveedor.json)
        return proveedor

    def put(self, id_entidad):
        self.proveedor.id_entidad = id_entidad
        print(f'put user endpoint; request: {request.json}')

        self.proveedor.nombre = request.json['nombre']
        self.proveedor.usuario_registro = request.json['usuario_registro']

        self.proveedor.actualizar()
        return {"mensaje": "proveedor actualizado correctamente"}, 200

    def delete(self, id_entidad):
        self.proveedor.id_entidad = id_entidad
        self.proveedor.eliminar()

        return {"mensaje": "proveedor eliminado correctamente"}, 204


class ProveedorList(Resource):
    """Creation and get_all
    """

    method_decorators = [jwt_required()]

    def __init__(self):
        self.proveedor = Proveedor()

    def get(self):
        return self.proveedor.listar()

    def post(self):
        print(f'post user endpoint; request: {request.json}')
        self.proveedor.id_entidad = request.json['id_entidad']
        self.proveedor.nombre = request.json['nombre']
        self.proveedor.usuario_registro = request.json['usuario_registro']

        self.proveedor.insertar()
        return {"mensaje": "proveedor agregado correctamente"}, 201
