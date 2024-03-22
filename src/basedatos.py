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
    # Establece una conexión con la base de datos utilizando la función 'dame_conexion'.
    conexion = dame_conexion()

    # Inicializa una lista vacía para almacenar los asesores que se recuperarán de la base de datos.
    asesores = []

    # Utiliza un manejador de contexto 'with' para trabajar con el cursor de la base de datos.
    # Esto asegura que los recursos, como la conexión y el cursor, se manejen eficientemente
    # y se liberen automáticamente después de completar las operaciones, incluso si ocurre un error.
    with conexion.cursor() as cursor:
        # Define y ejecuta una consulta SQL para obtener todos los registros de la tabla 'asesores',
        # ordenándolos por el campo 'id' de forma descendente. Esto significa que los asesores más recientes
        # aparecerán primero en la lista.
        cursor.execute("SELECT id, tipo_documento, numero_documento, nombre, edad, genero, estado_civil, tipo_vivienda, correo, telefono, nivel_estudios, estrato, num_hijos, personas_cargo, experiencia, area_experiencia, tiempo_ventas, experiencia_general, otra_area_experiencia FROM asesores ORDER BY id DESC")

        # Recupera todos los registros resultantes de la consulta y los asigna a la lista 'asesores'.
        # Cada registro se representa como una tupla de valores.
        asesores = cursor.fetchall()

    # Cierra la conexión a la base de datos. Esto es importante para liberar recursos del sistema
    # y evitar posibles problemas de rendimiento o límites en el número de conexiones.
    conexion.close()

    # Devuelve la lista completa de asesores. Si no se encontraron asesores, la lista estará vacía.
    return asesores


def listar_asesores_excel(search=None, estados_civiles=None, niveles_estudios=None, generos=None, areas_experiencia=None):
    # Establece una conexión con la base de datos utilizando la función 'dame_conexion'.
    conexion = dame_conexion()

    # Inicializa una lista vacía para almacenar los asesores que se recuperarán de la base de datos.
    asesores = []

    # Construye la consulta SQL inicial. La condición 'WHERE 1=1' es un truco utilizado para simplificar
    # la adición de condiciones adicionales a la consulta SQL de manera dinámica.
    query = "SELECT id, tipo_documento, numero_documento, nombre, edad, genero, estado_civil, tipo_vivienda, correo, telefono, nivel_estudios, estrato, num_hijos, personas_cargo, experiencia, area_experiencia, tiempo_ventas, experiencia_general, otra_area_experiencia FROM asesores WHERE 1=1"

    # Inicializa una lista para almacenar los parámetros que se pasarán a la consulta SQL.
    params = []

    # Añade condiciones a la consulta SQL en función de los parámetros proporcionados.
    # Cada condición añadida filtra los resultados de la consulta según los criterios de búsqueda especificados.
    if search:
        query += " AND (numero_documento LIKE %s OR nombre LIKE %s)"
        search_pattern = "%" + search + "%"
        params.extend([search_pattern, search_pattern])

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

    # Intenta ejecutar la consulta con los parámetros y recuperar los resultados.
    try:
        with conexion.cursor() as cursor:
            cursor.execute(query, params)
            # Recupera todos los registros resultantes de la consulta.
            asesores = cursor.fetchall()
    except Exception as e:
        # Captura y maneja cualquier excepción que pueda ocurrir durante la ejecución de la consulta.
        print(f"Ha ocurrido un error: {e}")
    finally:
        # Asegura que la conexión a la base de datos se cierre adecuadamente después de la operación.
        conexion.close()
        # Devuelve la lista de asesores recuperados de la base de datos.
        return asesores


