# Importa pymysql y la extensión MySQL de Flask.
import pymysql
from flask_mysqldb import MySQL

# Inicializa el objeto MySQL para su uso con Flask.
mysql = MySQL()


def dame_conexion():
    # Esta función crea y retorna una nueva conexión a la base de datos MySQL.
    return pymysql.connect(
        host='localhost',      # Dirección del servidor de la base de datos.
        # Nombre de usuario para acceder a la base de datos.
        user='admin',
        password='admin',      # Contraseña para el usuario especificado.
        # Nombre de la base de datos a la que conectarse.
        db='flask_login'
    )


def insertar_asesor(tipo_documento, numero_documento, nombre, edad, genero, estado_civil, correo, telefono, nivel_estudios, tipo_vivienda, estrato, num_hijos, personas_cargo, experiencia, area_experiencia, tiempo_ventas, experiencia_general, otra_area_experiencia, json_data):
    # Establece una conexión con la base de datos.
    conexion = dame_conexion()

    # Utiliza un manejador de contexto para asegurar que los recursos se liberen después de la operación.
    with conexion.cursor() as cursor:
        # Ejecuta una consulta SQL para insertar un nuevo asesor con los datos proporcionados.
        cursor.execute(
            "INSERT INTO asesores (tipo_documento, numero_documento, nombre, edad, genero, estado_civil, correo, telefono, nivel_estudios, tipo_vivienda, estrato, num_hijos, personas_cargo, experiencia , area_experiencia, tiempo_ventas, experiencia_general, otra_area_experiencia, Energia_Adaptado,Energia_Natural,Equilibrio_de_Energia,Intensidad_Perfil_Adaptado,Intensidad_Perfil_Natural,Modificacion_perfil,Nombre_Asesor,Perfil_Adaptado_A,Perfil_Adaptado_A_num,Perfil_Adaptado_A_IE,Perfil_Adaptado_E,Perfil_Adaptado_E_num,Perfil_Adaptado_E_IE,Perfil_Adaptado_N,Perfil_Adaptado_N_num,Perfil_Adaptado_N_IE,Perfil_Adaptado_P,Perfil_Adaptado_P_num,Perfil_Adaptado_P_IE,Perfil_Adaptado_R,Perfil_Adaptado_R_num,Perfil_Adaptado_R_IE,Perfil_Natural_A,Perfil_Natural_A_num,Perfil_Natural_A_IE,Perfil_Natural_E,Perfil_Natural_E_num,Perfil_Natural_E_IE,Perfil_Natural_N,Perfil_Natural_N_num,Perfil_Natural_N_IE,Perfil_Natural_P,Perfil_Natural_P_num,Perfil_Natural_P_IE,Perfil_Natural_R,Perfil_Natural_R_num,Perfil_Natural_R_IE,Tiempo_Formulario,Toma_decisiones_Adaptado,Toma_decisiones_Natural,Unidad_tiempo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            # Parámetros que se pasan a la consulta SQL.
            (tipo_documento,
             numero_documento,
             nombre,
             edad,
             genero,
             estado_civil,
             correo,
             telefono,
             nivel_estudios,
             tipo_vivienda,
             estrato,
             num_hijos,
             personas_cargo,
             experiencia,
             area_experiencia,
             tiempo_ventas,
             experiencia_general,
             otra_area_experiencia,
             json_data.get("Energia Adaptado"),
             json_data.get("Energia Natural"),
             json_data.get("Equilibrio de Energia"),
             json_data.get("Intensidad Perfil Adaptado"),
             json_data.get("Intensidad Perfil Natural"),
             json_data.get("Modificacion perfil"),
             json_data.get("Nombre Asesor"),
             json_data.get("Perfil Adaptado A"),
             json_data.get("Perfil Adaptado A#"),
             json_data.get("Perfil Adaptado A_IE"),
             json_data.get("Perfil Adaptado E"),
             json_data.get("Perfil Adaptado E#"),
             json_data.get("Perfil Adaptado E_IE"),
             json_data.get("Perfil Adaptado N"),
             json_data.get("Perfil Adaptado N#"),
             json_data.get("Perfil Adaptado N_IE"),
             json_data.get("Perfil Adaptado P"),
             json_data.get("Perfil Adaptado P#"),
             json_data.get("Perfil Adaptado P_IE"),
             json_data.get("Perfil Adaptado R"),
             json_data.get("Perfil Adaptado R#"),
             json_data.get("Perfil Adaptado R_IE"),
             json_data.get("Perfil Natural A"),
             json_data.get("Perfil Natural A#"),
             json_data.get("Perfil Natural A_IE"),
             json_data.get("Perfil Natural E"),
             json_data.get("Perfil Natural E#"),
             json_data.get("Perfil Natural E_IE"),
             json_data.get("Perfil Natural N"),
             json_data.get("Perfil Natural N#"),
             json_data.get("Perfil Natural N_IE"),
             json_data.get("Perfil Natural P"),
             json_data.get("Perfil Natural P#"),
             json_data.get("Perfil Natural P_IE"),
             json_data.get("Perfil Natural R"),
             json_data.get("Perfil Natural R#"),
             json_data.get("Perfil Natural R_IE"),
             json_data.get("Tiempo Formulario"),
             json_data.get("Toma decisiones Adaptado"),
             json_data.get("Toma decisiones Natural"),
             json_data.get("Unidad tiempo")))
        # Confirma la transacción.
        conexion.commit()
        # Cierra la conexión a la base de datos.
    conexion.close()


