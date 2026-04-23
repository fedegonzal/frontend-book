# Modelos de programación paralela

Disponer de hardware paralelo no garantiza por sí mismo una solución eficiente. También es necesario decidir cómo descomponer el problema, cómo distribuir tareas y cómo coordinar resultados. Los modelos de programación paralela ofrecen justamente marcos de organización para pensar estas decisiones.

## Objetivos del capítulo

- presentar algunos paradigmas clásicos de programación paralela;
- describir el tipo de problemas para los que cada modelo puede resultar útil;
- vincular cada paradigma con las nociones de comunicación, sincronización y distribución del trabajo.

## Por qué trabajar con modelos

Los modelos de programación paralela funcionan como esquemas conceptuales y prácticos. Permiten reconocer patrones recurrentes en problemas distintos y facilitan la elección de una estrategia de implementación. En lugar de empezar desde cero ante cada desafío, conviene apoyarse en estructuras conocidas que ya organizan la coordinación entre procesos o tareas.

Antes de revisar cada paradigma, conviene identificar algunas preguntas guía:

- ¿el problema puede dividirse en subtareas relativamente independientes o requiere una coordinación central fuerte?;
- ¿el trabajo se parece más a una secuencia de etapas, a una descomposición recursiva o a una aplicación repetida de la misma operación sobre muchos datos?;
- ¿la comunicación entre tareas será frecuente o esporádica?;
- ¿interesa más maximizar rendimiento, simplificar implementación o facilitar escalabilidad distribuida?;
- ¿el problema tiene una estructura estable y regular, o cambia dinámicamente durante la ejecución?

Estas preguntas no producen una respuesta automática, pero permiten justificar mejor por qué un modelo resulta más adecuado que otro.

## Modelo maestro-esclavo

El modelo maestro-esclavo, también llamado master-slave, organiza la ejecución a partir de un proceso principal que distribuye trabajo a varios procesos secundarios. El maestro coordina, asigna tareas y reúne resultados. Este enfoque resulta claro cuando existe una lógica central de reparto y control.

Este modelo es útil cuando las tareas son muchas, relativamente similares entre sí y pueden asignarse desde un punto central sin excesivo costo. Un caso típico es el procesamiento por lotes de archivos, imágenes o registros, donde un proceso maestro reparte unidades de trabajo independientes a varios workers.

Puede pensarse en la conversión de un conjunto grande de imágenes. El proceso maestro mantiene la lista de archivos pendientes y asigna una imagen a cada worker disponible. Cada worker aplica la misma transformación, por ejemplo cambiar formato o reducir tamaño, y luego devuelve el resultado o informa que terminó. El maestro continúa repartiendo trabajo hasta completar todo el lote.

Un esquema mínimo de pseudocódigo puede escribirse así:

```text
funcion maestro(tareas, workers):
	pendientes = copiar(tareas)

	mientras haya_tareas(pendientes):
		para cada worker disponible en workers:
			tarea = tomar_siguiente(pendientes)
			enviar(worker, tarea)

		recibir_resultados()
```

Su ventaja principal es la claridad organizativa. Su riesgo principal es que el maestro se convierta en cuello de botella o en punto único de falla si concentra demasiadas decisiones o demasiada comunicación.

## Divide and conquer

El modelo divide and conquer resuelve un problema descomponiéndolo en subproblemas más pequeños. Cada parte se resuelve por separado y luego los resultados parciales se combinan para obtener la solución final. En muchas implementaciones, esta descomposición se aplica de manera recursiva, pero la idea central del paradigma es la partición del problema y la posterior recomposición. Ejemplos clásicos son QuickSort y ciertas estrategias de multiplicación de matrices.

Este paradigma es útil cuando el problema admite una descomposición natural y relativamente equilibrada.

Un ejemplo más simple es la suma de un vector dividido en bloques. En lugar de recorrer todos los elementos en una sola secuencia, el conjunto de datos puede separarse en partes de tamaño semejante. Cada parte se procesa por separado y, al final, los subtotales se combinan para obtener el resultado global. Aunque muchas implementaciones de este paradigma usan recursión, la idea central puede entenderse también como una división del problema en partes comparables que luego se recomponen.

