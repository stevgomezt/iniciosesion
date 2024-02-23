-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 23-02-2024 a las 22:57:44
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `flask_login`
--

DELIMITER $$
--
-- Procedimientos
--
CREATE DEFINER=`root`@`localhost` PROCEDURE `InsertarDatosAleatorios` ()   BEGIN
    DECLARE contador INT DEFAULT 0;
    WHILE contador < 20 DO
        INSERT INTO asesores(
            tipo_documento,
            numero_documento,
            nombre,
            edad,
            genero,
            estado_civil,
            tipo_vivienda,
            estrato,
            num_hijos,
            personas_cargo,
            correo,
            telefono,
            nivel_estudios,
            experiencia_general,
            area_experiencia,
            tiempo_ventas,
            experiencia,
            otra_area_experiencia,
            perfil_natural_r,
            perfil_natural_e,
            perfil_natural_p,
            perfil_natural_n,
            perfil_natural_a,
            perfil_natural_r_ie,
            perfil_natural_e_ie,
            perfil_natural_p_ie,
            perfil_natural_n_ie,
            perfil_natural_a_ie,
            intensidad_perfil_natural,
            energia_natural,
            perfil_adaptado_r,
            perfil_adaptado_e,
            perfil_adaptado_p,
            perfil_adaptado_n,
            perfil_adaptado_a,
            perfil_adaptado_r_ie,
            perfil_adaptado_e_ie,
            perfil_adaptado_p_ie,
            perfil_adaptado_n_ie,
            perfil_adaptado_a_ie,
            toma_decisiones_adaptado,
            intensidad_perfil_adaptado,
            energia_adaptado,
            equilibrio_de_energia,
            modificacion_perfil,
            tiempo_formulario,
            unidad_tiempo,
            color,
            nombre_perfil,
            eje_dominante,
            perfil
        )
        VALUES (
            CASE WHEN RAND() < 0.5 THEN 'Cedula de ciudadanía' ELSE 'Cedula de extranjería' END,
            FLOOR(100000000 + RAND() * 900000000),
            CONCAT('Usuario', contador),
            DATE_SUB(NOW(), INTERVAL FLOOR(18 + RAND() * 50) YEAR),
            CASE WHEN RAND() < 0.33 THEN 'Masculino' WHEN RAND() < 0.66 THEN 'Femenino' ELSE 'Prefiero no decirlo' END,
            CASE WHEN RAND() < 0.2 THEN 'Soltero/a' WHEN RAND() < 0.4 THEN 'Casado/a' WHEN RAND() < 0.6 THEN 'Union libre' WHEN RAND() < 0.8 THEN 'Separado/a' ELSE 'Divorsiado/a' END,
            CASE WHEN RAND() < 0.33 THEN 'Familiar' WHEN RAND() < 0.66 THEN 'Propia' ELSE 'Alquilada' END,
            FLOOR(1 + RAND() * 6),
            FLOOR(RAND() * 5),
            FLOOR(RAND() * 5),
            CONCAT('usuario', contador, '@ejemplo.com'),
            CONCAT('3', FLOOR(10000000 + RAND() * 90000000)),
            CASE WHEN RAND() < 0.25 THEN 'Bachillerato' WHEN RAND() < 0.5 THEN 'Formación Técnica/Tecnologo' WHEN RAND() < 0.75 THEN 'Formación profesional - Pregrado' ELSE 'Posgrado' END,
            CASE WHEN RAND() < 0.2 THEN 'Sin experiencia' WHEN RAND() < 0.4 THEN 'Menor a 1 año' WHEN RAND() < 0.6 THEN 'Entre 1 y 2 años' WHEN RAND() < 0.8 THEN 'Entre 2 y 4 años' ELSE 'Mayor a 5 años' END,
            CASE WHEN RAND() < 0.2 THEN 'Sin experiencia' WHEN RAND() < 0.4 THEN 'Ventas' WHEN RAND() < 0.6 THEN 'Servicios de atención' WHEN RAND() < 0.8 THEN 'Recuperación y recobro' ELSE 'Back Office (BO)' END,
            CASE WHEN RAND() < 0.2 THEN 'Sin experiencia' WHEN RAND() < 0.4 THEN 'Menor a 1 año' WHEN RAND() < 0.6 THEN 'Entre 1 y 2 años' WHEN RAND() < 0.8 THEN 'Entre 2 y 4 años' ELSE 'Mayor a 5 años' END,
            CASE WHEN RAND() < 0.2 THEN 'Sin experiencia' WHEN RAND() < 0.4 THEN 'Menor a 1 año' WHEN RAND() < 0.6 THEN 'Entre 1 y 2 años' WHEN RAND() < 0.8 THEN 'Entre 2 y 4 años' ELSE 'Mayor a 5 años' END,
            CASE WHEN RAND() < 0.2 THEN 'Áreas administrativas' WHEN RAND() < 0.4 THEN 'Servicio al cliente presencial' WHEN RAND() < 0.6 THEN 'Venta al cliente presencial' ELSE 'Otros' END,
            NULL, 
			NULL, 
			NULL, 
			NULL, 
			NULL, 
			NULL, 
			NULL, 
			NULL, 
			NULL, 
			NULL,
			NULL,
			NULL, 
			NULL, 
			NULL, 
			NULL, 
			NULL, 
			NULL, 
			NULL, 
			NULL, 
			NULL,
			NULL,
			NULL, 
			NULL, 
			NULL, 
			NULL, 
			NULL, 
			NULL,
			NULL,
			NULL, 
			NULL, 
			NULL,
			NULL,
			NULL
        );
        SET contador = contador + 1;
    END WHILE;
END$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `articulos`
--

