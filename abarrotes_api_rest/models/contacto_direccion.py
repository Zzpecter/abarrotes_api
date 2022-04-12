from flask import jsonify
from abarrotes_api_rest.extensions import db


class ContactoDireccion():

    def __init__(self, id_contacto_direccion=None, id_contacto=None, id_localidad=None, id_entidad=None, calle=None,
                 numero_casa=None,zona=None, detalles=None, usuario_registro=None, fecha_registro=None,
                 es_registro_activo=None):
        self.id_contacto_direccion = id_contacto_direccion
        self.id_contacto = id_contacto
        self.id_localidad = id_localidad
        self.id_entidad= id_entidad
        self.calle = calle
        self.numero_casa = numero_casa
        self.zona = zona
        self.detalles = detalles
        self.usuario_registro = usuario_registro
        self.fecha_registro = fecha_registro
        self.es_registro_activo = es_registro_activo

        self.connection = db.connect()
        self.cursor = self.connection.cursor()

    def listar(self):
        sql_query = 'SELECT * FROM vi_contacto_direccion'
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        print(description[0] for description in self.cursor.description)
        r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in self.cursor.fetchall()]
        print(f'response from mySQL: {r}')
        return jsonify(r)

    def listar_por_entidad(self):
        sql_query = f"SELECT * FROM `vi_contacto_direccion-localidad-departamento` WHERE id_entidad = {self.id_entidad}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        all = self.cursor.fetchall()
        if len(all) > 0:
            r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in all][0]
            print(f'response from mySQL: {r}')
            return jsonify(r)
        return jsonify({"message": "contacto no encontrado"})

    def seleccionar(self):
        sql_query = f"SELECT * FROM vi_contacto_direccion WHERE id_contacto_direccion = {self.id_contacto_direccion}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in self.cursor.fetchall()][0]
        print(f'response from mySQL: {r}')
        return jsonify(r)

    def insertar(self):
        sql_query = f"INSERT INTO contacto_direccion (id_contacto, id_localidad, calle, numero_casa, zona, detalles," \
                    f" usuario_registro) VALUES ({self.id_contacto}, {self.id_localidad}, '{self.calle}', " \
                    f"'{self.numero_casa}', '{self.zona}', '{self.detalles}', '{self.usuario_registro}')"
        print(f'sending query to mySQL: {sql_query}')
        print(sql_query)
        self.cursor.execute(sql_query)
        self.connection.commit()

    def actualizar(self):
        sql_query = f"UPDATE contacto_direccion SET id_contacto = {self.id_contacto}, id_localidad = {self.id_localidad}, " \
                    f"calle = '{self.calle}', numero_casa = '{self.numero_casa}', zona = '{self.zona}'," \
                    f"detalles = '{self.detalles}', usuario_registro = '{self.usuario_registro}' " \
                    f"WHERE id_contacto_direccion = {self.id_contacto_direccion}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        self.connection.commit()

    def eliminar(self):
        sql_query = f"UPDATE contacto_direccion SET es_registro_activo = 0 WHERE id_contacto_direccion = {self.id_contacto_direccion}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        self.connection.commit()

    def validar(self):
        pass
