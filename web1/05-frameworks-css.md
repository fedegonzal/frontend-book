# Frameworks CSS (Bootstrap y Tailwind)

Después de trabajar CSS y una primera capa de organización con SASS, es útil conocer herramientas que ofrecen soluciones listas para resolver problemas frecuentes de interfaz. Este capítulo no busca reemplazar el razonamiento sobre CSS, sino mostrar dos enfoques muy extendidos para acelerar el desarrollo: uno más orientado a componentes predefinidos y otro más orientado a utilidades pequeñas y combinables.

## Objetivos del capítulo

- reconocer qué problemas resuelven los frameworks CSS y qué decisiones siguen dependiendo del criterio del desarrollador;
- comparar Bootstrap y Tailwind según filosofía, velocidad de trabajo y mantenimiento;
- identificar contextos en los que conviene usar CSS propio, un framework o una combinación de ambos;
- evaluar el costo pedagógico y técnico de incorporar abstracciones sobre CSS.

## Qué es un framework CSS

Un framework CSS es un conjunto de estilos, convenciones y componentes reutilizables que ayuda a construir interfaces más rápido. En lugar de escribir todo desde cero, el desarrollador trabaja sobre una base predefinida que ya resuelve buena parte del layout, los espaciados, la tipografía, los formularios o ciertos componentes comunes.

Esto no significa que un framework “reemplaza” a CSS. En realidad, sigue siendo CSS, pero organizado de una manera más sistemática y acompañado por clases listas para usar.

Los frameworks pueden aportar varias ventajas:

- aceleran el desarrollo inicial;
- ofrecen consistencia visual;
- reducen la cantidad de CSS personalizado necesario;
- facilitan el armado de prototipos y pantallas funcionales;
- resuelven problemas frecuentes de layout y responsive design.

Sin embargo, también introducen decisiones propias sobre nomenclatura, estructura y forma de trabajo. Por eso conviene estudiarlos después de conocer bien HTML, CSS y una base de organización del código.

En este módulo se trabajará con dos enfoques muy representativos: Bootstrap y Tailwind CSS.

## Bootstrap: incorporación, grilla, componentes y personalización

Bootstrap es uno de los frameworks CSS más conocidos y usados. Su propuesta combina una grilla responsive, un conjunto amplio de componentes y muchas clases utilitarias listas para aplicar. En otras palabras, ofrece una base visual y estructural bastante completa para resolver interfaces frecuentes sin empezar desde cero.

### **Incorporación básica**

Una forma simple de incorporarlo en un proyecto de práctica es mediante CDN:

```html
<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta
name="viewport"
content="width=device-width, initial-scale=1">
<link
href="https://unpkg.com/bootstrap/dist/css/bootstrap.min.css"
rel="stylesheet">
</head>
<body>
...
<script
src="https://unpkg.com/bootstrap/dist/js/bootstrap.bundle.min.js">
</script>
</body>
</html>
```

Para una primera aproximación esto alcanza. Sin embargo, conviene notar un detalle importante: ese archivo no trae solo una pequeña ayuda puntual, sino un conjunto bastante amplio de estilos y, en algunos casos, también comportamiento JavaScript ya resuelto. Esa amplitud es parte de su ventaja, pero también de su costo.

### **La grilla responsive como sistema de trabajo**

Una de las herramientas principales de Bootstrap es su grilla de 12 columnas. La estructura básica suele componerse con:

- `container` o `container-fluid`;
- `row`;
- `col`, `col-md-6`, `col-lg-4`, etc.

`container` centra el contenido y le da un ancho máximo progresivo según el tamaño de pantalla. `container-fluid`, en cambio, ocupa todo el ancho disponible. La elección entre ambos no es menor: cambia la sensación general de la interfaz.

Ejemplo:

```html
<div class="container py-4">
<div class="row g-3">
<div class="col-12 col-md-6 col-lg-4">Producto 1</div>
<div class="col-12 col-md-6 col-lg-4">Producto 2</div>
<div class="col-12 col-md-6 col-lg-4">Producto 3</div>
</div>
</div>
```

En este caso:

