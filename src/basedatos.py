import pymysql
from flask_mysqldb import MySQL

mysql = MySQL()


def dame_conexion():

    return pymysql.connect(
        host='localhost',
        user='admin',
        password='admin',
        db='flask_login')


def insertar_asesor(numero_documento, nombre, edad, genero, estado_civil, correo, telefono, nivel_estudios, estrato, num_hijos, personas_cargo, experiencia, area_experiencia, tiempo_ventas, experiencia_general, otra_area_experiencia, perfil_natural_r, perfil_natural_e, perfil_natural_p, perfil_natural_n, perfil_natural_a, perfil_natural_r_ie, perfil_natural_e_ie, perfil_natural_p_ie, perfil_natural_n_ie, perfil_natural_a_ie, intensidad_perfil_natural, energia_natural, perfil_adaptado_r, perfil_adaptado_e, perfil_adaptado_p, perfil_adaptado_n, perfil_adaptado_a, perfil_adaptado_r_ie, perfil_adaptado_e_ie, perfil_adaptado_p_ie, perfil_adaptado_n_ie, perfil_adaptado_a_ie, toma_decisiones_adaptado, intensidad_perfil_adaptado, energia_adaptado, equilibrio_de_energia, modificacion_perfil, tiempo_formulario, unidad_tiempo, color, nombre_perfil, eje_dominante, perfil):

    conexion = dame_conexion()
    with conexion.cursor() as cursor:
        cursor.execute(
            "INSERT INTO asesores(numero_documento,nombre,edad,genero,estado_civil,correo,telefono,nivel_estudios,estrato,num_hijos,personas_cargo,experiencia,area_experiencia,tiempo_ventas,experiencia_general,otra_area_experiencia,perfil_natural_r,perfil_natural_e,perfil_natural_p,perfil_natural_n,perfil_natural_a,perfil_natural_r_ie,perfil_natural_e_ie,perfil_natural_p_ie,perfil_natural_n_ie,perfil_natural_a_ie,intensidad_perfil_natural,energia_natural,perfil_adaptado_r,perfil_adaptado_e,perfil_adaptado_p,perfil_adaptado_n,perfil_adaptado_a,perfil_adaptado_r_ie,perfil_adaptado_e_ie,perfil_adaptado_p_ie,perfil_adaptado_n_ie,perfil_adaptado_a_ie,toma_decisiones_adaptado,intensidad_perfil_adaptado,energia_adaptado,equilibrio_de_energia,modificacion_perfil,tiempo_formulario,unidad_tiempo,color,nombre_perfil,eje_dominante,perfil) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (numero_documento, nombre, edad, genero, estado_civil, correo, telefono, nivel_estudios, estrato, num_hijos, personas_cargo, experiencia, area_experiencia, tiempo_ventas, experiencia_general, otra_area_experiencia, perfil_natural_r, perfil_natural_e, perfil_natural_p, perfil_natural_n, perfil_natural_a, perfil_natural_r_ie, perfil_natural_e_ie, perfil_natural_p_ie, perfil_natural_n_ie, perfil_natural_a_ie, intensidad_perfil_natural, energia_natural, perfil_adaptado_r, perfil_adaptado_e, perfil_adaptado_p, perfil_adaptado_n, perfil_adaptado_a, perfil_adaptado_r_ie, perfil_adaptado_e_ie, perfil_adaptado_p_ie, perfil_adaptado_n_ie, perfil_adaptado_a_ie, toma_decisiones_adaptado, intensidad_perfil_adaptado, energia_adaptado, equilibrio_de_energia, modificacion_perfil, tiempo_formulario, unidad_tiempo, color, nombre_perfil, eje_dominante, perfil))
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


def actualizar_asesor(id, numero_documento, nombre, edad, genero, estado_civil, correo, telefono, nivel_estudios, estrato, num_hijos, personas_cargo, experiencia, area_experiencia, tiempo_ventas, experiencia_general, otra_area_experiencia):
    conexion = dame_conexion()
    with conexion.cursor() as cursor:
        cursor.execute(
            "UPDATE asesores SET numero_documento= %s, nombre= %s, edad= %s, genero= %s, estado_civil= %s, correo= %s, telefono= %s, nivel_estudios= %s, estrato= %s, num_hijos= %s, personas_cargo= %s, experiencia= %s, area_experiencia= %s, tiempo_ventas= %s, experiencia_general= %s, otra_area_experiencia= %s WHERE id = %s", (numero_documento, nombre, edad, genero, estado_civil, correo, telefono, nivel_estudios, estrato, num_hijos, personas_cargo, experiencia, area_experiencia, tiempo_ventas, experiencia_general, otra_area_experiencia, id))
        conexion.commit()
        conexion.close()


def listar_asesores(page, per_page):
    start = (page - 1) * per_page
    end = start + per_page
    query = "SELECT * FROM asesores"
    cursor = mysql.connection.cursor()
    cursor.execute(query)
    asesores = cursor.fetchall()
    cursor.close()
    return asesores[start:end]

def count_asesores():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM asesores")
    total_records = cursor.fetchone()[0]
    cursor.close()
    return total_records



if __name__ == '__main__':
    conexion = dame_conexion()
