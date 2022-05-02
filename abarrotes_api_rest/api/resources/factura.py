from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from abarrotes_api_rest.models import Factura


class FacturaResource(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.factura = Factura()

    def get(self, id_factura):
        self.factura.id_factura = id_factura
        factura = self.factura.seleccionar()
        return factura

    def put(self, id_factura):
        self.factura.id_factura = id_factura
        print(f'put factura endpoint; request: {request.json}')

        self.factura.codigo_control = request.json['codigo_control']
        self.factura.datos_codigo_QR = request.json['datos_codigo_QR']
        self.factura.usuario_registro = request.json['usuario_registro']

        self.factura.actualizar()
        return {"mensaje": "factura actualizada correctamente"}

    def delete(self, id_factura):
        self.factura.id_factura = id_factura
        self.factura.eliminar()

        return {"mensaje": "factura eliminada correctamente"}


class FacturaList(Resource):
    """Creation and get_all
    """

    method_decorators = [jwt_required()]

    def __init__(self):
        self.factura = Factura()

    def get(self):
        return self.factura.listar()

    def post(self):
        print(f'post factura endpoint; request: {request.json}')
        self.factura.codigo_control = request.json['codigo_control']
        self.factura.datos_codigo_QR = request.json['datos_codigo_QR']
        self.factura.usuario_registro = request.json['usuario_registro']

        id_factura = self.factura.insertar()
        return {"id_factura": id_factura}