- `col-12` hace que cada bloque ocupe toda la fila en pantallas pequeñas;
- `col-md-6` reparte dos columnas desde un ancho mediano;
- `col-lg-4` reparte tres columnas desde un ancho mayor;
- `g-3` agrega separación entre columnas y filas;
- `py-4` suma espacio vertical al contenedor.

Esto muestra algo importante sobre Bootstrap: no solo aporta componentes, también ofrece una manera bastante estable de pensar layout responsive. Muchas decisiones frecuentes ya tienen una convención predefinida.

### **Componentes listos y componentes interactivos**

Bootstrap también ofrece componentes ya preparados, como botones, tarjetas, formularios, navbars, alerts o modals. Esto permite construir interfaces funcionales con rapidez, especialmente en etapas de prototipado o en proyectos administrativos donde la consistencia pesa más que la originalidad visual.

Por ejemplo, un formulario o una tarjeta suelen armarse combinando clases semánticamente bastante expresivas:

```html
<div class="card shadow-sm">
<div class="card-body">
<h2 class="card-title h5">Producto destacado</h2>
<p class="card-text">Disponible en promoción esta semana.</p>
<a href="#" class="btn btn-success">Ver detalle</a>
</div>
</div>
```

Además, algunos componentes no son solo visuales. Una navbar colapsable, un modal o un dropdown pueden depender también del paquete JavaScript de Bootstrap. Esto es útil porque resuelve interacciones frecuentes sin que haya que programarlas desde cero, pero también implica depender de una lógica ya diseñada por el framework.

Dicho de otro modo: Bootstrap no solo entrega estilos, también entrega decisiones de comportamiento.

### **Personalización y límites**

Uno de los cuestionamientos más frecuentes a Bootstrap es que muchas interfaces “se ven a Bootstrap”. Esa observación no es del todo injusta. Si se usan sus componentes casi sin cambios, el resultado tiende a ser reconocible.

Eso no siempre es un problema. En sistemas internos, paneles administrativos, prototipos o productos donde la prioridad está en estabilidad y velocidad, esa consistencia puede ser una ventaja. El problema aparece cuando se necesita una identidad visual más marcada y se espera lograrla sin intervenir demasiado el framework.

Por eso conviene pensar Bootstrap así:

- sirve muy bien cuando se quiere una base robusta y rápida;
- funciona mejor si el equipo acepta parte de su lenguaje visual;
- exige más trabajo cuando se necesita una estética muy específica.

En proyectos reales puede personalizarse mucho más, incluso a través de variables y compilación propia, pero ese nivel de configuración no es necesario para este capítulo. Lo importante aquí es entender el criterio: Bootstrap acelera mucho las decisiones repetidas, pero no elimina la necesidad de pensar diseño, accesibilidad y coherencia visual.

## Tailwind CSS: utility-first, responsive y composición

Tailwind CSS representa un enfoque distinto. En lugar de traer componentes completos como punto de partida, ofrece una gran cantidad de clases utilitarias pequeñas y combinables, con las que el diseño se construye directamente en el HTML.

### **Incorporación básica**

Para una prueba rápida o una instancia de aprendizaje puede incorporarse mediante su CDN de práctica:

```html
<script src="https://cdn.tailwindcss.com"></script>
```

Ese mecanismo es útil para explorar Tailwind en ejercicios breves, pero no representa la forma habitual de trabajo en proyectos más grandes. En contextos reales suele integrarse con tooling específico, algo que excede el alcance de esta materia.

### **La lógica utility-first**

Luego se pueden usar clases como estas:

```html
<button class="bg-green-700 text-white px-4 py-2 rounded-lg shadow">
Guardar
</button>
```

Cada clase expresa una decisión puntual:

- `bg-green-700`: color de fondo;
- `text-white`: color del texto;
- `px-4` y `py-2`: padding horizontal y vertical;
- `rounded-lg`: bordes redondeados;
- `shadow`: sombra.

Este enfoque suele llamarse utility-first porque prioriza el uso de utilidades breves y combinables en vez de crear una clase personalizada para cada componente.

Tailwind ofrece mucha velocidad para construir interfaces, pero también exige acostumbrarse a una forma de lectura distinta, donde buena parte del estilo vive directamente en el HTML. Quien trabaja con Tailwind no piensa primero en “nombrar un componente” sino en “componer decisiones pequeñas”.