Un esquema mínimo de pseudocódigo puede escribirse así:

```text
funcion suma_por_bloques(datos, cantidad_bloques):
	bloques = particionar(datos, cantidad_bloques)
	subtotales = []

	para cada bloque en bloques:
		subtotales.agregar(sumar(bloque))

	return sumar(subtotales)
```

En una implementación paralela, cada bloque podría procesarse al mismo tiempo y la fase final solo tendría que combinar los subtotales obtenidos.

Conviene usar este modelo cuando la división del problema produce subproblemas de tamaño semejante y con poca dependencia entre sí. Si las particiones quedan muy desbalanceadas o si la fase de combinación resulta costosa, la ventaja del modelo disminuye.

## Pipelining

El modelo de pipelining divide el procesamiento en etapas. Cada etapa realiza una parte del trabajo y pasa el resultado a la siguiente. Mientras una etapa procesa un nuevo elemento, otra puede estar terminando el elemento anterior. Se genera así un flujo continuo, similar a una línea de producción.

Su principal desafío consiste en gestionar correctamente las dependencias entre etapas para evitar cuellos de botella.

Este paradigma resulta especialmente útil cuando el trabajo puede describirse como una secuencia estable de transformaciones. Un caso reconocible es el procesamiento de datos provenientes de sensores, video o registros: una etapa lee, otra limpia, otra transforma y una última almacena o visualiza resultados.

Un caso simple aparece en el procesamiento de formularios enviados desde un sitio web. Una primera etapa recibe los datos, una segunda valida los campos, una tercera normaliza el formato y una cuarta guarda la información en una base de datos. Mientras un formulario se encuentra en la etapa de almacenamiento, otro puede estar siendo validado y un tercero puede estar ingresando al sistema.

Un esquema mínimo de pseudocódigo puede representarse de este modo:

```text
funcion pipeline(formulario):
	datos = recibir(formulario)
	datos_validados = validar(datos)
	datos_normalizados = normalizar(datos_validados)
	guardar(datos_normalizados)
```

## MapReduce

MapReduce organiza el cálculo en dos grandes fases: una etapa de mapeo, que aplica una operación sobre múltiples elementos, y una etapa de reducción, que combina los resultados parciales. Se trata de un modelo muy asociado al procesamiento distribuido de grandes volúmenes de datos y a herramientas como Hadoop o Apache Spark.

Aunque en este libro se presenta de forma introductoria, su valor conceptual es grande porque muestra una estrategia de paralelización centrada en datos y agregación de resultados.

El conteo de palabras en una gran colección de documentos permite verlo con claridad. La fase de map recorre cada documento y produce pares del tipo palabra, 1 cada vez que encuentra una aparición. Luego, la fase de reduce agrupa todas las ocurrencias de una misma palabra y suma esos valores parciales para obtener el total final. Más allá de la herramienta concreta, lo importante es observar que el modelo organiza con claridad la relación entre paralelismo de datos y agregación.

Conviene usar este enfoque cuando la tarea puede expresarse como una operación repetida sobre muchas entradas independientes seguida de una combinación de resultados. No suele ser la mejor opción cuando existen dependencias complejas, interacción frecuente entre tareas o estructuras de datos muy cambiantes.

## Modelo de actores

En el modelo de actores, cada componente se entiende como una entidad independiente con estado propio, que se comunica con otros actores mediante mensajes. No se basa necesariamente en una jerarquía fija, sino en interacciones coordinadas entre componentes autónomos. Se trata, ante todo, de un modelo de concurrencia y organización del sistema. Sin embargo, se incluye en este capítulo porque ofrece una forma de estructurar problemas en los que muchas actividades pueden avanzar en paralelo sin compartir memoria directamente.

Un caso reconocible es una plataforma compuesta por servicios que reciben eventos, procesan pedidos y envían respuestas sin compartir memoria directamente. Cada actor mantiene su estado local y responde a mensajes, lo que favorece desacoplamiento y escalabilidad.

