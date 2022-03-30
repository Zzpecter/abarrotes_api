from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from abarrotes_api_rest.models import ProductoAlmacen


class ProductoAlmacenResource(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.producto_almacen = ProductoAlmacen()

    def get(self, id_producto_almacen):
        self.producto_almacen.id_producto_almacen = id_producto_almacen
        producto_almacen = self.producto_almacen.seleccionar()
        print(producto_almacen.json)
        return producto_almacen

    def put(self, id_producto_almacen):
        self.producto_almacen.id_producto_almacen = id_producto_almacen
        print(f'put producto_almacen endpoint; request: {request.json}')

        self.producto_almacen.id_almacen = request.json['id_almacen']
        self.producto_almacen.id_producto = request.json['id_producto']
        self.producto_almacen.stock_actual = request.json['stock_actual']
        self.producto_almacen.usuario_registro = request.json['usuario_registro']

        self.producto_almacen.actualizar()
        return {"mensaje": "producto_almacen actualizado correctamente"}

    def delete(self, id_producto_almacen):
        self.producto_almacen.id_producto_almacen = id_producto_almacen
        self.producto_almacen.eliminar()

        return {"mensaje": "producto_almacen eliminado correctamente"}


class ProductoAlmacenList(Resource):
    """Creation and get_all
    """

    method_decorators = [jwt_required()]

    def __init__(self):
        self.producto_almacen = ProductoAlmacen()

    def get(self):
        return self.producto_almacen.listar()

    def post(self):
        print(f'post producto_almacen endpoint; request: {request.json}')
        self.producto_almacen.id_almacen = request.json['id_almacen']
        self.producto_almacen.id_producto = request.json['id_producto']
        self.producto_almacen.stock_actual = request.json['stock_actual']
        self.producto_almacen.usuario_registro = request.json['usuario_registro']

        self.producto_almacen.insertar()
        return {"mensaje": "producto_almacen agregado correctamente"}, 201


class ProductoAlmacenResourceProducto(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.producto_almacen = ProductoAlmacen()

    def get(self, id_producto):
        self.producto_almacen.id_producto = id_producto
        producto_almacen = self.producto_almacen.seleccionar_por_producto()
        print(producto_almacen.json)
        return producto_almacen


class ProductoAlmacenResourceAlmacen(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.producto_almacen = ProductoAlmacen()

    def get(self, id_almacen):
        self.producto_almacen.id_almacen = id_almacen
        producto_almacen = self.producto_almacen.seleccionar_por_almacen()
        print(producto_almacen.json)
        return producto_almacen