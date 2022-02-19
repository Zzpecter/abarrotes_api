from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from abarrotes_api_rest.models import PresentacionProducto


class PresentacionProductoResource(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.presentacion_producto = PresentacionProducto()

    def get(self, id_presentacion_producto):
        self.presentacion_producto.id_presentacion_producto = id_presentacion_producto
        presentacion_producto = self.presentacion_producto.seleccionar()
        print(presentacion_producto.json)
        return presentacion_producto

    def put(self, id_presentacion_producto):
        self.presentacion_producto.id_presentacion_producto = id_presentacion_producto
        print(f'put user endpoint; request: {request.json}')

        self.presentacion_producto.id_unidad_presentacion = request.json['id_unidad_presentacion']
        self.presentacion_producto.nombre_presentacion = request.json['nombre_presentacion']
        self.presentacion_producto.usuario_registro = request.json['usuario_registro']

        self.presentacion_producto.actualizar()
        return {"mensaje": "presentacion_producto actualizado correctamente"}

    def delete(self, id_presentacion_producto):
        self.presentacion_producto.id_presentacion_producto = id_presentacion_producto
        self.presentacion_producto.eliminar()

        return {"mensaje": "presentacion_producto eliminado correctamente"}


class PresentacionProductoList(Resource):
    """Creation and get_all
    """

    method_decorators = [jwt_required()]

    def __init__(self):
        self.presentacion_producto = PresentacionProducto()

    def get(self):
        return self.presentacion_producto.listar()

    def post(self):
        print(f'post user endpoint; request: {request.json}')
        self.presentacion_producto.id_unidad_presentacion = request.json['id_unidad_presentacion']
        self.presentacion_producto.nombre_presentacion = request.json['nombre_presentacion']
        self.presentacion_producto.usuario_registro = request.json['usuario_registro']

        self.presentacion_producto.insertar()
        return {"mensaje": "presentacion_producto agregado correctamente"}, 201
