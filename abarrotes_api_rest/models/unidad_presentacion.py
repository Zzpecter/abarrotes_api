from flask import jsonify
from abarrotes_api_rest.extensions import db


class UnidadPresentacion():

    def __init__(self, id_unidad_presentacion=None, nombre_medida=None, multiplicador_kg=None, usuario_registro=None,
                 fecha_registro=None, es_registro_activo=None):
        self.id_unidad_presentacion = id_unidad_presentacion
        self.nombre_medida = nombre_medida
        self.multiplicador_kg = multiplicador_kg
        self.usuario_registro = usuario_registro
        self.fecha_registro = fecha_registro
        self.es_registro_activo = es_registro_activo

        self.connection = db.connect()
        self.cursor = self.connection.cursor()

    def listar(self):
        sql_query = 'SELECT * FROM vi_unidad_presentacion'
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        print(description[0] for description in self.cursor.description)
        r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in self.cursor.fetchall()]
        print(f'response from mySQL: {r}')
        return jsonify(r)

    def seleccionar(self):
        sql_query = f"SELECT * FROM vi_unidad_presentacion WHERE id_unidad_presentacion = {self.id_unidad_presentacion}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in self.cursor.fetchall()][0]
        print(f'response from mySQL: {r}')
        return jsonify(r)

    def insertar(self):
        sql_query = f"INSERT INTO unidad_presentacion (nombre_medida, multiplicador_kg, usuario_registro) VALUES " \
                    f"('{self.nombre_medida}', '{self.multiplicador_kg}', '{self.usuario_registro}')"
        print(f'sending query to mySQL: {sql_query}')
        print(sql_query)
        self.cursor.execute(sql_query)
        self.connection.commit()

    def actualizar(self):
        sql_query = f"UPDATE unidad_presentacion SET nombre_medida = '{self.nombre_medida}', " \
                    f"multiplicador_kg = '{self.multiplicador_kg}', " \
                    f"usuario_registro = '{self.usuario_registro}' WHERE id_unidad_presentacion = {self.id_unidad_presentacion}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        self.connection.commit()

    def eliminar(self):
        sql_query = f"UPDATE unidad_presentacion SET es_registro_activo = 0 WHERE id_unidad_presentacion = {self.id_unidad_presentacion}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        self.connection.commit()

    def validar(self):
        pass
