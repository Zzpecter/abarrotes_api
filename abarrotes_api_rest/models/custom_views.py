from flask import jsonify
from abarrotes_api_rest.extensions import db
from datetime import datetime


class CustomViews:

    def __init__(self):
        self.connection = db.connect()
        self.cursor = self.connection.cursor()

    def listar_vi_venta_cliente(self):
        sql_query = 'SELECT * FROM vi_venta_cliente'
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        all = self.cursor.fetchall()
        if len(all) > 0:
            r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in all]
            print(f'response from mySQL: {r}')

            # Convert datetime to string reperesentation for JSON
            for idx, response in enumerate(r):
                r[idx]['fecha'] = response['fecha'].strftime("%m-%d-%Y %H:%M:%S")
            print(f'formatted response from mySQL: {r}')

            return jsonify(r)
        return jsonify({"message": "venta no encontrada"})

    def seleccionar_vi_venta_cliente(self, id_venta):
        sql_query = f'SELECT * FROM vi_venta_cliente WHERE id_venta = {id_venta}'
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        all = self.cursor.fetchall()
        if len(all) > 0:
            r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in all][0]
            print(f'response from mySQL: {r}')

            # Convert datetime to string reperesentation for JSON
            r['fecha'] = r['fecha'].strftime("%m-%d-%Y %H:%M:%S")
            print(f'formatted response from mySQL: {r}')

            return jsonify(r)
        return jsonify({"message": "venta no encontrada"})

    def listar_vi_venta_cliente_por_fecha(self, desde, hasta):
        desde = datetime.strptime(desde, '%m-%d-%Y')
        hasta = datetime.strptime(hasta, '%m-%d-%Y')
        sql_query = f"SELECT * FROM vi_venta_cliente WHERE fecha between '{desde}' and '{hasta}'"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        all = self.cursor.fetchall()
        if len(all) > 0:
            r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in all]
            print(f'response from mySQL: {r}')

            # Convert datetime to string reperesentation for JSON
            for idx, response in enumerate(r):
                r[idx]['fecha'] = response['fecha'].strftime("%m-%d-%Y %H:%M:%S")
            print(f'formatted response from mySQL: {r}')

            return jsonify(r)
        return jsonify({"message": "venta no encontrada"})

    def listar_vi_venta_cliente_por_cliente(self, query):
        sql_query = f"SELECT * FROM vi_venta_cliente WHERE cliente rlike '{query}' or nit_ci rlike '{query}'"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        all = self.cursor.fetchall()
        if len(all) > 0:
            r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in all]
            print(f'response from mySQL: {r}')

            # Convert datetime to string reperesentation for JSON
            for idx, response in enumerate(r):
                r[idx]['fecha'] = response['fecha'].strftime("%m-%d-%Y %H:%M:%S")
            print(f'formatted response from mySQL: {r}')

            return jsonify(r)
        return jsonify({"message": "venta no encontrada"})

    def listar_vi_compra_proveedor(self):
        sql_query = 'SELECT * FROM vi_compra_proveedor'
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        all = self.cursor.fetchall()
        if len(all) > 0:
            r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in all]
            print(f'response from mySQL: {r}')

            # Convert datetime to string reperesentation for JSON
            for idx, response in enumerate(r):
                r[idx]['fecha'] = response['fecha'].strftime("%m-%d-%Y %H:%M:%S")
            print(f'formatted response from mySQL: {r}')

            return jsonify(r)
        return jsonify({"message": "compra no encontrada"})

    def seleccionar_vi_compra_proveedor(self, id_compra):
        sql_query = f'SELECT * FROM vi_compra_proveedor WHERE id_compra = {id_compra}'
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        all = self.cursor.fetchall()
        if len(all) > 0:
            r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in all][0]
            print(f'response from mySQL: {r}')

            # Convert datetime to string reperesentation for JSON
            r['fecha'] = r['fecha'].strftime("%m-%d-%Y %H:%M:%S")
            print(f'formatted response from mySQL: {r}')

            return jsonify(r)
        return jsonify({"message": "compra no encontrada"})

    def listar_vi_compra_proveedor_por_fecha(self, desde, hasta):
        desde = datetime.strptime(desde, '%m-%d-%Y')
        hasta = datetime.strptime(hasta, '%m-%d-%Y')
        sql_query = f"SELECT * FROM vi_compra_proveedor WHERE fecha between '{desde}' and '{hasta}'"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        all = self.cursor.fetchall()
        if len(all) > 0:
            r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in all]
            print(f'response from mySQL: {r}')

            # Convert datetime to string reperesentation for JSON
            for idx, response in enumerate(r):
                r[idx]['fecha'] = response['fecha'].strftime("%m-%d-%Y %H:%M:%S")
            print(f'formatted response from mySQL: {r}')

            return jsonify(r)
        return jsonify({"message": "compra no encontrada"})

    def listar_vi_compra_proveedor_por_proveedor(self, query):
        sql_query = f"SELECT * FROM vi_compra_proveedor WHERE proveedor rlike '{query}'"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        all = self.cursor.fetchall()
        if len(all) > 0:
            r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in all]
            print(f'response from mySQL: {r}')

            # Convert datetime to string reperesentation for JSON
            for idx, response in enumerate(r):
                r[idx]['fecha'] = response['fecha'].strftime("%m-%d-%Y %H:%M:%S")
            print(f'formatted response from mySQL: {r}')

            return jsonify(r)
        return jsonify({"message": "compra no encontrada"})

    def listar_vi_disposicion_motivo(self):
        sql_query = 'SELECT * FROM vi_disposicion_motivo'
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in self.cursor.fetchall()]
        print(f'response from mySQL: {r}')
        return jsonify(r)

    def listar_vi_producto_en_almacen(self):
        sql_query = 'SELECT * FROM vi_producto_en_almacen'
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in self.cursor.fetchall()]
        print(f'response from mySQL: {r}')
        return jsonify(r)

    def seleccionar_vi_producto_en_almacen(self, id_producto):
        sql_query = f'SELECT * FROM vi_producto_en_almacen WHERE id_producto={id_producto}'
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        all = self.cursor.fetchall()
        if len(all) > 0:
            r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in all][0]
            print(f'response from mySQL: {r}')
            return jsonify(r)
        return jsonify({"message": "producto no encontrado"})

    def buscar_vi_producto_en_almacen(self, query):
        sql_query = f"SELECT * FROM vi_producto_en_almacen WHERE nombre rlike '{query}' or codigo rlike '{query}'"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        all = self.cursor.fetchall()
        if len(all) > 0:
            r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in all]
            print(f'response from mySQL: {r}')
            return jsonify(r)
        return jsonify({"message": "producto no encontrado"})

    def listar_vi_producto_presentacion_unidad(self):
        sql_query = 'SELECT * FROM vi_producto_presentacion_unidad'
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        all = self.cursor.fetchall()
        if len(all) > 0:
            r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in all]
            print(f'response from mySQL: {r}')
            return jsonify(r)
        return jsonify({"message": "producto no encontrado"})

    def seleccionar_vi_producto_presentacion_unidad(self, id_producto):
        sql_query = f'SELECT * FROM vi_producto_presentacion_unidad WHERE id_producto={id_producto}'
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        all = self.cursor.fetchall()
        if len(all) > 0:
            r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in all][0]
            print(f'response from mySQL: {r}')
            return jsonify(r)
        return jsonify({"message": "producto no encontrado"})

    def listar_vi_entidad_contacto_direccion(self, id_entidad):
        sql_query = f'SELECT * FROM vi_entidad_contacto_direccion WHERE id_entidad={id_entidad}'
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        all = self.cursor.fetchall()
        if len(all) > 0:
            r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in all]
            print(f'response from mySQL: {r}')
            return jsonify(r)
        return jsonify({"message": "contacto no encontrado"})

    def listar_vi_entidad_contacto_telefono(self, id_entidad):
        sql_query = f'SELECT * FROM vi_entidad_contacto_telefono WHERE id_entidad={id_entidad}'
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        all = self.cursor.fetchall()
        if len(all) > 0:
            r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in all]
            print(f'response from mySQL: {r}')
            return jsonify(r)
        return jsonify({"message": "contacto no encontrado"})

    def listar_vi_entidad_contacto_correo(self, id_entidad):
        sql_query = f'SELECT * FROM vi_entidad_contacto_correo WHERE id_entidad={id_entidad}'
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        all = self.cursor.fetchall()
        if len(all) > 0:
            r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in all]
            print(f'response from mySQL: {r}')
            return jsonify(r)
        return jsonify({"message": "contacto no encontrado"})


    def listar_vi_disposicion_usuario_motivo(self):
        sql_query = 'SELECT * FROM `vi_disposicion-usuario-motivo`'
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        all = self.cursor.fetchall()
        if len(all) > 0:
            r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in all]
            print(f'response from mySQL: {r}')

            # Convert datetime to string reperesentation for JSON
            for idx, response in enumerate(r):
                r[idx]['fecha'] = response['fecha'].strftime("%m-%d-%Y %H:%M:%S")
            print(f'formatted response from mySQL: {r}')

            return jsonify(r)
        return jsonify({"message": "disposicion no encontrada"})


    def listar_reporte_ventas_sin_producto(self, fecha_desde, fecha_hasta):
        fecha_desde = datetime.strptime(fecha_desde, '%m-%d-%Y')
        fecha_hasta = datetime.strptime(fecha_hasta, '%m-%d-%Y')
        sql_query = f"SELECT * FROM `vi_reporte_ventas` WHERE Fecha between '{fecha_desde}' and '{fecha_hasta}'"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        all = self.cursor.fetchall()
        if len(all) > 0:
            r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in all]
            print(f'response from mySQL: {r}')

            # Convert datetime to string reperesentation for JSON
            for idx, response in enumerate(r):
                r[idx]['Fecha'] = response['Fecha'].strftime("%m-%d-%Y %H:%M:%S")
                r[idx]['cantidad'] = float(response['cantidad'])
                r[idx]['total Bs'] = float(response['total Bs'])
            print(f'formatted response from mySQL: {r}')

            return jsonify(r)
        return jsonify({"message": "ventas no encontradas"})

    def listar_reporte_ventas_con_producto(self, fecha_desde, fecha_hasta, id_producto):
        fecha_desde = datetime.strptime(fecha_desde, '%m-%d-%Y')
        fecha_hasta = datetime.strptime(fecha_hasta, '%m-%d-%Y')
        sql_query = f"SELECT * FROM `vi_reporte_ventas` WHERE Fecha between '{fecha_desde}' and '{fecha_hasta}' and " \
                    f"id_producto = {id_producto}"
        print(f'sending query to mySQL: {sql_query}')
        self.cursor.execute(sql_query)
        all = self.cursor.fetchall()
        if len(all) > 0:
            r = [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in all]
            print(f'response from mySQL: {r}')

            # Convert datetime to string reperesentation for JSON
            for idx, response in enumerate(r):
                r[idx]['Fecha'] = response['Fecha'].strftime("%m-%d-%Y %H:%M:%S")
                r[idx]['cantidad'] = float(response['cantidad'])
                r[idx]['total Bs'] = float(response['total Bs'])
            print(f'formatted response from mySQL: {r}')

            return jsonify(r)
        return jsonify({"message": "ventas no encontradas"})