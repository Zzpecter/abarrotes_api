from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from abarrotes_api_rest.models import Localidad


class LocalidadResource(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.localidad = Localidad()

    def get(self, id_localidad):
        self.localidad.id_localidad = id_localidad
        localidad = self.localidad.seleccionar()
        print(localidad.json)
        return localidad

    def put(self, id_localidad):
        self.localidad.id_localidad = id_localidad
        print(f'put user endpoint; request: {request.json}')

        self.localidad.id_departamento = request.json['id_departamento']
        self.localidad.nombre_localidad = request.json['nombre_localidad']
        self.localidad.usuario_registro = request.json['usuario_registro']

        self.localidad.actualizar()
        return {"mensaje": "localidad actualizada correctamente"}

    def delete(self, id_localidad):
        self.localidad.id_localidad = id_localidad
        self.localidad.eliminar()

        return {"mensaje": "localidad eliminada correctamente"}


class LocalidadList(Resource):
    """Creation and get_all
    """

    method_decorators = [jwt_required()]

    def __init__(self):
        self.localidad = Localidad()

    def get(self):
        return self.localidad.listar()

    def post(self):
        print(f'post user endpoint; request: {request.json}')
        self.localidad.id_departamento = request.json['id_departamento']
        self.localidad.nombre_localidad = request.json['nombre_localidad']
        self.localidad.usuario_registro = request.json['usuario_registro']

        self.localidad.insertar()
        return {"mensaje": "localidad agregada correctamente"}, 201
