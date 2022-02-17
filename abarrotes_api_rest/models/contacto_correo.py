from flask import jsonify
from abarrotes_api_rest.extensions import db


class ContactoCorreo():

    def __init__(self, id_contacto_correo=None, id_contacto=None, correo=None, usuario_registro=None,
                 fecha_registro=None, es_registro_activo=None):
        self.id_contacto_correo = id_contacto_correo
        self.id_contacto = id_contacto
        self.correo = correo
        self.usuario_registro = usuario_registro
        self.fecha_registro = fecha_registro
        self.es_registro_activo = es_registro_activo

        self.connection = db.connect()
        self.cursor = self.connection.cursor()

    def listar(self):
        sql_query = 'SELECT * FROM vi_contacto_correo'
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        print(description[0] for description in self.cursor.description)
        r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in self.cursor.fetchall()]
        print(f'response from mySQL: {r}')
        return jsonify(r)

    def seleccionar(self):
        sql_query = f"SELECT * FROM vi_contacto_correo WHERE id_contacto_correo = {self.id_contacto_correo}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in self.cursor.fetchall()][0]
        print(f'response from mySQL: {r}')
        return jsonify(r)

    def insertar(self):
        sql_query = f"INSERT INTO contacto_correo (id_contacto, correo, usuario_registro) VALUES " \
                    f"({self.id_contacto}, '{self.correo}', '{self.usuario_registro}')"
        print(f'sending query to mySQL: {sql_query}')
        print(sql_query)
        self.cursor.execute(sql_query)
        self.connection.commit()

    def actualizar(self):
        sql_query = f"UPDATE contacto_correo SET id_contacto = {self.id_contacto}, correo = '{self.correo}', " \
                    f"usuario_registro = '{self.usuario_registro}' WHERE id_contacto_correo = {self.id_contacto_correo}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        self.connection.commit()

    def eliminar(self):
        sql_query = f"UPDATE contacto_correo SET es_registro_activo = 0 WHERE id_contacto_correo = {self.id_contacto_correo}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        self.connection.commit()

    def validar(self):
        pass
