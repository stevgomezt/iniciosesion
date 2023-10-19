-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 20-10-2023 a las 00:45:31
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
(36, 'steven', 99999),
(37, 'juanjo', 7777);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `asesores`
--

CREATE TABLE `asesores` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `numero_documento` int(11) NOT NULL,
  `nombre` text DEFAULT NULL,
  `edad` int(11) DEFAULT NULL,
  `genero` text DEFAULT NULL,
  `estado_civil` text DEFAULT NULL,
  `correo` text DEFAULT NULL,
  `telefono` int(11) DEFAULT NULL,
  `nivel_estudios` text DEFAULT NULL,
  `estrato` int(11) DEFAULT NULL,
  `num_hijos` int(11) DEFAULT NULL,
  `personas_cargo` int(11) DEFAULT NULL,
  `experiencia` int(11) DEFAULT NULL,
  `area_experiencia` int(11) DEFAULT NULL,
  `tiempo_ventas` int(11) DEFAULT NULL,
  `experiencia_general` int(11) DEFAULT NULL,
  `otra_area_experiencia` text DEFAULT NULL,
  `nombre_asesor` text DEFAULT NULL,
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

INSERT INTO `asesores` (`id`, `numero_documento`, `nombre`, `edad`, `genero`, `estado_civil`, `correo`, `telefono`, `nivel_estudios`, `estrato`, `num_hijos`, `personas_cargo`, `experiencia`, `area_experiencia`, `tiempo_ventas`, `experiencia_general`, `otra_area_experiencia`, `nombre_asesor`, `perfil_natural_r`, `perfil_natural_e`, `perfil_natural_p`, `perfil_natural_n`, `perfil_natural_a`, `perfil_natural_r_ie`, `perfil_natural_e_ie`, `perfil_natural_p_ie`, `perfil_natural_n_ie`, `perfil_natural_a_ie`, `intensidad_perfil_natural`, `energia_natural`, `perfil_adaptado_r`, `perfil_adaptado_e`, `perfil_adaptado_p`, `perfil_adaptado_n`, `perfil_adaptado_a`, `perfil_adaptado_r_ie`, `perfil_adaptado_e_ie`, `perfil_adaptado_p_ie`, `perfil_adaptado_n_ie`, `perfil_adaptado_a_ie`, `toma_decisiones_adaptado`, `intensidad_perfil_adaptado`, `energia_adaptado`, `equilibrio_de_energia`, `modificacion_perfil`, `tiempo_formulario`, `unidad_tiempo`, `color`, `nombre_perfil`, `eje_dominante`, `perfil`) VALUES
(1, 111111, '111111', 111, '111', '111', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(2, 22222222, '22222', 22222, '22222', '222', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);

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
(1, 'admin', 'pbkdf2:sha256:260000$F68WjspAXM2Vaj65$aa175f1a39e21d0cd968f9e32702043aaaf64eed3272e3663231642ba80e50e2', 'admin');

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
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `numero_documento` (`numero_documento`);

--
-- Indices de la tabla `contacts`
--
ALTER TABLE `contacts`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `numero_documento` (`numero_documento`);

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
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `contacts`
--
ALTER TABLE `contacts`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=162;

--
-- AUTO_INCREMENT de la tabla `user`
--
ALTER TABLE `user`
  MODIFY `id` smallint(3) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
