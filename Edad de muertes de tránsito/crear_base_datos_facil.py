import sqlite3
import pandas as pd

# Conectar a la base de datos SQLite
conn = sqlite3.connect('database.db')

# Configurar el DataFrame para mostrar todas las columnas
pd.set_option('display.max_columns', None)

# Cargar el archivo CSV en un DataFrame
df = pd.read_csv('muertes_y_accidentes_transito_neiva.csv')


# Guardar el DataFrame en la base de datos SQLite
df.to_sql('muertes_y_accidentes_transito_neiva', conn, if_exists='replace', index=False)
