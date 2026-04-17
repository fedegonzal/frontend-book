# Hooks fundamentales: useState, useEffect y useContext

Los hooks permiten resolver problemas habituales de las aplicaciones React sin abandonar el modelo de componentes funcionales. Entre ellos, algunos ocupan un lugar especialmente importante porque organizan estado local, efectos y acceso compartido a información dentro del árbol de componentes.

Este capítulo se concentra en tres hooks básicos: `useState`, `useEffect` y `useContext`.

## Objetivos del capítulo

- comprender qué función cumplen los hooks en React;
- usar `useState` para manejar estado local;
- interpretar `useEffect` para efectos y sincronización;
- introducir `useContext` como mecanismo de acceso compartido a datos.

## Contenidos mínimos

### UseState

Se revisa el manejo de estado local como recurso central para construir componentes dinámicos.

### UseEffect

Se introduce la idea de efecto como respuesta a cambios, montaje de componentes o sincronización con recursos externos.

### UseContext

Se presenta el contexto como mecanismo para compartir datos sin prop drilling excesivo en ciertos casos.

### Criterios de uso

Se discute de forma introductoria cuándo conviene usar cada hook y qué problemas puede generar un uso desordenado.

## Relación con el proyecto integrador

Los hooks permitirán manejar filtros, estados de carga, sincronización con la API y acceso compartido a ciertas configuraciones o datos del proyecto.

## Cierre

Una vez incorporados estos hooks fundamentales, conviene estudiar cómo se organiza la navegación en una aplicación React mediante un sistema de rutas.