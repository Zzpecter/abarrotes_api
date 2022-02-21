from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from abarrotes_api_rest.models import Disposicion


class DisposicionResource(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.disposicion = Disposicion()

    def get(self, id_salida_producto):
        self.disposicion.id_salida_producto = id_salida_producto
        disposicion = self.disposicion.seleccionar()
        print(disposicion.json)
        return disposicion

    def put(self, id_salida_producto):
        self.disposicion.id_salida_producto = id_salida_producto
        print(f'put disposicion endpoint; request: {request.json}')

        self.disposicion.id_usuario = request.json['id_usuario']
        self.disposicion.id_motivo = request.json['id_motivo']
        self.disposicion.comentario = request.json['comentario']
        self.disposicion.usuario_registro = request.json['usuario_registro']

        self.disposicion.actualizar()
        return {"mensaje": "disposicion actualizada correctamente"}

    def delete(self, id_salida_producto):
        self.disposicion.id_salida_producto = id_salida_producto
        self.disposicion.eliminar()

        return {"mensaje": "disposicion eliminada correctamente"}


class DisposicionList(Resource):
    """Creation and get_all
    """

    method_decorators = [jwt_required()]

    def __init__(self):
        self.disposicion = Disposicion()

    def get(self):
        return self.disposicion.listar()

    def post(self):
        print(f'post disposicion endpoint; request: {request.json}')
        self.disposicion.id_salida_producto = request.json['id_salida_producto']
        self.disposicion.id_usuario = request.json['id_usuario']
        self.disposicion.id_motivo = request.json['id_motivo']
        self.disposicion.comentario = request.json['comentario']
        self.disposicion.usuario_registro = request.json['usuario_registro']

        self.disposicion.insertar()
        return {"mensaje": "disposicion agregada correctamente"}, 201
