# Accesibilidad web y responsive design

Después de trabajar estructura con HTML, presentación con CSS, organización con SASS y aceleración de interfaz con frameworks, aparece una pregunta más exigente: ¿lo que construimos realmente puede ser usado por personas distintas, en dispositivos distintos y en contextos distintos? Accesibilidad y responsive design ya aparecieron en capítulos anteriores, pero su importancia justifica tratarlos de forma específica. No se trata solo de “corregir detalles” después de diseñar una interfaz, sino de incorporar desde el principio criterios que hagan que la experiencia sea usable, clara y robusta para más personas y en más contextos.

## Objetivos del capítulo

- comprender accesibilidad y responsive design como criterios de calidad, no como agregados finales;
- aplicar principios básicos de estructura semántica, foco, contraste y navegación por teclado;
- diseñar interfaces que respondan bien a distintos tamaños de pantalla y contextos de uso;
- revisar un proyecto existente detectando mejoras concretas de accesibilidad y adaptación.

## Por qué este módulo es específico

La accesibilidad y el responsive design ya aparecieron varias veces en los módulos anteriores. No fue casualidad: son temas transversales al desarrollo frontend. Sin embargo, cuando se los menciona solo de paso, es fácil que queden reducidos a una lista de consejos sueltos.

En este módulo el objetivo es trabajar ambos temas de forma articulada. La accesibilidad se ocupa de que una interfaz pueda ser comprendida y utilizada por personas con diferentes condiciones, tecnologías y contextos. El responsive design se ocupa de que esa misma interfaz se adapte a distintos tamaños de pantalla y formas de interacción. En la práctica, ambos problemas suelen cruzarse.

Una interfaz que se ve bien solo en escritorio no está realmente resuelta. Una interfaz que cambia de tamaño pero pierde foco visible, contraste o navegación por teclado tampoco. Por eso conviene pensarlos como parte de una misma responsabilidad de diseño e implementación.

### **Lo que no resuelve un framework por sí solo**

El capítulo anterior mostró que herramientas como Bootstrap o Tailwind pueden acelerar mucho el trabajo. Sin embargo, también dejan algo en evidencia: una interfaz no se vuelve accesible o usable solo porque usa clases bien conocidas o componentes populares.

Por ejemplo:

- una tarjeta armada con Bootstrap sigue necesitando una jerarquía de títulos razonable, textos alternativos útiles y enlaces claros;
- un botón hecho con Tailwind puede verse correcto y aun así no tener foco visible suficiente;
- una grilla responsive puede reorganizarse bien en mobile y, sin embargo, seguir teniendo botones demasiado pequeños o formularios difíciles de usar con teclado.

Esto importa porque obliga a cambiar la pregunta. Ya no alcanza con pensar “¿funciona la clase?” o “¿se ve bien?”. También hace falta preguntar:

- ¿se entiende la estructura?
- ¿se puede recorrer con teclado?
- ¿los estados interactivos siguen siendo visibles?
- ¿el contenido mantiene orden y legibilidad cuando el espacio cambia?

Ese desplazamiento de foco es justamente el objetivo de este módulo.

## Qué es accesibilidad web

La accesibilidad web consiste en construir sitios y aplicaciones que puedan ser utilizados por la mayor diversidad posible de personas. Esto incluye personas con discapacidades visuales, auditivas, motrices o cognitivas, pero no se limita a ellas. También abarca contextos de uso muy distintos: pantallas pequeñas, conexiones lentas, entornos con mucha luz, uso exclusivo de teclado, lectores de pantalla o navegadores con soporte parcial.

No se trata de hacer una “versión especial” para ciertos usuarios. La idea central es diseñar una única experiencia que funcione razonablemente bien para cualquier persona. Ese enfoque, además de ser más justo, suele producir interfaces más claras, más robustas y más fáciles de mantener.

Desde esta perspectiva, la accesibilidad no es un agregado final ni una capa opcional. Es una forma de evaluar la calidad de una interfaz. Si el contenido no puede percibirse, si los controles no pueden operarse o si la estructura no se entiende, entonces la implementación todavía está incompleta.

## Principios POUR y niveles de conformidad

