# Props y state

En React, una interfaz no solo se compone de piezas. También necesita intercambiar información y actualizarse cuando cambian los datos o las acciones del usuario. Props y state son dos conceptos centrales para comprender esa dinámica.

Este capítulo introduce ambos conceptos como base para construir componentes que no sean solo estáticos, sino capaces de adaptarse a distintas situaciones de uso.

## Objetivos del capítulo

- distinguir entre props y state;
- comprender cómo circula la información entre componentes;
- reconocer el papel del estado local en interfaces dinámicas;
- preparar capítulos posteriores de renderizado y eventos.

## Contenidos mínimos

### Qué son las props

Se presenta a las props como mecanismo para pasar datos y configuraciones entre componentes.

### Qué es el state

Se introduce el state como información interna del componente que puede cambiar a lo largo del tiempo.

### Diferencias y relaciones

Se comparan ambos conceptos para aclarar qué información conviene recibir y cuál conviene administrar localmente.

### Actualización de la interfaz

Se relaciona el cambio de props o state con la actualización declarativa del componente.

## Relación con el proyecto integrador

El proyecto e-commerce necesitará props para transferir datos entre componentes y estado para manejar selección, vistas, formularios y otras interacciones locales.

## Cierre

Con esta base ya es posible estudiar patrones muy frecuentes en la interfaz: el renderizado condicional y la representación de listas.