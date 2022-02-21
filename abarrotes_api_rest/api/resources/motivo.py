from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from abarrotes_api_rest.models import Motivo


class MotivoResource(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.motivo = Motivo()

    def get(self, id_motivo):
        self.motivo.id_motivo = id_motivo
        motivo = self.motivo.seleccionar()
        print(motivo.json)
        return motivo

    def put(self, id_motivo):
        self.motivo.id_motivo = id_motivo
        print(f'put motivo endpoint; request: {request.json}')

        self.motivo.descripcion_motivo = request.json['descripcion_motivo']
        self.motivo.usuario_registro = request.json['usuario_registro']

        self.motivo.actualizar()
        return {"mensaje": "motivo actualizado correctamente"}

    def delete(self, id_motivo):
        self.motivo.id_motivo = id_motivo
        self.motivo.eliminar()

        return {"mensaje": "motivo eliminado correctamente"}


class MotivoList(Resource):
    """Creation and get_all
    """

    method_decorators = [jwt_required()]

    def __init__(self):
        self.motivo = Motivo()

    def get(self):
        return self.motivo.listar()

    def post(self):
        print(f'post motivo endpoint; request: {request.json}')
        self.motivo.descripcion_motivo = request.json['descripcion_motivo']
        self.motivo.usuario_registro = request.json['usuario_registro']

        self.motivo.insertar()
        return {"mensaje": "motivo agregado correctamente"}, 201
