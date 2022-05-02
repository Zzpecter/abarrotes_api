from flask import jsonify
from abarrotes_api_rest.extensions import db


class Factura():

    def __init__(self, id_factura=None, codigo_control=None, datos_codigo_QR=None, usuario_registro=None,
                 fecha_registro=None, es_registro_activo=None):
        self.id_factura = id_factura
        self.codigo_control = codigo_control
        self.datos_codigo_QR = datos_codigo_QR
        self.usuario_registro = usuario_registro
        self.fecha_registro = fecha_registro
        self.es_registro_activo = es_registro_activo

        self.connection = db.connect()
        self.cursor = self.connection.cursor()

    def listar(self):
        sql_query = 'SELECT * FROM vi_factura'
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        print(description[0] for description in self.cursor.description)
        r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in self.cursor.fetchall()]
        print(f'response from mySQL: {r}')

        print(f'formatted response: {r}')
        return jsonify(r)

    def seleccionar(self):
        sql_query = f"SELECT * FROM vi_factura WHERE id_factura = {self.id_factura}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in self.cursor.fetchall()][0]
        print(f'response from mySQL: {r}')

        print(f'formatted response: {r}')

        return jsonify(r)

    def insertar(self):
        sql_query = f"INSERT INTO factura (codigo_control, datos_codigo_QR, usuario_registro) VALUES " \
                    f"('{self.codigo_control}', '{self.datos_codigo_QR}', '{self.usuario_registro}')"
        print(f'sending query to mySQL: {sql_query}')
        print(sql_query)
        self.cursor.execute(sql_query)
        self.connection.commit()
        return self.cursor.lastrowid

    def actualizar(self):
        sql_query = f"UPDATE factura SET codigo_control = '{self.codigo_control}', datos_codigo_QR = '{self.datos_codigo_QR}', " \
                    f"usuario_registro = '{self.usuario_registro}' WHERE id_factura = {self.id_factura}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        self.connection.commit()

    def eliminar(self):
        sql_query = f"UPDATE factura SET es_registro_activo = 0 WHERE id_factura = {self.id_factura}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        self.connection.commit()

    def validar(self):
        pass
