import pandas as pd

# Leer el archivo CSV
df = pd.read_csv('muertes_y_accidentes_transito_neiva.csv')

# Crear la declaración SQL para crear la tabla
tabla = "CREATE TABLE IF NOT EXISTS muertes_transito (\n"
for column in df.columns:
    # Reemplazar espacios y barras inclinadas con guiones bajos en los nombres de las columnas
    column_name = column.replace(" ", "_").replace("/", "_").replace("(", "_").replace(")", "_").replace(":", "_")   
    tabla += column_name + " TEXT,\n"
tabla = tabla[:-2]  
tabla += ");\n"

print(tabla)

# Crear la declaración SQL para insertar datos en la tabla
insert = "INSERT INTO muertes_transito ("
for column in df.columns:
    # Reemplazar espacios y barras inclinadas con guiones bajos en los nombres de las columnas
    column_name = column.replace(" ", "_").replace("/", "_").replace("(", "_").replace(")", "_").replace(":", "_")     
    insert += column_name + ", "
insert = insert[:-2]  # Eliminar la coma y el espacio extra al final
insert += ") VALUES\n"

# Iterar sobre cada fila del DataFrame
for index, row in df.iterrows():
    # Agregar valores de cada fila al comando INSERT
    insert += "("
    for column in df.columns:
        insert += "'" + str(row[column]) + "', "
    insert = insert[:-2]  # Eliminar la coma y el espacio extra al final
    insert += "),\n"

insert = insert[:-2]  # Eliminar la coma y el espacio extra al final
insert += ";\n"

print(insert)

# Crear el archivo SQL 
with open("sql.sql", "w", encoding="UTF-8") as f:
    f.write(insert)