import psycopg2
conexion = psycopg2.connect(
    hots = "localhost",
    port = "5432"
    database = "credenciales",
    user = "Admin",
    password = "p4ssw0rdDB"
)

cursor = conexion.cursor()

cursor.execute("SELEC * FROM usuarios")
regsitros = cursor.fetchall()