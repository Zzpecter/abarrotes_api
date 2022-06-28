from flask_restful import Resource
from flask_jwt_extended import jwt_required
from abarrotes_api_rest.models import CustomViews
import pandas as pd
import abarrotes_api_rest.helpers as helpers
import abarrotes_api_rest.models.pdf_ventas as PDF


class ViVentaClienteResource(Resource):
    method_decorators = [jwt_required()]

    def get(self):
        CUSTOM_VIEW = CustomViews()
        return CUSTOM_VIEW.listar_vi_venta_cliente()

class ViVentaClienteById(Resource):
    method_decorators = [jwt_required()]

    def get(self, id_venta):
        CUSTOM_VIEW = CustomViews()
        return CUSTOM_VIEW.seleccionar_vi_venta_cliente(id_venta)

class ViVentaClientePorFechaResource(Resource):
    method_decorators = [jwt_required()]

    def get(self, desde, hasta):
        CUSTOM_VIEW = CustomViews()
        return CUSTOM_VIEW.listar_vi_venta_cliente_por_fecha(desde, hasta)


class ViVentaClientePorClienteResource(Resource):
    method_decorators = [jwt_required()]

    def get(self, query):
        CUSTOM_VIEW = CustomViews()
        return CUSTOM_VIEW.listar_vi_venta_cliente_por_cliente(query)


class ViCompraProveedorResource(Resource):
    method_decorators = [jwt_required()]

    def get(self):
        CUSTOM_VIEW = CustomViews()
        return CUSTOM_VIEW.listar_vi_compra_proveedor()


class ViCompraProveedorById(Resource):
    method_decorators = [jwt_required()]

    def get(self, id_compra):
        CUSTOM_VIEW = CustomViews()
        return CUSTOM_VIEW.seleccionar_vi_compra_proveedor(id_compra)


class ViCompraProveedorPorFechaResource(Resource):
    method_decorators = [jwt_required()]

    def get(self, desde, hasta):
        CUSTOM_VIEW = CustomViews()
        return CUSTOM_VIEW.listar_vi_compra_proveedor_por_fecha(desde, hasta)


class ViCompraProveedorPorProveedorResource(Resource):
    method_decorators = [jwt_required()]

    def get(self, query):
        CUSTOM_VIEW = CustomViews()
        return CUSTOM_VIEW.listar_vi_compra_proveedor_por_proveedor(query)

class ViDisposicionMotivoResource(Resource):
    method_decorators = [jwt_required()]

    def get(self):
        CUSTOM_VIEW = CustomViews()
        return CUSTOM_VIEW.listar_vi_disposicion_motivo()


class ViProductoEnAlmacenList(Resource):
    method_decorators = [jwt_required()]

    def get(self):
        CUSTOM_VIEW = CustomViews()
        return CUSTOM_VIEW.listar_vi_producto_en_almacen()

class ViProductoEnAlmacenResource(Resource):
    method_decorators = [jwt_required()]

    def get(self, id_producto):
        CUSTOM_VIEW = CustomViews()
        return CUSTOM_VIEW.seleccionar_vi_producto_en_almacen(id_producto)

class ViProductoEnAlmacenBuscar(Resource):
    method_decorators = [jwt_required()]

    def get(self, query):
        CUSTOM_VIEW = CustomViews()
        return CUSTOM_VIEW.buscar_vi_producto_en_almacen(query)

class ViProductoPresentacionUnidadList(Resource):
    method_decorators = [jwt_required()]

    def get(self):
        CUSTOM_VIEW = CustomViews()
        return CUSTOM_VIEW.listar_vi_producto_presentacion_unidad()


class ViProductoPresentacionUnidadResource(Resource):
    method_decorators = [jwt_required()]

    def get(self, id_producto):
        CUSTOM_VIEW = CustomViews()
        return CUSTOM_VIEW.seleccionar_vi_producto_presentacion_unidad(id_producto)


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


class ViDisposicionUsuarioMotivo(Resource):
    method_decorators = [jwt_required()]

    def get(self):
        CUSTOM_VIEW = CustomViews()
        return CUSTOM_VIEW.listar_vi_disposicion_usuario_motivo()


class ViReporteVentasSinProducto(Resource):
    method_decorators = [jwt_required()]

    def get(self, fecha_desde, fecha_hasta):
        CUSTOM_VIEW = CustomViews()
        returned_json = CUSTOM_VIEW.listar_reporte_ventas_sin_producto(fecha_desde, fecha_hasta)
        # TODO: agregar logica para generar pdf
        # 1. cargar los datos devueltos en un pandas dataframe
        print(f'json: {returned_json.json}')
        df_ventas = pd.json_normalize(returned_json.json)
        print(f'pandas json: {df_ventas}')
        print(df_ventas)

        # 2. generar plot
        # helpers.plot(df_ventas, "nombre_archivo")

        # 3. generar el pdf
        pdf = PDF.PDF_Ventas()

        pdf.print_page(df_ventas)

        pdf.output('SalesRepot.pdf', 'F')
        return 200


class ViReporteVentasConProducto(Resource):
    method_decorators = [jwt_required()]

    def get(self, fecha_desde, fecha_hasta, id_producto):
        CUSTOM_VIEW = CustomViews()
        return CUSTOM_VIEW.listar_reporte_ventas_con_producto(fecha_desde, fecha_hasta, id_producto)
