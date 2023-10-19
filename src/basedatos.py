import pymysql


def dame_conexion():

    return pymysql.connect(
        host='localhost',
        user='admin',
        password='admin',
        db='flask_login')


def insertar_asesor(nombre, precio):

    conexion = dame_conexion()
    with conexion.cursor() as cursor:
        cursor.execute(
            "INSERT INTO articulos(nombre,precio) VALUES (%s, %s)", (nombre, precio))
        conexion.commit()
        conexion.close()


def listar_asesores():
    conexion = dame_conexion()
    asesores = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id, nombre, precio FROM articulos")
        asesores = cursor.fetchall()
        conexion.close()
        return asesores


def eliminar_articulo(id):
    conexion = dame_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM articulos WHERE id = %s", (id))
        conexion.commit()
        conexion.close()


def obtener_articulo(id):
    conexion = dame_conexion()
    articulo = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT id, nombre, precio FROM articulos WHERE id = %s", (id))
        articulo = cursor.fetchone()
        conexion.close()
        return articulo


def actualizar_articulo(id, nombre, precio):
    conexion = dame_conexion()
    with conexion.cursor() as cursor:
        cursor.execute(
            "UPDATE articulos SET nombre = %s, precio = %s WHERE id = %s", (nombre, precio, id))
        conexion.commit()
        conexion.close()


if __name__ == '__main__':
    conexion = dame_conexion()
