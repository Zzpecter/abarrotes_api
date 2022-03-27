import csv
import pymysql

conn = pymysql.connect(host='localhost', user='root', password='tryhard.python', charset='utf8', db='abarrotes_db')
cur = conn.cursor()

# IDS DE DEPARTAMENTOS:
# 1 Beni
# 2 Chuquisaca
# 3 La Paz
# 4 Oruro
# 5 Pando
# 6 Potosí
# 7 Santa Cruz
# 8 Tarija
# 9 Cochabamba

with open('localidades_bolivia.csv', newline='') as csvfile:
    for row in csv.reader(csvfile, delimiter=',', quotechar='|'):
        id_departamento=0
        print(row)
        if row[2].startswith("Beni"):
            id_departamento = 1
        elif row[2].startswith("Chuqui"):
            id_departamento = 2
        elif row[2].startswith("La Paz"):
            id_departamento = 3
        elif row[2].startswith("Oruro"):
            id_departamento = 4
        elif row[2].startswith("Pando"):
            id_departamento = 5
        elif row[2].startswith("Poto"):
            id_departamento = 6
        elif row[2].startswith("Santa"):
            id_departamento = 7
        elif row[2].startswith("Tari"):
            id_departamento = 8
        elif row[2].startswith("Cocha"):
            id_departamento = 9
        nombre_localidad = row[1]
        usuario_registro = "dev"

        print(f'Insertando localidad:\nid_dep: {id_departamento}, nombre: {nombre_localidad}, usr: {usuario_registro}')

        sql_query = f"INSERT INTO localidad (id_departamento, nombre_localidad, usuario_registro) VALUES " \
                    f"({id_departamento}, '{nombre_localidad}', '{usuario_registro}')"
        cur.execute(sql_query)
        conn.commit()