### **Responsive design en el propio HTML**

Uno de los rasgos más característicos de Tailwind es que el responsive design también se expresa mediante clases. Para eso se usan prefijos como `sm:`, `md:`, `lg:` y otros similares.

```html
<div class="grid grid-cols-1 gap-4 md:grid-cols-2 lg:grid-cols-3">
    <article class="rounded-xl border bg-white p-4 shadow-sm">
        Producto 1
    </article>
    <article class="rounded-xl border bg-white p-4 shadow-sm">
        Producto 2
    </article>
    <article class="rounded-xl border bg-white p-4 shadow-sm">
        Producto 3
    </article>
</div>
```

Este ejemplo expresa una lógica mobile-first:

- en pantallas pequeñas hay una sola columna;
- en pantallas medianas aparecen dos;
- en pantallas grandes aparecen tres.

La idea es similar a la de otros sistemas responsive, pero aquí la decisión queda explícita en el propio HTML. Eso puede resultar muy cómodo para iterar rápido, aunque también hace que el marcado concentre más información visual.

### **Estados y variantes**

Tailwind no se limita a colores, bordes y espaciados. También permite expresar estados interactivos con prefijos como `hover:`, `focus:` o `disabled:`.

```html
<a href="#" class="inline-block rounded-lg bg-green-700 px-4 py-2
text-white transition hover:bg-green-800 focus:outline-none
focus:ring-2 focus:ring-green-400">
Ver más
</a>
```

Esto permite describir desde el HTML no solo cómo se ve un elemento, sino también cómo responde al cursor o al foco de teclado. Esa posibilidad es potente, pero exige criterio: no alcanza con que una interfaz “cambie de color”; también debe seguir siendo accesible y legible.

### **Mantenibilidad y organización**

Una crítica habitual a Tailwind es que el HTML puede volverse largo y difícil de leer. Esa crítica tiene parte de verdad si se acumulan clases sin orden ni criterio.

Sin embargo, el problema no está solo en Tailwind, sino en cómo se usa. Algunas prácticas ayudan bastante:

- agrupar clases con una lógica reconocible, por ejemplo primero layout, luego espaciado y después color;
- repetir utilidades simples cuando eso mantiene claridad;
- extraer patrones repetidos cuando un bloque deja de ser puntual y empieza a comportarse como componente.

En proyectos más grandes también existen estrategias como `@apply` o la extensión de configuración para reutilizar decisiones visuales. No hace falta profundizar aquí en su sintaxis, pero sí entender la idea: incluso en un enfoque utility-first, tarde o temprano también aparece el problema de organizar y abstraer.

## Bootstrap vs Tailwind

Aunque ambos son frameworks CSS, no responden exactamente a la misma filosofía.

Bootstrap parte de una idea más tradicional: componentes predefinidos, grilla, clases utilitarias y una estética relativamente reconocible. Ayuda mucho cuando se necesita producir rápido con una base ya establecida.

Tailwind parte de una idea más compositiva: no impone tanto un componente cerrado, sino una caja de herramientas para construir componentes desde cero usando utilidades pequeñas.

Una forma más precisa de compararlos es esta:

- Bootstrap acelera mucho el arranque cuando el problema se parece a componentes frecuentes;
- Tailwind da más libertad visual cuando se quiere construir una interfaz con identidad propia desde utilidades;
- Bootstrap suele dejar un HTML más breve, pero desplaza más decisiones al propio framework;
- Tailwind vuelve el HTML más expresivo en términos visuales, aunque también más cargado;
- Bootstrap ofrece convenciones muy estables para grilla, formularios y componentes comunes;
- Tailwind ofrece un vocabulario muy amplio para componer casi cualquier interfaz sin depender tanto de componentes cerrados.

También cambia la experiencia mental de trabajo. Con Bootstrap, muchas veces la pregunta es: "¿qué componente del framework resuelve mejor esto?". Con Tailwind, la pregunta suele ser: "¿qué combinaciones de utilidades describen este diseño con claridad?".

Ninguno es “mejor” de forma absoluta. La elección depende del contexto del proyecto, del tiempo disponible, del equipo y del tipo de interfaz que se necesite construir.

