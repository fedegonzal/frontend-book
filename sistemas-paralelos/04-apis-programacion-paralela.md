# APIs de programación paralela

Luego de estudiar modelos de diseño, conviene presentar algunas APIs clásicas que han tenido un papel relevante en la programación paralela. Estas herramientas no solo permiten implementar soluciones, sino que también representan enfoques distintos según el tipo de arquitectura disponible.

Aunque en este libro el trabajo aplicado se desarrolla principalmente con Python, conviene conocer estas APIs porque siguen siendo una referencia importante para entender cómo se programa cerca del hardware y por qué muchas herramientas de más alto nivel toman ideas de estos modelos.

## Objetivos del capítulo

- introducir Pthreads, OpenMP y MPI como referencias clásicas del área;
- vincular cada API con su ámbito de aplicación principal;
- reconocer diferencias entre memoria compartida, memoria distribuida e implementaciones híbridas;
- comparar mecanismos de comunicación, sincronización y nivel de abstracción;
- mostrar decisiones concretas de diseño a partir de un mismo problema.

## Por qué estudiar estas APIs

Pthreads, OpenMP y MPI forman una tríada clásica porque condensan tres modos distintos de pensar la programación paralela. Pthreads expone control fino sobre hilos y sincronización. OpenMP simplifica la incorporación de paralelismo en memoria compartida mediante directivas. MPI organiza la cooperación entre procesos independientes que intercambian mensajes.

## Pthreads

Pthreads es una API POSIX orientada a la programación con hilos en sistemas de memoria compartida. Su importancia histórica radica en ofrecer una forma estandarizada de crear, coordinar y sincronizar hilos de ejecución. En lenguajes como C, C++ y Fortran ha sido una herramienta importante para trabajar con paralelismo a bajo nivel.

Pthreads conviene cuando se necesita control detallado sobre la creación de hilos, la asignación de trabajo y la sincronización. Ese control fino es una fortaleza, pero también aumenta la complejidad. Un mutex permite asegurar exclusión mutua sobre una sección crítica, es decir, impedir que dos hilos modifiquen al mismo tiempo un mismo dato compartido. Las variables compartidas son justamente los datos accesibles por varios hilos, y por eso deben protegerse o coordinarse con cuidado. Las barreras obligan a que varios hilos esperen hasta alcanzar un mismo punto de ejecución antes de continuar, mientras que las variables de condición permiten suspender un hilo hasta que se cumpla cierto estado o evento.

Trabajar con estos mecanismos exige mucha atención porque un uso incorrecto puede producir race conditions, es decir, resultados que dependen del orden imprevisible en que acceden los hilos a los datos. También puede generar bloqueos, por ejemplo cuando dos hilos quedan esperando indefinidamente recursos o señales del otro. En términos de aprendizaje, Pthreads permite ver con claridad que paralelizar no consiste solo en repartir trabajo, sino también en coordinar accesos, esperas y dependencias de manera segura.

En términos de diseño, Pthreads resulta útil para entender qué significa realmente paralelizar en memoria compartida sin ayudas adicionales del compilador.

## OpenMP

OpenMP es una API orientada a memoria compartida que simplifica la incorporación de paralelismo mediante directivas del compilador. Se usa principalmente con C, C++ y Fortran, y resulta adecuada para paralelizar bucles y secciones de código en equipos con múltiples núcleos.

En el recorrido del libro, OpenMP cumple una doble función: por un lado, es una referencia estándar del área; por otro, sirve como antecedente conceptual para entender herramientas en Python que ofrecen estrategias semejantes.

Su ventaja principal es que permite agregar paralelismo incremental sobre código secuencial existente. En muchos casos basta con identificar un bucle independiente y marcarlo como región paralela. OpenMP ofrece menos control explícito que Pthreads porque el programador no suele crear y coordinar hilos uno por uno, sino que describe regiones paralelas, bucles o reducciones y deja que el compilador y el entorno de ejecución decidan cómo materializar esa estrategia. Dicho de otro modo, en Pthreads se programa de manera directa la lógica de creación, sincronización y reparto; en OpenMP se declara qué partes pueden ejecutarse en paralelo y con qué restricciones.

Por ese motivo, OpenMP se apoya fuertemente en el compilador y en la semántica de sus directivas. Una instrucción como `#pragma omp parallel for` no implementa por sí misma el paralelismo, sino que le indica al compilador cómo transformar ese bloque para ejecutarlo con varios hilos. Esa mediación simplifica mucho el trabajo y reduce código de sincronización explícita, pero también implica aceptar menor control fino sobre decisiones como la organización exacta de los hilos o ciertos detalles del reparto de trabajo.

