from abarrotes_api_rest.api.resources.usuario import UserResource, UserList
from abarrotes_api_rest.api.resources.proveedor import ProveedorResource, ProveedorList
from abarrotes_api_rest.api.resources.cliente import ClienteResource, ClienteList
from abarrotes_api_rest.api.resources.localidad import LocalidadResource, LocalidadList
from abarrotes_api_rest.api.resources.departamento import DepartamentoResource, DepartamentoList
from abarrotes_api_rest.api.resources.contacto import ContactoResource, ContactoList
from abarrotes_api_rest.api.resources.contacto_correo import ContactoCorreoResource, ContactoCorreoList
from abarrotes_api_rest.api.resources.contacto_telefono import ContactoTelefonoResource, ContactoTelefonoList
from abarrotes_api_rest.api.resources.contacto_direccion import ContactoDireccionResource, ContactoDireccionList


__all__ = ["UserResource", "UserList", "ProveedorResource", "ProveedorList", "ClienteResource", "ClienteList",
           "LocalidadResource", "LocalidadList", "DepartamentoResource", "DepartamentoList", "ContactoResource",
           "ContactoList", "ContactoCorreoResource", "ContactoCorreoList", "ContactoTelefonoResource",
           "ContactoTelefonoList", "ContactoDireccionResource", "ContactoDireccionList"]
