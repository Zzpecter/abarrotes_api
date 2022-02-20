from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from abarrotes_api_rest.models import Almacen


class AlmacenResource(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.almacen = Almacen()

    def get(self, id_almacen):
        self.almacen.id_almacen = id_almacen
        almacen = self.almacen.seleccionar()
        print(almacen.json)
        return almacen

    def put(self, id_almacen):
        self.almacen.id_almacen = id_almacen
        print(f'put almacen endpoint; request: {request.json}')

        self.almacen.descripcion = request.json['descripcion']
        self.almacen.usuario_registro = request.json['usuario_registro']

        self.almacen.actualizar()
        return {"mensaje": "almacen actualizado correctamente"}

    def delete(self, id_almacen):
        self.almacen.id_almacen = id_almacen
        self.almacen.eliminar()

        return {"mensaje": "almacen eliminado correctamente"}


class AlmacenList(Resource):
    """Creation and get_all
    """

    method_decorators = [jwt_required()]

    def __init__(self):
        self.almacen = Almacen()

    def get(self):
        return self.almacen.listar()

    def post(self):
        print(f'post almacen endpoint; request: {request.json}')
        self.almacen.descripcion = request.json['descripcion']
        self.almacen.usuario_registro = request.json['usuario_registro']

        self.almacen.insertar()
        return {"mensaje": "almacen agregado correctamente"}, 201