## Cuándo conviene usar un framework y cuándo no

La decisión no es solo "usar o no usar framework". En la práctica, suele haber al menos cuatro caminos posibles:

- CSS propio;
- Bootstrap;
- Tailwind;
- una combinación entre CSS propio y algún framework.

CSS propio puede ser suficiente cuando el proyecto todavía es pequeño, cuando conviene afianzar fundamentos o cuando se necesita un control visual muy específico sin sumar capas adicionales.

Bootstrap puede ser una buena opción cuando:

- se necesita prototipar rápido;
- la interfaz repite patrones clásicos;
- la prioridad está en consistencia y velocidad;
- el equipo valora tener componentes ya resueltos.

Tailwind puede ser una buena opción cuando:

- se quiere iterar rápido sin depender de componentes cerrados;
- el diseño necesita más flexibilidad visual;
- el equipo acepta trabajar con clases utilitarias en el HTML;
- se busca un punto intermedio entre rapidez y control fino del estilo.

Un enfoque mixto también es frecuente. Por ejemplo, puede usarse Bootstrap para resolver layout y componentes administrativos, y CSS propio para personalizar partes específicas. O puede usarse Tailwind para maquetar rápido, pero extraer algunos patrones comunes a componentes más estables.

En cambio, un framework puede no ser la mejor opción cuando:

- el proyecto es pequeño y el CSS propio ya alcanza;
- el equipo todavía no comprende bien los fundamentos de CSS;
- el framework termina ocultando decisiones que conviene entender desde la base;
- el costo de adoptar sus convenciones es mayor que el beneficio real.

En una materia inicial, lo importante es que el framework no tape el aprendizaje del lenguaje. Por eso tiene sentido estudiarlo después de haber trabajado CSS puro.

En otras palabras, un framework puede ahorrar tiempo, pero no debería reemplazar el criterio técnico. Si una clase funciona y no se entiende por qué, el aprendizaje queda incompleto. Por eso conviene usar estos recursos como apoyo sobre una base ya construida, no como un atajo para evitar comprender CSS.

En el marco de Web 1, el objetivo de este capítulo es reconocer estos enfoques y poder evaluarlos con criterio. Su uso más profundo en combinación con otros lenguajes, librerías o arquitecturas corresponde a etapas posteriores del recorrido.

## Ejemplo comparativo sobre una misma interfaz

Supongamos una pequeña sección de productos del sistema de supermercado, con una tarjeta, algo de layout responsive y un botón con estado visual.

En Bootstrap podría escribirse así:

```html
<section class="container py-4">
<div class="row g-4">
<div class="col-12 col-md-6 col-lg-4">
<article class="card h-100 shadow-sm">
<img src="galletitas.jpg" class="card-img-top" alt="Paquete de
galletitas">
<div class="card-body d-flex flex-column">
<h2 class="card-title h5">Galletitas</h2>
<p class="card-text text-secondary">Paquete de 250 gramos.</p>
<a href="#" class="btn btn-success mt-auto">Ver más</a>
</div>
</article>
</div>
</div>
</section>
```

En Tailwind, una interfaz parecida podría escribirse así:

```html
<section class="mx-auto max-w-6xl px-4 py-6">
<div class="grid grid-cols-1 gap-4 md:grid-cols-2 lg:grid-cols-3">
<article class="overflow-hidden rounded-xl border bg-white shadow-sm">
<img src="galletitas.jpg" alt="Paquete de galletitas" class="h-48
w-full object-cover">
<div class="flex h-full flex-col p-4">
<h2 class="mb-2 text-lg font-semibold">Galletitas</h2>
<p class="mb-4 text-sm text-gray-600">Paquete de 250 gramos.</p>
<a href="#" class="mt-auto inline-block rounded-lg bg-green-700 px-4
py-2 text-white transition hover:bg-green-800 focus:outline-none
focus:ring-2 focus:ring-green-400">Ver más</a>
</div>
</article>
</div>
</section>
```

Ambos ejemplos resuelven un problema parecido, pero la experiencia de construcción cambia bastante. Bootstrap se apoya más en clases que representan componentes y patrones ya establecidos. Tailwind se apoya más en la composición explícita de decisiones pequeñas sobre layout, espaciado, color y estado.

