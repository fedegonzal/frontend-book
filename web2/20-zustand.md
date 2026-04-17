# Estado global con Zustand

No toda la información de una aplicación puede quedar encerrada en un único componente. Algunas decisiones de interfaz y ciertos datos deben estar disponibles en varias partes del sistema al mismo tiempo. Cuando esa necesidad aparece, conviene incorporar una solución de estado global que no agregue complejidad innecesaria al recorrido de aprendizaje.

Este capítulo introduce Zustand como herramienta concreta para administrar estado compartido en la aplicación.

## Objetivos del capítulo

- comprender el problema del estado global;
- introducir Zustand como solución simple para compartir estado;
- distinguir estado local de estado global;
- preparar el manejo del carrito y otras estructuras compartidas.

## Contenidos mínimos

### Qué es estado global

Se presenta el problema de los datos que deben ser accedidos o modificados desde varias partes de la aplicación.

### Qué aporta Zustand

Se introduce Zustand como biblioteca ligera orientada a definir stores simples y comprensibles.

### Casos adecuados de uso

Se discute qué tipos de información conviene ubicar en estado global y cuáles deberían permanecer como estado local.

### Organización de stores

Se adelantan criterios básicos para mantener claridad en la definición y uso del store.

## Relación con el proyecto integrador

El carrito de compras, ciertos filtros globales o el estado compartido entre vistas del e-commerce resultan buenos candidatos para trabajar con Zustand.

## Cierre

Con estado local, navegación y estado global ya organizados, el siguiente paso consiste en integrar todo eso al consumo real de datos desde una API.