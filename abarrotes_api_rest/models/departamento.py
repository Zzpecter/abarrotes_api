from flask import jsonify
from abarrotes_api_rest.extensions import db


class Departamento():

    def __init__(self, id_departamento=None, nombre_departamento=None):
        self.id_departamento = id_departamento
        self.nombre_departamento = nombre_departamento

        self.connection = db.connect()
        self.cursor = self.connection.cursor()

    def listar(self):
        sql_query = 'SELECT * FROM departamento'
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        print(description[0] for description in self.cursor.description)
        r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in self.cursor.fetchall()]
        print(f'response from mySQL: {r}')
        return jsonify(r)

    def seleccionar(self):
        sql_query = f"SELECT * FROM departamento WHERE id_departamento = {self.id_departamento}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in self.cursor.fetchall()][0]
        print(f'response from mySQL: {r}')
        return jsonify(r)
