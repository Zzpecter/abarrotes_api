from flask import jsonify
from abarrotes_api_rest.extensions import db


class Compra():

    def __init__(self, id_compra=None, id_usuario=None, id_proveedor=None, monto_total=None, fecha=None, 
                  usuario_registro=None, fecha_registro=None, es_registro_activo=None):
        self.id_compra = id_compra
        self.id_usuario = id_usuario
        self.id_proveedor = id_proveedor
        self.monto_total = monto_total
        self.fecha = fecha
        self.usuario_registro = usuario_registro
        self.fecha_registro = fecha_registro
        self.es_registro_activo = es_registro_activo

        self.connection = db.connect()
        self.cursor = self.connection.cursor()

    def listar(self):
        sql_query = 'SELECT * FROM vi_compra'
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        print(description[0] for description in self.cursor.description)
        r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in self.cursor.fetchall()]
        print(f'response from mySQL: {r}')

        # Convert decimal to float for json.
        for idx, response in enumerate(r):
            r[idx]['monto_total'] = float(response['monto_total'])

        print(f'formatted response: {r}')
        return jsonify(r)

    def seleccionar(self):
        sql_query = f"SELECT * FROM vi_compra WHERE id_compra = {self.id_compra}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in self.cursor.fetchall()][0]
        print(f'response from mySQL: {r}')

        # Convert decimal to float for json.
        r['monto_total'] = float(r['monto_total'])

        print(f'formatted response: {r}')

        return jsonify(r)

    def insertar(self):
        sql_query = f"INSERT INTO compra (id_usuario, id_proveedor, monto_total, fecha, usuario_registro) VALUES " \
                    f"({self.id_usuario}, {self.id_proveedor}, {self.monto_total}, '{self.fecha}', '{self.usuario_registro}')"
        print(f'sending query to mySQL: {sql_query}')
        print(sql_query)
        self.cursor.execute(sql_query)
        self.connection.commit()

    def actualizar(self):
        sql_query = f"UPDATE compra SET id_usuario = {self.id_usuario}, id_proveedor = {self.id_proveedor}, " \
                    f"fecha = '{self.fecha}', monto_total = {self.monto_total}, " \
                    f"usuario_registro = '{self.usuario_registro}' WHERE id_compra = {self.id_compra}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        self.connection.commit()

    def eliminar(self):
        sql_query = f"UPDATE compra SET es_registro_activo = 0 WHERE id_compra = {self.id_compra}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        self.connection.commit()

    def validar(self):
        pass
