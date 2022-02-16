from flask_restful import Resource
from flask_jwt_extended import jwt_required
from abarrotes_api_rest.models import Departamento


class DepartamentoResource(Resource):
    method_decorators = [jwt_required()]

    def __init__(self):
        self.departamento = Departamento()

    def get(self, id_departamento):
        self.departamento.id_departamento = id_departamento
        departamento = self.departamento.seleccionar()
        print(departamento.json)
        return departamento


class DepartamentoList(Resource):
    """Creation and get_all
    """

    method_decorators = [jwt_required()]

    def __init__(self):
        self.departamento = Departamento()

    def get(self):
        return self.departamento.listar()