def eliminar_asesor(id):
    # Establece una conexión con la base de datos utilizando la función 'dame_conexion'.
    # Esto garantiza que tengamos una conexión activa a la base de datos para ejecutar nuestra consulta.
    conexion = dame_conexion()

    # Utiliza un manejador de contexto 'with' al trabajar con el cursor.
    # Esto es importante porque garantiza que los recursos del cursor se liberen automáticamente
    # después de que las operaciones de base de datos se hayan completado, incluso si se lanza una excepción.
    with conexion.cursor() as cursor:
        # Prepara y ejecuta una instrucción SQL para eliminar el asesor de la base de datos.
        # El '%s' es un marcador de posición para el ID del asesor que se pasará a la consulta para evitar inyecciones SQL.
        cursor.execute("DELETE FROM asesores WHERE id = %s", (id,))

        # Una vez que la instrucción DELETE se ha ejecutado correctamente, se hace un 'commit' para
        # asegurar que los cambios (la eliminación del registro) se apliquen permanentemente en la base de datos.
        conexion.commit()

    # Después de completar todas las operaciones de base de datos, se cierra la conexión.
    # Esto es crucial para liberar los recursos de la base de datos y evitar problemas de rendimiento.
    conexion.close()


def obtener_asesor(id):
    # Establece una conexión con la base de datos utilizando la función 'dame_conexion'.
    # Esto asegura que tengamos una conexión válida para realizar consultas.
    conexion = dame_conexion()

    # Inicializa la variable 'asesor' a None, que se usará para almacenar la información del asesor si se encuentra en la base de datos.
    asesor = None

    # Usa un manejador de contexto 'with' para trabajar con el cursor de la base de datos.
    # Esto asegura que los recursos se manejen de manera eficiente, cerrando el cursor automáticamente después de su uso.
    with conexion.cursor() as cursor:
        # Define y ejecuta la consulta SQL para obtener los detalles del asesor por su ID.
        # Se utiliza el marcador de posición '%s' para evitar inyecciones SQL y mejorar la seguridad.
        cursor.execute("SELECT id, tipo_documento, numero_documento, nombre, edad, genero, estado_civil, tipo_vivienda, correo, telefono, nivel_estudios, estrato, num_hijos, personas_cargo, experiencia, area_experiencia, tiempo_ventas, experiencia_general, otra_area_experiencia FROM asesores WHERE id = %s", (id,))

        # Intenta obtener el primer resultado de la consulta. Si existe un registro que coincide con el ID,
        # 'fetchone' devuelve una tupla con los datos del asesor; de lo contrario, devuelve None.
        asesor = cursor.fetchone()

    # Después de realizar la consulta, se cierra la conexión a la base de datos para liberar recursos.
    conexion.close()

    # Devuelve los detalles del asesor si se encontraron; de lo contrario, devuelve None.
    # Esto permite al código que llama a esta función saber si se pudo recuperar un asesor con el ID dado.
    return asesor


def actualizar_asesor(id, tipo_documento, numero_documento, nombre, edad, genero, estado_civil, tipo_vivienda, correo, telefono, nivel_estudios, estrato, num_hijos, personas_cargo, experiencia, area_experiencia, tiempo_ventas, experiencia_general, otra_area_experiencia):
    # Establece una conexión con la base de datos usando la función 'dame_conexion'.
    # Esta acción garantiza que tenemos una conexión abierta para realizar las actualizaciones.
    conexion = dame_conexion()

    # Utiliza un manejador de contexto 'with' para asegurar la correcta administración de recursos del cursor.
    # Esto significa que el cursor se cerrará automáticamente al final del bloque 'with', incluso si se produce una excepción.
    with conexion.cursor() as cursor:
        # Prepara y ejecuta la consulta SQL para actualizar los datos del asesor identificado por 'id'.
        # Se utilizan marcadores de posición '%s' para los valores para prevenir inyecciones SQL.
        cursor.execute("""
            UPDATE asesores 
            SET tipo_documento = %s, numero_documento = %s, nombre = %s, edad = %s, genero = %s, estado_civil = %s, 
                tipo_vivienda = %s, correo = %s, telefono = %s, nivel_estudios = %s, estrato = %s, num_hijos = %s, 
                personas_cargo = %s, experiencia = %s, area_experiencia = %s, tiempo_ventas = %s, 
                experiencia_general = %s, otra_area_experiencia = %s 
            WHERE id = %s""",
                       (tipo_documento, numero_documento, nombre, edad, genero, estado_civil, tipo_vivienda, correo,
                        telefono, nivel_estudios, estrato, num_hijos, personas_cargo, experiencia, area_experiencia,
                        tiempo_ventas, experiencia_general, otra_area_experiencia, id))

        # Realiza un 'commit' de la transacción para asegurar que los cambios se apliquen de manera permanente en la base de datos.
        conexion.commit()

    # Cierra la conexión a la base de datos después de completar la actualización.
    # Esto es importante para liberar los recursos de conexión.
    conexion.close()


