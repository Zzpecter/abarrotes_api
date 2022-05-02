from abarrotes_api_rest.extensions import db


class SalidaProducto:
    def __init__(self, id_salida_producto=None):
        self.id_salida_producto = id_salida_producto

        self.connection = db.connect()
        self.cursor = self.connection.cursor()

    def insertar(self):
        sql_query = "INSERT INTO salida_producto () VALUES ()"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        self.connection.commit()
        return self.cursor.lastrowid

    def eliminar(self):
        sql_query = f"DELETE FROM salida_producto WHERE id_salida_producto = {self.id_salida_producto}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        self.connection.commit()
