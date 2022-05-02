from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from abarrotes_api_rest.models import Producto


class ProductoResource(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.producto = Producto()

    def get(self, id_producto):
        self.producto.id_producto = id_producto
        producto = self.producto.seleccionar()
        print(producto.json)
        return producto

    def put(self, id_producto):
        self.producto.id_producto = id_producto
        print(f'put producto endpoint; request: {request.json}')

        self.producto.id_presentacion_producto = request.json['id_presentacion_producto']
        self.producto.nombre = request.json['nombre']
        self.producto.codigo = request.json['codigo']
        self.producto.precio_compra = request.json['precio_compra']
        self.producto.precio_venta = request.json['precio_venta']
        self.producto.usuario_registro = request.json['usuario_registro']

        self.producto.actualizar()
        return {"mensaje": "producto actualizado correctamente"}

    def delete(self, id_producto):
        self.producto.id_producto = id_producto
        self.producto.eliminar()

        return {"mensaje": "producto eliminado correctamente"}


class ProductoList(Resource):
    """Creation and get_all
    """

    method_decorators = [jwt_required()]

    def __init__(self):
        self.producto = Producto()

    def get(self):
        return self.producto.listar()

    def post(self):
        print(f'post producto endpoint; request: {request.json}')
        self.producto.id_presentacion_producto = request.json['id_presentacion_producto']
        self.producto.nombre = request.json['nombre']
        self.producto.codigo = request.json['codigo']
        self.producto.precio_compra = request.json['precio_compra']
        self.producto.precio_venta = request.json['precio_venta']
        self.producto.usuario_registro = request.json['usuario_registro']

        id_producto = self.producto.insertar()
        return {"id_producto": id_producto}


class ProductoBusqueda(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.producto = Producto()

    def get(self, query):
        producto = self.producto.buscar(query)
        print(producto.json)
        return self.producto.buscar(query)