Las recomendaciones de accesibilidad de la W3C suelen organizarse alrededor de cuatro principios generales, conocidos por la sigla POUR:

- Perceptible: la información debe presentarse de manera que pueda ser percibida por distintas personas y tecnologías.
- Operable: la interfaz debe poder utilizarse, por ejemplo, con teclado y sin exigir acciones imposibles o confusas.
- Comprensible: el contenido y los comportamientos deben resultar previsibles y claros.
- Robusto: el código debe poder ser interpretado correctamente por navegadores y tecnologías de asistencia.

Estos principios no reemplazan a los criterios técnicos concretos, pero sirven como guía para tomar decisiones. Por ejemplo, un texto alternativo en una imagen mejora lo perceptible; un botón con foco visible mejora lo operable; un formulario con etiquetas claras mejora lo comprensible; un HTML válido y semántico mejora lo robusto.

Además, las pautas suelen organizarse en niveles de conformidad: A, AA y AAA. En términos pedagógicos, conviene pensar el nivel A como un mínimo obligatorio, mientras que AA suele ser una referencia muy razonable para proyectos reales. AAA existe como nivel más exigente, pero no siempre es viable en todos los contextos.

## HTML semántico y estructura comprensible

Una gran parte de la accesibilidad se construye antes del CSS y antes de JavaScript. La primera decisión importante es usar HTML con sentido semántico. Cuando un documento usa encabezados ordenados, listas reales, enlaces reales y regiones semánticas como `header`, `main`, `nav`, `section` o `footer`, la estructura resulta más clara tanto para personas como para software.

Eso significa, por ejemplo, evitar usar un `div` para todo cuando existe una etiqueta más apropiada. También significa respetar una jerarquía razonable de títulos, sin saltar arbitrariamente de `h1` a `h4`, y declarar correctamente el idioma del documento.

Una estructura semántica no garantiza por sí sola que el sitio sea accesible, pero sí establece una base mucho más sólida. Cuando esa base falta, luego se intenta corregir con CSS o con atributos extra lo que en realidad debería estar resuelto desde el HTML.

## Imágenes, enlaces y formularios accesibles

Hay tres zonas donde suelen aparecer errores frecuentes: imágenes, enlaces y formularios.

En las imágenes, el atributo `alt` debe describir la función o el contenido relevante de la imagen. Si la imagen es decorativa y no aporta información, el `alt` puede quedar vacío. Lo importante es no repetir automáticamente nombres de archivo ni dejar textos genéricos sin sentido.

En los enlaces, conviene que el texto enlace describa adónde lleva o qué acción produce. Un texto como “ver producto”, “descargar programa” o “ir al formulario de contacto” comunica más que un simple “click aquí”.

En los formularios, cada campo debería tener su `label` asociado. El `placeholder` puede servir como ayuda adicional, pero no debería reemplazar a la etiqueta. También es importante que los mensajes de error sean claros y que no dependan solo del color para comunicar el problema.

Un ejemplo simple sería:

```html
<label for="precio">Precio</label>
<input id="precio" name="precio" type="number">
```

Ese pequeño vínculo entre `for` e `id` mejora mucho la usabilidad general y la interpretación por tecnologías de asistencia.

## Contraste, foco y navegación por teclado

Muchas decisiones visuales afectan directamente la accesibilidad. Un diseño puede verse atractivo y, sin embargo, ser difícil de usar si el contraste es pobre, si los estados interactivos no se distinguen o si el foco desaparece.

Algunas reglas prácticas importantes son:

- mantener suficiente contraste entre texto y fondo;
- no usar el color como único medio para comunicar estados o errores;
- conservar un indicador de foco visible en enlaces, botones e inputs;
- verificar que la interfaz pueda recorrerse con teclado en un orden lógico.

Una mala práctica común es escribir algo como esto:

```css
.boton:focus {
  outline: none;
}
```

Si se elimina el foco por razones visuales, hay que reemplazarlo por otra señal clara. Por ejemplo:

```css
.boton:focus-visible {
  outline: 3px solid #1f6feb;
  outline-offset: 2px;
}
```

Este tipo de detalle parece pequeño, pero determina si una interfaz puede o no usarse con teclado de forma confiable.

