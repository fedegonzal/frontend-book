# Conceptos básicos

Antes de analizar arquitecturas o escribir código paralelo, conviene comprender con precisión los conceptos básicos que organizan el campo. En esta unidad se distinguen distintos modos de ejecución, se revisan límites históricos de la computación secuencial y se introducen ideas centrales como núcleo de procesamiento, sincronización y niveles de paralelismo.

La computación paralela ocupa hoy un lugar central en la informática, porque muchos problemas actuales ya no pueden resolverse de manera eficiente programando algo secuencialmente de forma tradicional. Procesamiento de imágenes y video, simulaciones, análisis de grandes volúmenes de datos, inteligencia artificial y servicios distribuidos exigen aprovechar mejor los recursos de hardware disponibles. Por ese motivo, conviene estudiar el paralelismo no como un tema aislado, sino como una respuesta técnica a necesidades concretas de rendimiento.

También es importante notar que el problema involucra al mismo tiempo hardware y software. No alcanza con disponer de múltiples núcleos, clústeres o GPU: es necesario diseñar algoritmos capaces de dividir el trabajo, coordinar tareas y sincronizar resultados. Dicho de forma simple, los sistemas paralelos se ubican en la intersección entre arquitectura de cómputo, y modelos de programación.

## Objetivos del capítulo

- distinguir computación secuencial, concurrente, paralela y distribuida;
- explicar de manera introductoria cómo ejecuta instrucciones un procesador;
- relacionar la evolución del hardware con la necesidad de paralelizar;
- presentar los principales niveles de paralelismo.

## Por qué estudiar paralelismo

El paralelismo ya forma parte del hardware cotidiano. Computadoras personales, notebooks, teléfonos móviles y placas de video incorporan distintos niveles de ejecución simultánea. En consecuencia, incluso en desarrollos que no pertenecen a la computación de alto rendimiento, conviene entender cómo se reparten tareas, qué costos introduce la sincronización y qué límites aparecen cuando se busca acelerar un programa.

Estudiar sistemas paralelos implica construir criterios para distinguir cuándo un problema puede beneficiarse del paralelismo, qué arquitectura resulta más adecuada y cómo evaluar si la mejora obtenida justifica los recursos empleados.

Por ese motivo, conviene pensar el paralelismo también como una forma de analizar problemas. Antes de escribir una implementación paralela, suele ser necesario preguntarse qué partes del trabajo pueden ejecutarse de manera independiente, cuáles dependen de resultados previos y en qué momento será necesario recombinar los resultados parciales. Esa mirada de descomposición es tan importante como la herramienta elegida para programar.

## Computación secuencial

La computación secuencial es la forma tradicional de ejecución de programas. Las instrucciones se realizan una tras otra, en un orden determinado, y en cada instante solo una rama de ejecución avanza efectivamente. Aunque existan estructuras condicionales o repetitivas, el programa sigue un recorrido único en cada paso.

Comprender esta modalidad es importante porque el paralelismo no reemplaza por completo a la ejecución secuencial. Más bien se construye sobre ella, identificando qué partes de un problema pueden descomponerse y cuáles deben mantenerse en orden.

Un ejemplo simple ayuda a ver esta diferencia. Si se desea sumar los valores `(40 + 20 + 10 + 60)`, una implementación secuencial realiza una acumulación lineal: primero suma `(40 + 20)`, luego agrega `10` y finalmente `60`. En cambio, una descomposición paralela puede organizar el mismo cálculo en dos sumas parciales independientes, por ejemplo `(40 + 20)` y `(10 + 60)`, para luego combinar ambos resultados. El problema es el mismo, pero cambia la forma de organizar el trabajo.

Un pseudocódigo mínimo permite ver con más claridad esa reorganización:

```text
total = 40 + 20
total = total + 10
total = total + 60
```

Frente a una descomposición en árbol de dos etapas:

```text
parcial_1 = 40 + 20
parcial_2 = 10 + 60
total = parcial_1 + parcial_2
```

En la segunda formulación, `parcial_1` y `parcial_2` podrían calcularse de manera simultánea. La sincronización aparece en el momento de combinar ambos resultados para producir el valor final.

Esta observación parece menor, aunque en realidad introduce una idea central: paralelizar no consiste únicamente en ejecutar más cosas al mismo tiempo, sino en reorganizar un problema para exponer partes independientes sin perder corrección.

## Velocidad de ejecución y ciclo del procesador

Conviene introducir la idea de ciclo de reloj para explicar cómo la CPU sincroniza sus operaciones básicas. También puede presentarse, de forma simplificada, el ciclo de ejecución mediante las etapas fetch, decode, execute y write. Esta descripción permite entender que el rendimiento no depende solo de la cantidad de instrucciones, sino también de cómo las ejecuta el hardware.

