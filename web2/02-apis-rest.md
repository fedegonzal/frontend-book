# Consumo de APIs REST en aplicaciones web

Las interfaces modernas suelen depender de información que no está escrita de manera fija en el documento, sino que llega desde servicios externos. Por ese motivo, conviene comprender cómo se organiza el intercambio de datos entre una aplicación cliente y una API.

Este capítulo presenta una introducción al consumo de APIs REST, suficiente para interpretar rutas, métodos, respuestas y estructuras de datos que luego serán utilizadas dentro del proyecto integrador.

## Objetivos del capítulo

- reconocer qué función cumple una API en una aplicación web;
- interpretar métodos HTTP y respuestas frecuentes;
- comprender el papel de JSON en el intercambio de datos;
- preparar el trabajo con `fetch` y con APIs reales.

## Contenidos mínimos

### Qué es una API y para qué se usa

Se introduce la API como interfaz de comunicación entre sistemas. En el contexto del frontend, su papel principal consiste en proveer datos y recibir acciones desde la interfaz.

### REST como estilo de intercambio

Se presentan de forma general los principios más visibles del estilo REST: recursos, rutas, métodos y respuestas.

### Métodos HTTP frecuentes

Se revisan `GET`, `POST`, `PUT`, `PATCH` y `DELETE` como operaciones habituales para leer o modificar datos.

### Respuestas, códigos de estado y JSON

Se explica cómo leer respuestas del servidor, interpretar códigos de estado y trabajar con datos en formato JSON.

## Relación con el proyecto integrador

El proyecto e-commerce utilizará una API real para consultar productos, mostrar detalles y construir interacciones de mayor complejidad sobre información remota.

## Cierre

Sobre esta base, el siguiente capítulo introduce TypeScript como herramienta de apoyo para trabajar con mayor precisión sobre datos, funciones y componentes.