También conviene no depender solo del hover para comunicar que un elemento es interactivo. En escritorio, el cursor puede sugerir bastante. En pantallas táctiles o en navegación por teclado, ese recurso desaparece. Por eso los estados activos, el foco visible y el tamaño de los controles siguen siendo decisiones centrales incluso cuando un framework ya ofrece estilos prearmados.

## Responsive design como parte de la experiencia

El responsive design no consiste solo en “hacer que entre” en una pantalla más chica. Consiste en reorganizar el contenido para que siga siendo legible, navegable y útil en distintos tamaños y condiciones de uso.

Esto incluye mucho más que el ancho de la ventana. En un teléfono, por ejemplo, cambian el espacio disponible, la forma de leer, la precisión del puntero y el contexto de uso. Por eso una interfaz responsive necesita priorizar contenido, simplificar patrones y revisar jerarquías.

Visto así, el responsive design se conecta con la accesibilidad: una interfaz que obliga a hacer zoom horizontal, que deja botones demasiado pequeños o que satura la pantalla con columnas innecesarias no ofrece una buena experiencia.

### **Responsive no es solo cambiar columnas**

En capítulos anteriores ya aparecieron media queries, Flexbox, Grid e incluso grillas de Bootstrap o variantes responsive de Tailwind. Todo eso sirve, pero no alcanza por sí solo. Una interfaz puede pasar de tres columnas a una y seguir estando mal resuelta.

Algunas preguntas más útiles son estas:

- ¿los botones y enlaces siguen teniendo un tamaño cómodo para tocar?
- ¿los textos mantienen una longitud razonable y una jerarquía clara?
- ¿los formularios apilan sus campos de una manera legible?
- ¿las tablas, menús o filtros complejos siguen siendo utilizables en poco espacio?

Pensado así, responsive design deja de ser una colección de breakpoints y pasa a ser una revisión de prioridades, lectura e interacción.

## Viewport, media queries y mobile first

Una de las primeras decisiones para trabajar diseño adaptable es incluir correctamente la etiqueta viewport:

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

Esa configuración ayuda a que el navegador interprete el ancho de la pantalla de forma adecuada. También es importante no bloquear el zoom del usuario, porque ampliarlo puede ser necesario para muchas personas.

Las media queries permiten ajustar el diseño cuando cambian ciertas condiciones, especialmente el ancho disponible. Por ejemplo:

```css
.productos {
  display: grid;
  grid-template-columns: 1fr;
  gap: 1rem;
}
```

```css
@media (min-width: 768px) {
  .productos {
    grid-template-columns: repeat(2, 1fr);
  }
}
```

```css
@media (min-width: 1024px) {
  .productos {
    grid-template-columns: repeat(3, 1fr);
  }
}
```

Este enfoque parte desde una base simple y luego agrega complejidad. Esa lógica coincide con mobile first: diseñar primero para pantallas pequeñas y extender después. Pedagógicamente, también obliga a distinguir qué contenido es realmente importante.

## Contenido flexible e imágenes responsivas

Para que un diseño responda bien, no alcanza con escribir media queries. Los componentes también tienen que estar construidos con cierta flexibilidad. Esto implica usar anchos relativos cuando corresponde, evitar medidas rígidas innecesarias y dejar que el contenido pueda reacomodarse.

En imágenes y multimedia, una regla muy habitual es:

```css
img, video {
  max-width: 100%;
  height: auto;
}
```

Con esto se evita que una imagen desborde su contenedor cuando el espacio disponible se reduce. Algo parecido ocurre con tablas, tarjetas, menús y formularios: si la estructura depende demasiado de tamaños fijos, el diseño se rompe con facilidad.

También conviene pensar en la longitud de línea, el tamaño de tipografía, el espaciado y el tamaño táctil de botones y enlaces. Un sitio puede ser técnicamente responsive y, aun así, seguir siendo incómodo si todo queda demasiado pequeño o demasiado apretado en mobile.

## Proyecto guiado: mejorar accesibilidad y responsive del supermercado

Este módulo puede aplicarse directamente sobre el proyecto de supermercado desarrollado en los capítulos anteriores. La idea no es rehacerlo por completo, sino revisar decisiones y mejorarlo con criterios concretos.

Una posible secuencia de trabajo es la siguiente:

- revisar que cada página tenga estructura semántica reconocible;
- comprobar que las imágenes de productos tengan textos alternativos útiles;
- verificar que los formularios de carga vinculen correctamente `label` e `id`;
- revisar contraste entre textos, botones y fondos;
- asegurar que enlaces y botones tengan foco visible;
- comprobar que los estados `hover` no sean la única pista de interacción;
- reorganizar listados o fichas para que funcionen bien en pantallas pequeñas;
- revisar si botones, enlaces y controles tienen tamaño táctil suficiente;
- aplicar media queries solo donde la estructura realmente lo necesite.

Un buen ejercicio consiste en abrir la página de listado y preguntarse: ¿qué pasa si la grilla de productos se ve en un teléfono? ¿Los textos siguen siendo legibles? ¿Los botones pueden tocarse sin dificultad? ¿El orden de lectura sigue siendo claro?

Esa clase de preguntas transforma el responsive design y la accesibilidad en criterios de revisión concretos, no en teoría abstracta.

## Validación y recursos recomendados para accesibilidad y responsive design

Antes de dar por terminado este módulo, conviene revisar el proyecto con una lista simple de control:

- ¿el documento declara idioma y viewport correctamente?
- ¿la jerarquía de títulos tiene sentido?
- ¿las imágenes importantes tienen `alt` útil?
- ¿los enlaces describen su destino o acción?
- ¿los formularios usan `label` asociado?
- ¿la interfaz puede recorrerse con teclado?
- ¿el foco es visible?
- ¿hay contraste suficiente entre texto y fondo?
- ¿la interfaz sigue siendo usable en pantallas pequeñas?

Además de la revisión manual, existen herramientas que ayudan a detectar problemas frecuentes. Lighthouse, las herramientas de desarrollo del navegador y validadores automáticos pueden señalar errores, aunque no reemplazan el criterio humano ni las pruebas reales de uso.

Recursos recomendados para profundizar:

- W3C Web Accessibility Initiative: [https://www.w3.org/WAI/](https://www.w3.org/WAI/)
- MDN sobre accesibilidad: [https://developer.mozilla.org/es/docs/Learn/Accessibility](https://developer.mozilla.org/es/docs/Learn/Accessibility)
- MDN sobre media queries: [https://developer.mozilla.org/es/docs/Web/CSS/CSS_media_queries/Using_media_queries](https://developer.mozilla.org/es/docs/Web/CSS/CSS_media_queries/Using_media_queries)
- The A11Y Project: [https://www.a11yproject.com/](https://www.a11yproject.com/)
- WCAG Quick Reference: [https://www.w3.org/WAI/WCAG22/quickref/](https://www.w3.org/WAI/WCAG22/quickref/)
- WebAIM Contrast Checker: [https://webaim.org/resources/contrastchecker/](https://webaim.org/resources/contrastchecker/)

Con este módulo queda consolidada una idea importante: desarrollar para la web no es construir una única versión pensada para un usuario ideal, sino producir interfaces capaces de adaptarse a la diversidad. A esta altura, ya debería poder mirar una interfaz con más criterio y detectar problemas de foco, contraste, estructura semántica o adaptación a pantallas pequeñas.

En el próximo módulo el foco pasará a JavaScript, incorporando lógica, comportamiento e interacción del lado del navegador.

## Ejercicios del capítulo

### Comprensión

1. Explique con sus palabras qué significan los principios POUR y por qué sirven como guía para evaluar una interfaz.
2. Describa por qué responsive design y accesibilidad no deberían pensarse como temas separados.
3. Explique qué problemas puede generar usar `placeholder` como reemplazo de `label` en un formulario.

### Aplicación

1. Revise una página web y detecte al menos tres problemas posibles de accesibilidad o adaptación responsive. Justifique por qué los considera problemáticos.
2. Ajuste una interfaz simple para que tenga foco visible, contraste razonable e imágenes responsivas, y registre qué cambios realizó.

### Integración

1. Tome una de las pantallas del proyecto del supermercado y haga una revisión integral a partir de dos preguntas: ¿se puede usar con teclado? y ¿se adapta bien a una pantalla pequeña? A partir de esa revisión, proponga y aplique un conjunto de mejoras concretas.