Durante buena parte de la historia de la computación personal y de servidores, la mejora del rendimiento estuvo asociada sobre todo al aumento de la frecuencia de reloj y al perfeccionamiento de los procesadores mononúcleo. En ese contexto, la expectativa habitual era que cada nueva generación de hardware ejecutara el mismo software más rápido, aun sin cambios importantes en los programas. Esta etapa estuvo acompañada por la influencia de la llamada ley de Moore, que describía el crecimiento sostenido de la cantidad de transistores integrados en un chip y funcionó durante muchos años como marco general para pensar la evolución del hardware.

Sin embargo, ese crecimiento no podía traducirse indefinidamente en aumentos lineales de frecuencia. A medida que los procesadores alcanzaron velocidades cada vez mayores, comenzaron a hacerse más visibles problemas de temperatura, consumo energético y disipación térmica. En otras palabras, ya no resultaba viable sostener la mejora del rendimiento simplemente haciendo que un único núcleo trabajara cada vez más rápido. Ese límite marcó un cambio técnico e histórico importante en la industria.

La respuesta consistió en orientar la evolución de los procesadores hacia la integración de varios núcleos dentro de un mismo chip. En lugar de depender solo de un núcleo más veloz, comenzó a ganar importancia la posibilidad de ejecutar varias tareas o varias partes de un mismo problema en paralelo. En el mercado de consumo, esta transición se volvió especialmente visible con familias de procesadores de doble núcleo, entre ellas Intel Core 2 Duo, que ayudaron a consolidar la idea de que el rendimiento futuro dependería cada vez más de explotar concurrencia y paralelismo, y no únicamente de aumentar megahertz.

Este cambio tuvo consecuencias directas sobre el software. Mientras en la etapa mononúcleo gran parte de la mejora podía obtenerse por renovación de hardware, la era multicore exigió programas capaces de distribuir trabajo entre varios núcleos. Por ese motivo, estudiar paralelismo dejó de ser una cuestión reservada a supercomputadoras o a nichos especializados y pasó a convertirse en un problema general del desarrollo de software contemporáneo.

## Los límites de la computación secuencial

La disponibilidad de varios núcleos no elimina, por sí sola, los límites de la computación secuencial. Aunque el hardware permita ejecutar varias tareas al mismo tiempo, muchos programas contienen partes que deben mantenerse en orden, ya sea porque dependen de resultados previos o porque concentran decisiones que no pueden repartirse fácilmente.

A esto se suman los costos de coordinación. Dividir trabajo entre varios núcleos exige crear tareas, sincronizar resultados, compartir datos y, en muchos casos, esperar a que una parte del programa alcance a otra. Por ese motivo, una implementación paralela no siempre mejora en proporción directa a la cantidad de recursos disponibles. A veces la ganancia es modesta y, en situaciones mal diseñadas, incluso puede ocurrir que el overhead reduzca o anule la ventaja esperada.

Este punto resulta decisivo porque obliga a abandonar una idea ingenua: la de suponer que más hardware garantiza automáticamente más velocidad. En realidad, el rendimiento depende de la estructura del problema, del porcentaje de trabajo que puede ejecutarse en paralelo y del costo introducido por la coordinación. Más adelante se verá que estas restricciones pueden expresarse de manera más formal mediante nociones como speed-up, eficiencia y fracción secuencial.

## Concurrencia, paralelismo y distribución

La concurrencia se refiere a la coexistencia de varias tareas en ejecución o en progreso, aun cuando no siempre se resuelva un mismo problema. El paralelismo, en cambio, apunta específicamente a dividir un problema en partes que puedan ejecutarse simultáneamente para obtener un resultado común.

La computación distribuida agrega otra dimensión: los procesadores o nodos pueden encontrarse físicamente separados y cooperar mediante intercambio de datos. En la práctica contemporánea, estos enfoques suelen combinarse. Por ese motivo, conviene distinguir sus diferencias conceptuales sin perder de vista que en sistemas reales aparecen mezclados.

Una comparación breve permite aclarar la distinción. Si en una computadora se descarga un archivo mientras se reproduce música y se edita un documento, hay concurrencia: varias tareas avanzan en el mismo intervalo, aunque no cooperan para resolver un único problema. En cambio, si una suma grande de datos se divide en bloques para que varios núcleos calculen subtotales y luego se integren en un único resultado, hay paralelismo. En ambos casos puede haber actividad simultánea, pero solo en el segundo existe cooperación directa sobre una misma tarea.

## Niveles de paralelismo

Conviene distinguir distintos niveles de paralelismo porque no todos operan en la misma escala ni exigen el mismo tipo de intervención por parte de quien programa. Algunos aparecen cerca del hardware y funcionan de manera casi transparente, mientras que otros requieren decisiones explícitas sobre cómo dividir trabajo, datos y sincronización.

Entre los niveles más cercanos al hardware suele mencionarse el paralelismo a nivel de bit, que aparece cuando una arquitectura amplía la cantidad de bits que puede procesar en una sola operación. También resulta importante el paralelismo a nivel de instrucción, donde el procesador reorganiza y solapa internamente la ejecución de varias instrucciones. En este punto conviene incorporar la idea de pipelining en hardware. Un pipeline divide la ejecución de una instrucción en etapas, por ejemplo búsqueda, decodificación, ejecución y escritura, y permite que distintas instrucciones ocupen simultáneamente distintas etapas del procesador. De ese modo, mientras una instrucción se ejecuta, otra puede estar siendo decodificada y una tercera puede estar siendo traída desde memoria. No se trata todavía de paralelismo entre programas diferentes, sino de una forma de aumentar el rendimiento interno del procesador mediante solapamiento.