def listar_asesores():
    # Establece una conexión con la base de datos.
    conexion = dame_conexion()

    # Inicializa una lista vacía para almacenar los asesores.
    asesores = []

    # Utiliza un manejador de contexto para asegurar que los recursos se liberen después de la operación.
    with conexion.cursor() as cursor:
        # Ejecuta una consulta SQL para obtener todos los asesores,
        #  ordenados por ID de forma descendente.
        cursor.execute("SELECT id, tipo_documento, numero_documento, nombre, edad, genero, estado_civil, tipo_vivienda, correo, telefono, nivel_estudios, estrato, num_hijos, personas_cargo, experiencia, area_experiencia, tiempo_ventas, experiencia_general, otra_area_experiencia FROM asesores order by id desc")

        # Recupera todos los registros resultantes de la consulta.
        asesores = cursor.fetchall()

    # Cierra la conexión a la base de datos.
    conexion.close()

    # Devuelve la lista de asesores.
    return asesores


def listar_asesores_excel(search=None, estados_civiles=None, niveles_estudios=None, generos=None, areas_experiencia=None):
    # Establece una conexión con la base de datos.
    conexion = dame_conexion()

    # Inicializa una lista vacía para almacenar los asesores.
    asesores = []

    # Comienza a construir la consulta SQL con una condición siempre verdadera para facilitar la adición de filtros.
    query = "SELECT id, tipo_documento, numero_documento, nombre, edad, genero, estado_civil, tipo_vivienda, correo, telefono, nivel_estudios, estrato, num_hijos, personas_cargo, experiencia, area_experiencia, tiempo_ventas, experiencia_general, otra_area_experiencia FROM asesores WHERE 1=1"

    # Lista para almacenar los parámetros de la consulta.
    params = []

    # Añade condiciones a la consulta basadas en los parámetros proporcionados.
    if search:
        # Filtra por número de documento o nombre si se proporciona un término de búsqueda.
        query += " AND (numero_documento LIKE %s OR nombre LIKE %s)"
        search_pattern = "%" + search + "%"
        params.extend([search_pattern, search_pattern])

    if estados_civiles:
        # Filtra por estado civil si se proporciona.
        query += " AND estado_civil IN (" + \
            ",".join(["%s"] * len(estados_civiles)) + ")"
        params.extend(estados_civiles)

    if niveles_estudios:
        # Filtra por nivel de estudios si se proporciona.
        query += " AND nivel_estudios IN (" + \
            ",".join(["%s"] * len(niveles_estudios)) + ")"
        params.extend(niveles_estudios)

    if generos:
        # Filtra por género si se proporciona.
        query += " AND genero IN (" + ",".join(["%s"] * len(generos)) + ")"
        params.extend(generos)

    if areas_experiencia:
        # Filtra por área de experiencia si se proporciona.
        query += " AND area_experiencia IN (" + \
            ",".join(["%s"] * len(areas_experiencia)) + ")"
        params.extend(areas_experiencia)

    try:
        # Ejecuta la consulta con los parámetros.
        with conexion.cursor() as cursor:
            cursor.execute(query, params)
            # Recupera todos los registros resultantes de la consulta.
            asesores = cursor.fetchall()
    except Exception as e:
        # Maneja cualquier excepción que ocurra durante la ejecución de la consulta.
        print(f"Ha ocurrido un error: {e}")
    finally:
        # Cierra la conexión a la base de datos y devuelve los asesores.
        conexion.close()
        return asesores


