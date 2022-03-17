from flask import jsonify
from abarrotes_api_rest.extensions import db


class Entidad:
    def __init__(self, id_entidad=None):
        self.id_entidad = id_entidad

        self.connection = db.connect()
        self.cursor = self.connection.cursor()

    def insertar(self):
        sql_query = "INSERT INTO entidad () VALUES ()"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        self.connection.commit()
        return self.cursor.lastrowid

    def eliminar(self):
        sql_query = f"DELETE FROM entidad WHERE id_entidad = {self.id_entidad}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        self.connection.commit()

