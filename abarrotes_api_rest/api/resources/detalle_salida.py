from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from abarrotes_api_rest.models import DetalleSalida


class DetalleSalidaResource(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.detalle_salida = DetalleSalida()

    def get(self, id_detalle_salida):
        self.detalle_salida.id_detalle_salida = id_detalle_salida
        detalle_salida = self.detalle_salida.seleccionar()
        print(detalle_salida.json)
        return detalle_salida

    def put(self, id_detalle_salida):
        self.detalle_salida.id_detalle_salida = id_detalle_salida
        print(f'put detalle_salida endpoint; request: {request.json}')

        self.detalle_salida.id_salida_producto = request.json['id_salida_producto']
        self.detalle_salida.id_producto = request.json['id_producto']
        self.detalle_salida.cantidad = request.json['cantidad']
        self.detalle_salida.precio_unidad = request.json['precio_unidad']
        self.detalle_salida.usuario_registro = request.json['usuario_registro']

        self.detalle_salida.actualizar()
        return {"mensaje": "detalle_salida actualizado correctamente"}

    def delete(self, id_detalle_salida):
        self.detalle_salida.id_detalle_salida = id_detalle_salida
        self.detalle_salida.eliminar()

        return {"mensaje": "detalle_salida eliminado correctamente"}


class DetalleSalidaList(Resource):
    """Creation and get_all
    """

    method_decorators = [jwt_required()]

    def __init__(self):
        self.detalle_salida = DetalleSalida()

    def get(self):
        return self.detalle_salida.listar()

    def post(self):
        print(f'post detalle_salida endpoint; request: {request.json}')
        self.detalle_salida.id_salida_producto = request.json['id_salida_producto']
        self.detalle_salida.id_producto = request.json['id_producto']
        self.detalle_salida.cantidad = request.json['cantidad']
        self.detalle_salida.precio_unidad = request.json['precio_unidad']
        self.detalle_salida.usuario_registro = request.json['usuario_registro']

        self.detalle_salida.insertar()
        return {"mensaje": "detalle_salida agregado correctamente"}, 201