Un ejemplo posible es un sistema de simulación en el que cada partícula o entidad del modelo se representa como un actor. Cada una mantiene su propio estado y envía mensajes a otras cuando necesita informar un cambio, por ejemplo una colisión, una proximidad o una modificación de velocidad. De ese modo, la simulación no depende de una memoria compartida central para coordinar todas las interacciones. Si muchas entidades evolucionan al mismo tiempo, distintos actores pueden procesar mensajes de manera concurrente, y en muchos entornos esa concurrencia también puede traducirse en ejecución paralela.

Este modelo conviene cuando interesa reducir acoplamiento entre componentes y tolerar mejor la complejidad de la concurrencia. No siempre su objetivo principal es acelerar un cálculo del mismo modo que divide and conquer o MapReduce, pero sí puede servir para organizar sistemas donde muchas tareas o eventos deben resolverse de manera simultánea. A cambio, obliga a pensar cuidadosamente el diseño de mensajes, la coordinación entre actores y el seguimiento del estado distribuido.

## Comparación conceptual entre modelos

Si se observa el conjunto, maestro-esclavo y divide and conquer son modelos orientados con más claridad al reparto del trabajo. Pipelining organiza una cadena de etapas. MapReduce enfatiza transformación de datos y agregación. Actores, en cambio, privilegia la coordinación entre componentes autónomos y por eso queda más cerca de los modelos de concurrencia que de los esquemas clásicos de paralelización de datos.

Ningún modelo resuelve por sí solo todos los problemas. En sistemas reales es frecuente combinar varios. Por ejemplo, un clúster puede usar un esquema maestro-esclavo para distribuir bloques de datos y, dentro de cada bloque, aplicar una estrategia divide and conquer o un pipeline de procesamiento.

La siguiente tabla resume el rasgo dominante de cada modelo y el tipo de problema en el que suele resultar más útil.

| Modelo | Idea central | Conviene usarlo cuando | Caso reconocible |
|---|---|---|---|
| Maestro-esclavo | un coordinador reparte trabajo y reúne resultados | hay una lógica central clara de asignación y control | procesamiento de lotes independientes |
| Divide and conquer | el problema se divide en partes y luego se combinan resultados | la tarea admite particiones naturales y balanceadas | suma por bloques, ordenamiento, matrices |
| Pipelining | el trabajo se organiza en etapas consecutivas | los datos fluyen por fases con operaciones diferenciadas | procesamiento de imágenes o streaming |
| MapReduce | se aplica una función a muchos datos y luego se agregan resultados | hay grandes volúmenes de datos con operaciones homogéneas | conteo de palabras, agregaciones masivas |
| Actores | componentes autónomos intercambian mensajes | el sistema requiere desacoplamiento, concurrencia y evolución dinámica | servicios distribuidos o sistemas reactivos |

## Cierre de la unidad

Este capítulo subraya un punto decisivo: programar algoritmos paralelos suele ser más difícil que programar algoritmos secuenciales. La sincronización, la comunicación entre procesos y la necesidad de evitar errores como esperas innecesarias o incoherencias de datos introducen complejidad adicional.

Por ese motivo, los modelos no solo ayudan a organizar soluciones, sino también a razonar sobre sus riesgos y limitaciones.

En este sentido, elegir un modelo adecuado no es solo una cuestión de estilo. Una buena elección puede reducir comunicación, simplificar sincronización y mejorar la escalabilidad. Una mala elección puede producir cuellos de botella, tareas desbalanceadas o una implementación innecesariamente difícil de mantener.

Con estos paradigmas ya es posible pasar de la discusión arquitectónica a una discusión de diseño. El capítulo mostró que programar en paralelo no consiste solo en lanzar hilos o procesos, sino en decidir cómo se estructura el trabajo y cómo se relacionan las tareas entre sí.

En el próximo capítulo estas ideas se traducirán a APIs clásicas de programación paralela. Allí se verá cómo modelos como memoria compartida, memoria distribuida y reparto de tareas se concretan en herramientas específicas de implementación.

## Ejercicios del capítulo

- Describa las características básicas del modelo maestro-esclavo.
- Explique en qué se diferencia un pipeline de una estrategia divide and conquer.
- Indique qué papel cumplen los mensajes en el modelo de actores.
- Justifique por qué MapReduce se asocia especialmente con problemas de gran volumen de datos.
- Proponga un caso en el que maestro-esclavo sea una mejor elección que actores y explique por qué.
