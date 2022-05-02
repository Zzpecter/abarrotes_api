from abarrotes_api_rest.api.resources.usuario import UserResource, UserList, UsuarioNivelView, UserByLogin
from abarrotes_api_rest.api.resources.proveedor import ProveedorResource, ProveedorList
from abarrotes_api_rest.api.resources.cliente import ClienteResource, ClienteList, ClienteNit
from abarrotes_api_rest.api.resources.localidad import LocalidadResource, LocalidadList, LocalidadPorDepartamentoResource
from abarrotes_api_rest.api.resources.departamento import DepartamentoResource, DepartamentoList
from abarrotes_api_rest.api.resources.contacto import ContactoResource, ContactoList, ContactoUnified
from abarrotes_api_rest.api.resources.contacto_correo import ContactoCorreoResource, ContactoCorreoList, \
    ContactoCorreoByContactoResource
from abarrotes_api_rest.api.resources.contacto_telefono import ContactoTelefonoResource, ContactoTelefonoList, \
    ContactoTelefonoByContactoResource
from abarrotes_api_rest.api.resources.contacto_direccion import ContactoDireccionResource, ContactoDireccionList, \
    ContactoDireccionByContactoResource
from abarrotes_api_rest.api.resources.unidad_presentacion import UnidadPresentacionResource, UnidadPresentacionList
from abarrotes_api_rest.api.resources.presentacion_producto import PresentacionProductoResource, PresentacionProductoList
from abarrotes_api_rest.api.resources.producto import ProductoResource, ProductoList, ProductoBusqueda
from abarrotes_api_rest.api.resources.almacen import AlmacenResource, AlmacenList
from abarrotes_api_rest.api.resources.producto_almacen import ProductoAlmacenResource, ProductoAlmacenList, \
    ProductoAlmacenResourceProducto, ProductoAlmacenResourceAlmacen
from abarrotes_api_rest.api.resources.disposicion import DisposicionList, DisposicionResource
from abarrotes_api_rest.api.resources.motivo import MotivoResource, MotivoList
from abarrotes_api_rest.api.resources.venta import VentaResource, VentaList
from abarrotes_api_rest.api.resources.detalle_salida import DetalleSalidaResource, DetalleSalidaList, DetalleSalidaByVenta
from abarrotes_api_rest.api.resources.detalle_entrada import DetalleEntradaResource, DetalleEntradaList
from abarrotes_api_rest.api.resources.compra import CompraResource, CompraList
from abarrotes_api_rest.api.resources.factura import FacturaResource, FacturaList
from abarrotes_api_rest.api.resources.nivel import NivelResource, NivelList
from abarrotes_api_rest.api.resources.entidad import EntidadList, EntidadResource
from abarrotes_api_rest.api.resources.custom_views import ViVentaClienteResource, ViCompraProveedorResource, \
    ViProductoEnAlmacenResource, ViProductoPresentacionUnidadList, ViDisposicionMotivoResource, \
    ViEntidadContactoDireccionResource, ViEntidadContactoTelefonoResource, ViEntidadContactoCorreoResource, \
    ViProductoPresentacionUnidadResource, ViProductoEnAlmacenList, ViProductoEnAlmacenBuscar, \
    ViVentaClientePorFechaResource, ViVentaClientePorClienteResource, ViVentaClienteById
from abarrotes_api_rest.api.resources.status import Status
from abarrotes_api_rest.api.resources.salida_producto import SalidaProductoList, SalidaProductoResource


__all__ = ["UserResource", "UserList", "ProveedorResource", "ProveedorList", "ClienteResource", "ClienteList",
           "LocalidadResource", "LocalidadList", "DepartamentoResource", "DepartamentoList", "ContactoResource",
           "ContactoList", "ContactoCorreoResource", "ContactoCorreoList", "ContactoTelefonoResource",
           "ContactoTelefonoList", "ContactoDireccionResource", "ContactoDireccionList", "UnidadPresentacionResource",
           "UnidadPresentacionList", "PresentacionProductoResource", "PresentacionProductoList", "ProductoResource",
           "ProductoList", "AlmacenResource", "AlmacenList", "ProductoAlmacenResource", "ProductoAlmacenList",
           "DisposicionList", "DisposicionResource", "MotivoResource", "MotivoList", "VentaResource", "VentaList",
           "DetalleSalidaResource", "DetalleSalidaList", "DetalleEntradaResource", "DetalleEntradaList",
           "CompraResource", "CompraList", "FacturaResource", "FacturaList", "NivelResource", "NivelList",
           "UsuarioNivelView", "ContactoUnified", "EntidadResource", "EntidadList", "ViVentaClienteResource",
           "ViCompraProveedorResource", "ViProductoEnAlmacenResource", "ViProductoPresentacionUnidadList",
           "ViDisposicionMotivoResource", "ProductoAlmacenResourceProducto", "ProductoAlmacenResourceAlmacen",
           "ProductoBusqueda", "LocalidadPorDepartamentoResource", "ViEntidadContactoDireccionResource",
           "ViEntidadContactoCorreoResource", "ViEntidadContactoTelefonoResource",
           "ViProductoPresentacionUnidadResource", "ClienteNit", "ViProductoEnAlmacenList", "ViProductoEnAlmacenBuscar",
           "Status", "UserByLogin", "SalidaProductoList", "SalidaProductoResource", "ViVentaClientePorFechaResource",
           "ViVentaClientePorClienteResource", "ViVentaClienteById", "DetalleSalidaByVenta"]
