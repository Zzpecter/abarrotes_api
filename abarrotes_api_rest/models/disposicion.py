from flask import jsonify
from abarrotes_api_rest.extensions import db


class Disposicion:

    def __init__(self, id_salida_producto=None, id_usuario=None, id_motivo=None, id_producto=None, cantidad=None,
                 fecha=None, comentario=None, usuario_registro=None, fecha_registro=None, es_registro_activo=None):
        self.id_salida_producto = id_salida_producto
        self.id_usuario = id_usuario
        self.id_motivo = id_motivo
        self.id_producto = id_producto
        self.cantidad = cantidad
        self.fecha = fecha
        self.comentario = comentario
        self.usuario_registro = usuario_registro
        self.fecha_registro = fecha_registro
        self.es_registro_activo = es_registro_activo

        self.connection = db.connect()
        self.cursor = self.connection.cursor()

    def listar(self):
        sql_query = 'SELECT * FROM vi_disposicion'
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        print(description[0] for description in self.cursor.description)
        r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in self.cursor.fetchall()]
        print(f'response from mySQL: {r}')
        return jsonify(r)

    def seleccionar(self):
        sql_query = f"SELECT * FROM vi_disposicion WHERE id_salida_producto = {self.id_salida_producto}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in self.cursor.fetchall()][0]
        print(f'response from mySQL: {r}')
        return jsonify(r)

    def insertar(self):
        sql_query = f"INSERT INTO disposicion (id_salida_producto, id_usuario, id_motivo, id_producto, cantidad, fecha, comentario, usuario_registro) VALUES " \
                    f"({self.id_salida_producto}, {self.id_usuario}, {self.id_motivo}, {self.id_producto}, {self.cantidad}, '{self.fecha}', '{self.comentario}', '{self.usuario_registro}')"
        print(f'sending query to mySQL: {sql_query}')
        print(sql_query)
        self.cursor.execute(sql_query)
        self.connection.commit()

    def actualizar(self):
        sql_query = f"UPDATE disposicion SET id_usuario = {self.id_usuario}, id_motivo = {self.id_motivo}, " \
                    f"id_producto = {self.id_producto}, cantidad = {self.cantidad}, fecha = '{self.fecha}'," \
                    f"comentario = '{self.comentario}', usuario_registro = '{self.usuario_registro}' " \
                    f"WHERE id_salida_producto = {self.id_salida_producto}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        self.connection.commit()

    def eliminar(self):
        sql_query = f"UPDATE disposicion SET es_registro_activo = 0 WHERE id_salida_producto = {self.id_salida_producto}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        self.connection.commit()

    def validar(self):
        pass