def eliminar_asesor(id):
    # Establece una conexión con la base de datos.
    conexion = dame_conexion()

    # Utiliza un manejador de contexto para asegurar que los recursos se liberen después de la operación.
    with conexion.cursor() as cursor:
        # Ejecuta una consulta SQL para eliminar el asesor con el ID especificado.
        cursor.execute("DELETE FROM asesores WHERE id = %s", (id,))

        # Confirma (commit) la transacción para asegurar que los cambios se apliquen en la base de datos.
        conexion.commit()

    # Cierra la conexión a la base de datos.
    conexion.close()


def obtener_asesor(id):
    # Establece una conexión con la base de datos.
    conexion = dame_conexion()

    # Inicializa la variable 'asesor' como None. Esto servirá para almacenar la información del asesor si se encuentra.
    asesor = None

    # Utiliza un manejador de contexto para asegurar que los recursos se liberen después de la operación.
    with conexion.cursor() as cursor:
        # Ejecuta una consulta SQL para obtener los detalles del asesor con el ID especificado.
        cursor.execute("SELECT id, tipo_documento, numero_documento, nombre, edad, genero, estado_civil, tipo_vivienda, correo, telefono, nivel_estudios, estrato, num_hijos, personas_cargo, experiencia, area_experiencia, tiempo_ventas, experiencia_general, otra_area_experiencia FROM asesores WHERE id = %s", (id,))

        # Recupera el primer registro (si existe) del resultado de la consulta.
        asesor = cursor.fetchone()

    # Cierra la conexión a la base de datos.
    conexion.close()

    # Devuelve la información del asesor. Será 'None' si no se encontró un asesor con el ID proporcionado.
    return asesor


def actualizar_asesor(id, tipo_documento, numero_documento, nombre, edad, genero, estado_civil, tipo_vivienda, correo, telefono, nivel_estudios, estrato, num_hijos, personas_cargo, experiencia, area_experiencia, tiempo_ventas, experiencia_general, otra_area_experiencia):
    # Establece una conexión con la base de datos.
    conexion = dame_conexion()

    # Utiliza un manejador de contexto para asegurar que los recursos se liberen después de la operación.
    with conexion.cursor() as cursor:
        # Ejecuta una consulta SQL para actualizar los detalles del asesor con el ID especificado.
        cursor.execute("UPDATE asesores SET tipo_documento= %s, numero_documento= %s, nombre= %s, edad= %s, genero= %s, estado_civil= %s, tipo_vivienda= %s, correo= %s, telefono= %s, nivel_estudios= %s, estrato= %s, num_hijos= %s, personas_cargo= %s, experiencia= %s, area_experiencia= %s, tiempo_ventas= %s, experiencia_general= %s, otra_area_experiencia= %s WHERE id = %s",
                       (tipo_documento, numero_documento, nombre, edad, genero, estado_civil, tipo_vivienda, correo, telefono, nivel_estudios, estrato, num_hijos, personas_cargo, experiencia, area_experiencia, tiempo_ventas, experiencia_general, otra_area_experiencia, id))

        # Confirma (commit) la transacción para asegurar que los cambios se apliquen en la base de datos.
        conexion.commit()

    # Cierra la conexión a la base de datos.
    conexion.close()


