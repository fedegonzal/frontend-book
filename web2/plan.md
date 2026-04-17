# Plan del libro: Desarrollo Web 2

## Introducción

Este documento organiza el plan general del libro **Desarrollo Web 2** a partir del programa de la materia y en continuidad con el enfoque editorial del libro anterior. La propuesta conserva el recorrido pedagógico original, amplía el cierre con una cuarta parte específica y utiliza el proyecto integrador como hilo transversal a lo largo de todo el libro.

En términos generales, el recorrido propuesto avanza desde los fundamentos del entorno y del lenguaje hacia el desarrollo basado en componentes, luego se concentra en React como herramienta principal de construcción de interfaces y finalmente cierra con testing, integración, despliegue y proyección del trayecto.

## Objetivos del plan

- Definir una estructura general clara para el libro.
- Convertir los temas del programa en capítulos con progresión pedagógica.
- Integrar el proyecto e-commerce como hilo transversal del recorrido.
- Alinear el nuevo libro con el tono, la organización y la forma de exposición de la colección previa.
- Dejar establecida una base de trabajo para la posterior redacción de cada capítulo.

## Criterios generales de organización

- El libro se divide en cuatro partes.
- Cada ítem principal del programa se desarrolla como capítulo.
- TypeScript aparece primero como capítulo introductorio y luego se incorpora progresivamente en ejemplos con JSX y TSX.
- El proyecto integrador no se presenta como bloque autónomo, sino como una aplicación que acompaña el desarrollo de los contenidos.
- Cada capítulo deberá redactarse con una estructura estable: introducción breve, objetivos, desarrollo conceptual, cierre y ejercicios.

## Estructura propuesta del libro

## Parte 1. Fundamentos del desarrollo web moderno

Esta primera parte establece la base técnica común del resto del libro. Su función es ordenar el entorno de trabajo, recuperar y ampliar los conocimientos previos sobre JavaScript y presentar las herramientas necesarias para comprender el desarrollo frontend contemporáneo.

### Capítulo 1. Introducción a JavaScript moderno

Presenta el lugar de JavaScript en el desarrollo web actual y recupera los aspectos del lenguaje necesarios para trabajar con aplicaciones modernas.

### Capítulo 2. Asincronía en JavaScript: promesas, async y await

Introduce el problema de las operaciones no bloqueantes y desarrolla las herramientas principales para trabajar con tareas asincrónicas en el navegador y en aplicaciones frontend.

### Capítulo 3. Consumo de APIs REST en aplicaciones web

Explica cómo una aplicación cliente se comunica con servicios remotos, cómo se estructuran las peticiones HTTP más frecuentes y cómo interpretar respuestas en formato JSON.

### Capítulo 4. Introducción a TypeScript para frontend

Presenta los fundamentos del tipado estático gradual y su utilidad en proyectos de interfaz. Este capítulo funciona como base para la incorporación progresiva de TSX en la parte dedicada a React.

### Capítulo 5. Control de versiones con Git en proyectos web

Ordena las prácticas básicas de versionado necesarias para trabajar con proyectos reales, mantener historial y colaborar de manera organizada.

### Capítulo 6. Node.js y npm como entorno de trabajo

Introduce el rol de Node.js fuera del navegador y presenta npm como herramienta central para gestionar dependencias, scripts y flujo de trabajo.

## Parte 2. Desarrollo basado en componentes

Esta segunda parte cumple una función de puente conceptual. Antes de ingresar en React, conviene comprender por qué el enfoque basado en componentes se volvió central en el desarrollo de interfaces y qué problemas ayuda a resolver.

### Capítulo 7. El enfoque basado en componentes en la interfaz

Desarrolla la idea de componente como unidad de composición, reutilización y mantenimiento de una interfaz.

### Capítulo 8. SPA y MPA: modelos de navegación y composición

Compara los modelos de aplicación de página única y de múltiples páginas, destacando sus diferencias en navegación, experiencia de usuario y organización técnica.

### Capítulo 9. Web Components como estándar de la plataforma

Presenta la respuesta nativa de la plataforma web al desarrollo basado en componentes y ubica sus conceptos principales dentro del ecosistema frontend.

### Capítulo 10. Lit como puerta de entrada al desarrollo declarativo

Introduce Lit de forma acotada como un ejemplo de biblioteca orientada a componentes, útil para tender un puente entre estándares web y enfoques declarativos más amplios.

### Capítulo 11. Arquitectura de frontend y organización del código

Trabaja criterios de organización de carpetas, separación de responsabilidades y distinción entre componentes presentacionales y contenedores.

## Parte 3. Desarrollo web con React

Esta tercera parte constituye el núcleo aplicado del libro. Aquí se desarrolla React como herramienta principal para construir interfaces modernas, recuperando lo visto en las partes anteriores y avanzando desde los conceptos más básicos hacia problemas de mayor complejidad.

