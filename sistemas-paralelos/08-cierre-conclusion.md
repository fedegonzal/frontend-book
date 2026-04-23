# Cierre y conclusión

Al llegar a este punto, conviene recuperar la idea central que recorrió todo el libro: paralelizar no consiste solamente en usar más hardware, sino en aprender a descomponer problemas, elegir una estrategia de ejecución adecuada, medir resultados e interpretar límites reales de escalabilidad. Esa perspectiva atraviesa desde los conceptos más generales hasta los casos de vectorización y GPU.

El recorrido desarrollado buscó justamente construir esa mirada. Primero se distinguieron los conceptos fundamentales del paralelismo y su diferencia respecto de la concurrencia y la computación distribuida. Luego se introdujeron arquitecturas, métricas y límites teóricos. Sobre esa base se estudiaron modelos de programación, APIs clásicas y herramientas accesibles en Python. En la parte final del libro, esa progresión se organizó en tres movimientos complementarios: paralelismo explícito en CPU, reformulación eficiente del cálculo sobre arreglos y tensores en CPU, y aceleración sobre GPU.

En términos generales, el libro deja cuatro aprendizajes principales.

El primero es conceptual. Resulta importante distinguir con precisión entre ejecución secuencial, concurrencia, paralelismo y distribución. Esa diferenciación inicial evita muchas confusiones posteriores y permite leer con mayor claridad las decisiones de diseño.

El segundo es arquitectónico. El rendimiento de una implementación no depende solo del algoritmo, sino también del tipo de memoria, de la jerarquía de caché, del ancho de banda disponible y de los costos de sincronización. Por ese motivo, una solución correcta puede exhibir resultados muy distintos según la plataforma en la que se ejecute.

El tercero es metodológico. Medir tiempos no alcanza por sí solo. Conviene interpretar speed-up, eficiencia, fracción secuencial, acceso a memoria y sobrecarga de coordinación. Sin ese paso analítico, la comparación entre implementaciones queda incompleta.

El cuarto es práctico. En muchos problemas no existe una única forma correcta de mejorar rendimiento. A veces conviene repartir tareas de manera explícita en CPU; en otros casos, reformular el cálculo mediante vectorización o trabajo con tensores; en otros, aprovechar GPU; y en otros, aceptar que el costo de paralelizar o acelerar no justifica el beneficio esperado.

## Criterios que conviene conservar

Más allá de las bibliotecas o arquitecturas puntuales, este libro intentó sostener algunos criterios generales que conviene conservar al seguir estudiando el tema.

Uno de ellos es que la elección de una estrategia debe responder a la estructura del problema. No se elige primero una herramienta y luego se busca dónde usarla. Conviene analizar si el trabajo es regular o irregular, si predomina el cómputo o el acceso a memoria, si el problema admite división natural en subtareas y qué costo introduce la coordinación entre ellas.

Otro criterio importante es que el paralelismo siempre debe leerse junto con sus límites. Las leyes de Amdahl y Gustafson, la jerarquía de memoria, la localidad de caché, el false sharing, NUMA o los costos de transferencia en GPU muestran que escalar no es simplemente agregar recursos. También exige comprender dónde aparece el cuello de botella.

Un tercer criterio tiene que ver con la observación. A lo largo del recorrido aparecieron señales de debugging y profiling en CPU y GPU. Ese punto conviene subrayarlo: en sistemas paralelos, muchos errores no son evidentes a primera vista. Un resultado no determinista, una mejora menor a la esperada o un kernel correcto pero ineficiente exigen mirar más allá del código fuente y prestar atención al comportamiento real del sistema.

Como cierre sintético del recorrido, conviene recuperar una tabla de decisión general sobre algunas de las herramientas discutidas en el libro. No debe leerse como una receta cerrada, sino como un recordatorio de que la elección siempre depende de la estructura del problema, de la arquitectura disponible y de la medición posterior.