Un ejemplo mínimo en C permite ver esa lógica:

```c
#include <omp.h>
#include <stdio.h>

int main() {
	int total = 0;

	#pragma omp parallel for reduction(+:total)
	for (int i = 0; i < 100; i++) {
		total += i;
	}

	printf("Total: %d\n", total);
	return 0;
}
```

En este fragmento, la directiva `#pragma omp parallel for` indica que las iteraciones del bucle pueden repartirse entre varios hilos. La cláusula `reduction` resuelve de forma segura la acumulación parcial. El interés pedagógico del ejemplo no está en el detalle sintáctico, sino en mostrar que OpenMP expresa paralelismo de forma declarativa y compacta.

## MPI

MPI, sigla de Message Passing Interface, es una API pensada para sistemas distribuidos. Cada proceso es independiente y la coordinación se realiza mediante envío y recepción explícita de mensajes. Esto la vuelve especialmente relevante para clústeres y contextos de computación científica.

En este libro se incluyen ejemplos introductorios con `mpi4py`, lo que permite acercar este modelo al entorno Python sin perder la lógica central del intercambio de mensajes entre procesos.

MPI es útil cuando los procesos no comparten memoria y la distribución de datos debe explicitarse. Esa es su principal diferencia con Pthreads y OpenMP: aquí la comunicación no está implícita en variables compartidas, sino que debe diseñarse conscientemente mediante primitivas como `send`, `recv`, `scatter`, `gather`, `broadcast` y `reduce`.

En términos conceptuales, algunas de las operaciones más importantes son estas:

- `broadcast`: un proceso envía el mismo dato a todos los demás;
- `scatter`: un proceso reparte fragmentos distintos de un conjunto de datos;
- `gather`: varios procesos devuelven resultados parciales a un proceso raíz;
- `reduce`: varios resultados parciales se combinan mediante una operación como suma, máximo o mínimo.

Un ejemplo mínimo con `mpi4py` muestra la lógica de `scatter` y `gather`:

```python
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
	data = [10, 20, 30, 40]
else:
	data = None

value = comm.scatter(data, root=0)
partial = value * 2
results = comm.gather(partial, root=0)

if rank == 0:
	print(results)
```

Aquí el proceso raíz distribuye cuatro valores, cada proceso calcula un resultado local y luego el conjunto de resultados vuelve al proceso raíz. Se trata de un patrón muy frecuente en problemas distribuidos.

También es habitual combinar `scatter` con `reduce` cuando interesa repartir datos y obtener directamente un agregado final sin reconstruir toda la colección intermedia.

## Diferencias y ámbitos de aplicación

Pthreads y OpenMP se asocian, en general, a sistemas de memoria compartida. MPI, en cambio, responde de forma más natural a escenarios de memoria distribuida. También es posible combinar enfoques, por ejemplo mediante OpenMP más MPI, dando lugar a modelos híbridos.

Reconocer estas diferencias permite evitar un error frecuente: pensar que existe una única forma de paralelizar. En realidad, la arquitectura disponible condiciona de manera fuerte qué herramientas resultan más adecuadas.

En una estación de trabajo multicore, Pthreads u OpenMP suelen ser elecciones naturales. En un clúster donde cada nodo tiene memoria propia, MPI se vuelve la opción más razonable. En un sistema híbrido, una estrategia común consiste en usar MPI para repartir trabajo entre nodos y OpenMP dentro de cada nodo para explotar los cores locales.

## Vista comparativa

Antes de revisar cada API por separado, conviene ordenar sus diferencias principales en una única comparación.

| API | Arquitectura más natural | Comunicación o sincronización principal | Nivel de abstracción | Dificultad relativa | Fortaleza principal | Riesgo principal | Uso típico |
|---|---|---|---|---|---|---|---|
| Pthreads | memoria compartida | acceso compartido a memoria, mutexes, joins y variables de condición | bajo | alta | control fino | errores de concurrencia | control detallado de hilos |
| OpenMP | memoria compartida | regiones paralelas, barreras implícitas y reducciones | medio | media | rapidez para paralelizar código existente | uso ingenuo de directivas | paralelización rápida de bucles y secciones |
| MPI | memoria distribuida | envío y recepción explícita de mensajes entre procesos | medio a bajo | media a alta | escalabilidad distribuida | costo de comunicación y diseño de intercambio | clústeres y procesos distribuidos |

