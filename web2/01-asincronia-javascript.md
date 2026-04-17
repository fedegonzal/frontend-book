# Asincronía en JavaScript: promesas, async y await

Una gran parte de las aplicaciones frontend actuales depende de tareas que no se resuelven de manera inmediata: pedidos a servidores, lectura de datos remotos, espera de respuestas o procesamiento diferido. Por ese motivo, comprender la asincronía es un paso necesario para construir interfaces que interactúan con servicios externos.

Este capítulo organiza las herramientas principales que ofrece JavaScript para trabajar con ese tipo de situaciones y prepara el camino para el consumo de APIs y el manejo de estados de carga en React.

## Objetivos del capítulo

- comprender el problema técnico de la asincronía;
- distinguir entre callbacks, promesas y funciones `async`;
- interpretar el uso de `await` como mejora de legibilidad;
- preparar el uso posterior de datos remotos en el frontend.

## Contenidos mínimos

### Operaciones síncronas y asincrónicas

Conviene comenzar por la diferencia entre tareas que se resuelven en secuencia inmediata y tareas que requieren espera. Esa distinción organiza muchas decisiones posteriores del desarrollo web.

### Promesas

Las promesas permiten representar operaciones cuyo resultado estará disponible más adelante. Se presentan estados posibles, encadenamiento y manejo básico de errores.

### Async y await

Las funciones `async` y la palabra clave `await` permiten expresar flujos asincrónicos con una sintaxis más cercana a la lectura secuencial.

### Manejo de errores

Se introduce el uso de `try`, `catch` y criterios básicos para tratar errores de red o fallos de ejecución.

## Relación con el proyecto integrador

La aplicación e-commerce deberá consultar productos, obtener detalles y reaccionar frente a demoras o errores. Todo ese comportamiento depende de una comprensión básica de la asincronía.

## Cierre

Una vez comprendida la lógica asincrónica, el siguiente paso consiste en analizar cómo se comunican las aplicaciones frontend con servicios externos mediante APIs REST.