def listar_asesores_pages(page, per_page, search=None, estados_civiles=None, niveles_estudios=None, generos=None, areas_experiencia=None):
    # Establece una conexión con la base de datos mediante la función 'dame_conexion'.
    conexion = dame_conexion()

    # Calcula los índices de inicio y fin para la paginación basándose en la página actual y la cantidad de resultados por página.
    start = (page - 1) * per_page

    # Prepara una lista vacía para almacenar los parámetros que se pasarán a la consulta SQL,
    # facilitando la adición de filtros de búsqueda de manera segura contra inyecciones SQL.
    params = []

    # Inicia la construcción de la consulta SQL para obtener los asesores.
    # La condición 'WHERE 1=1' facilita la adición de filtros adicionales.
    query = "SELECT * FROM asesores WHERE 1=1"

    # Agrega condiciones dinámicas a la consulta SQL basadas en los criterios de búsqueda proporcionados por el usuario.
    if search:
        # Agrega condiciones para filtrar asesores por número de documento o nombre, usando un patrón de búsqueda.
        query += " AND (numero_documento LIKE %s OR nombre LIKE %s)"
        search_pattern = "%" + search + "%"
        params.extend([search_pattern, search_pattern])

    if estados_civiles:
        # Agrega un filtro por estado civil si se especifica.
        query += " AND estado_civil IN (" + \
            ",".join(["%s"] * len(estados_civiles)) + ")"
        params.extend(estados_civiles)

    if niveles_estudios:
        # Agrega un filtro por nivel de estudios si se especifica.
        query += " AND nivel_estudios IN (" + \
            ",".join(["%s"] * len(niveles_estudios)) + ")"
        params.extend(niveles_estudios)

    if generos:
        # Agrega un filtro por género si se especifica.
        query += " AND genero IN (" + ",".join(["%s"] * len(generos)) + ")"
        params.extend(generos)

    if areas_experiencia:
        # Agrega un filtro por área de experiencia si se especifica.
        query += " AND area_experiencia IN (" + \
            ",".join(["%s"] * len(areas_experiencia)) + ")"
        params.extend(areas_experiencia)

    # Ordena los resultados por 'id' de forma descendente para obtener los registros más recientes primero.
    query += " ORDER BY id DESC"

    # Aplica la paginación a la consulta SQL mediante la cláusula 'LIMIT'.
    query += " LIMIT %s, %s"
    params.extend([start, per_page])

    # Intenta ejecutar la consulta y recuperar los resultados.
    try:
        with conexion.cursor() as cursor:
            cursor.execute(query, params)
            # Recoge todos los asesores que cumplen con los criterios de búsqueda y paginación.
            asesores = cursor.fetchall()
    except Exception as e:
        # Maneja cualquier excepción que pueda surgir durante la ejecución de la consulta, imprimiendo el error.
        print(f"Ha ocurrido el error {e}")
    finally:
        # Asegura que la conexión a la base de datos se cierre después de realizar la consulta.
        conexion.close()
        # Devuelve la lista de asesores.
        return asesores


