from flask import jsonify
from abarrotes_api_rest.extensions import db


class Localidad():

    def __init__(self, id_localidad=None, id_departamento=None, nombre_localidad=None, usuario_registro=None,
                 fecha_registro=None, es_registro_activo=None):
        self.id_localidad = id_localidad
        self.id_departamento = id_departamento
        self.nombre_localidad = nombre_localidad
        self.usuario_registro = usuario_registro
        self.fecha_registro = fecha_registro
        self.es_registro_activo = es_registro_activo

        self.connection = db.connect()
        self.cursor = self.connection.cursor()

    def listar(self):
        sql_query = 'SELECT * FROM vi_localidad'
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        print(description[0] for description in self.cursor.description)
        r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in self.cursor.fetchall()]
        print(f'response from mySQL: {r}')
        return jsonify(r)

    def seleccionar(self):
        sql_query = f"SELECT * FROM vi_localidad WHERE id_localidad = {self.id_localidad}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in self.cursor.fetchall()][0]
        print(f'response from mySQL: {r}')
        return jsonify(r)

    def seleccionar_por_departamento(self):
        sql_query = f"SELECT * FROM vi_localidad WHERE id_departamento = {self.id_departamento}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        all = self.cursor.fetchall()
        if len(all) > 0:
            r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in all]
            print(f'response from mySQL: {r}')
            return jsonify(r)
        return jsonify({"message": "localidad no encontrada"})

    def insertar(self):
        sql_query = f"INSERT INTO localidad (id_departamento, nombre_localidad, usuario_registro) VALUES " \
                    f"({self.id_departamento}, '{self.nombre_localidad}', '{self.usuario_registro}')"
        print(f'sending query to mySQL: {sql_query}')
        print(sql_query)
        self.cursor.execute(sql_query)
        self.connection.commit()

    def actualizar(self):
        sql_query = f"UPDATE localidad SET id_departamento = {self.id_departamento}, " \
                    f"nombre_localidad = '{self.nombre_localidad}', " \
                    f"usuario_registro = '{self.usuario_registro}' WHERE id_localidad = {self.id_localidad}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        self.connection.commit()

    def eliminar(self):
        sql_query = f"UPDATE localidad SET es_registro_activo = 0 WHERE id_localidad = {self.id_localidad}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        self.connection.commit()

    def validar(self):
        pass
