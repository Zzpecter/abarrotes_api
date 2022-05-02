from flask_restful import Resource
from flask_jwt_extended import jwt_required
from abarrotes_api_rest.models import SalidaProducto


class SalidaProductoResource(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.salida_producto = SalidaProducto()

    def delete(self, id_salida_producto):
        self.salida_producto.id_salida_producto = id_salida_producto
        self.salida_producto.eliminar()

        return {"mensaje": "salida_producto eliminada correctamente"}


class SalidaProductoList(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.salida_producto = SalidaProducto()

    def post(self):
        id_salida_producto = self.salida_producto.insertar()
        return {"id_salida_producto": id_salida_producto}
