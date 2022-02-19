from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from abarrotes_api_rest.models import UnidadPresentacion


class UnidadPresentacionResource(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.unidad_presentacion = UnidadPresentacion()

    def get(self, id_unidad_presentacion):
        self.unidad_presentacion.id_unidad_presentacion = id_unidad_presentacion
        unidad_presentacion = self.unidad_presentacion.seleccionar()
        print(unidad_presentacion.json)
        return unidad_presentacion

    def put(self, id_unidad_presentacion):
        self.unidad_presentacion.id_unidad_presentacion = id_unidad_presentacion
        print(f'put unidad_presentacion endpoint; request: {request.json}')

        self.unidad_presentacion.nombre_medida = request.json['nombre_medida']
        self.unidad_presentacion.multiplicador_kg = request.json['multiplicador_kg']
        self.unidad_presentacion.usuario_registro = request.json['usuario_registro']

        self.unidad_presentacion.actualizar()
        return {"mensaje": "unidad_presentacion actualizada correctamente"}

    def delete(self, id_unidad_presentacion):
        self.unidad_presentacion.id_unidad_presentacion = id_unidad_presentacion
        self.unidad_presentacion.eliminar()

        return {"mensaje": "unidad_presentacion eliminada correctamente"}


class UnidadPresentacionList(Resource):
    """Creation and get_all
    """

    method_decorators = [jwt_required()]

    def __init__(self):
        self.unidad_presentacion = UnidadPresentacion()

    def get(self):
        return self.unidad_presentacion.listar()

    def post(self):
        print(f'post unidad_presentacion endpoint; request: {request.json}')
        self.unidad_presentacion.nombre_medida = request.json['nombre_medida']
        self.unidad_presentacion.multiplicador_kg = request.json['multiplicador_kg']
        self.unidad_presentacion.usuario_registro = request.json['usuario_registro']

        self.unidad_presentacion.insertar()
        return {"mensaje": "unidad_presentacion agregada correctamente"}, 201
