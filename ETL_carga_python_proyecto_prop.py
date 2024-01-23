import pandas as pd
import time
import datetime
from datetime import datetime

#Extraccion
audiencia=pd.read_excel("https://raw.githubusercontent.com/espadaone/proyecto_prueba_etl/main/PRUEBA/AUDIENCIA%20PRUEBA.xlsx")

#Transformacion
audiencia.columns = audiencia.iloc[0]

audiencia = audiencia.drop(0)

audiencia = audiencia.reset_index(drop=True)

audiencia[["First Name","Last Name","Email Address","Phone Number","Empresa","Segmento","País"]]=audiencia[["First Name","Last Name","Email Address","Phone Number","Empresa","Segmento","País"]].fillna("Sin datos")


audiencia['Customers'] = range(1,len(audiencia)+1)

audiencia = audiencia[['Customers','First Name','Last Name',"Email Address",'Phone Number','Empresa','Segmento','País']]



# ___________________________________________________________
# CARGA A SQL
import pymysql
connection = pymysql.connect(
    host = '',
    user = '',
    password = '',
    db = ''
  )
cursor = connection.cursor()
# Creación de la tabla auditoría
#data_auditoria = {'fecha_creacion': [],'name_table': [], 'quantity_rows_original': [],'quantity_rows_sql': [], 'time_load': [], 'estado': []}
#auditoria = pd.DataFrame(data_auditoria)
# CALLOUT
#start_time = time.time()
# Tuncar las tablas para no perder la configuración
#cursor = connection.cursor()
sql ="truncate table customer"
cursor.execute(sql)
connection.commit()
# Crea una lista de los valores de la Tabla
clientes = audiencia.values.tolist()
# Insertar valores
cursor = connection.cursor()
cursor.executemany("""INSERT INTO customer VALUES (%s,%s,%s,%s,%s,%s,%s,%s)""",clientes)
connection.commit()
#end_time = time.time()
# name_table
#name_table='customer'                                # CAMBIAR NOMBRE DE TABLA
#quantity_rows_original
#quantity_rows_original=callout.shape[0]              # CAMBIAR NOMBRE DE TABLA
#___________________________________________________________
# time
#fecha_creacion = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
#fecha_creacion = str(fecha_creacion)
#quantity_rows_sql
#cursor = connection.cursor()
#sql ="SELECT COUNT(*) FROM "+name_table+""""""
#cursor.execute(sql)
#result = cursor.fetchone()
#quantity_rows_sql=result[0]
#connection.commit()
#time_load
#time_load= round(int(end_time - start_time))
# Estado
#if quantity_rows_original==quantity_rows_sql:
#    estado='Carga Normal'
#else:
#    estado='Carga incompleta'
# Ingesta de resultados de auditoria
#new_audit = {'fecha_creacion': fecha_creacion, 'name_table': name_table, 'quantity_rows_original': quantity_rows_original, 'quantity_rows_sql': quantity_rows_sql, 'time_load': time_load, 'estado': estado }
# add the new row to the DataFrame
#auditoria = auditoria.append(new_audit, ignore_index=True)
connection.close()