### Capítulo 12. Introducción a React y su modelo de trabajo

Presenta el enfoque general de React, su lógica declarativa y su lugar en el desarrollo frontend actual.

### Capítulo 13. JSX y TSX: sintaxis declarativa para interfaces

Explica la sintaxis que permite combinar estructura e interactividad en componentes, mostrando tanto variantes con JavaScript como con TypeScript.

### Capítulo 14. Componentes en React

Desarrolla la construcción de componentes como unidades básicas de trabajo dentro de una aplicación React.

### Capítulo 15. Props y state

Introduce dos conceptos centrales para la composición y el comportamiento dinámico de la interfaz.

### Capítulo 16. Renderizado condicional y listas

Aborda patrones frecuentes para mostrar colecciones de datos y para modificar la interfaz según distintas condiciones de ejecución.

### Capítulo 17. Eventos e interacción

Explica cómo responder a acciones de la persona usuaria y cómo conectar eventos con cambios de estado e interfaz.

### Capítulo 18. Formularios con React Hook Form

Presenta estrategias para construir formularios mantenibles, organizar validaciones y administrar el ingreso de datos.

### Capítulo 19. Hooks fundamentales: useState, useEffect y useContext

Desarrolla los hooks básicos que permiten manejar estado local, efectos y mecanismos simples de compartición de información.

### Capítulo 20. Navegación en aplicaciones con React Router

Introduce la organización de rutas en aplicaciones de página única y su relación con la estructura general del proyecto.

### Capítulo 21. Estado global con Zustand

Presenta una solución concreta para administrar estado compartido sin introducir complejidad innecesaria en el recorrido de aprendizaje.

### Capítulo 22. Consumo de APIs en React: datos, loading, error y success

Integra asincronía, renderizado y organización del estado para trabajar con datos remotos dentro de una aplicación real.

### Capítulo 23. Librerías de componentes y criterios de adopción

Propone una discusión sobre el uso de bibliotecas externas para acelerar el desarrollo de interfaces y analizar criterios de selección, ventajas y límites.

## Parte 4. Testing, integración y cierre

La última parte recupera el recorrido completo y lo orienta hacia el cierre del proyecto. Por ese motivo, reúne testing, integración funcional de la aplicación, criterios básicos de despliegue y una síntesis que conecte este libro con etapas posteriores de formación.

### Capítulo 24. Testing de interfaces con Jest y React Testing Library

Introduce las pruebas de componentes e interfaces como parte de una práctica de desarrollo más robusta y mantenible.

### Capítulo 25. Integración del proyecto e-commerce: del catálogo al checkout

Recupera el recorrido previo y organiza la integración de las distintas piezas de la aplicación en un producto coherente.

### Capítulo 26. Despliegue, mantenimiento y próximos pasos en el ecosistema frontend

Ofrece un cierre ampliado del libro, conectando la construcción de la aplicación con criterios mínimos de publicación, mantenimiento y continuidad formativa.

## Hilo transversal del proyecto integrador

El proyecto integrador consiste en el desarrollo incremental de una aplicación e-commerce apoyada en una API real documentada con Swagger. Su función no es aparecer como bloque separado, sino acompañar el desarrollo de los contenidos y darles una referencia práctica común.

- En la Parte 1 se prepara el entorno y se introduce el trabajo con datos remotos.
- En la Parte 2 se organiza la interfaz en componentes y se define una arquitectura de trabajo.
- En la Parte 3 se construye la aplicación en React: listado, detalle, carrito, formularios, estado global y consumo de API.
- En la Parte 4 se prueba, integra y proyecta la publicación del desarrollo realizado.

## Criterios de redacción para los capítulos

- Abrir cada capítulo con una introducción breve que ubique el problema o la relevancia del tema.
- Incluir una sección de objetivos del capítulo.
- Desarrollar los contenidos desde lo general hacia lo particular.
- Sostener una terminología estable a lo largo de todo el libro.
- Usar ejemplos concretos, simples y reconocibles para estudiantes.
- Evitar listas extensas sin desarrollo conceptual.
- Cerrar cada capítulo retomando lo visto y enlazando con el siguiente.
- Incorporar ejercicios finales organizados por comprensión, aplicación e integración.

## Decisiones ya establecidas

- El libro se organizará en cuatro partes.
- TypeScript tendrá un capítulo introductorio en la Parte 1.
- En la Parte 3 habrá ejemplos tanto en JSX como en TSX.
- El proyecto integrador será un hilo transversal del libro.
- El cierre incluirá testing, integración y una proyección hacia despliegue y continuidad.

## Próximos pasos sugeridos

1. Ajustar, si hace falta, los títulos definitivos de los capítulos.
2. Redactar los objetivos específicos de cada capítulo.
3. Diseñar la secuencia del proyecto integrador a lo largo de las cuatro partes.
4. Comenzar la escritura del primer capítulo a partir de esta estructura.