def listar_asesores_pages(page, per_page, search=None, estados_civiles=None, niveles_estudios=None, generos=None, areas_experiencia=None):
    # Establece una conexión con la base de datos.
    conexion = dame_conexion()

    # Calcula los índices de inicio y fin para la paginación.
    start = (page - 1) * per_page
    end = start + per_page

    # Inicializa una lista para almacenar los parámetros de la consulta SQL.
    params = []

    # Comienza a construir la consulta SQL.
    query = "SELECT * FROM asesores WHERE 1=1"

    # Añade condiciones de búsqueda para 'numero_documento' y 'nombre' si se proporciona un término de búsqueda.
    if search:
        query += " AND (numero_documento LIKE %s OR nombre LIKE %s)"
        search_pattern = "%" + search + "%"
        params.extend([search_pattern, search_pattern])

    # Añade condiciones para filtrar por 'estado_civil', 'nivel_estudios', 'genero', y 'area_experiencia' si se proporcionan.
    if estados_civiles:
        query += " AND estado_civil IN (" + \
            ",".join(["%s"] * len(estados_civiles)) + ")"
        params.extend(estados_civiles)

    if niveles_estudios:
        query += " AND nivel_estudios IN (" + \
            ",".join(["%s"] * len(niveles_estudios)) + ")"
        params.extend(niveles_estudios)

    if generos:
        query += " AND genero IN (" + ",".join(["%s"] * len(generos)) + ")"
        params.extend(generos)

    if areas_experiencia:
        query += " AND area_experiencia IN (" + \
            ",".join(["%s"] * len(areas_experiencia)) + ")"
        params.extend(areas_experiencia)

    # Ordena los resultados por 'id' en orden descendente.
    query += " order by id desc"

    # Añade la cláusula LIMIT para implementar la paginación.
    query += " LIMIT %s, %s"
    params.extend([start, per_page])

    # Inicializa una lista vacía para almacenar los asesores.
    asesores = []

    # Ejecuta la consulta y recupera los resultados.
    try:
        with conexion.cursor() as cursor:
            cursor.execute(query, params)
            asesores = cursor.fetchall()
    except Exception as e:
        print(f"Ha ocurrido el error {e}")
    finally:
        # Cierra la conexión a la base de datos.
        conexion.close()
        return asesores


def count_asesores(search=None, estados_civiles=None, niveles_estudios=None, generos=None, areas_experiencia=None):
    # Establece una conexión con la base de datos.
    conexion = dame_conexion()

    # Inicializa una lista para almacenar los parámetros de la consulta SQL.
    params = []

    # Comienza a construir la consulta SQL para contar asesores.
    query = "SELECT COUNT(*) FROM asesores WHERE 1=1"

    # Añade condiciones de búsqueda para 'numero_documento' y 'nombre' si se proporciona un término de búsqueda.
    if search:
        query += " AND (numero_documento LIKE %s OR nombre LIKE %s)"
        search_pattern = "%" + search + "%"
        params.extend([search_pattern, search_pattern])

    # Añade condiciones para filtrar por 'estado_civil', 'nivel_estudios', 'genero', y 'area_experiencia' si se proporcionan.
    if estados_civiles:
        query += " AND estado_civil IN (" + \
            ",".join(["%s"] * len(estados_civiles)) + ")"
        params.extend(estados_civiles)

    if niveles_estudios:
        query += " AND nivel_estudios IN (" + \
            ",".join(["%s"] * len(niveles_estudios)) + ")"
        params.extend(niveles_estudios)

    if generos:
        query += " AND genero IN (" + ",".join(["%s"] * len(generos)) + ")"
        params.extend(generos)

    if areas_experiencia:
        query += " AND area_experiencia IN (" + \
            ",".join(["%s"] * len(areas_experiencia)) + ")"
        params.extend(areas_experiencia)

    # Variable para almacenar el total de registros encontrados.
    total_records = 0

    # Ejecuta la consulta y recupera el número total de registros.
    try:
        with conexion.cursor() as cursor:
            cursor.execute(query, params)
            # Obtiene el resultado de la consulta (el conteo de registros).
            total_records = cursor.fetchone()[0]
    except Exception as e:
        print(f"Ha ocurrido el error {e}")
    finally:
        # Cierra la conexión a la base de datos.
        conexion.close()
        return total_records


# if __name__ == '__main__':
#     conexion = dame_conexion()