def count_asesores(search=None, estados_civiles=None, niveles_estudios=None, generos=None, areas_experiencia=None):
    # Establece una conexión con la base de datos usando la función 'dame_conexion'.
    # Esto garantiza que se establece una conexión válida antes de realizar cualquier operación.
    conexion = dame_conexion()

    # Prepara una lista vacía para los parámetros que se utilizarán en la consulta SQL.
    # Esta técnica permite construir consultas SQL dinámicas y seguras.
    params = []

    # Inicia la construcción de la consulta SQL para contar el número total de asesores.
    # La cláusula 'WHERE 1=1' facilita la adición de condiciones adicionales de forma dinámica.
    query = "SELECT COUNT(*) FROM asesores WHERE 1=1"

    # Evalúa y añade condiciones de búsqueda basadas en los argumentos proporcionados.
    # Estas condiciones permiten filtrar los asesores según diversos criterios como número de documento, nombre, etc.
    if search:
        query += " AND (numero_documento LIKE %s OR nombre LIKE %s)"
        search_pattern = "%" + search + "%"
        params.extend([search_pattern, search_pattern])

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

    # Intenta ejecutar la consulta SQL preparada y obtener el total de registros que cumplen con los criterios especificados.
    try:
        with conexion.cursor() as cursor:
            cursor.execute(query, params)
            # Recupera el resultado de la consulta, que es el número total de asesores que cumplen con los criterios.
            total_records = cursor.fetchone()[0]
    except Exception as e:
        # Maneja cualquier excepción que pueda surgir durante la ejecución de la consulta,
        # por ejemplo, errores de sintaxis SQL, problemas de conexión, etc.
        print(f"Ha ocurrido el error {e}")
    finally:
        # Asegura que la conexión con la base de datos se cierre adecuadamente después de la operación.
        conexion.close()
        # Devuelve el número total de registros encontrados.
        return total_records


def existe_numero_documento(numero_documento):
    # Establece una conexión con la base de datos utilizando la función dame_conexion.
    conexion = dame_conexion()
    try:
        # Usa un manejador de contexto para asegurar que el cursor se cierre después de la operación.
        with conexion.cursor() as cursor:
            # Prepara la consulta SQL que cuenta cuántas entradas en la tabla 'asesores' tienen el 'numero_documento' dado.
            query = "SELECT COUNT(*) FROM asesores WHERE numero_documento = %s"
            # Ejecuta la consulta SQL con el número de documento proporcionado.
            cursor.execute(query, (numero_documento,))
            # Recupera el resultado de la consulta, que es el número de registros que coinciden con el número de documento.
            count = cursor.fetchone()[0]
            # Comprueba si existe al menos un asesor con el número de documento dado.
            # Retorna True si el conteo es mayor que 0, lo que significa que ya existe un registro con ese número.
            return count > 0
    except Exception as e:
        # Captura cualquier excepción que pueda ocurrir durante la operación de la base de datos.
        # Imprime el error para propósitos de depuración.
        print(f"Ha ocurrido un error: {e}")
        # Retorna False, indicando que no se pudo verificar si el número de documento existe,
        # generalmente debido a un problema de conexión o de la consulta SQL.
        return False
    finally:
        # Asegura que la conexión a la base de datos se cierre correctamente después de completar la operación.
        conexion.close()


def existe_otro_numero_documento(numero_documento, id):
    # Establece una conexión con la base de datos utilizando la función dame_conexion.
    conexion = dame_conexion()
    try:
        # Utiliza un manejador de contexto para gestionar el cursor de la base de datos.
        # Esto asegura que los recursos se liberen correctamente después de ejecutar la consulta.
        with conexion.cursor() as cursor:
            # Prepara la consulta SQL para contar las entradas en la tabla 'asesores' con el mismo 'numero_documento',
            # excluyendo el registro del asesor con el 'id' especificado. Esto es para evitar falsos positivos
            # cuando un asesor intenta actualizar sus datos sin cambiar su número de documento.
            query = "SELECT COUNT(*) FROM asesores WHERE numero_documento = %s AND id <> %s"
            # Ejecuta la consulta SQL pasando el número de documento y el ID como parámetros.
            cursor.execute(query, (numero_documento, id))
            # Obtiene el resultado de la consulta, que es el número de registros encontrados que cumplen con los criterios.
            count = cursor.fetchone()[0]
            # Devuelve True si se encontró al menos un registro que cumpla los criterios (otro asesor con el mismo número de documento).
            return count > 0
    except Exception as e:
        # Captura y maneja cualquier excepción que ocurra durante el proceso de ejecución de la consulta.
        # Imprime el error para fines de depuración.
        print(f"Ha ocurrido un error: {e}")
        # Retorna False, lo que significa que no se pudo completar la verificación debido al error.
        return False
    finally:
        # Garantiza que la conexión a la base de datos se cierre adecuadamente una vez finalizada la operación.
        # Esto es crucial para prevenir fugas de recursos y mantener la gestión eficiente de la conexión.
        conexion.close()


# if __name__ == '__main__':
#     conexion = dame_conexion()
