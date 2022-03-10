from flask_restful import Resource
from flask_jwt_extended import jwt_required
from abarrotes_api_rest.models import Nivel


class NivelResource(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.nivel = Nivel()

    def get(self, id_nivel):
        self.nivel.id_nivel = id_nivel
        nivel = self.nivel.seleccionar()
        print(nivel.json)
        return nivel


class NivelList(Resource):
    """Creation and get_all
    """
    method_decorators = [jwt_required()]

    def __init__(self):
        self.nivel = Nivel()

    def get(self):
        return self.nivel.listar()

