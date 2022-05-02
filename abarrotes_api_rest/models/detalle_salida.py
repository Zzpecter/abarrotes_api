from flask import jsonify
from abarrotes_api_rest.extensions import db


class DetalleSalida():

    def __init__(self, id_detalle_salida=None, id_salida_producto=None, id_producto=None, cantidad=None,
                 precio_unidad=None, usuario_registro=None,fecha_registro=None, es_registro_activo=None):
        self.id_detalle_salida = id_detalle_salida
        self.id_salida_producto = id_salida_producto
        self.id_producto = id_producto
        self.cantidad = cantidad
        self.precio_unidad = precio_unidad
        self.usuario_registro = usuario_registro
        self.fecha_registro = fecha_registro
        self.es_registro_activo = es_registro_activo

        self.connection = db.connect()
        self.cursor = self.connection.cursor()

    def listar(self):
        sql_query = 'SELECT * FROM vi_detalle_salida'
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        print(description[0] for description in self.cursor.description)
        r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in self.cursor.fetchall()]
        print(f'response from mySQL: {r}')

        # Convert decimal to float for json.
        for idx, response in enumerate(r):
            r[idx]['precio_unidad'] = float(response['precio_unidad'])

        return jsonify(r)

    def seleccionar(self):
        sql_query = f"SELECT * FROM vi_detalle_salida WHERE id_detalle_salida = {self.id_detalle_salida}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in self.cursor.fetchall()][0]
        print(f'response from mySQL: {r}')

        r['precio_unidad'] = float(r['precio_unidad'])

        return jsonify(r)

    def seleccionar_por_venta(self):
        sql_query = f"SELECT * FROM `vi_detalle_salida-producto` WHERE id_salida_producto = {self.id_salida_producto}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        all = self.cursor.fetchall()
        if len(all) > 0:
            r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in all]
            print(f'response from mySQL: {r}')

            for idx, response in enumerate(r):
                r[idx]['precio_unidad'] = float(response['precio_unidad'])
                r[idx]['cantidad'] = float(response['cantidad'])

            return jsonify(r)
        return jsonify({"message": "detalle_salida no encontrado"})

    def insertar(self):
        sql_query = f"INSERT INTO detalle_salida (id_salida_producto, id_producto, cantidad, precio_unidad, usuario_registro) VALUES " \
                    f"({self.id_salida_producto}, {self.id_producto}, {self.cantidad}, {self.precio_unidad}, '{self.usuario_registro}')"
        print(f'sending query to mySQL: {sql_query}')
        print(sql_query)
        self.cursor.execute(sql_query)
        self.connection.commit()

    def actualizar(self):
        sql_query = f"UPDATE detalle_salida SET id_salida_producto = {self.id_salida_producto}, id_producto = {self.id_producto}, " \
                    f"cantidad = {self.cantidad}, precio_unidad = {self.precio_unidad}, " \
                    f"usuario_registro = '{self.usuario_registro}' WHERE id_detalle_salida = {self.id_detalle_salida}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        self.connection.commit()

    def eliminar(self):
        sql_query = f"UPDATE detalle_salida SET es_registro_activo = 0 WHERE id_detalle_salida = {self.id_detalle_salida}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        self.connection.commit()

    def validar(self):
        pass
