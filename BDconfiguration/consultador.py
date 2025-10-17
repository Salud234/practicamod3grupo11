import psycopg2
conexion = psycopg2.connect(
    hots = "localhost",
    port = "5432",
    database = "credenciales",
    user = "Admin",
    password = "p4ssw0rdDB"
)

cursor = conexion.cursor()

cursor.execute("SELEC * FROM usuarios")
registros = cursor.fetchall()

for fila in registros:
    print(fila)

cursor.close()
conexion.close()