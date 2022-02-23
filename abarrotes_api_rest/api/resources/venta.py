from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from abarrotes_api_rest.models import Venta


class VentaResource(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.venta = Venta()

    def get(self, id_salida_producto):
        self.venta.id_salida_producto = id_salida_producto
        venta = self.venta.seleccionar()
        return venta

    def put(self, id_salida_producto):
        self.venta.id_salida_producto = id_salida_producto
        print(f'put venta endpoint; request: {request.json}')

        self.venta.id_usuario = request.json['id_usuario']
        self.venta.id_cliente = request.json['id_cliente']
        self.venta.id_factura = request.json['id_factura']
        self.venta.fecha = request.json['fecha']
        self.venta.monto_total = request.json['monto_total']
        self.venta.usuario_registro = request.json['usuario_registro']

        self.venta.actualizar()
        return {"mensaje": "venta actualizada correctamente"}

    def delete(self, id_salida_producto):
        self.venta.id_salida_producto = id_salida_producto
        self.venta.eliminar()

        return {"mensaje": "venta eliminada correctamente"}


class VentaList(Resource):
    """Creation and get_all
    """

    method_decorators = [jwt_required()]

    def __init__(self):
        self.venta = Venta()

    def get(self):
        return self.venta.listar()

    def post(self):
        print(f'post venta endpoint; request: {request.json}')
        self.venta.id_salida_producto = request.json['id_salida_producto']
        self.venta.id_usuario = request.json['id_usuario']
        self.venta.id_cliente = request.json['id_cliente']
        self.venta.id_factura = request.json['id_factura']
        self.venta.fecha = request.json['fecha']
        self.venta.monto_total = request.json['monto_total']
        self.venta.usuario_registro = request.json['usuario_registro']

        self.venta.insertar()
        return {"mensaje": "venta agregada correctamente"}, 201
