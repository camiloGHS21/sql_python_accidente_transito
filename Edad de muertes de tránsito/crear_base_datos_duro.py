import sqlite3

conn = sqlite3.connect('prueba.db')

cursor = conn.cursor()

_SQL = """
CREATE TABLE IF NOT EXISTS muertes_transito (
Fecha_y_Hora_del_hecho TEXT,
Fecha_del_hecho TEXT,
Dia_de_la_semana TEXT,
Hora_del_hecho__HH_MM_ TEXT,
Comuna_Corregimiento TEXT,
Tipo_de_via_de_Hechos TEXT,
Clase_de_Accidente TEXT,
Genero TEXT,
Edad TEXT,
Caracteristicas_de_la_victima TEXT,
Vehiculo_de_la_Victima TEXT,
Vehiculo_2_de_la_contraparte TEXT,
Vehiculo_3_de_la_contraparte TEXT,
Vehiculo_4_de_la_contraparte TEXT);
"""
cursor.execute(_SQL)


with open('sql.sql', 'r',encoding="UTF-8") as f:
      cursor.execute(f.read())
      
conn.commit()
conn.close()