from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from abarrotes_api_rest.models import DetalleEntrada


class DetalleEntradaResource(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.detalle_entrada = DetalleEntrada()

    def get(self, id_detalle_entrada):
        self.detalle_entrada.id_detalle_entrada = id_detalle_entrada
        detalle_entrada = self.detalle_entrada.seleccionar()
        print(detalle_entrada.json)
        return detalle_entrada

    def put(self, id_detalle_entrada):
        self.detalle_entrada.id_detalle_entrada = id_detalle_entrada
        print(f'put detalle_entrada endpoint; request: {request.json}')

        self.detalle_entrada.id_compra = request.json['id_compra']
        self.detalle_entrada.id_producto = request.json['id_producto']
        self.detalle_entrada.cantidad = request.json['cantidad']
        self.detalle_entrada.precio_unidad = request.json['precio_unidad']
        self.detalle_entrada.usuario_registro = request.json['usuario_registro']

        self.detalle_entrada.actualizar()
        return {"mensaje": "detalle_entrada actualizado correctamente"}

    def delete(self, id_detalle_entrada):
        self.detalle_entrada.id_detalle_entrada = id_detalle_entrada
        self.detalle_entrada.eliminar()

        return {"mensaje": "detalle_entrada eliminado correctamente"}


class DetalleEntradaByCompra(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.detalle_entrada = DetalleEntrada()

    def get(self, id_compra):
        self.detalle_entrada.id_compra = id_compra
        detalle_entrada = self.detalle_entrada.seleccionar_por_compra()
        print(detalle_entrada.json)
        return detalle_entrada


class DetalleEntradaList(Resource):
    """Creation and get_all
    """

    method_decorators = [jwt_required()]

    def __init__(self):
        self.detalle_entrada = DetalleEntrada()

    def get(self):
        return self.detalle_entrada.listar()

    def post(self):
        print(f'post detalle_entrada endpoint; request: {request.json}')
        self.detalle_entrada.id_compra = request.json['id_compra']
        self.detalle_entrada.id_producto = request.json['id_producto']
        self.detalle_entrada.cantidad = request.json['cantidad']
        self.detalle_entrada.precio_unidad = request.json['precio_unidad']
        self.detalle_entrada.usuario_registro = request.json['usuario_registro']

        self.detalle_entrada.insertar()
        return {"mensaje": "detalle_entrada agregado correctamente"}, 201