## Validación y recursos recomendados para frameworks CSS

Cuando se trabaja con frameworks CSS conviene revisar no solo si las clases “funcionan”, sino también si el resultado sigue siendo claro, mantenible y coherente con la interfaz.

Algunas preguntas útiles son:

- ¿el framework realmente acelera el trabajo en este proyecto?
- ¿las clases utilizadas siguen siendo legibles?
- ¿la interfaz mantiene coherencia visual?
- ¿la accesibilidad sigue cuidada, especialmente en formularios, contraste y foco?
- ¿se está entendiendo qué resuelve el framework y qué sigue dependiendo del criterio del desarrollador?
- ¿la personalización necesaria justifica seguir con ese framework o convendría CSS propio?

Recursos recomendados para profundizar:

- Bootstrap: [https://getbootstrap.com/](https://getbootstrap.com/)
- Tailwind CSS: [https://tailwindcss.com/](https://tailwindcss.com/)
- Documentación del grid de Bootstrap: [https://getbootstrap.com/docs/5.3/layout/grid/](https://getbootstrap.com/docs/5.3/layout/grid/)
- Utilidades de espacio en Bootstrap: [https://getbootstrap.com/docs/5.3/utilities/spacing/](https://getbootstrap.com/docs/5.3/utilities/spacing/)
- Componentes de Bootstrap: [https://getbootstrap.com/docs/5.3/components/](https://getbootstrap.com/docs/5.3/components/)
- Documentación de utility classes en Tailwind: [https://tailwindcss.com/docs/utility-first](https://tailwindcss.com/docs/utility-first)
- Diseño responsive en Tailwind: [https://tailwindcss.com/docs/responsive-design](https://tailwindcss.com/docs/responsive-design)
- Estados interactivos en Tailwind: [https://tailwindcss.com/docs/hover-focus-and-other-states](https://tailwindcss.com/docs/hover-focus-and-other-states)
- Personalización en Tailwind: [https://tailwindcss.com/docs/configuration](https://tailwindcss.com/docs/configuration)

Con esto queda cubierto un primer panorama de frameworks CSS. A esta altura, ya debería poder reconocer qué problemas resuelve un framework, qué costo introduce y por qué la elección entre Bootstrap y Tailwind depende más del contexto que de una preferencia abstracta.

También conviene sacar una conclusión importante antes de seguir: ningún framework garantiza por sí solo una interfaz accesible ni verdaderamente responsive. Bootstrap puede ofrecer componentes y convenciones útiles. Tailwind puede acelerar mucho la composición visual. Pero en ambos casos siguen dependiendo del criterio del desarrollador cuestiones como la estructura semántica, el foco visible, el contraste, el tamaño táctil de los controles, el orden de lectura y la adaptación real a pantallas pequeñas.

El siguiente módulo retoma precisamente ese punto. Ya no se tratará de elegir una herramienta de maquetación, sino de revisar cómo asegurar que lo construido con HTML, CSS, SASS o frameworks siga siendo usable, claro y robusto en distintos contextos.

## Ejercicios del capítulo

### Comprensión

1. Explique con sus palabras cuál es la diferencia entre un framework orientado a componentes y un enfoque utility-first.
2. Describa una ventaja y una desventaja de Bootstrap considerando no solo velocidad, sino también personalización.
3. Describa una ventaja y una desventaja de Tailwind CSS considerando no solo flexibilidad, sino también legibilidad del HTML.
4. Explique por qué usar un framework no reemplaza la necesidad de comprender CSS.

### Aplicación

1. Construya una pequeña sección responsive de productos con Bootstrap usando `container`, `row`, al menos dos breakpoints de columna y una tarjeta con botón.
2. Reproduzca esa misma interfaz con Tailwind CSS usando grilla responsive y al menos un estado interactivo en el botón.
3. Compare ambas implementaciones e identifique qué decisiones quedaron más explícitas en el HTML en cada caso.

### Integración

1. Elija una pantalla del proyecto del supermercado y justifique qué enfoque sería más conveniente para desarrollarla: CSS propio, Bootstrap, Tailwind o una solución mixta. Argumente su respuesta en términos de tiempo, claridad, mantenimiento, control visual y accesibilidad.
