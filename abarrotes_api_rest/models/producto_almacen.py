from flask import jsonify
from abarrotes_api_rest.extensions import db


class ProductoAlmacen():

    def __init__(self, id_producto_almacen=None, id_almacen=None, id_producto=None, stock_actual=None, 
                 usuario_registro=None, fecha_registro=None, es_registro_activo=None):
        self.id_producto_almacen = id_producto_almacen
        self.id_almacen = id_almacen
        self.id_producto = id_producto
        self.stock_actual = stock_actual
        self.usuario_registro = usuario_registro
        self.fecha_registro = fecha_registro
        self.es_registro_activo = es_registro_activo

        self.connection = db.connect()
        self.cursor = self.connection.cursor()

    def listar(self):
        sql_query = 'SELECT * FROM vi_producto_almacen'
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        print(description[0] for description in self.cursor.description)
        r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in self.cursor.fetchall()]
        print(f'response from mySQL: {r}')
        return jsonify(r)

    def seleccionar(self):
        sql_query = f"SELECT * FROM vi_producto_almacen WHERE id_producto_almacen = {self.id_producto_almacen}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in self.cursor.fetchall()][0]
        print(f'response from mySQL: {r}')
        return jsonify(r)


    def seleccionar_por_producto(self):
        sql_query = f"SELECT * FROM vi_producto_almacen WHERE id_producto = {self.id_producto}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        all = self.cursor.fetchall()
        if len(all) > 1:
            r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in all][0]
            print(f'response from mySQL: {r}')
            return jsonify(r)
        return jsonify({"message": "producto no encontrado"})


    def seleccionar_por_almacen(self):
        sql_query = f"SELECT * FROM vi_producto_almacen WHERE id_almacen = {self.id_almacen}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in self.cursor.fetchall()][0]
        print(f'response from mySQL: {r}')
        return jsonify(r)

    def insertar(self):
        sql_query = f"INSERT INTO producto_almacen ( id_almacen, id_producto, stock_actual, usuario_registro) VALUES " \
                    f"({self.id_almacen}, {self.id_producto}, {self.stock_actual}, '{self.usuario_registro}')"
        print(f'sending query to mySQL: {sql_query}')
        print(sql_query)
        self.cursor.execute(sql_query)
        self.connection.commit()

    def actualizar(self):
        sql_query = f"UPDATE producto_almacen SET id_almacen = {self.id_almacen}, id_producto = {self.id_producto}, " \
                    f"stock_actual = {self.stock_actual}, usuario_registro = '{self.usuario_registro}' " \
                    f"WHERE id_producto_almacen = {self.id_producto_almacen}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        self.connection.commit()

    def eliminar(self):
        sql_query = f"UPDATE producto_almacen SET es_registro_activo = 0 WHERE id_producto_almacen = {self.id_producto_almacen}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        self.connection.commit()

    def validar(self):
        pass