Esta tabla permite advertir una diferencia central: no todas las APIs atacan el mismo problema. Elegir una herramienta adecuada depende primero de la arquitectura y luego del grado de control o simplicidad que se necesite. También ayuda a pasar de la taxonomía a la decisión práctica: no se trata solo de saber qué API existe, sino de entender qué costo de implementación y qué modelo mental exige cada una.

## Multiplicación de matrices como caso de estudio

La multiplicación de matrices aparece de manera recurrente en este libro porque reúne varias razones pedagógicas y técnicas a la vez. Desde el punto de vista conceptual, permite ver con claridad cómo se descompone un problema, cómo se distribuyen filas, columnas o bloques y cómo se recomponen luego los resultados parciales. Desde el punto de vista del costo, se trata de una tarea suficientemente intensiva como para que las decisiones de paralelización, acceso a memoria y sincronización tengan efectos visibles en el rendimiento. Además, posee gran versatilidad matemática: aparece en álgebra lineal, simulación numérica, gráficos por computadora, procesamiento de señales, aprendizaje automático y numerosos problemas científicos e ingenieriles. Por ese motivo, funciona como un ejemplo útil para conectar fundamentos teóricos, diseño de algoritmos y aplicaciones reales.

Desde el punto de vista del diseño, la multiplicación de matrices puede leerse de varias maneras:

- con Pthreads, varias filas o bloques pueden asignarse manualmente a hilos distintos;
- con OpenMP, un bucle externo puede paralelizarse con directivas del compilador;
- con MPI, las matrices pueden repartirse por bloques entre nodos y luego combinar resultados parciales.

En una versión distribuida conceptual, un proceso raíz podría repartir bloques de filas de la matriz `A`, enviar la matriz `B` completa o partes relevantes a otros procesos y luego recolectar los bloques de la matriz resultado `C`. La dificultad ya no está solo en el cálculo local, sino en decidir cómo dividir y comunicar datos con un costo razonable.

Un esquema mínimo con MPI puede resumirse así:

```python
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
	blocks_of_a = split_rows(matrix_a, size)
else:
	blocks_of_a = None

local_a = comm.scatter(blocks_of_a, root=0)
full_b = comm.bcast(matrix_b, root=0)
local_c = local_a @ full_b
result_blocks = comm.gather(local_c, root=0)
```

El interés de este fragmento no está en los detalles de implementación, sino en la secuencia de diseño: repartir filas de `A`, difundir `B`, calcular un bloque local de `C` y reunir luego los resultados parciales. Esa estructura permite ver con claridad dónde aparece el costo de comunicación y dónde se concentra el cómputo local.

Este ejemplo permite ver que una misma tarea puede expresarse con APIs diferentes, pero la estrategia concreta cambia con la arquitectura y con el costo de sincronización o transferencia.

## Cierre del capítulo

Conviene leer estas APIs no solo como herramientas aisladas, sino como respuestas a problemas de arquitectura diferentes. Pthreads enfatiza control fino sobre memoria compartida. OpenMP privilegia productividad en ese mismo entorno. MPI, en cambio, obliga a pensar datos, partición y comunicación como parte explícita del algoritmo.

Vistas en conjunto, estas APIs ayudan a formular mejor una pregunta de diseño: no cuál herramienta es mejor en abstracto, sino cuál se ajusta mejor a la arquitectura disponible, al tipo de problema y al nivel de complejidad aceptable.

En el próximo capítulo el foco estará puesto en las herramientas disponibles en Python para trabajar con estos problemas en un contexto de aprendizaje accesible.

## Ejercicios del capítulo

- Explique qué tipo de arquitectura se asocia más naturalmente con Pthreads y OpenMP.
- Describa por qué MPI resulta importante en sistemas distribuidos.
- Utilice un ejemplo para explicar qué se entiende por un enfoque híbrido en programación paralela.
- Compare el tipo de control que ofrecen Pthreads y OpenMP sobre la ejecución paralela.
- Explique qué función cumplen `scatter`, `gather` y `reduce` en MPI.
- Proponga qué API sería más adecuada para un clúster de computadoras y justifique la respuesta.
- Describa qué dificultades podrían aparecer al paralelizar una multiplicación de matrices.
- Indique en qué situación OpenMP podría ser preferible a Pthreads en memoria compartida.
- Explique cómo podría combinarse MPI con OpenMP en un sistema híbrido.
