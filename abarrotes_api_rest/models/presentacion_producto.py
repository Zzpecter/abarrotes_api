from flask import jsonify
from abarrotes_api_rest.extensions import db


class PresentacionProducto():

    def __init__(self, id_presentacion_producto=None, id_unidad_presentacion=None, nombre_presentacion=None, usuario_registro=None,
                 fecha_registro=None, es_registro_activo=None):
        self.id_presentacion_producto = id_presentacion_producto
        self.id_unidad_presentacion = id_unidad_presentacion
        self.nombre_presentacion = nombre_presentacion
        self.usuario_registro = usuario_registro
        self.fecha_registro = fecha_registro
        self.es_registro_activo = es_registro_activo

        self.connection = db.connect()
        self.cursor = self.connection.cursor()

    def listar(self):
        sql_query = 'SELECT * FROM vi_presentacion_unidad'
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        print(description[0] for description in self.cursor.description)
        r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in self.cursor.fetchall()]
        print(f'response from mySQL: {r}')
        return jsonify(r)

    def seleccionar(self):
        sql_query = f"SELECT * FROM vi_presentacion_producto WHERE id_presentacion_producto = {self.id_presentacion_producto}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in self.cursor.fetchall()][0]
        print(f'response from mySQL: {r}')
        return jsonify(r)

    def insertar(self):
        sql_query = f"INSERT INTO presentacion_producto (id_unidad_presentacion, nombre_presentacion, usuario_registro) VALUES " \
                    f"({self.id_unidad_presentacion}, '{self.nombre_presentacion}', '{self.usuario_registro}')"
        print(f'sending query to mySQL: {sql_query}')
        print(sql_query)
        self.cursor.execute(sql_query)
        self.connection.commit()

    def actualizar(self):
        sql_query = f"UPDATE presentacion_producto SET id_unidad_presentacion = {self.id_unidad_presentacion}, " \
                    f"nombre_presentacion = '{self.nombre_presentacion}', " \
                    f"usuario_registro = '{self.usuario_registro}' WHERE id_presentacion_producto = {self.id_presentacion_producto}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        self.connection.commit()

    def eliminar(self):
        sql_query = f"UPDATE presentacion_producto SET es_registro_activo = 0 WHERE id_presentacion_producto = {self.id_presentacion_producto}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        self.connection.commit()

    def validar(self):
        pass
