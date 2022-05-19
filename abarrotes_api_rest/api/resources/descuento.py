from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from abarrotes_api_rest.models import Descuento


class DescuentoResource(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.descuento = Descuento()

    def get(self, id_descuento):
        self.descuento.id_descuento = id_descuento
        descuento = self.descuento.seleccionar()
        print(descuento.json)
        return descuento

    def put(self, id_descuento):
        self.descuento.id_descuento = id_descuento
        print(f'put descuento endpoint; request: {request.json}')

        self.descuento.id_producto = request.json['id_producto']
        self.descuento.precio_oferta = request.json['precio_oferta']
        self.descuento.fecha_expiracion = request.json['fecha_expiracion']
        self.descuento.usuario_registro = request.json['usuario_registro']

        self.descuento.actualizar()
        return {"mensaje": "descuento actualizado correctamente"}

    def delete(self, id_descuento):
        self.descuento.id_descuento = id_descuento
        self.descuento.eliminar()

        return {"mensaje": "descuento eliminado correctamente"}


class DescuentoByProducto(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.descuento = Descuento()

    def get(self, id_producto):
        self.descuento.id_producto = id_producto
        descuento = self.descuento.seleccionar_por_producto()
        print(descuento.json)
        return descuento


class DescuentoList(Resource):
    """Creation and get_all
    """

    method_decorators = [jwt_required()]

    def __init__(self):
        self.descuento = Descuento()

    def get(self):
        return self.descuento.listar()

    def post(self):
        print(f'post descuento endpoint; request: {request.json}')
        self.descuento.id_producto = request.json['id_producto']
        self.descuento.precio_oferta = request.json['precio_oferta']
        self.descuento.fecha_expiracion = request.json['fecha_expiracion']
        self.descuento.usuario_registro = request.json['usuario_registro']

        id_descuento = self.descuento.insertar()
        return {"id_descuento": id_descuento}
