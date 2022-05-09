from flask import Blueprint, current_app, jsonify
from flask_restful import Api
from abarrotes_api_rest.api.resources import UserResource, UserList, ProveedorResource, ProveedorList,ClienteResource, \
    ClienteList, LocalidadResource, LocalidadList, DepartamentoResource, DepartamentoList, ContactoResource, \
    ContactoList, ContactoCorreoResource, ContactoCorreoList, ContactoTelefonoResource, ContactoTelefonoList, \
    ContactoDireccionList, ContactoDireccionResource, UnidadPresentacionList, UnidadPresentacionResource, \
    PresentacionProductoResource, PresentacionProductoList, ProductoResource, ProductoList, AlmacenResource, \
    AlmacenList, ProductoAlmacenList, ProductoAlmacenResource, DisposicionList, DisposicionResource, MotivoResource, \
    MotivoList, VentaList, VentaResource, DetalleSalidaResource, DetalleSalidaList, DetalleEntradaList, \
    DetalleEntradaResource, CompraResource, CompraList, FacturaResource, FacturaList, NivelResource, NivelList, \
    UsuarioNivelView, ContactoUnified, EntidadResource, EntidadList, ViDisposicionMotivoResource, \
    ViProductoEnAlmacenResource, ViProductoPresentacionUnidadList, ViCompraProveedorResource, ViVentaClienteResource, \
    ProductoAlmacenResourceProducto, ProductoAlmacenResourceAlmacen, ProductoBusqueda, ContactoCorreoByContactoResource, \
    ContactoDireccionByContactoResource, ContactoTelefonoByContactoResource, LocalidadPorDepartamentoResource, \
    ViEntidadContactoTelefonoResource, ViEntidadContactoCorreoResource, ViEntidadContactoDireccionResource, \
    ViProductoPresentacionUnidadResource, ClienteNit, ViProductoEnAlmacenBuscar, ViProductoEnAlmacenList, Status, \
    UserByLogin, SalidaProductoList, SalidaProductoResource, ViVentaClientePorFechaResource, \
    ViVentaClientePorClienteResource, ViVentaClienteById, DetalleSalidaByVenta, ViDisposicionUsuarioMotivo, \
    ViCompraProveedorPorProveedorResource, ViCompraProveedorPorFechaResource, ViCompraProveedorById, \
    DetalleEntradaByCompra, DescuentoList, DescuentoResource, DescuentoByProducto



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
api.add_resource(ContactoResource, "/contactos/<int:id_contacto>", endpoint="contacto_by_id")
api.add_resource(ContactoList, "/contactos", endpoint="contactos")
api.add_resource(ContactoCorreoResource, "/contactos_correo/<int:id_contacto_correo>", endpoint="contacto_correo_by_id")
api.add_resource(ContactoCorreoList, "/contactos_correo", endpoint="contactos_correo")
api.add_resource(ContactoTelefonoResource, "/contactos_telefono/<int:id_contacto_telefono>", endpoint="contacto_telefono_by_id")
api.add_resource(ContactoTelefonoList, "/contactos_telefono", endpoint="contactos_telefono")
api.add_resource(ContactoDireccionResource, "/contactos_direccion/<int:id_contacto_direccion>", endpoint="contacto_direccion_by_id")
api.add_resource(ContactoDireccionList, "/contactos_direccion", endpoint="contactos_direccion")
api.add_resource(UnidadPresentacionResource, "/unidad_presentacion/<int:id_unidad_presentacion>", endpoint="unidad_presentacion_by_id")
api.add_resource(UnidadPresentacionList, "/unidad_presentacion", endpoint="unidad_presentacion")
api.add_resource(PresentacionProductoResource, "/presentacion_producto/<int:id_presentacion_producto>", endpoint="presentacion_producto_by_id")
api.add_resource(PresentacionProductoList, "/presentacion_producto", endpoint="presentacion_producto")
api.add_resource(ProductoResource, "/productos/<int:id_producto>", endpoint="producto_by_id")
api.add_resource(ProductoList, "/productos", endpoint="productos")
api.add_resource(AlmacenResource, "/almacenes/<int:id_almacen>", endpoint="almacen_by_id")
api.add_resource(AlmacenList, "/almacenes", endpoint="almacenes")
api.add_resource(ProductoAlmacenResource, "/producto_almacen/<int:id_producto_almacen>", endpoint="producto_almacen_by_id")
api.add_resource(ProductoAlmacenList, "/producto_almacen", endpoint="producto_almacen")
api.add_resource(DisposicionResource, "/disposicion/<int:id_salida_producto>", endpoint="disposicion_by_id")
api.add_resource(DisposicionList, "/disposicion", endpoint="disposicion")
api.add_resource(MotivoResource, "/motivos/<int:id_motivo>", endpoint="motivos_by_id")
api.add_resource(MotivoList, "/motivos", endpoint="motivos")
api.add_resource(VentaResource, "/ventas/<int:id_salida_producto>", endpoint="ventas_by_id")
api.add_resource(VentaList, "/ventas", endpoint="ventas")
api.add_resource(DetalleSalidaResource, "/detalle_salida/<int:id_detalle_salida>", endpoint="detalle_salida_by_id")
api.add_resource(DetalleSalidaList, "/detalle_salida", endpoint="detalle_salida")
api.add_resource(DetalleEntradaResource, "/detalle_entrada/<int:id_detalle_entrada>", endpoint="detalle_entrada_by_id")
api.add_resource(DetalleEntradaList, "/detalle_entrada", endpoint="detalle_entrada")
api.add_resource(CompraResource, "/compras/<int:id_compra>", endpoint="compras_by_id")
api.add_resource(CompraList, "/compras", endpoint="compras")
api.add_resource(FacturaResource, "/factura/<int:id_factura>", endpoint="factura_by_id")
api.add_resource(FacturaList, "/factura", endpoint="factura")
api.add_resource(NivelResource, "/niveles/<int:id_nivel>", endpoint="niveles_by_id")
api.add_resource(NivelList, "/niveles", endpoint="niveles")
api.add_resource(UsuarioNivelView, "/usuario-nivel", endpoint="usuario-nivel_view")
api.add_resource(ContactoUnified, "/contactos_unified/<int:id_contacto>", endpoint="contacto_unified_by_id")
api.add_resource(EntidadResource, "/entidades/<int:id_entidad>", endpoint="entidades_by_id")
api.add_resource(EntidadList, "/entidades", endpoint="entidades")
api.add_resource(ViDisposicionMotivoResource, "/views/disposicion_motivo", endpoint="vi_disposicion_motivo")
api.add_resource(ViVentaClienteResource, "/views/venta_cliente", endpoint="vi_venta_cliente")
api.add_resource(ViCompraProveedorResource, "/views/compra_proveedor", endpoint="vi_compra_proveedor")
api.add_resource(ViProductoEnAlmacenResource, "/views/producto_almacen/<int:id_producto>", endpoint="vi_producto_almacen_by_id")
api.add_resource(ViProductoEnAlmacenList, "/views/producto_almacen", endpoint="vi_producto_almacen")
api.add_resource(ViProductoEnAlmacenBuscar, "/views/producto_almacen/buscar/<string:query>", endpoint="vi_producto_almacen_buscar")
api.add_resource(ViProductoPresentacionUnidadList, "/views/producto_presentacion", endpoint="vi_producto_presentacion")
api.add_resource(ViProductoPresentacionUnidadResource, "/views/producto_presentacion/<int:id_producto>", endpoint="vi_producto_presentacion_by_id")
api.add_resource(ProductoAlmacenResourceProducto, "/producto_almacen/producto/<int:id_producto>", endpoint="producto_almacen_by_producto_id")
api.add_resource(ProductoAlmacenResourceAlmacen, "/producto_almacen/almacen/<int:id_almacen>", endpoint="producto_almacen_by_almacen_id")
api.add_resource(ProductoBusqueda, "/productos/buscar/<string:query>", endpoint="productos_buscar")
api.add_resource(ContactoCorreoByContactoResource, "/contactos_correo/contacto/<int:id_contacto>", endpoint="contacto_correo_by_contacto")
api.add_resource(ContactoDireccionByContactoResource, "/contactos_direccion/contacto/<int:id_contacto>", endpoint="contacto_direccion_by_contacto")
api.add_resource(ContactoTelefonoByContactoResource, "/contactos_telefono/contacto/<int:id_contacto>", endpoint="contacto_telefono_by_contacto")
api.add_resource(LocalidadPorDepartamentoResource, "/localidades/departamento/<int:id_departamento>", endpoint="localidad_departamento")
api.add_resource(ViEntidadContactoDireccionResource, "/entidad/contacto_direccion/<int:id_entidad>", endpoint="contacto_direccion_by_entidad")
api.add_resource(ViEntidadContactoTelefonoResource, "/entidad/contacto_telefono/<int:id_entidad>", endpoint="contacto_telefono_by_entidad")
api.add_resource(ViEntidadContactoCorreoResource, "/entidad/contacto_correo/<int:id_entidad>", endpoint="contacto_correo_by_entidad")
api.add_resource(ClienteNit, "/cliente/nit/<string:nit_ci>", endpoint="cliente_by_nit")
api.add_resource(Status, "/status", endpoint="api_status")
api.add_resource(UserByLogin, "/users/login/<string:login_usuario>", endpoint="user_by_login")
api.add_resource(SalidaProductoResource, "/salida_producto/<int:id_salida_producto>", endpoint="salida_producto_by_id")
api.add_resource(SalidaProductoList, "/salida_producto", endpoint="salida_producto")
api.add_resource(ViVentaClientePorFechaResource, "/views/venta_cliente/<string:desde>/<string:hasta>", endpoint="venta_cliente_by_date")
api.add_resource(ViVentaClienteById, "/views/venta_cliente/<int:id_venta>", endpoint="venta_cliente_by_id")
api.add_resource(DetalleSalidaByVenta, "/detalle_salida/venta/<int:id_venta>", endpoint="detalle_salida_by_venta")
api.add_resource(ViDisposicionUsuarioMotivo, "/disposicion/completo", endpoint="disposicion_completo")
api.add_resource(ViCompraProveedorPorFechaResource, "/views/compra_proveedor/<string:desde>/<string:hasta>", endpoint="compra_proveedor_by_date")
api.add_resource(ViCompraProveedorById, "/views/compra_proveedor/<int:id_compra>", endpoint="compra_proveedor_by_id")
api.add_resource(ViCompraProveedorPorProveedorResource, "/views/compra_proveedor/<string:query>", endpoint="compra_proveedor_by_proveedor")
api.add_resource(DetalleEntradaByCompra, "/detalle_entrada/compra/<int:id_compra>", endpoint="detalle_entrada_by_compra")
api.add_resource(DescuentoResource, "/descuentos/<int:id_descuento>", endpoint="descuento_by_id")
api.add_resource(DescuentoList, "/descuentos", endpoint="descuento")
api.add_resource(DescuentoByProducto, "/descuentos/producto/<int:id_producto>", endpoint="descuento_by_producto")
