from flask import jsonify
from abarrotes_api_rest.extensions import db


class CustomViews():

    def __init__(self):
        self.connection = db.connect()
        self.cursor = self.connection.cursor()

    def listar_vi_venta_cliente(self):
        sql_query = 'SELECT * FROM vi_venta_cliente'
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in self.cursor.fetchall()]
        print(f'response from mySQL: {r}')
        return jsonify(r)

    def listar_vi_compra_proveedor(self):
        sql_query = 'SELECT * FROM vi_compra_proveedor'
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in self.cursor.fetchall()]
        print(f'response from mySQL: {r}')
        return jsonify(r)

    def listar_vi_disposicion_motivo(self):
        sql_query = 'SELECT * FROM vi_disposicion_motivo'
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in self.cursor.fetchall()]
        print(f'response from mySQL: {r}')
        return jsonify(r)

    def listar_vi_producto_en_almacen(self):
        sql_query = 'SELECT * FROM vi_producto_en_almacen'
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in self.cursor.fetchall()]
        print(f'response from mySQL: {r}')
        return jsonify(r)

    def listar_vi_producto_presentacion_unidad(self):
        sql_query = 'SELECT * FROM vi_producto_presentacion_unidad'
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in self.cursor.fetchall()]
        print(f'response from mySQL: {r}')
        return jsonify(r)