-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 27-02-2024 a las 22:30:28
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
-- Estructura de tabla para la tabla `asesores`
--

CREATE TABLE `asesores` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `tipo_documento` varchar(250) DEFAULT NULL,
  `numero_documento` varchar(250) DEFAULT NULL,
  `nombre` varchar(250) DEFAULT NULL,
  `edad` varchar(250) DEFAULT NULL,
  `genero` varchar(250) DEFAULT NULL,
  `estado_civil` varchar(250) DEFAULT NULL,
  `correo` varchar(250) DEFAULT NULL,
  `telefono` varchar(250) DEFAULT NULL,
  `nivel_estudios` varchar(250) DEFAULT NULL,
  `tipo_vivienda` varchar(250) DEFAULT NULL,
  `estrato` varchar(250) DEFAULT NULL,
  `num_hijos` varchar(250) DEFAULT NULL,
  `personas_cargo` varchar(250) DEFAULT NULL,
  `experiencia` varchar(250) DEFAULT NULL,
  `area_experiencia` varchar(250) DEFAULT NULL,
  `tiempo_ventas` varchar(250) DEFAULT NULL,
  `experiencia_general` varchar(250) DEFAULT NULL,
  `otra_area_experiencia` varchar(250) DEFAULT NULL,
  `Energia_Adaptado` int(11) DEFAULT NULL,
  `Energia_Natural` int(11) DEFAULT NULL,
  `Equilibrio_de_Energia` int(11) DEFAULT NULL,
  `Intensidad_Perfil_Adaptado` int(11) DEFAULT NULL,
  `Intensidad_Perfil_Natural` int(11) DEFAULT NULL,
  `Modificacion_perfil` int(11) DEFAULT NULL,
  `Nombre_Asesor` varchar(250) DEFAULT NULL,
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
  `Unidad_tiempo` varchar(250) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `asesores`
--

