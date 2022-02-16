from flask import Blueprint, current_app, jsonify
from flask_restful import Api
from abarrotes_api_rest.api.resources import UserResource, UserList, ProveedorResource, ProveedorList,ClienteResource, \
    ClienteList, LocalidadResource, LocalidadList, DepartamentoResource, DepartamentoList


blueprint = Blueprint("api", __name__, url_prefix="/api/v1")
api = Api(blueprint)


api.add_resource(UserResource, "/users/<int:id_entidad>", endpoint="user_by_id")
api.add_resource(UserList, "/users", endpoint="users")
api.add_resource(ProveedorResource, "/proveedores/<int:id_entidad>", endpoint="proveedor_by_id")
api.add_resource(ProveedorList, "/proveedores", endpoint="proveedores")
api.add_resource(ClienteResource, "/clientes/<int:id_entidad>", endpoint="cliente_by_id")
api.add_resource(ClienteList, "/clientes", endpoint="clientes")
api.add_resource(LocalidadResource, "/localidades/<int:id_localidad>", endpoint="localidad_by_id")
api.add_resource(LocalidadList, "/localidades", endpoint="localidades")
api.add_resource(DepartamentoResource, "/departamentos/<int:id_departamento>", endpoint="departamento_by_id")
api.add_resource(DepartamentoList, "/departamentos", endpoint="departamentos")


