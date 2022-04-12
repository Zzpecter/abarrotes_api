from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from abarrotes_api_rest.models import CustomViews



class ViVentaClienteResource(Resource):
    method_decorators = [jwt_required()]

    def get(self):
        CUSTOM_VIEW = CustomViews()
        return CUSTOM_VIEW.listar_vi_venta_cliente()


class ViCompraProveedorResource(Resource):
    method_decorators = [jwt_required()]

    def get(self):
        CUSTOM_VIEW = CustomViews()
        return CUSTOM_VIEW.listar_vi_compra_proveedor()


class ViDisposicionMotivoResource(Resource):
    method_decorators = [jwt_required()]

    def get(self):
        CUSTOM_VIEW = CustomViews()
        return CUSTOM_VIEW.listar_vi_disposicion_motivo()


class ViProductoEnAlmacenResource(Resource):
    method_decorators = [jwt_required()]

    def get(self):
        CUSTOM_VIEW = CustomViews()
        return CUSTOM_VIEW.listar_vi_producto_en_almacen()


class ViProductoPresentacionUnidadResource(Resource):
    method_decorators = [jwt_required()]

    def get(self):
        CUSTOM_VIEW = CustomViews()
        return CUSTOM_VIEW.listar_vi_producto_presentacion_unidad()


class ViEntidadContactoDireccionResource(Resource):
    method_decorators = [jwt_required()]

    def get(self, id_entidad):
        CUSTOM_VIEW = CustomViews()
        return CUSTOM_VIEW.listar_vi_entidad_contacto_direccion(id_entidad)


class ViEntidadContactoTelefonoResource(Resource):
    method_decorators = [jwt_required()]

    def get(self, id_entidad):
        CUSTOM_VIEW = CustomViews()
        return CUSTOM_VIEW.listar_vi_entidad_contacto_telefono(id_entidad)


class ViEntidadContactoCorreoResource(Resource):
    method_decorators = [jwt_required()]

    def get(self, id_entidad):
        CUSTOM_VIEW = CustomViews()
        return CUSTOM_VIEW.listar_vi_entidad_contacto_correo(id_entidad)
