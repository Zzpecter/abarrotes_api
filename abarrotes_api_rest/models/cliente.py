from flask import jsonify
from abarrotes_api_rest.extensions import db


class Cliente():

    def __init__(self, id_entidad=None, razon_social=None, nit_ci=None, usuario_registro=None, fecha_registro=None,
                 es_registro_activo=None):
        self.id_entidad = id_entidad
        self.razon_social = razon_social
        self.nit_ci = nit_ci
        self.usuario_registro = usuario_registro
        self.fecha_registro = fecha_registro
        self.es_registro_activo = es_registro_activo

        self.connection = db.connect()
        self.cursor = self.connection.cursor()

    def listar(self):
        sql_query = 'SELECT * FROM vi_cliente'
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        print(description[0] for description in self.cursor.description)
        r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in self.cursor.fetchall()]
        print(f'response from mySQL: {r}')
        return jsonify(r)

    def seleccionar(self):
        sql_query = f"SELECT * FROM vi_cliente WHERE id_entidad = {self.id_entidad}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in self.cursor.fetchall()][0]
        print(f'response from mySQL: {r}')
        return jsonify(r)

    def seleccionar_por_nit(self):
        sql_query = f"SELECT * FROM vi_cliente WHERE nit_ci = '{self.nit_ci}'"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)

        all = self.cursor.fetchall()
        if len(all) > 0:
            r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in all][0]
            print(f'response from mySQL: {r}')
            return jsonify(r)
        return jsonify({"message": "cliente no encontrado"})

    def insertar(self):
        sql_query = f"INSERT INTO cliente (id_entidad, razon_social, nit_ci, usuario_registro) VALUES " \
                    f"({self.id_entidad}, '{self.razon_social}', '{self.nit_ci}', '{self.usuario_registro}')"
        print(f'sending query to mySQL: {sql_query}')
        print(sql_query)
        self.cursor.execute(sql_query)
        self.connection.commit()
        return self.cursor.lastrowid

    def actualizar(self):
        sql_query = f"UPDATE cliente SET razon_social = '{self.razon_social}', nit_ci = '{self.nit_ci}', " \
                    f"usuario_registro = '{self.usuario_registro}' WHERE id_entidad = {self.id_entidad}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        self.connection.commit()

    def eliminar(self):
        sql_query = f"UPDATE cliente SET es_registro_activo = 0 WHERE id_entidad = {self.id_entidad}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        self.connection.commit()

    def validar(self):
        pass
