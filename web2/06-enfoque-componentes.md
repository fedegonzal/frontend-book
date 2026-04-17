# El enfoque basado en componentes en la interfaz

Una de las transformaciones más importantes del desarrollo frontend consistió en dejar de pensar la interfaz como una única página extensa para empezar a organizarla en piezas más pequeñas, reutilizables y con responsabilidades más claras. Ese cambio no es solamente técnico: también modifica la forma de analizar problemas y de estructurar proyectos.

Este capítulo introduce la lógica del desarrollo basado en componentes como puente conceptual hacia la parte del libro dedicada a React.

## Objetivos del capítulo

- comprender qué se entiende por componente en una interfaz;
- reconocer ventajas de composición y reutilización;
- relacionar componentes con mantenibilidad y escalabilidad;
- preparar el paso hacia herramientas orientadas a componentes.

## Contenidos mínimos

### La interfaz como conjunto de piezas

Conviene pensar una aplicación como un conjunto de partes que pueden separarse, reutilizarse y combinarse. Esta forma de organización mejora la lectura del sistema y facilita cambios posteriores.

### Reutilización y composición

Se trabaja la idea de componer pantallas a partir de unidades más pequeñas y relativamente independientes.

### Responsabilidades acotadas

Se introduce el valor de asignar a cada componente una función comprensible dentro de la interfaz.

### Impacto en el mantenimiento

Se relaciona el enfoque por componentes con la reducción de duplicación y con una evolución más ordenada del código.

## Relación con el proyecto integrador

El e-commerce podrá descomponerse en piezas como tarjetas de producto, barra de navegación, carrito, formulario y vistas específicas, lo que facilitará su construcción incremental.

## Cierre

A partir de esta lógica, conviene comparar dos modelos frecuentes de organización de aplicaciones web: las aplicaciones de múltiples páginas y las de página única.