INSERT INTO `asesores` (`id`, `tipo_documento`, `numero_documento`, `nombre`, `edad`, `genero`, `estado_civil`, `correo`, `telefono`, `nivel_estudios`, `tipo_vivienda`, `estrato`, `num_hijos`, `personas_cargo`, `experiencia`, `area_experiencia`, `tiempo_ventas`, `experiencia_general`, `otra_area_experiencia`, `Energia_Adaptado`, `Energia_Natural`, `Equilibrio_de_Energia`, `Intensidad_Perfil_Adaptado`, `Intensidad_Perfil_Natural`, `Modificacion_perfil`, `Nombre_Asesor`, `Perfil_Adaptado_A`, `Perfil_Adaptado_A_num`, `Perfil_Adaptado_A_IE`, `Perfil_Adaptado_E`, `Perfil_Adaptado_E_num`, `Perfil_Adaptado_E_IE`, `Perfil_Adaptado_N`, `Perfil_Adaptado_N_num`, `Perfil_Adaptado_N_IE`, `Perfil_Adaptado_P`, `Perfil_Adaptado_P_num`, `Perfil_Adaptado_P_IE`, `Perfil_Adaptado_R`, `Perfil_Adaptado_R_num`, `Perfil_Adaptado_R_IE`, `Perfil_Natural_A`, `Perfil_Natural_A_num`, `Perfil_Natural_A_IE`, `Perfil_Natural_E`, `Perfil_Natural_E_num`, `Perfil_Natural_E_IE`, `Perfil_Natural_N`, `Perfil_Natural_N_num`, `Perfil_Natural_N_IE`, `Perfil_Natural_P`, `Perfil_Natural_P_num`, `Perfil_Natural_P_IE`, `Perfil_Natural_R`, `Perfil_Natural_R_num`, `Perfil_Natural_R_IE`, `Tiempo_Formulario`, `Toma_decisiones_Adaptado`, `Toma_decisiones_Natural`, `Unidad_tiempo`) VALUES
(6, '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', 60, 53, 63, 26, 81, 75, 'Ana Constanza Jaramillo Posada', 2, 0, 45, 8, 2, 47, 3, 1, 56, 4, 9, 41, 4, 1, 56, 57, 12, 55, 34, 5, 36, 100, 14, 93, 16, 5, 15, 50, 9, 50, 15, 50, 12, 'min'),
(7, 'CC', '1', 'a', '1990-01-01', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', 60, 53, 63, 26, 81, 75, 'Ana Constanza Jaramillo Posada', 2, 0, 45, 8, 2, 47, 3, 1, 56, 4, 9, 41, 4, 1, 56, 57, 12, 55, 34, 5, 36, 100, 14, 93, 16, 5, 15, 50, 9, 50, 15, 50, 12, 'min'),
(8, 'CC', '1', 'a', '1990-01-01', 'masculino', 'soltero', '1@1.com', '1', 'bachillerato', 'familiar', '1', '1', '1', 'sin_experiencia', 'sin_experiencia', 'sin_experiencia', 'sin_experiencia', 'areas administrativas', 60, 53, 63, 26, 81, 75, 'Ana Constanza Jaramillo Posada', 2, 0, 45, 8, 2, 47, 3, 1, 56, 4, 9, 41, 4, 1, 56, 57, 12, 55, 34, 5, 36, 100, 14, 93, 16, 5, 15, 50, 9, 50, 15, 50, 12, 'min'),
(9, 'CC', '1053818158', 'steven gomez', '1994-03-20', 'masculino', 'soltero', 'stevgomezt@gmail.com', '3246671593', 'tecnica_tecnologo', 'familiar', '6', '0', '2', 'sin_experiencia', 'ventas', 'menor_1', 'entre_1_2', 'otros', 60, 53, 63, 26, 81, 75, 'Ana Constanza Jaramillo Posada', 2, 0, 45, 8, 2, 47, 3, 1, 56, 4, 9, 41, 4, 1, 56, 57, 12, 55, 34, 5, 36, 100, 14, 93, 16, 5, 15, 50, 9, 50, 15, 50, 12, 'min');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `datos_evaluacion`
--

CREATE TABLE `datos_evaluacion` (
  `ID` int(11) NOT NULL,
  `tipo_documento` varchar(250) NOT NULL,
  `numero_documento` varchar(250) NOT NULL,
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
  `Unidad_tiempo` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `datos_evaluacion`
--

INSERT INTO `datos_evaluacion` (`ID`, `tipo_documento`, `numero_documento`, `Energia_Adaptado`, `Energia_Natural`, `Equilibrio_de_Energia`, `Intensidad_Perfil_Adaptado`, `Intensidad_Perfil_Natural`, `Modificacion_perfil`, `Nombre_Asesor`, `Perfil_Adaptado_A`, `Perfil_Adaptado_A_num`, `Perfil_Adaptado_A_IE`, `Perfil_Adaptado_E`, `Perfil_Adaptado_E_num`, `Perfil_Adaptado_E_IE`, `Perfil_Adaptado_N`, `Perfil_Adaptado_N_num`, `Perfil_Adaptado_N_IE`, `Perfil_Adaptado_P`, `Perfil_Adaptado_P_num`, `Perfil_Adaptado_P_IE`, `Perfil_Adaptado_R`, `Perfil_Adaptado_R_num`, `Perfil_Adaptado_R_IE`, `Perfil_Natural_A`, `Perfil_Natural_A_num`, `Perfil_Natural_A_IE`, `Perfil_Natural_E`, `Perfil_Natural_E_num`, `Perfil_Natural_E_IE`, `Perfil_Natural_N`, `Perfil_Natural_N_num`, `Perfil_Natural_N_IE`, `Perfil_Natural_P`, `Perfil_Natural_P_num`, `Perfil_Natural_P_IE`, `Perfil_Natural_R`, `Perfil_Natural_R_num`, `Perfil_Natural_R_IE`, `Tiempo_Formulario`, `Toma_decisiones_Adaptado`, `Toma_decisiones_Natural`, `Unidad_tiempo`) VALUES
(1, '123', '456', 60, 53, 63, 26, 81, 75, 'Ana Constanza Jaramillo Posada', 2, 0, 45, 8, 2, 47, 3, 1, 56, 4, 9, 41, 4, 1, 56, 57, 12, 55, 34, 5, 36, 100, 14, 93, 16, 5, 15, 50, 9, 50, 15, 50, 12, 'min'),
(2, '121212', '454545', 60, 53, 63, 26, 81, 75, 'Ana Constanza Jaramillo Posada', 2, 0, 45, 8, 2, 47, 3, 1, 56, 4, 9, 41, 4, 1, 56, 57, 12, 55, 34, 5, 36, 100, 14, 93, 16, 5, 15, 50, 9, 50, 15, 50, 12, 'min'),
(3, '1', '1', 60, 53, 63, 26, 81, 75, 'Ana Constanza Jaramillo Posada', 2, 0, 45, 8, 2, 47, 3, 1, 56, 4, 9, 41, 4, 1, 56, 57, 12, 55, 34, 5, 36, 100, 14, 93, 16, 5, 15, 50, 9, 50, 15, 50, 12, 'min');

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
-- Indices de la tabla `asesores`
--
ALTER TABLE `asesores`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `datos_evaluacion`
--
ALTER TABLE `datos_evaluacion`
  ADD PRIMARY KEY (`ID`);

--
-- Indices de la tabla `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `asesores`
--
ALTER TABLE `asesores`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT de la tabla `datos_evaluacion`
--
ALTER TABLE `datos_evaluacion`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `user`
--
ALTER TABLE `user`
  MODIFY `id` smallint(3) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
