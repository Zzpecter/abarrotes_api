from flask import jsonify
from abarrotes_api_rest.extensions import db


class ContactoTelefono():

    def __init__(self, id_contacto_telefono=None, id_contacto=None, codigo_pais=None, numero= None, usuario_registro=None,
                 fecha_registro=None, es_registro_activo=None):
        self.id_contacto_telefono = id_contacto_telefono
        self.id_contacto = id_contacto
        self.codigo_pais = codigo_pais
        self.numero = numero
        self.usuario_registro = usuario_registro
        self.fecha_registro = fecha_registro
        self.es_registro_activo = es_registro_activo

        self.connection = db.connect()
        self.cursor = self.connection.cursor()

    def listar(self):
        sql_query = 'SELECT * FROM vi_contacto_telefono'
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        print(description[0] for description in self.cursor.description)
        r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in self.cursor.fetchall()]
        print(f'response from mySQL: {r}')
        return jsonify(r)

    def listar_por_contacto(self):
        sql_query = f"SELECT * FROM vi_contacto_telefono WHERE id_contacto = {self.id_contacto}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        all = self.cursor.fetchall()
        if len(all) > 0:
            r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in all][0]
            print(f'response from mySQL: {r}')
            return jsonify(r)
        return jsonify({"message": "contacto no encontrado"})

    def seleccionar(self):
        sql_query = f"SELECT * FROM vi_contacto_telefono WHERE id_contacto_telefono = {self.id_contacto_telefono}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in self.cursor.fetchall()][0]
        print(f'response from mySQL: {r}')
        return jsonify(r)

    def insertar(self):
        sql_query = f"INSERT INTO contacto_telefono (id_contacto, codigo_pais, numero, usuario_registro) VALUES " \
                    f"({self.id_contacto}, '{self.codigo_pais}', '{self.numero}', '{self.usuario_registro}')"
        print(f'sending query to mySQL: {sql_query}')
        print(sql_query)
        self.cursor.execute(sql_query)
        self.connection.commit()

    def actualizar(self):
        sql_query = f"UPDATE contacto_telefono SET id_contacto = {self.id_contacto}, codigo_pais = '{self.codigo_pais}', " \
                    f"numero = '{self.numero}', usuario_registro = '{self.usuario_registro}' " \
                    f"WHERE id_contacto_telefono = {self.id_contacto_telefono}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        self.connection.commit()

    def eliminar(self):
        sql_query = f"UPDATE contacto_telefono SET es_registro_activo = 0 WHERE id_contacto_telefono = {self.id_contacto_telefono}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        self.connection.commit()

    def validar(self):
        pass
