# Introducción a JavaScript moderno

Antes de estudiar bibliotecas y marcos de trabajo conviene recuperar el papel de JavaScript como lenguaje central del frontend. En el ecosistema actual, buena parte de las herramientas que se utilizan para construir interfaces modernas se apoyan en las capacidades del lenguaje, en su evolución reciente y en prácticas de escritura más claras y mantenibles.

Este capítulo ofrece una base común para el resto del libro. No busca revisar todo JavaScript desde cero, sino organizar aquellos conceptos que resultan más importantes para comprender el trabajo posterior con asincronía, componentes, estado y consumo de datos.

## Objetivos del capítulo

- reconocer el lugar de JavaScript en el desarrollo web actual;
- repasar rasgos centrales de la sintaxis moderna del lenguaje;
- distinguir prácticas heredadas de enfoques más actuales;
- preparar el marco conceptual para los capítulos siguientes.

## Contenidos mínimos

### JavaScript en el navegador y fuera del navegador

Conviene distinguir el lenguaje de sus entornos de ejecución. JavaScript se ejecuta en el navegador, pero también en otros entornos como Node.js. Esa diferencia será importante más adelante cuando se trabaje con herramientas de desarrollo y proyectos React.

### Variables, funciones y alcance

Se recuperan nociones de `let`, `const`, funciones flecha y alcance léxico, porque forman parte de la escritura cotidiana de código moderno.

### Objetos, arreglos y desestructuración

Se revisan las estructuras de datos más habituales y operaciones frecuentes como desestructuración, spread y transformaciones básicas de colecciones.

### Módulos y organización del código

Se introduce la idea de módulos como forma de separar responsabilidades y mejorar la organización del proyecto.

## Relación con el proyecto integrador

La aplicación e-commerce requerirá manejar datos, transformar listas de productos, organizar funciones y trabajar con módulos. Por ese motivo, esta base conceptual atraviesa casi todo el libro.

## Cierre

Con este marco resulta más sencillo avanzar hacia uno de los problemas más importantes del desarrollo web actual: cómo trabajar con operaciones asincrónicas sin perder claridad en el código.