CREATE TABLE `articulos` (
  `id` int(11) NOT NULL,
  `nombre` varchar(255) DEFAULT NULL,
  `precio` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `articulos`
--

INSERT INTO `articulos` (`id`, `nombre`, `precio`) VALUES
(36, 'steven gomez', 55555);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `asesores`
--

CREATE TABLE `asesores` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `tipo_documento` varchar(250) NOT NULL,
  `numero_documento` varchar(250) NOT NULL,
  `nombre` varchar(250) DEFAULT NULL,
  `edad` varchar(250) DEFAULT NULL,
  `genero` varchar(250) DEFAULT NULL,
  `estado_civil` varchar(250) DEFAULT NULL,
  `correo` varchar(250) DEFAULT NULL,
  `telefono` varchar(250) DEFAULT NULL,
  `nivel_estudios` varchar(250) DEFAULT NULL,
  `tipo_vivienda` varchar(250) DEFAULT NULL,
  `estrato` int(11) DEFAULT NULL,
  `num_hijos` int(11) DEFAULT NULL,
  `personas_cargo` int(11) DEFAULT NULL,
  `experiencia` varchar(250) DEFAULT NULL,
  `area_experiencia` varchar(250) DEFAULT NULL,
  `tiempo_ventas` varchar(250) DEFAULT NULL,
  `experiencia_general` varchar(250) DEFAULT NULL,
  `otra_area_experiencia` varchar(250) DEFAULT NULL,
  `perfil_natural_r` int(11) DEFAULT NULL,
  `perfil_natural_e` int(11) DEFAULT NULL,
  `perfil_natural_p` int(11) DEFAULT NULL,
  `perfil_natural_n` int(11) DEFAULT NULL,
  `perfil_natural_a` int(11) DEFAULT NULL,
  `perfil_natural_r_ie` int(11) DEFAULT NULL,
  `perfil_natural_e_ie` int(11) DEFAULT NULL,
  `perfil_natural_p_ie` int(11) DEFAULT NULL,
  `perfil_natural_n_ie` int(11) DEFAULT NULL,
  `perfil_natural_a_ie` int(11) DEFAULT NULL,
  `intensidad_perfil_natural` int(11) DEFAULT NULL,
  `energia_natural` int(11) DEFAULT NULL,
  `perfil_adaptado_r` int(11) DEFAULT NULL,
  `perfil_adaptado_e` int(11) DEFAULT NULL,
  `perfil_adaptado_p` int(11) DEFAULT NULL,
  `perfil_adaptado_n` int(11) DEFAULT NULL,
  `perfil_adaptado_a` int(11) DEFAULT NULL,
  `perfil_adaptado_r_ie` int(11) DEFAULT NULL,
  `perfil_adaptado_e_ie` int(11) DEFAULT NULL,
  `perfil_adaptado_p_ie` int(11) DEFAULT NULL,
  `perfil_adaptado_n_ie` int(11) DEFAULT NULL,
  `perfil_adaptado_a_ie` int(11) DEFAULT NULL,
  `toma_decisiones_adaptado` int(11) DEFAULT NULL,
  `intensidad_perfil_adaptado` int(11) DEFAULT NULL,
  `energia_adaptado` int(11) DEFAULT NULL,
  `equilibrio_de_energia` int(11) DEFAULT NULL,
  `modificacion_perfil` int(11) DEFAULT NULL,
  `tiempo_formulario` int(11) DEFAULT NULL,
  `unidad_tiempo` text DEFAULT NULL,
  `color` text DEFAULT NULL,
  `nombre_perfil` text DEFAULT NULL,
  `eje_dominante` text DEFAULT NULL,
  `perfil` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `asesores`
--

INSERT INTO `asesores` (`id`, `tipo_documento`, `numero_documento`, `nombre`, `edad`, `genero`, `estado_civil`, `correo`, `telefono`, `nivel_estudios`, `tipo_vivienda`, `estrato`, `num_hijos`, `personas_cargo`, `experiencia`, `area_experiencia`, `tiempo_ventas`, `experiencia_general`, `otra_area_experiencia`, `perfil_natural_r`, `perfil_natural_e`, `perfil_natural_p`, `perfil_natural_n`, `perfil_natural_a`, `perfil_natural_r_ie`, `perfil_natural_e_ie`, `perfil_natural_p_ie`, `perfil_natural_n_ie`, `perfil_natural_a_ie`, `intensidad_perfil_natural`, `energia_natural`, `perfil_adaptado_r`, `perfil_adaptado_e`, `perfil_adaptado_p`, `perfil_adaptado_n`, `perfil_adaptado_a`, `perfil_adaptado_r_ie`, `perfil_adaptado_e_ie`, `perfil_adaptado_p_ie`, `perfil_adaptado_n_ie`, `perfil_adaptado_a_ie`, `toma_decisiones_adaptado`, `intensidad_perfil_adaptado`, `energia_adaptado`, `equilibrio_de_energia`, `modificacion_perfil`, `tiempo_formulario`, `unidad_tiempo`, `color`, `nombre_perfil`, `eje_dominante`, `perfil`) VALUES
(1, 'Cedula de ciudadanía', '409991835', 'Usuario0', '1989-02-20 11:00:41', 'Femenino', 'Divorsiado/a', 'usuario0@ejemplo.com', '394359105', 'Formación Técnica/Tecnologo', 'Propia', 6, 2, 0, 'Menor a 1 año', 'Sin experiencia', 'Menor a 1 año', 'Entre 1 y 2 años', 'Venta al cliente presencial', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(2, 'Cedula de extranjería', '270171312', 'Usuario1', '1997-02-20 11:00:41', 'Femenino', 'Soltero/a', 'usuario1@ejemplo.com', '387128229', 'Formación profesional - Pregrado', 'Familiar', 6, 3, 2, 'Entre 1 y 2 años', 'Servicios de atención', 'Entre 2 y 4 años', 'Entre 1 y 2 años', 'Servicio al cliente presencial', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(3, 'Cedula de ciudadanía', '345806166', 'Usuario2', '1965-02-20 11:00:41', 'Femenino', 'Union libre', 'usuario2@ejemplo.com', '335814654', 'Bachillerato', 'Propia', 4, 1, 0, 'Sin experiencia', 'Servicios de atención', 'Entre 1 y 2 años', 'Sin experiencia', 'Otros', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(4, 'Cedula de ciudadanía', '905356081', 'Usuario3', '1965-02-20 11:00:41', 'Femenino', 'Separado/a', 'usuario3@ejemplo.com', '322732757', 'Formación Técnica/Tecnologo', 'Propia', 1, 3, 1, 'Entre 2 y 4 años', 'Back Office (BO)', 'Menor a 1 año', 'Mayor a 5 años', 'Otros', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(5, 'Cedula de ciudadanía', '302558626', 'Usuario4', '1982-02-20 11:00:41', 'Femenino', 'Union libre', 'usuario4@ejemplo.com', '390890253', 'Formación profesional - Pregrado', 'Familiar', 6, 3, 2, 'Menor a 1 año', 'Ventas', 'Menor a 1 año', 'Sin experiencia', 'Otros', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(6, 'Cedula de extranjería', '578782490', 'Usuario5', '1965-02-20 11:00:41', 'Femenino', 'Union libre', 'usuario5@ejemplo.com', '356621454', 'Formación Técnica/Tecnologo', 'Propia', 4, 0, 1, 'Entre 1 y 2 años', 'Ventas', 'Sin experiencia', 'Mayor a 5 años', 'Servicio al cliente presencial', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(7, 'Cedula de ciudadanía', '150300663', 'Usuario6', '2000-02-20 11:00:41', 'Prefiero no decirlo', 'Casado/a', 'usuario6@ejemplo.com', '327719389', 'Formación profesional - Pregrado', 'Familiar', 2, 4, 0, 'Entre 1 y 2 años', 'Ventas', 'Entre 2 y 4 años', 'Sin experiencia', 'Otros', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(8, 'Cedula de ciudadanía', '864712827', 'Usuario7', '2002-02-20 11:00:41', 'Femenino', 'Casado/a', 'usuario7@ejemplo.com', '311169877', 'Formación profesional - Pregrado', 'Propia', 2, 4, 0, 'Entre 2 y 4 años', 'Recuperación y recobro', 'Entre 1 y 2 años', 'Menor a 1 año', 'Venta al cliente presencial', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(9, 'Cedula de extranjería', '600235399', 'Usuario8', '1985-02-20 11:00:41', 'Femenino', 'Separado/a', 'usuario8@ejemplo.com', '366987114', 'Formación Técnica/Tecnologo', 'Propia', 3, 3, 2, 'Sin experiencia', 'Sin experiencia', 'Entre 1 y 2 años', 'Entre 2 y 4 años', 'Áreas administrativas', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(10, 'Cedula de ciudadanía', '141322833', 'Usuario9', '1988-02-20 11:00:41', 'Femenino', 'Union libre', 'usuario9@ejemplo.com', '383509621', 'Bachillerato', 'Propia', 6, 0, 3, 'Menor a 1 año', 'Servicios de atención', 'Menor a 1 año', 'Entre 1 y 2 años', 'Otros', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(11, 'Cedula de extranjería', '449414418', 'Usuario10', '1986-02-20 11:00:41', 'Femenino', 'Casado/a', 'usuario10@ejemplo.com', '351863235', 'Posgrado', 'Propia', 5, 1, 2, 'Menor a 1 año', 'Sin experiencia', 'Sin experiencia', 'Menor a 1 año', 'Servicio al cliente presencial', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(12, 'Cedula de extranjería', '961291418', 'Usuario11', '2004-02-20 11:00:41', 'Prefiero no decirlo', 'Union libre', 'usuario11@ejemplo.com', '319064345', 'Formación Técnica/Tecnologo', 'Familiar', 2, 4, 4, 'Menor a 1 año', 'Sin experiencia', 'Menor a 1 año', 'Sin experiencia', 'Servicio al cliente presencial', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(13, 'Cedula de ciudadanía', '965082816', 'Usuario12', '1989-02-20 11:00:41', 'Femenino', 'Union libre', 'usuario12@ejemplo.com', '358942438', 'Bachillerato', 'Familiar', 5, 4, 2, 'Menor a 1 año', 'Servicios de atención', 'Menor a 1 año', 'Menor a 1 año', 'Servicio al cliente presencial', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(14, 'Cedula de extranjería', '904640254', 'Usuario13', '1964-02-20 11:00:41', 'Femenino', 'Union libre', 'usuario13@ejemplo.com', '359026752', 'Formación profesional - Pregrado', 'Familiar', 3, 2, 2, 'Menor a 1 año', 'Sin experiencia', 'Sin experiencia', 'Sin experiencia', 'Otros', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(15, 'Cedula de extranjería', '888075362', 'Usuario14', '1981-02-20 11:00:41', 'Femenino', 'Casado/a', 'usuario14@ejemplo.com', '371656689', 'Bachillerato', 'Propia', 5, 0, 3, 'Entre 1 y 2 años', 'Recuperación y recobro', 'Entre 1 y 2 años', 'Menor a 1 año', 'Otros', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(16, 'Cedula de extranjería', '506217524', 'Usuario15', '1995-02-20 11:00:41', 'Femenino', 'Union libre', 'usuario15@ejemplo.com', '390268129', 'Posgrado', 'Familiar', 1, 2, 1, 'Sin experiencia', 'Recuperación y recobro', 'Menor a 1 año', 'Entre 1 y 2 años', 'Servicio al cliente presencial', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(17, 'Cedula de extranjería', '344174506', 'Usuario16', '1964-02-20 11:00:41', 'Prefiero no decirlo', 'Union libre', 'usuario16@ejemplo.com', '357105270', 'Bachillerato', 'Propia', 6, 0, 3, 'Entre 1 y 2 años', 'Servicios de atención', 'Entre 1 y 2 años', 'Menor a 1 año', 'Servicio al cliente presencial', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(18, 'Cedula de ciudadanía', '808511796', 'Usuario17', '1965-02-20 11:00:41', 'Femenino', 'Soltero/a', 'usuario17@ejemplo.com', '340223653', 'Posgrado', 'Familiar', 5, 4, 3, 'Sin experiencia', 'Recuperación y recobro', 'Entre 1 y 2 años', 'Entre 1 y 2 años', 'Otros', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(19, 'Cedula de extranjería', '440994553', 'Usuario18', '1981-02-20 11:00:41', 'Femenino', 'Casado/a', 'usuario18@ejemplo.com', '366984358', 'Bachillerato', 'Familiar', 4, 1, 3, 'Entre 1 y 2 años', 'Ventas', 'Sin experiencia', 'Menor a 1 año', 'Servicio al cliente presencial', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(20, 'Cedula de extranjería', '426214431', 'Usuario19', '1972-02-20 11:00:41', 'Prefiero no decirlo', 'Union libre', 'usuario19@ejemplo.com', '353303865', 'Formación profesional - Pregrado', 'Familiar', 2, 2, 0, 'Entre 1 y 2 años', 'Recuperación y recobro', 'Entre 1 y 2 años', 'Entre 2 y 4 años', 'Venta al cliente presencial', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(21, 'Cedula de ciudadanía', '1053818158', 'stevenson', '1990-01-01', 'Masculino', 'Soltero/a', 'ejemplo@gmail.com', '1', 'Bachillerato', 'Familiar', 1, 1, 1, 'Sin experiencia', 'Sin experiencia', 'Sin experiencia', 'Sin experiencia', 'Áreas administrativas', 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, '1', '1', '1', '1', '1'),
(22, 'Cedula de extranjera', '1053872991', 'Adrian Gomez', '1990-01-31', 'Masculino', 'Soltero/a', 'ejemplo@gmail.com', '0', 'Formación Técnica/Tecnologo', 'Propia', 3, 0, 0, 'Entre 2 y 4 años', 'Servicios de atención', 'Entre 1 y 2 años', 'Menor a 1 año', 'Servicio al cliente presencial', 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, '1', '1', '1', '1', '1');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `contacts`
--

CREATE TABLE `contacts` (
  `id` int(11) NOT NULL,
  `numero_documento` varchar(100) NOT NULL,
  `nombre` varchar(255) DEFAULT NULL,
  `edad` int(11) DEFAULT NULL,
  `genero` varchar(255) DEFAULT NULL,
  `estado_civil` varchar(255) DEFAULT NULL,
  `correo` varchar(255) DEFAULT NULL,
  `telefono` int(11) DEFAULT NULL,
  `nivel_estudios` varchar(255) DEFAULT NULL,
  `estrato` int(11) DEFAULT NULL,
  `num_hijos` int(11) DEFAULT NULL,
  `personas_cargo` int(11) DEFAULT NULL,
  `experiencia` int(11) DEFAULT NULL,
  `area_experiencia` varchar(255) DEFAULT NULL,
  `tiempo_ventas` int(11) DEFAULT NULL,
  `experiencia_general` int(11) DEFAULT NULL,
  `otra_area_experiencia` varchar(255) DEFAULT NULL,
  `pda_color` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `contacts`
--

INSERT INTO `contacts` (`id`, `numero_documento`, `nombre`, `edad`, `genero`, `estado_civil`, `correo`, `telefono`, `nivel_estudios`, `estrato`, `num_hijos`, `personas_cargo`, `experiencia`, `area_experiencia`, `tiempo_ventas`, `experiencia_general`, `otra_area_experiencia`, `pda_color`) VALUES
(132, '00000000103', 'Andres Gomez', 30, 'masculino', 'viudo', 'andres@example.com', 1313131313, 'tecnologo', 2, 0, 0, 2, 'bo', 2, 2, 'servicio al cliente presencial', 'azul y/o verde'),
(133, '00000000104', 'Sara Torres', 28, 'femenino', 'casado', 'sara@example.com', 1414141414, 'tecnologo', 4, 2, 1, 4, 'ventas', 4, 3, 'venta al cliente presencial', 'amarillo y/o verde'),
(134, '00000000105', 'Juan Hernandez', 32, 'masculino', 'casado', 'juan@example.com', 1515151515, 'bachillerato', 2, 0, 0, 2, 'cobranza', 2, 2, 'otros', 'amarillo y/o verde'),
(135, '00000000106', 'Valentina Gomez', 29, 'femenino', 'viudo', 'valentina@example.com', 1616161616, 'tecnologo', 3, 1, 1, 4, 'cobranza', 4, 4, 'venta al cliente presencial', 'azul y/o rojo'),
(136, '00000000107', 'Andres Ramirez', 35, 'masculino', 'divorciado', 'andres@example.com', 1717171717, 'tecnologo', 4, 2, 1, 4, 'ventas', 4, 3, 'otros', 'amarillo y/o azul'),
(137, '00000000108', 'Maria Gomez', 26, 'femenino', 'viudo', 'maria@example.com', 1818181818, 'universitario', 2, 0, 0, 2, 'retencion', 2, 2, 'otros', 'amarillo'),
(138, '00000000109', 'Santiago Torres', 33, 'masculino', 'soltero', 'santiago@example.com', 1919191919, 'bachillerato', 4, 2, 1, 4, 'venta cruzada', 4, 3, 'otros', 'verde'),
(139, '00000000110', 'Valeria Ramirez', 29, 'femenino', 'viudo', 'valeria@example.com', 2020202020, 'universitario', 2, 0, 0, 2, 'retencion', 2, 2, 'otros', 'azul y/o rojo'),
(140, '00000000111', 'Juan Perez', 28, 'masculino', 'divorciado', 'juan@example.com', 2121212121, 'universitario', 3, 1, 1, 4, 'venta cruzada', 4, 4, 'servicio al cliente presencial', 'azul y/o verde'),
(141, '00000000112', 'Maria Gomez', 34, 'femenino', 'viudo', 'maria@example.com', 2147483647, 'universitario', 2, 0, 0, 2, 'cobranza', 2, 2, 'otros', 'azul y/o verde'),
(142, '00000000113', 'Andres Vargas', 27, 'masculino', 'soltero', 'andres@example.com', 2147483647, 'tecnologo', 4, 2, 1, 4, 'cobranza', 4, 3, 'venta al cliente presencial', 'amarillo y/o rojo'),
(143, '00000000114', 'Valentina Ramirez', 35, 'femenino', 'viudo', 'valentina@example.com', 2147483647, 'bachillerato', 2, 0, 0, 2, 'retencion', 2, 2, 'venta al cliente presencial', 'amarillo'),
(144, '00000000115', 'Juan Gomez', 30, 'masculino', 'soltero', 'juan@example.com', 2147483647, 'universitario', 3, 1, 1, 4, 'cobranza', 4, 4, 'servicio al cliente presencial', 'verde'),
(145, '00000000116', 'Maria Torres', 27, 'femenino', 'divorciado', 'maria@example.com', 2147483647, 'tecnico', 4, 2, 1, 4, 'ventas', 4, 3, 'otros', 'verde'),
(146, '00000000117', 'Santiago Ramirez', 34, 'masculino', 'casado', 'santiago@example.com', 2147483647, 'universitario', 2, 0, 0, 2, 'cobranza', 2, 2, 'servicio al cliente presencial', 'azul y/o amarillo'),
(147, '00000000118', 'Valeria Gomez', 27, 'femenino', 'divorciado', 'valeria@example.com', 2147483647, 'universitario', 4, 2, 1, 4, 'servicio al cliente', 4, 3, 'servicio al cliente presencial', 'amarillo y/o rojo'),
(148, '00000000119', 'Andres Torres', 35, 'masculino', 'soltero', 'andres@example.com', 2147483647, 'bachillerato', 2, 0, 0, 2, 'servicio al cliente', 2, 2, 'venta al cliente presencial', 'azul y/o amarillo'),
(149, '00000000120', 'Maria Perez', 27, 'femenino', 'divorciado', 'maria@example.com', 2147483647, 'tecnologo', 4, 2, 1, 4, 'servicio al cliente', 4, 3, 'venta al cliente presencial', 'verde y/o azul'),
(150, '00000000121', 'Santiago Gomez', 34, 'masculino', 'viudo', 'santiago@example.com', 2147483647, 'bachillerato', 2, 0, 0, 2, 'venta cruzada', 2, 2, 'venta al cliente presencial', 'verde y/o azul'),
(151, '00000000122', 'Valentina Ramirez', 30, 'femenino', 'viudo', 'valentina@example.com', 2147483647, 'universitario', 3, 1, 1, 4, 'bo', 4, 4, 'otros', 'verde y/o azul'),
(152, '00000000123', 'Juan Hernandez', 27, 'masculino', 'divorciado', 'juan@example.com', 2147483647, 'universitario', 4, 2, 1, 4, 'servicio al cliente', 4, 3, 'otros', 'azul y/o amarillo'),
(153, '00000000124', 'Maria Gomez', 35, 'femenino', 'casado', 'maria@example.com', 2147483647, 'bachillerato', 2, 0, 0, 2, 'cobranza', 2, 2, 'servicio al cliente presencial', 'verde'),
(154, '00000000125', 'Santiago Vargas', 27, 'masculino', 'viudo', 'santiago@example.com', 2147483647, 'universitario', 4, 2, 1, 4, 'servicio al cliente', 4, 3, 'venta al cliente presencial', 'azul y/o verde'),
(155, '00000000126', 'Valeria Ramirez', 34, 'femenino', 'casado', 'valeria@example.com', 2147483647, 'tecnologo', 2, 0, 0, 2, 'cobranza', 2, 2, 'otros', 'amarillo'),
(156, '00000000127', 'Juan Gomez', 27, 'masculino', 'soltero', 'juan@example.com', 2147483647, 'bachillerato', 4, 2, 1, 4, 'cobranza', 4, 3, 'servicio al cliente presencial', 'amarillo y/o rojo'),
(157, '00000000128', 'Maria Torres', 34, 'femenino', 'casado', 'maria@example.com', 2147483647, 'tecnico', 2, 0, 0, 2, 'venta cruzada', 2, 2, 'venta al cliente presencial', 'verde'),
(158, '00000000129', 'Santiago Ramirez', 28, 'masculino', 'casado', 'santiago@example.com', 2147483647, 'tecnico', 4, 2, 1, 4, 'ventas', 4, 3, 'servicio al cliente presencial', 'azul'),
(159, '00000000130', 'Valentina Gomez', 35, 'femenino', 'viudo', 'valentina@example.com', 2147483647, 'bachillerato', 2, 0, 0, 2, 'servicio al cliente', 2, 2, 'otros', 'azul y/o amarillo'),
(160, '00000000131', 'Juan Torres', 28, 'masculino', 'divorciado', 'juan@example.com', 2147483647, 'tecnologo', 3, 1, 1, 4, 'ventas', 4, 4, 'venta al cliente presencial', 'amarillo y/o rojo'),
(161, '1515631265', 'aaaaaaaaaaaaaaaaaaaaaaaaaaaa', 99, 'femenino', 'soltero', 'l@gmail.o', 2147483647, 'tecnico', 3, 5, 5, 1, 'cobranza', 2, 2, 'otros', 'amarillo');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `datos_evaluacion`
--

CREATE TABLE `datos_evaluacion` (
  `ID` int(11) NOT NULL,
  `Energia_Adaptado` int(11) DEFAULT NULL,
  `Energia_Natural` int(11) DEFAULT NULL,
  `Equilibrio_de_Energia` int(11) DEFAULT NULL,
  `Intensidad_Perfil_Adaptado` int(11) DEFAULT NULL,
  `Intensidad_Perfil_Natural` int(11) DEFAULT NULL,
  `Modificacion_perfil` int(11) DEFAULT NULL,
  `Nombre_Asesor` varchar(255) DEFAULT NULL,
  `Perfil_Adaptado_A` int(11) DEFAULT NULL,
  `Perfil_Adaptado_A_num` int(11) DEFAULT NULL,
  `Perfil_Adaptado_A_IE` int(11) DEFAULT NULL,
  `Perfil_Adaptado_E` int(11) DEFAULT NULL,
  `Perfil_Adaptado_E_num` int(11) DEFAULT NULL,
  `Perfil_Adaptado_E_IE` int(11) DEFAULT NULL,
  `Perfil_Adaptado_N` int(11) DEFAULT NULL,
  `Perfil_Adaptado_N_num` int(11) DEFAULT NULL,
  `Perfil_Adaptado_N_IE` int(11) DEFAULT NULL,
  `Perfil_Adaptado_P` int(11) DEFAULT NULL,
  `Perfil_Adaptado_P_num` int(11) DEFAULT NULL,
  `Perfil_Adaptado_P_IE` int(11) DEFAULT NULL,
  `Perfil_Adaptado_R` int(11) DEFAULT NULL,
  `Perfil_Adaptado_R_num` int(11) DEFAULT NULL,
  `Perfil_Adaptado_R_IE` int(11) DEFAULT NULL,
  `Perfil_Natural_A` int(11) DEFAULT NULL,
  `Perfil_Natural_A_num` int(11) DEFAULT NULL,
  `Perfil_Natural_A_IE` int(11) DEFAULT NULL,
  `Perfil_Natural_E` int(11) DEFAULT NULL,
  `Perfil_Natural_E_num` int(11) DEFAULT NULL,
  `Perfil_Natural_E_IE` int(11) DEFAULT NULL,
  `Perfil_Natural_N` int(11) DEFAULT NULL,
  `Perfil_Natural_N_num` int(11) DEFAULT NULL,
  `Perfil_Natural_N_IE` int(11) DEFAULT NULL,
  `Perfil_Natural_P` int(11) DEFAULT NULL,
  `Perfil_Natural_P_num` int(11) DEFAULT NULL,
  `Perfil_Natural_P_IE` int(11) DEFAULT NULL,
  `Perfil_Natural_R` int(11) DEFAULT NULL,
  `Perfil_Natural_R_num` int(11) DEFAULT NULL,
  `Perfil_Natural_R_IE` int(11) DEFAULT NULL,
  `Tiempo_Formulario` int(11) DEFAULT NULL,
  `Toma_decisiones_Adaptado` int(11) DEFAULT NULL,
  `Toma_decisiones_Natural` int(11) DEFAULT NULL,
  `Unidad_tiempo` varchar(10) DEFAULT NULL,
  `additionalData1` varchar(250) NOT NULL,
  `additionalData2` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `datos_evaluacion`
--

INSERT INTO `datos_evaluacion` (`ID`, `Energia_Adaptado`, `Energia_Natural`, `Equilibrio_de_Energia`, `Intensidad_Perfil_Adaptado`, `Intensidad_Perfil_Natural`, `Modificacion_perfil`, `Nombre_Asesor`, `Perfil_Adaptado_A`, `Perfil_Adaptado_A_num`, `Perfil_Adaptado_A_IE`, `Perfil_Adaptado_E`, `Perfil_Adaptado_E_num`, `Perfil_Adaptado_E_IE`, `Perfil_Adaptado_N`, `Perfil_Adaptado_N_num`, `Perfil_Adaptado_N_IE`, `Perfil_Adaptado_P`, `Perfil_Adaptado_P_num`, `Perfil_Adaptado_P_IE`, `Perfil_Adaptado_R`, `Perfil_Adaptado_R_num`, `Perfil_Adaptado_R_IE`, `Perfil_Natural_A`, `Perfil_Natural_A_num`, `Perfil_Natural_A_IE`, `Perfil_Natural_E`, `Perfil_Natural_E_num`, `Perfil_Natural_E_IE`, `Perfil_Natural_N`, `Perfil_Natural_N_num`, `Perfil_Natural_N_IE`, `Perfil_Natural_P`, `Perfil_Natural_P_num`, `Perfil_Natural_P_IE`, `Perfil_Natural_R`, `Perfil_Natural_R_num`, `Perfil_Natural_R_IE`, `Tiempo_Formulario`, `Toma_decisiones_Adaptado`, `Toma_decisiones_Natural`, `Unidad_tiempo`, `additionalData1`, `additionalData2`) VALUES
(1, 60, 53, 63, 26, 81, 75, 'Ana Constanza Jaramillo Posada', 2, 0, 45, 8, 2, 47, 3, 1, 56, 4, 9, 41, 4, 1, 56, 57, 12, 55, 34, 5, 36, 100, 14, 93, 16, 5, 15, 50, 9, 50, 15, 50, 12, 'min', '', ''),
(2, 60, 53, 63, 26, 81, 75, 'Ana Constanza Jaramillo Posada', 2, 0, 45, 8, 2, 47, 3, 1, 56, 4, 9, 41, 4, 1, 56, 57, 12, 55, 34, 5, 36, 100, 14, 93, 16, 5, 15, 50, 9, 50, 15, 50, 12, 'min', '', ''),
(3, 60, 53, 63, 26, 81, 75, 'Ana Constanza Jaramillo Posada', 2, 0, 45, 8, 2, 47, 3, 1, 56, 4, 9, 41, 4, 1, 56, 57, 12, 55, 34, 5, 36, 100, 14, 93, 16, 5, 15, 50, 9, 50, 15, 50, 12, 'min', '', ''),
(4, 60, 53, 63, 26, 81, 75, 'Ana Constanza Jaramillo Posada', 2, 0, 45, 8, 2, 47, 3, 1, 56, 4, 9, 41, 4, 1, 56, 57, 12, 55, 34, 5, 36, 100, 14, 93, 16, 5, 15, 50, 9, 50, 15, 50, 12, 'min', '', ''),
(5, 60, 53, 63, 26, 81, 75, 'Ana Constanza Jaramillo Posada', 2, 0, 45, 8, 2, 47, 3, 1, 56, 4, 9, 41, 4, 1, 56, 57, 12, 55, 34, 5, 36, 100, 14, 93, 16, 5, 15, 50, 9, 50, 15, 50, 12, 'min', '', ''),
(6, 60, 53, 63, 26, 81, 75, 'Ana Constanza Jaramillo Posada', 2, 0, 45, 8, 2, 47, 3, 1, 56, 4, 9, 41, 4, 1, 56, 57, 12, 55, 34, 5, 36, 100, 14, 93, 16, 5, 15, 50, 9, 50, 15, 50, 12, 'min', '', ''),
(7, 60, 53, 63, 26, 81, 75, 'Ana Constanza Jaramillo Posada', 2, 0, 45, 8, 2, 47, 3, 1, 56, 4, 9, 41, 4, 1, 56, 57, 12, 55, 34, 5, 36, 100, 14, 93, 16, 5, 15, 50, 9, 50, 15, 50, 12, 'min', '', ''),
(8, 60, 53, 63, 26, 81, 75, 'Ana Constanza Jaramillo Posada', 2, 0, 45, 8, 2, 47, 3, 1, 56, 4, 9, 41, 4, 1, 56, 57, 12, 55, 34, 5, 36, 100, 14, 93, 16, 5, 15, 50, 9, 50, 15, 50, 12, 'min', '', ''),
(9, 60, 53, 63, 26, 81, 75, 'Ana Constanza Jaramillo Posada', 2, 0, 45, 8, 2, 47, 3, 1, 56, 4, 9, 41, 4, 1, 56, 57, 12, 55, 34, 5, 36, 100, 14, 93, 16, 5, 15, 50, 9, 50, 15, 50, 12, 'min', '', ''),
(10, 60, 53, 63, 26, 81, 75, 'Ana Constanza Jaramillo Posada', 2, 0, 45, 8, 2, 47, 3, 1, 56, 4, 9, 41, 4, 1, 56, 57, 12, 55, 34, 5, 36, 100, 14, 93, 16, 5, 15, 50, 9, 50, 15, 50, 12, 'min', '', ''),
(11, 60, 53, 63, 26, 81, 75, 'Ana Constanza Jaramillo Posada', 2, 0, 45, 8, 2, 47, 3, 1, 56, 4, 9, 41, 4, 1, 56, 57, 12, 55, 34, 5, 36, 100, 14, 93, 16, 5, 15, 50, 9, 50, 15, 50, 12, 'min', '', ''),
(12, 60, 53, 63, 26, 81, 75, 'Ana Constanza Jaramillo Posada', 2, 0, 45, 8, 2, 47, 3, 1, 56, 4, 9, 41, 4, 1, 56, 57, 12, 55, 34, 5, 36, 100, 14, 93, 16, 5, 15, 50, 9, 50, 15, 50, 12, 'min', '', ''),
(13, 60, 53, 63, 26, 81, 75, 'Ana Constanza Jaramillo Posada', 2, 0, 45, 8, 2, 47, 3, 1, 56, 4, 9, 41, 4, 1, 56, 57, 12, 55, 34, 5, 36, 100, 14, 93, 16, 5, 15, 50, 9, 50, 15, 50, 12, 'min', '', ''),
(14, 60, 53, 63, 26, 81, 75, 'Ana Constanza Jaramillo Posada', 2, 0, 45, 8, 2, 47, 3, 1, 56, 4, 9, 41, 4, 1, 56, 57, 12, 55, 34, 5, 36, 100, 14, 93, 16, 5, 15, 50, 9, 50, 15, 50, 12, 'min', '', ''),
(15, 60, 53, 63, 26, 81, 75, 'Ana Constanza Jaramillo Posada', 2, 0, 45, 8, 2, 47, 3, 1, 56, 4, 9, 41, 4, 1, 56, 57, 12, 55, 34, 5, 36, 100, 14, 93, 16, 5, 15, 50, 9, 50, 15, 50, 12, 'min', '', ''),
(16, 60, 53, 63, 26, 81, 75, 'Ana Constanza Jaramillo Posada', 2, 0, 45, 8, 2, 47, 3, 1, 56, 4, 9, 41, 4, 1, 56, 57, 12, 55, 34, 5, 36, 100, 14, 93, 16, 5, 15, 50, 9, 50, 15, 50, 12, 'min', 'additionalData1', 'additionalData1'),
(17, 60, 53, 63, 26, 81, 75, 'Ana Constanza Jaramillo Posada', 2, 0, 45, 8, 2, 47, 3, 1, 56, 4, 9, 41, 4, 1, 56, 57, 12, 55, 34, 5, 36, 100, 14, 93, 16, 5, 15, 50, 9, 50, 15, 50, 12, 'min', '1', '1'),
(18, 60, 53, 63, 26, 81, 75, 'Ana Constanza Jaramillo Posada', 2, 0, 45, 8, 2, 47, 3, 1, 56, 4, 9, 41, 4, 1, 56, 57, 12, 55, 34, 5, 36, 100, 14, 93, 16, 5, 15, 50, 9, 50, 15, 50, 12, 'min', '1', '1'),
(19, 60, 53, 63, 26, 81, 75, 'Ana Constanza Jaramillo Posada', 2, 0, 45, 8, 2, 47, 3, 1, 56, 4, 9, 41, 4, 1, 56, 57, 12, 55, 34, 5, 36, 100, 14, 93, 16, 5, 15, 50, 9, 50, 15, 50, 12, 'min', '', ''),
(20, 60, 53, 63, 26, 81, 75, 'Ana Constanza Jaramillo Posada', 2, 0, 45, 8, 2, 47, 3, 1, 56, 4, 9, 41, 4, 1, 56, 57, 12, 55, 34, 5, 36, 100, 14, 93, 16, 5, 15, 50, 9, 50, 15, 50, 12, 'min', '', ''),
(21, 60, 53, 63, 26, 81, 75, 'Ana Constanza Jaramillo Posada', 2, 0, 45, 8, 2, 47, 3, 1, 56, 4, 9, 41, 4, 1, 56, 57, 12, 55, 34, 5, 36, 100, 14, 93, 16, 5, 15, 50, 9, 50, 15, 50, 12, 'min', '', ''),
(22, 60, 53, 63, 26, 81, 75, 'Ana Constanza Jaramillo Posada', 2, 0, 45, 8, 2, 47, 3, 1, 56, 4, 9, 41, 4, 1, 56, 57, 12, 55, 34, 5, 36, 100, 14, 93, 16, 5, 15, 50, 9, 50, 15, 50, 12, 'min', '', ''),
(23, 60, 53, 63, 26, 81, 75, 'Ana Constanza Jaramillo Posada', 2, 0, 45, 8, 2, 47, 3, 1, 56, 4, 9, 41, 4, 1, 56, 57, 12, 55, 34, 5, 36, 100, 14, 93, 16, 5, 15, 50, 9, 50, 15, 50, 12, 'min', 'additionalData1', 'additionalData2'),
(24, 60, 53, 63, 26, 81, 75, 'Ana Constanza Jaramillo Posada', 2, 0, 45, 8, 2, 47, 3, 1, 56, 4, 9, 41, 4, 1, 56, 57, 12, 55, 34, 5, 36, 100, 14, 93, 16, 5, 15, 50, 9, 50, 15, 50, 12, 'min', 'additionalData1', 'additionalData2'),
(25, 60, 53, 63, 26, 81, 75, 'Ana Constanza Jaramillo Posada', 2, 0, 45, 8, 2, 47, 3, 1, 56, 4, 9, 41, 4, 1, 56, 57, 12, 55, 34, 5, 36, 100, 14, 93, 16, 5, 15, 50, 9, 50, 15, 50, 12, 'min', 'additionalData1', 'additionalData2'),
(26, 60, 53, 63, 26, 81, 75, 'Ana Constanza Jaramillo Posada', 2, 0, 45, 8, 2, 47, 3, 1, 56, 4, 9, 41, 4, 1, 56, 57, 12, 55, 34, 5, 36, 100, 14, 93, 16, 5, 15, 50, 9, 50, 15, 50, 12, 'min', 'additionalData1', 'additionalData2'),
(27, 60, 53, 63, 26, 81, 75, 'Ana Constanza Jaramillo Posada', 2, 0, 45, 8, 2, 47, 3, 1, 56, 4, 9, 41, 4, 1, 56, 57, 12, 55, 34, 5, 36, 100, 14, 93, 16, 5, 15, 50, 9, 50, 15, 50, 12, 'min', '1', '2'),
(28, 60, 53, 63, 26, 81, 75, 'Ana Constanza Jaramillo Posada', 2, 0, 45, 8, 2, 47, 3, 1, 56, 4, 9, 41, 4, 1, 56, 57, 12, 55, 34, 5, 36, 100, 14, 93, 16, 5, 15, 50, 9, 50, 15, 50, 12, 'min', '1', '2'),
(29, 60, 53, 63, 26, 81, 75, 'Ana Constanza Jaramillo Posada', 2, 0, 45, 8, 2, 47, 3, 1, 56, 4, 9, 41, 4, 1, 56, 57, 12, 55, 34, 5, 36, 100, 14, 93, 16, 5, 15, 50, 9, 50, 15, 50, 12, 'min', '1', '1'),
(30, 60, 53, 63, 26, 81, 75, 'Ana Constanza Jaramillo Posada', 2, 0, 45, 8, 2, 47, 3, 1, 56, 4, 9, 41, 4, 1, 56, 57, 12, 55, 34, 5, 36, 100, 14, 93, 16, 5, 15, 50, 9, 50, 15, 50, 12, 'min', '1', '2'),
(31, 60, 53, 63, 26, 81, 75, 'Ana Constanza Jaramillo Posada', 2, 0, 45, 8, 2, 47, 3, 1, 56, 4, 9, 41, 4, 1, 56, 57, 12, 55, 34, 5, 36, 100, 14, 93, 16, 5, 15, 50, 9, 50, 15, 50, 12, 'min', '1', '2'),
(32, 60, 53, 63, 26, 81, 75, 'Ana Constanza Jaramillo Posada', 2, 0, 45, 8, 2, 47, 3, 1, 56, 4, 9, 41, 4, 1, 56, 57, 12, 55, 34, 5, 36, 100, 14, 93, 16, 5, 15, 50, 9, 50, 15, 50, 12, 'min', '1', '2');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `posts`
--

CREATE TABLE `posts` (
  `id` int(11) NOT NULL,
  `userId` int(11) DEFAULT NULL,
  `title` varchar(255) DEFAULT NULL,
  `body` text DEFAULT NULL,
  `campo1` varchar(255) DEFAULT NULL,
  `campo2` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `posts`
--

INSERT INTO `posts` (`id`, `userId`, `title`, `body`, `campo1`, `campo2`) VALUES
(1, 1, 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit', 'quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto', 'test', 'test2'),
(2, 1, 'qui est esse', 'est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla', 'test', 'test2'),
(3, 1, 'ea molestias quasi exercitationem repellat qui ipsa sit aut', 'et iusto sed quo iure\nvoluptatem occaecati omnis eligendi aut ad\nvoluptatem doloribus vel accusantium quis pariatur\nmolestiae porro eius odio et labore et velit aut', 'test', 'test2'),
(4, 1, 'eum et est occaecati', 'ullam et saepe reiciendis voluptatem adipisci\nsit amet autem assumenda provident rerum culpa\nquis hic commodi nesciunt rem tenetur doloremque ipsam iure\nquis sunt voluptatem rerum illo velit', 'test', 'test2'),
(5, 1, 'nesciunt quas odio', 'repudiandae veniam quaerat sunt sed\nalias aut fugiat sit autem sed est\nvoluptatem omnis possimus esse voluptatibus quis\nest aut tenetur dolor neque', 'test', 'test2'),
(6, 1, 'dolorem eum magni eos aperiam quia', 'ut aspernatur corporis harum nihil quis provident sequi\nmollitia nobis aliquid molestiae\nperspiciatis et ea nemo ab reprehenderit accusantium quas\nvoluptate dolores velit et doloremque molestiae', 'test', 'test2'),
(7, 1, 'magnam facilis autem', 'dolore placeat quibusdam ea quo vitae\nmagni quis enim qui quis quo nemo aut saepe\nquidem repellat excepturi ut quia\nsunt ut sequi eos ea sed quas', 'test', 'test2'),
(8, 1, 'dolorem dolore est ipsam', 'dignissimos aperiam dolorem qui eum\nfacilis quibusdam animi sint suscipit qui sint possimus cum\nquaerat magni maiores excepturi\nipsam ut commodi dolor voluptatum modi aut vitae', 'test', 'test2'),
(9, 1, 'nesciunt iure omnis dolorem tempora et accusantium', 'consectetur animi nesciunt iure dolore\nenim quia ad\nveniam autem ut quam aut nobis\net est aut quod aut provident voluptas autem voluptas', 'test', 'test2'),
(10, 1, 'optio molestias id quia eum', 'quo et expedita modi cum officia vel magni\ndoloribus qui repudiandae\nvero nisi sit\nquos veniam quod sed accusamus veritatis error', 'test', 'test2'),
(11, 2, 'et ea vero quia laudantium autem', 'delectus reiciendis molestiae occaecati non minima eveniet qui voluptatibus\naccusamus in eum beatae sit\nvel qui neque voluptates ut commodi qui incidunt\nut animi commodi', 'test', 'test2'),
(12, 2, 'in quibusdam tempore odit est dolorem', 'itaque id aut magnam\npraesentium quia et ea odit et ea voluptas et\nsapiente quia nihil amet occaecati quia id voluptatem\nincidunt ea est distinctio odio', 'test', 'test2'),
(13, 2, 'dolorum ut in voluptas mollitia et saepe quo animi', 'aut dicta possimus sint mollitia voluptas commodi quo doloremque\niste corrupti reiciendis voluptatem eius rerum\nsit cumque quod eligendi laborum minima\nperferendis recusandae assumenda consectetur porro architecto ipsum ipsam', 'test', 'test2'),
(14, 2, 'voluptatem eligendi optio', 'fuga et accusamus dolorum perferendis illo voluptas\nnon doloremque neque facere\nad qui dolorum molestiae beatae\nsed aut voluptas totam sit illum', 'test', 'test2'),
(15, 2, 'eveniet quod temporibus', 'reprehenderit quos placeat\nvelit minima officia dolores impedit repudiandae molestiae nam\nvoluptas recusandae quis delectus\nofficiis harum fugiat vitae', 'test', 'test2'),
(16, 2, 'sint suscipit perspiciatis velit dolorum rerum ipsa laboriosam odio', 'suscipit nam nisi quo aperiam aut\nasperiores eos fugit maiores voluptatibus quia\nvoluptatem quis ullam qui in alias quia est\nconsequatur magni mollitia accusamus ea nisi voluptate dicta', 'test', 'test2'),
(17, 2, 'fugit voluptas sed molestias voluptatem provident', 'eos voluptas et aut odit natus earum\naspernatur fuga molestiae ullam\ndeserunt ratione qui eos\nqui nihil ratione nemo velit ut aut id quo', 'test', 'test2'),
(18, 2, 'voluptate et itaque vero tempora molestiae', 'eveniet quo quis\nlaborum totam consequatur non dolor\nut et est repudiandae\nest voluptatem vel debitis et magnam', 'test', 'test2'),
(19, 2, 'adipisci placeat illum aut reiciendis qui', 'illum quis cupiditate provident sit magnam\nea sed aut omnis\nveniam maiores ullam consequatur atque\nadipisci quo iste expedita sit quos voluptas', 'test', 'test2'),
(20, 2, 'doloribus ad provident suscipit at', 'qui consequuntur ducimus possimus quisquam amet similique\nsuscipit porro ipsam amet\neos veritatis officiis exercitationem vel fugit aut necessitatibus totam\nomnis rerum consequatur expedita quidem cumque explicabo', 'test', 'test2'),
(21, 3, 'asperiores ea ipsam voluptatibus modi minima quia sint', 'repellat aliquid praesentium dolorem quo\nsed totam minus non itaque\nnihil labore molestiae sunt dolor eveniet hic recusandae veniam\ntempora et tenetur expedita sunt', 'test', 'test2'),
(22, 3, 'dolor sint quo a velit explicabo quia nam', 'eos qui et ipsum ipsam suscipit aut\nsed omnis non odio\nexpedita earum mollitia molestiae aut atque rem suscipit\nnam impedit esse', 'test', 'test2'),
(23, 3, 'maxime id vitae nihil numquam', 'veritatis unde neque eligendi\nquae quod architecto quo neque vitae\nest illo sit tempora doloremque fugit quod\net et vel beatae sequi ullam sed tenetur perspiciatis', 'test', 'test2'),
(24, 3, 'autem hic labore sunt dolores incidunt', 'enim et ex nulla\nomnis voluptas quia qui\nvoluptatem consequatur numquam aliquam sunt\ntotam recusandae id dignissimos aut sed asperiores deserunt', 'test', 'test2'),
(25, 3, 'rem alias distinctio quo quis', 'ullam consequatur ut\nomnis quis sit vel consequuntur\nipsa eligendi ipsum molestiae et omnis error nostrum\nmolestiae illo tempore quia et distinctio', 'test', 'test2'),
(26, 3, 'est et quae odit qui non', 'similique esse doloribus nihil accusamus\nomnis dolorem fuga consequuntur reprehenderit fugit recusandae temporibus\nperspiciatis cum ut laudantium\nomnis aut molestiae vel vero', 'test', 'test2'),
(27, 3, 'quasi id et eos tenetur aut quo autem', 'eum sed dolores ipsam sint possimus debitis occaecati\ndebitis qui qui et\nut placeat enim earum aut odit facilis\nconsequatur suscipit necessitatibus rerum sed inventore temporibus consequatur', 'test', 'test2'),
(28, 3, 'delectus ullam et corporis nulla voluptas sequi', 'non et quaerat ex quae ad maiores\nmaiores recusandae totam aut blanditiis mollitia quas illo\nut voluptatibus voluptatem\nsimilique nostrum eum', 'test', 'test2'),
(29, 3, 'iusto eius quod necessitatibus culpa ea', 'odit magnam ut saepe sed non qui\ntempora atque nihil\naccusamus illum doloribus illo dolor\neligendi repudiandae odit magni similique sed cum maiores', 'test', 'test2'),
(30, 3, 'a quo magni similique perferendis', 'alias dolor cumque\nimpedit blanditiis non eveniet odio maxime\nblanditiis amet eius quis tempora quia autem rem\na provident perspiciatis quia', 'test', 'test2'),
(31, 4, 'ullam ut quidem id aut vel consequuntur', 'debitis eius sed quibusdam non quis consectetur vitae\nimpedit ut qui consequatur sed aut in\nquidem sit nostrum et maiores adipisci atque\nquaerat voluptatem adipisci repudiandae', 'test', 'test2'),
(32, 4, 'doloremque illum aliquid sunt', 'deserunt eos nobis asperiores et hic\nest debitis repellat molestiae optio\nnihil ratione ut eos beatae quibusdam distinctio maiores\nearum voluptates et aut adipisci ea maiores voluptas maxime', 'test', 'test2'),
(33, 4, 'qui explicabo molestiae dolorem', 'rerum ut et numquam laborum odit est sit\nid qui sint in\nquasi tenetur tempore aperiam et quaerat qui in\nrerum officiis sequi cumque quod', 'test', 'test2'),
(34, 4, 'magnam ut rerum iure', 'ea velit perferendis earum ut voluptatem voluptate itaque iusto\ntotam pariatur in\nnemo voluptatem voluptatem autem magni tempora minima in\nest distinctio qui assumenda accusamus dignissimos officia nesciunt nobis', 'test', 'test2'),
(35, 4, 'id nihil consequatur molestias animi provident', 'nisi error delectus possimus ut eligendi vitae\nplaceat eos harum cupiditate facilis reprehenderit voluptatem beatae\nmodi ducimus quo illum voluptas eligendi\net nobis quia fugit', 'test', 'test2'),
(36, 4, 'fuga nam accusamus voluptas reiciendis itaque', 'ad mollitia et omnis minus architecto odit\nvoluptas doloremque maxime aut non ipsa qui alias veniam\nblanditiis culpa aut quia nihil cumque facere et occaecati\nqui aspernatur quia eaque ut aperiam inventore', 'test', 'test2'),
(37, 4, 'provident vel ut sit ratione est', 'debitis et eaque non officia sed nesciunt pariatur vel\nvoluptatem iste vero et ea\nnumquam aut expedita ipsum nulla in\nvoluptates omnis consequatur aut enim officiis in quam qui', 'test', 'test2'),
(38, 4, 'explicabo et eos deleniti nostrum ab id repellendus', 'animi esse sit aut sit nesciunt assumenda eum voluptas\nquia voluptatibus provident quia necessitatibus ea\nrerum repudiandae quia voluptatem delectus fugit aut id quia\nratione optio eos iusto veniam iure', 'test', 'test2'),
(39, 4, 'eos dolorem iste accusantium est eaque quam', 'corporis rerum ducimus vel eum accusantium\nmaxime aspernatur a porro possimus iste omnis\nest in deleniti asperiores fuga aut\nvoluptas sapiente vel dolore minus voluptatem incidunt ex', 'test', 'test2'),
(40, 4, 'enim quo cumque', 'ut voluptatum aliquid illo tenetur nemo sequi quo facilis\nipsum rem optio mollitia quas\nvoluptatem eum voluptas qui\nunde omnis voluptatem iure quasi maxime voluptas nam', 'test', 'test2'),
(41, 5, 'non est facere', 'molestias id nostrum\nexcepturi molestiae dolore omnis repellendus quaerat saepe\nconsectetur iste quaerat tenetur asperiores accusamus ex ut\nnam quidem est ducimus sunt debitis saepe', 'test', 'test2'),
(42, 5, 'commodi ullam sint et excepturi error explicabo praesentium voluptas', 'odio fugit voluptatum ducimus earum autem est incidunt voluptatem\nodit reiciendis aliquam sunt sequi nulla dolorem\nnon facere repellendus voluptates quia\nratione harum vitae ut', 'test', 'test2'),
(43, 5, 'eligendi iste nostrum consequuntur adipisci praesentium sit beatae perferendis', 'similique fugit est\nillum et dolorum harum et voluptate eaque quidem\nexercitationem quos nam commodi possimus cum odio nihil nulla\ndolorum exercitationem magnam ex et a et distinctio debitis', 'test', 'test2'),
(44, 5, 'optio dolor molestias sit', 'temporibus est consectetur dolore\net libero debitis vel velit laboriosam quia\nipsum quibusdam qui itaque fuga rem aut\nea et iure quam sed maxime ut distinctio quae', 'test', 'test2'),
(45, 5, 'ut numquam possimus omnis eius suscipit laudantium iure', 'est natus reiciendis nihil possimus aut provident\nex et dolor\nrepellat pariatur est\nnobis rerum repellendus dolorem autem', 'test', 'test2'),
(46, 5, 'aut quo modi neque nostrum ducimus', 'voluptatem quisquam iste\nvoluptatibus natus officiis facilis dolorem\nquis quas ipsam\nvel et voluptatum in aliquid', 'test', 'test2'),
(47, 5, 'quibusdam cumque rem aut deserunt', 'voluptatem assumenda ut qui ut cupiditate aut impedit veniam\noccaecati nemo illum voluptatem laudantium\nmolestiae beatae rerum ea iure soluta nostrum\neligendi et voluptate', 'test', 'test2'),
(48, 5, 'ut voluptatem illum ea doloribus itaque eos', 'voluptates quo voluptatem facilis iure occaecati\nvel assumenda rerum officia et\nillum perspiciatis ab deleniti\nlaudantium repellat ad ut et autem reprehenderit', 'test', 'test2'),
(49, 5, 'laborum non sunt aut ut assumenda perspiciatis voluptas', 'inventore ab sint\nnatus fugit id nulla sequi architecto nihil quaerat\neos tenetur in in eum veritatis non\nquibusdam officiis aspernatur cumque aut commodi aut', 'test', 'test2'),
(50, 5, 'repellendus qui recusandae incidunt voluptates tenetur qui omnis exercitationem', 'error suscipit maxime adipisci consequuntur recusandae\nvoluptas eligendi et est et voluptates\nquia distinctio ab amet quaerat molestiae et vitae\nadipisci impedit sequi nesciunt quis consectetur', 'test', 'test2'),
(51, 6, 'soluta aliquam aperiam consequatur illo quis voluptas', 'sunt dolores aut doloribus\ndolore doloribus voluptates tempora et\ndoloremque et quo\ncum asperiores sit consectetur dolorem', 'test', 'test2'),
(52, 6, 'qui enim et consequuntur quia animi quis voluptate quibusdam', 'iusto est quibusdam fuga quas quaerat molestias\na enim ut sit accusamus enim\ntemporibus iusto accusantium provident architecto\nsoluta esse reprehenderit qui laborum', 'test', 'test2'),
(53, 6, 'ut quo aut ducimus alias', 'minima harum praesentium eum rerum illo dolore\nquasi exercitationem rerum nam\nporro quis neque quo\nconsequatur minus dolor quidem veritatis sunt non explicabo similique', 'test', 'test2'),
(54, 6, 'sit asperiores ipsam eveniet odio non quia', 'totam corporis dignissimos\nvitae dolorem ut occaecati accusamus\nex velit deserunt\net exercitationem vero incidunt corrupti mollitia', 'test', 'test2'),
(55, 6, 'sit vel voluptatem et non libero', 'debitis excepturi ea perferendis harum libero optio\neos accusamus cum fuga ut sapiente repudiandae\net ut incidunt omnis molestiae\nnihil ut eum odit', 'test', 'test2'),
(56, 6, 'qui et at rerum necessitatibus', 'aut est omnis dolores\nneque rerum quod ea rerum velit pariatur beatae excepturi\net provident voluptas corrupti\ncorporis harum reprehenderit dolores eligendi', 'test', 'test2'),
(57, 6, 'sed ab est est', 'at pariatur consequuntur earum quidem\nquo est laudantium soluta voluptatem\nqui ullam et est\net cum voluptas voluptatum repellat est', 'test', 'test2'),
(58, 6, 'voluptatum itaque dolores nisi et quasi', 'veniam voluptatum quae adipisci id\net id quia eos ad et dolorem\naliquam quo nisi sunt eos impedit error\nad similique veniam', 'test', 'test2'),
(59, 6, 'qui commodi dolor at maiores et quis id accusantium', 'perspiciatis et quam ea autem temporibus non voluptatibus qui\nbeatae a earum officia nesciunt dolores suscipit voluptas et\nanimi doloribus cum rerum quas et magni\net hic ut ut commodi expedita sunt', 'test', 'test2'),
(60, 6, 'consequatur placeat omnis quisquam quia reprehenderit fugit veritatis facere', 'asperiores sunt ab assumenda cumque modi velit\nqui esse omnis\nvoluptate et fuga perferendis voluptas\nillo ratione amet aut et omnis', 'test', 'test2'),
(61, 7, 'voluptatem doloribus consectetur est ut ducimus', 'ab nemo optio odio\ndelectus tenetur corporis similique nobis repellendus rerum omnis facilis\nvero blanditiis debitis in nesciunt doloribus dicta dolores\nmagnam minus velit', 'test', 'test2'),
(62, 7, 'beatae enim quia vel', 'enim aspernatur illo distinctio quae praesentium\nbeatae alias amet delectus qui voluptate distinctio\nodit sint accusantium autem omnis\nquo molestiae omnis ea eveniet optio', 'test', 'test2'),
(63, 7, 'voluptas blanditiis repellendus animi ducimus error sapiente et suscipit', 'enim adipisci aspernatur nemo\nnumquam omnis facere dolorem dolor ex quis temporibus incidunt\nab delectus culpa quo reprehenderit blanditiis asperiores\naccusantium ut quam in voluptatibus voluptas ipsam dicta', 'test', 'test2'),
(64, 7, 'et fugit quas eum in in aperiam quod', 'id velit blanditiis\neum ea voluptatem\nmolestiae sint occaecati est eos perspiciatis\nincidunt a error provident eaque aut aut qui', 'test', 'test2'),
(65, 7, 'consequatur id enim sunt et et', 'voluptatibus ex esse\nsint explicabo est aliquid cumque adipisci fuga repellat labore\nmolestiae corrupti ex saepe at asperiores et perferendis\nnatus id esse incidunt pariatur', 'test', 'test2'),
(66, 7, 'repudiandae ea animi iusto', 'officia veritatis tenetur vero qui itaque\nsint non ratione\nsed et ut asperiores iusto eos molestiae nostrum\nveritatis quibusdam et nemo iusto saepe', 'test', 'test2'),
(67, 7, 'aliquid eos sed fuga est maxime repellendus', 'reprehenderit id nostrum\nvoluptas doloremque pariatur sint et accusantium quia quod aspernatur\net fugiat amet\nnon sapiente et consequatur necessitatibus molestiae', 'test', 'test2'),
(68, 7, 'odio quis facere architecto reiciendis optio', 'magnam molestiae perferendis quisquam\nqui cum reiciendis\nquaerat animi amet hic inventore\nea quia deleniti quidem saepe porro velit', 'test', 'test2'),
(69, 7, 'fugiat quod pariatur odit minima', 'officiis error culpa consequatur modi asperiores et\ndolorum assumenda voluptas et vel qui aut vel rerum\nvoluptatum quisquam perspiciatis quia rerum consequatur totam quas\nsequi commodi repudiandae asperiores et saepe a', 'test', 'test2'),
(70, 7, 'voluptatem laborum magni', 'sunt repellendus quae\nest asperiores aut deleniti esse accusamus repellendus quia aut\nquia dolorem unde\neum tempora esse dolore', 'test', 'test2'),
(71, 8, 'et iusto veniam et illum aut fuga', 'occaecati a doloribus\niste saepe consectetur placeat eum voluptate dolorem et\nqui quo quia voluptas\nrerum ut id enim velit est perferendis', 'test', 'test2'),
(72, 8, 'sint hic doloribus consequatur eos non id', 'quam occaecati qui deleniti consectetur\nconsequatur aut facere quas exercitationem aliquam hic voluptas\nneque id sunt ut aut accusamus\nsunt consectetur expedita inventore velit', 'test', 'test2'),
(73, 8, 'consequuntur deleniti eos quia temporibus ab aliquid at', 'voluptatem cumque tenetur consequatur expedita ipsum nemo quia explicabo\naut eum minima consequatur\ntempore cumque quae est et\net in consequuntur voluptatem voluptates aut', 'test', 'test2'),
(74, 8, 'enim unde ratione doloribus quas enim ut sit sapiente', 'odit qui et et necessitatibus sint veniam\nmollitia amet doloremque molestiae commodi similique magnam et quam\nblanditiis est itaque\nquo et tenetur ratione occaecati molestiae tempora', 'test', 'test2'),
(75, 8, 'dignissimos eum dolor ut enim et delectus in', 'commodi non non omnis et voluptas sit\nautem aut nobis magnam et sapiente voluptatem\net laborum repellat qui delectus facilis temporibus\nrerum amet et nemo voluptate expedita adipisci error dolorem', 'test', 'test2'),
(76, 8, 'doloremque officiis ad et non perferendis', 'ut animi facere\ntotam iusto tempore\nmolestiae eum aut et dolorem aperiam\nquaerat recusandae totam odio', 'test', 'test2'),
(77, 8, 'necessitatibus quasi exercitationem odio', 'modi ut in nulla repudiandae dolorum nostrum eos\naut consequatur omnis\nut incidunt est omnis iste et quam\nvoluptates sapiente aliquam asperiores nobis amet corrupti repudiandae provident', 'test', 'test2'),
(78, 8, 'quam voluptatibus rerum veritatis', 'nobis facilis odit tempore cupiditate quia\nassumenda doloribus rerum qui ea\nillum et qui totam\naut veniam repellendus', 'test', 'test2'),
(79, 8, 'pariatur consequatur quia magnam autem omnis non amet', 'libero accusantium et et facere incidunt sit dolorem\nnon excepturi qui quia sed laudantium\nquisquam molestiae ducimus est\nofficiis esse molestiae iste et quos', 'test', 'test2'),
(80, 8, 'labore in ex et explicabo corporis aut quas', 'ex quod dolorem ea eum iure qui provident amet\nquia qui facere excepturi et repudiandae\nasperiores molestias provident\nminus incidunt vero fugit rerum sint sunt excepturi provident', 'test', 'test2'),
(81, 9, 'tempora rem veritatis voluptas quo dolores vero', 'facere qui nesciunt est voluptatum voluptatem nisi\nsequi eligendi necessitatibus ea at rerum itaque\nharum non ratione velit laboriosam quis consequuntur\nex officiis minima doloremque voluptas ut aut', 'test', 'test2'),
(82, 9, 'laudantium voluptate suscipit sunt enim enim', 'ut libero sit aut totam inventore sunt\nporro sint qui sunt molestiae\nconsequatur cupiditate qui iste ducimus adipisci\ndolor enim assumenda soluta laboriosam amet iste delectus hic', 'test', 'test2'),
(83, 9, 'odit et voluptates doloribus alias odio et', 'est molestiae facilis quis tempora numquam nihil qui\nvoluptate sapiente consequatur est qui\nnecessitatibus autem aut ipsa aperiam modi dolore numquam\nreprehenderit eius rem quibusdam', 'test', 'test2'),
(84, 9, 'optio ipsam molestias necessitatibus occaecati facilis veritatis dolores aut', 'sint molestiae magni a et quos\neaque et quasi\nut rerum debitis similique veniam\nrecusandae dignissimos dolor incidunt consequatur odio', 'test', 'test2'),
(85, 9, 'dolore veritatis porro provident adipisci blanditiis et sunt', 'similique sed nisi voluptas iusto omnis\nmollitia et quo\nassumenda suscipit officia magnam sint sed tempora\nenim provident pariatur praesentium atque animi amet ratione', 'test', 'test2'),
(86, 9, 'placeat quia et porro iste', 'quasi excepturi consequatur iste autem temporibus sed molestiae beatae\net quaerat et esse ut\nvoluptatem occaecati et vel explicabo autem\nasperiores pariatur deserunt optio', 'test', 'test2'),
(87, 9, 'nostrum quis quasi placeat', 'eos et molestiae\nnesciunt ut a\ndolores perspiciatis repellendus repellat aliquid\nmagnam sint rem ipsum est', 'test', 'test2'),
(88, 9, 'sapiente omnis fugit eos', 'consequatur omnis est praesentium\nducimus non iste\nneque hic deserunt\nvoluptatibus veniam cum et rerum sed', 'test', 'test2'),
(89, 9, 'sint soluta et vel magnam aut ut sed qui', 'repellat aut aperiam totam temporibus autem et\narchitecto magnam ut\nconsequatur qui cupiditate rerum quia soluta dignissimos nihil iure\ntempore quas est', 'test', 'test2'),
(90, 9, 'ad iusto omnis odit dolor voluptatibus', 'minus omnis soluta quia\nqui sed adipisci voluptates illum ipsam voluptatem\neligendi officia ut in\neos soluta similique molestias praesentium blanditiis', 'test', 'test2'),
(91, 10, 'aut amet sed', 'libero voluptate eveniet aperiam sed\nsunt placeat suscipit molestias\nsimilique fugit nam natus\nexpedita consequatur consequatur dolores quia eos et placeat', 'test', 'test2'),
(92, 10, 'ratione ex tenetur perferendis', 'aut et excepturi dicta laudantium sint rerum nihil\nlaudantium et at\na neque minima officia et similique libero et\ncommodi voluptate qui', 'test', 'test2'),
(93, 10, 'beatae soluta recusandae', 'dolorem quibusdam ducimus consequuntur dicta aut quo laboriosam\nvoluptatem quis enim recusandae ut sed sunt\nnostrum est odit totam\nsit error sed sunt eveniet provident qui nulla', 'test', 'test2'),
(94, 10, 'qui qui voluptates illo iste minima', 'aspernatur expedita soluta quo ab ut similique\nexpedita dolores amet\nsed temporibus distinctio magnam saepe deleniti\nomnis facilis nam ipsum natus sint similique omnis', 'test', 'test2'),
(95, 10, 'id minus libero illum nam ad officiis', 'earum voluptatem facere provident blanditiis velit laboriosam\npariatur accusamus odio saepe\ncumque dolor qui a dicta ab doloribus consequatur omnis\ncorporis cupiditate eaque assumenda ad nesciunt', 'test', 'test2'),
(96, 10, 'quaerat velit veniam amet cupiditate aut numquam ut sequi', 'in non odio excepturi sint eum\nlabore voluptates vitae quia qui et\ninventore itaque rerum\nveniam non exercitationem delectus aut', 'test', 'test2'),
(97, 10, 'quas fugiat ut perspiciatis vero provident', 'eum non blanditiis soluta porro quibusdam voluptas\nvel voluptatem qui placeat dolores qui velit aut\nvel inventore aut cumque culpa explicabo aliquid at\nperspiciatis est et voluptatem dignissimos dolor itaque sit nam', 'test', 'test2'),
(98, 10, 'laboriosam dolor voluptates', 'doloremque ex facilis sit sint culpa\nsoluta assumenda eligendi non ut eius\nsequi ducimus vel quasi\nveritatis est dolores', 'test', 'test2'),
(99, 10, 'temporibus sit alias delectus eligendi possimus magni', 'quo deleniti praesentium dicta non quod\naut est molestias\nmolestias et officia quis nihil\nitaque dolorem quia', 'test', 'test2'),
(100, 10, 'at nam consequatur ea labore ea harum', 'cupiditate quo est a modi nesciunt soluta\nipsa voluptas error itaque dicta in\nautem qui minus magnam et distinctio eum\naccusamus ratione error aut', 'test', 'test2');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `user`
--

CREATE TABLE `user` (
  `id` smallint(3) UNSIGNED NOT NULL,
  `username` varchar(20) NOT NULL,
  `password` char(102) NOT NULL,
  `fullname` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='Stores the user''s data.';

--
-- Volcado de datos para la tabla `user`
--

INSERT INTO `user` (`id`, `username`, `password`, `fullname`) VALUES
(1, 'admin', 'pbkdf2:sha256:260000$F68WjspAXM2Vaj65$aa175f1a39e21d0cd968f9e32702043aaaf64eed3272e3663231642ba80e50e2', 'admin'),
(2, 'steven', 'pbkdf2:sha256:260000$QxVwOxzW59ojowTI$00ef267439622531aa238f692f42f92c4dc309fdc02d2aac5b56a4357b81953e', 'Sg');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `articulos`
--
ALTER TABLE `articulos`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `asesores`
--
ALTER TABLE `asesores`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `contacts`
--
ALTER TABLE `contacts`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `numero_documento` (`numero_documento`);

--
-- Indices de la tabla `datos_evaluacion`
--
ALTER TABLE `datos_evaluacion`
  ADD PRIMARY KEY (`ID`);

--
-- Indices de la tabla `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `articulos`
--
ALTER TABLE `articulos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=38;

--
-- AUTO_INCREMENT de la tabla `asesores`
--
ALTER TABLE `asesores`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- AUTO_INCREMENT de la tabla `contacts`
--
ALTER TABLE `contacts`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=162;

--
-- AUTO_INCREMENT de la tabla `datos_evaluacion`
--
ALTER TABLE `datos_evaluacion`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

--
-- AUTO_INCREMENT de la tabla `posts`
--
ALTER TABLE `posts`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=101;

--
-- AUTO_INCREMENT de la tabla `user`
--
ALTER TABLE `user`
  MODIFY `id` smallint(3) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
