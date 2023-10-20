import pymysql


def dame_conexion():

    return pymysql.connect(
        host='localhost',
        user='admin',
        password='admin',
        db='flask_login')


def insertar_asesor(numero_documento, nombre, edad, genero, estado_civil, correo, telefono, nivel_estudios, estrato, num_hijos, personas_cargo, experiencia, area_experiencia, tiempo_ventas, experiencia_general, otra_area_experiencia):

    conexion = dame_conexion()
    with conexion.cursor() as cursor:
        cursor.execute(
            "INSERT INTO asesores(numero_documento, nombre, edad, genero, estado_civil, correo, telefono, nivel_estudios, estrato, num_hijos, personas_cargo, experiencia, area_experiencia, tiempo_ventas, experiencia_general, otra_area_experiencia) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (numero_documento, nombre, edad, genero, estado_civil, correo, telefono, nivel_estudios, estrato, num_hijos, personas_cargo, experiencia, area_experiencia, tiempo_ventas, experiencia_general, otra_area_experiencia))
        conexion.commit()
        conexion.close()


def listar_asesores():
    conexion = dame_conexion()
    asesores = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id, numero_documento, nombre, edad, genero, estado_civil, correo, telefono, nivel_estudios, estrato, num_hijos, personas_cargo, experiencia, area_experiencia, tiempo_ventas, experiencia_general, otra_area_experiencia FROM asesores")
        asesores = cursor.fetchall()
        conexion.close()
        return asesores


def eliminar_articulo(id):
    conexion = dame_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM asesores WHERE id = %s", (id))
        conexion.commit()
        conexion.close()


def obtener_asesor(id):
    conexion = dame_conexion()
    asesor = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT id, numero_documento, nombre, edad, genero, estado_civil, correo, telefono, nivel_estudios, estrato, num_hijos, personas_cargo, experiencia, area_experiencia, tiempo_ventas, experiencia_general, otra_area_experiencia FROM asesores WHERE id = %s", (id))
        asesor = cursor.fetchone()
        conexion.close()
        return asesor


# def actualizar_asesor(id, nombre, precio):
#     conexion = dame_conexion()
#     with conexion.cursor() as cursor:
#         cursor.execute(
#             "UPDATE articulos SET nombre = %s, precio = %s WHERE id = %s", (id, nombre, precio))
#         conexion.commit()
#         conexion.close()


def actualizar_asesor(id, numero_documento, nombre, edad, genero, estado_civil, correo, telefono, nivel_estudios, estrato, num_hijos, personas_cargo, experiencia, area_experiencia, tiempo_ventas, experiencia_general, otra_area_experiencia):
    conexion = dame_conexion()
    with conexion.cursor() as cursor:
        cursor.execute(
            "UPDATE asesores SET numero_documento= %s, nombre= %s, edad= %s, genero= %s, estado_civil= %s, correo= %s, telefono= %s, nivel_estudios= %s, estrato= %s, num_hijos= %s, personas_cargo= %s, experiencia= %s, area_experiencia= %s, tiempo_ventas= %s, experiencia_general= %s, otra_area_experiencia= %s WHERE id = %s", (numero_documento, nombre, edad, genero, estado_civil, correo, telefono, nivel_estudios, estrato, num_hijos, personas_cargo, experiencia, area_experiencia, tiempo_ventas, experiencia_general, otra_area_experiencia, id))
        conexion.commit()
        conexion.close()


if __name__ == '__main__':
    conexion = dame_conexion()
