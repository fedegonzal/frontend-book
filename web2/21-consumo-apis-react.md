# Consumo de APIs en React: datos, loading, error y success

Una interfaz que depende de datos remotos no solo necesita obtener información. También debe representar estados intermedios, errores de conexión y respuestas exitosas sin perder claridad para quien usa la aplicación. Este problema reúne muchos de los conceptos trabajados hasta aquí y los integra dentro de un flujo más realista.

## Objetivos del capítulo

- integrar consumo de APIs con componentes React;
- organizar estados de loading, error y success;
- mejorar la lectura de interfaces conectadas a datos remotos;
- consolidar herramientas vistas en capítulos anteriores.

## Contenidos mínimos

### Fetching de datos en componentes

Se trabaja el pedido de datos remotos dentro del flujo de una aplicación React.

### Estado de carga

Se introduce la necesidad de representar la espera como parte explícita de la interfaz.

### Estado de error

Se discuten criterios básicos para detectar y comunicar errores de red o respuestas inválidas.

### Estado de éxito y renderizado final

Se integra la respuesta exitosa con la representación de listas, detalles y otras vistas.

## Relación con el proyecto integrador

El catálogo, el detalle de producto y parte del checkout del e-commerce dependerán de este tipo de integración con la API real.

## Cierre

Después de integrar datos remotos, conviene sumar una discusión sobre bibliotecas de componentes y criterios para adoptarlas con sentido técnico.