En un nivel más visible para el software aparecen formas de paralelismo que sí exigen decisiones de diseño. El paralelismo de tareas divide un problema en subtareas que pueden asignarse a distintas unidades de procesamiento. El paralelismo de datos, en cambio, aplica la misma operación sobre particiones independientes de un conjunto de entrada. La vectorización puede entenderse como una forma particularmente importante de este segundo enfoque, ya que aprovecha operaciones repetitivas sobre estructuras de datos para ejecutarlas de manera más eficiente, muchas veces apoyándose en capacidades del hardware como SIMD.

Distinguir estos niveles es importante porque la mejora de rendimiento no siempre proviene del mismo lugar. A veces surge de mecanismos internos del procesador, como el pipelining o el paralelismo a nivel de instrucción, que resultan casi invisibles para quien programa. En otros casos depende de decisiones explícitas, como repartir tareas entre varios workers o reorganizar datos para aplicar la misma operación muchas veces. Reconocer estas diferencias ayuda a elegir mejor las herramientas, formular expectativas realistas y entender por qué dos programas pueden comportarse de manera distinta aun cuando se ejecuten sobre el mismo hardware.

## Observación del uso de CPU

En los trabajos prácticos conviene observar la carga de cada core y no solo un porcentaje global de CPU. Esa diferencia es importante porque un programa puede mostrar un uso alto del procesador en términos generales y, sin embargo, seguir concentrando casi todo su trabajo en un único núcleo. Mirar la actividad por core permite detectar con más claridad si una implementación realmente distribuye el trabajo o si mantiene un comportamiento predominantemente secuencial.

En Linux, una primera herramienta útil es `top`, disponible desde la línea de comandos. Permite ver procesos activos, consumo de CPU y memoria, y sirve como punto de partida para observar qué ocurre mientras se ejecuta un programa. También existen alternativas más visuales, como `htop` o `btop`, que facilitan la lectura porque muestran barras por núcleo, colores y una organización más clara de los procesos en ejecución. Para los fines de este libro, cualquiera de estas herramientas resulta suficiente siempre que permita responder una pregunta simple: si el programa intenta paralelizar trabajo, ¿se reparte efectivamente entre varios cores o no?

En macOS, la referencia más directa es el Monitor de Actividad, que ofrece una vista gráfica del uso del sistema y permite inspeccionar procesos, consumo de CPU y carga general. Si se prefiere trabajar desde terminal, también puede usarse `top`, aunque en la práctica la herramienta visual suele ser más cómoda para una observación inicial. En Windows, el Administrador de tareas cumple un papel equivalente y permite ver el uso global de CPU, la actividad por proceso y, en la pestaña de rendimiento, la distribución de carga del procesador. Según la versión del sistema, también puede recurrirse al Monitor de recursos para un análisis algo más detallado.

Lo importante no es dominar una herramienta específica, sino adquirir un criterio de observación. Si un programa secuencial mantiene ocupado principalmente un solo core, ese comportamiento es esperable. Si una versión paralela usa varios núcleos, conviene mirar si la carga se reparte de manera relativamente equilibrada o si algunos cores trabajan mucho más que otros. Esa observación no reemplaza la medición de tiempos, pero ayuda a interpretar mejor los resultados y a detectar tempranamente problemas de diseño o de implementación.

## Cierre de la unidad

Con este marco ya se cuenta con una base conceptual suficiente para avanzar hacia el análisis de plataformas y métricas. En particular, el capítulo permitió distinguir tipos de ejecución, entender por qué el multicore modificó el problema del rendimiento y ver que paralelizar exige descomponer, coordinar y sincronizar trabajo.

En el próximo capítulo se estudiarán clasificaciones de arquitecturas paralelas y medidas de rendimiento como speed-up y eficiencia. Ese paso permitirá no solo describir plataformas, sino también analizar por qué una implementación paralela puede rendir mucho mejor, apenas mejor o incluso peor de lo esperado.

## Ejercicios del capítulo

- Distinga computación secuencial, concurrente, paralela y distribuida.
- Explique por qué la aparición de procesadores multicore modificó las exigencias sobre el software.
- Describa la diferencia entre paralelismo de tareas y paralelismo de datos.
- Explique por qué conviene entender el paralelismo también como una forma de descomponer problemas.
- Proponga un ejemplo cotidiano de tarea concurrente y otro de tarea paralela.
- Observe el monitor de actividad de su sistema y describa qué información ofrece sobre el uso de los distintos cores.
- Reescriba conceptualmente una suma secuencial de cuatro valores como una suma en árbol de dos etapas e indique dónde aparece la sincronización.
- Justifique por qué disponer de más cores no garantiza, por sí solo, una mejora lineal del rendimiento.