| Estrategia | Conviene usarla cuando | Ventaja principal | Límite principal |
|---|---|---|---|
| `threading` | la tarea espera entrada/salida | bajo costo y buena respuesta concurrente | no acelera bien tareas CPU-bound por el GIL |
| `multiprocessing` | la tarea es CPU-bound y puede repartirse en bloques | evita el GIL | serialización y comunicación entre procesos |
| NumPy | el problema es numérico y regular sobre arreglos | vectorización eficiente con una interfaz simple | menor flexibilidad para lógica irregular |
| Numba CPU | se quiere acelerar código numérico en Python sin abandonar loops y estructuras explícitas | compilación JIT y paralelismo cercano al hardware sobre CPU | requiere código compatible y cierto cuidado con tipos y estructuras |
| Numba GPU | interesa controlar kernels, índices y configuración de ejecución sobre GPU | hace visible el modelo de ejecución del acelerador | exige mayor atención a memoria, configuración y detalles del hardware |
| PyTorch CPU | el problema ya se expresa de manera natural sobre tensores en CPU | continuidad clara con operaciones sobre tensores y puente natural hacia GPU | agrega una biblioteca más pesada si solo se necesita cálculo numérico simple |
| PyTorch GPU | el cálculo ya se formula sobre tensores y puede beneficiarse del acelerador | permite mantener una interfaz de alto nivel sobre GPU | el costo de transferencia puede anular la mejora si el volumen de trabajo es bajo |

Esta síntesis no reemplaza la medición, pero ayuda a recuperar de un vistazo parte de los criterios prácticos construidos a lo largo del libro. También permite leer con más claridad la progresión final del recorrido: de repartir trabajo en CPU, a reformular el cálculo sobre estructuras de datos completas, y de allí a mover ese cálculo hacia un acelerador cuando el problema lo justifica.

En ese sentido, el caso de Sobel utilizado en la parte final del libro funciona como un buen recordatorio metodológico. El mismo problema pudo leerse como loop secuencial, como cálculo compilado sobre CPU, como reformulación sobre arreglos y tensores, y finalmente como ejecución sobre GPU. Esa continuidad no convierte al caso en una receta universal, pero sí ayuda a ver que lo decisivo no es la herramienta aislada, sino la relación entre estructura del problema, forma de expresarlo y arquitectura elegida.

## Del fundamento a la práctica contemporánea

Otro aspecto que conviene retener es que los fundamentos clásicos siguen siendo relevantes incluso cuando se trabaja con herramientas modernas. Los modelos de programación paralela, las APIs históricas y la distinción entre memoria compartida y distribuida, siguen apareciendo en bibliotecas de alto nivel, frameworks de datos y entornos de aceleración contemporáneos.

En ese sentido, aprender paralelismo no equivale a memorizar tecnologías pasajeras. Supone construir una base conceptual que permita entender por qué una herramienta funciona, en qué contexto resulta adecuada y cuáles son sus límites. Esa base es la que hace posible adaptarse a nuevas bibliotecas y nuevas plataformas sin empezar siempre desde cero.

## Continuidad del estudio

Este libro presentó conceptos y herramientas contemporáneas para introducir el estudio del paralelismo desde una perspectiva a la vez conceptual y práctica. A lo largo del recorrido se abordaron modelos, métricas, arquitecturas y bibliotecas que permiten comprender cómo se descompone un problema, cómo se distribuye el trabajo y bajo qué criterios conviene evaluar el rendimiento obtenido.

Si bien aquí fue necesario separar algunos conceptos para volverlos más claros en un trayecto introductorio, conviene subrayar que, en aplicaciones reales, paralelismo, concurrencia y sistemas distribuidos suelen convivir. Un mismo sistema puede coordinar múltiples tareas concurrentes, paralelizar partes de su cómputo y, al mismo tiempo, repartir trabajo o datos entre varios nodos. Por ese motivo, el cierre de este libro no debe leerse como un punto final, sino como una base desde la cual pueden continuarse varias líneas de profundización.

Una de esas líneas de continuidad aparece en el estudio más profundo de modelos y herramientas ya introducidos de manera inicial en el recorrido. En ese marco, una posibilidad clara es avanzar hacia MPI en un nivel más desarrollado. El uso introductorio de operaciones colectivas permite comprender el modelo, pero un estudio posterior podría incorporar topologías, patrones de comunicación más complejos y escenarios más cercanos a clústeres reales.

También existe una continuidad natural hacia frameworks y modelos más recientes, como Dask, Ray o enfoques de dataflow. Estos temas no fueron desarrollados en el cuerpo principal del libro porque exceden su carácter introductorio, pero constituyen una expansión razonable para quien quiera conectar fundamentos de paralelismo con ecosistemas contemporáneos de datos y sistemas distribuidos.

Por último, puede profundizarse el estudio de GPU desde una perspectiva más cercana a la optimización fina, incorporando herramientas de profiling específicas, análisis detallado de kernels y estrategias avanzadas de memoria.
