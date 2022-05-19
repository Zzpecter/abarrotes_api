from flask import jsonify
from abarrotes_api_rest.extensions import db


class Descuento:

    def __init__(self, id_descuento=None, id_producto=None, precio_oferta=None, fecha_expiracion=None,
                 usuario_registro=None, fecha_registro=None, es_registro_activo=None):
        self.id_descuento = id_descuento
        self.id_producto = id_producto
        self.precio_oferta = precio_oferta
        self.fecha_expiracion = fecha_expiracion
        self.usuario_registro = usuario_registro
        self.fecha_registro = fecha_registro
        self.es_registro_activo = es_registro_activo

        self.connection = db.connect()
        self.cursor = self.connection.cursor()

    def listar(self):
        sql_query = 'SELECT * FROM vi_descuento_producto'
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)

        all = self.cursor.fetchall()
        if len(all) > 0:
            r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in all]
            print(f'response from mySQL: {r}')
            for idx, response in enumerate(r):
                r[idx]['precio_oferta'] = float(response['precio_oferta'])
                r[idx]['fecha_expiracion'] = r[idx]['fecha_expiracion'].strftime("%Y-%m-%d %H:%M:%S")
            print(f'formatted response from mySQL: {r}')

            return jsonify(r)
        return jsonify({"message": "descuento no encontrado"})

    def seleccionar(self):
        sql_query = f"SELECT * FROM vi_descuento_producto WHERE id_descuento = {self.id_descuento}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        all = self.cursor.fetchall()
        if len(all) > 0:
            r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in all][0]
            print(f'response from mySQL: {r}')

            # Convert decimal to float for json.
            r['precio_oferta'] = float(r['precio_oferta'])
            r['fecha_expiracion'] = r['fecha_expiracion'].strftime("%Y-%m-%d %H:%M:%S")

            return jsonify(r)
        return jsonify({"message": "descuento no encontrado"})

    def seleccionar_por_producto(self):
        sql_query = f"SELECT * FROM vi_descuento_producto WHERE id_producto = {self.id_producto}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        all = self.cursor.fetchall()
        if len(all) > 0:
            r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in all][0]
            print(f'response from mySQL: {r}')
            r['precio_unidad'] = float(r['precio_unidad'])
            r['fecha_expiracion'] = r['fecha_expiracion'].strftime("%Y-%m-%d %H:%M:%S")
            print(f'formatted response from mySQL: {r}')

            return jsonify(r)
        return jsonify({"message": "descuento no encontrado"})

    def insertar(self):
        sql_query = f"INSERT INTO descuento (id_producto, precio_oferta, fecha_expiracion, usuario_registro) VALUES " \
                    f"({self.id_producto}, {self.precio_oferta}, '{self.fecha_expiracion}', '{self.usuario_registro}')"
        print(f'sending query to mySQL: {sql_query}')
        print(sql_query)
        self.cursor.execute(sql_query)
        self.connection.commit()
        return self.cursor.lastrowid

    def actualizar(self):
        sql_query = f"UPDATE descuento SET id_producto = {self.id_producto}, " \
                    f"precio_oferta = {self.precio_oferta}, fecha_expiracion = '{self.fecha_expiracion}', " \
                    f"usuario_registro = '{self.usuario_registro}' WHERE id_descuento = {self.id_descuento}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        self.connection.commit()

    def eliminar(self):
        sql_query = f"UPDATE descuento SET es_registro_activo = 0 WHERE id_descuento = {self.id_descuento}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        self.connection.commit()
