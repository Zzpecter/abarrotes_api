from flask import jsonify
from abarrotes_api_rest.extensions import db


class Producto():

    def __init__(self, id_producto=None, id_presentacion_producto=None, nombre=None, codigo=None, usuario_registro=None,
                 fecha_registro=None, es_registro_activo=None):
        self.id_producto = id_producto
        self.id_presentacion_producto = id_presentacion_producto
        self.nombre = nombre
        self.codigo = codigo
        self.usuario_registro = usuario_registro
        self.fecha_registro = fecha_registro
        self.es_registro_activo = es_registro_activo

        self.connection = db.connect()
        self.cursor = self.connection.cursor()

    def listar(self):
        sql_query = 'SELECT * FROM vi_producto'
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        print(description[0] for description in self.cursor.description)
        r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in self.cursor.fetchall()]
        print(f'response from mySQL: {r}')
        return jsonify(r)

    def seleccionar(self):
        sql_query = f"SELECT * FROM vi_producto WHERE id_producto = {self.id_producto}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in self.cursor.fetchall()][0]
        print(f'response from mySQL: {r}')
        return jsonify(r)

    def buscar(self, query):
        sql_query = f"SELECT * FROM vi_producto WHERE nombre rlike '{query}' or codigo rlike '{query}'"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        all = self.cursor.fetchall()
        if len(all) > 1:
            r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in all][0]
            print(f'response from mySQL: {r}')
            return jsonify(r)
        return jsonify({"message": "producto no encontrado"})

    def insertar(self):
        sql_query = f"INSERT INTO producto (id_presentacion_producto, nombre, codigo, usuario_registro) VALUES " \
                    f"({self.id_presentacion_producto}, '{self.nombre}', '{self.codigo}', '{self.usuario_registro}')"
        print(f'sending query to mySQL: {sql_query}')
        print(sql_query)
        self.cursor.execute(sql_query)
        self.connection.commit()

    def actualizar(self):
        sql_query = f"UPDATE producto SET id_presentacion_producto = {self.id_presentacion_producto}, " \
                    f"nombre = '{self.nombre}', codigo = '{self.codigo}', " \
                    f"usuario_registro = '{self.usuario_registro}' WHERE id_producto = {self.id_producto}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        self.connection.commit()

    def eliminar(self):
        sql_query = f"UPDATE producto SET es_registro_activo = 0 WHERE id_producto = {self.id_producto}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        self.connection.commit()

    def validar(self):
        pass
