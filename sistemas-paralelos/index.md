# Presentación

Este libro fue elaborado para la asignatura Sistemas Paralelos de la Universidad Nacional de Tierra del Fuego (UNTDF), Argentina, y está dirigido a estudiantes universitarios que necesitan una introducción ordenada a los fundamentos del procesamiento paralelo, sus arquitecturas, sus modelos de programación y sus herramientas de implementación.

La computación paralela tiene hoy un lugar relevante en el desarrollo de software, el procesamiento de datos, la simulación científica y la inteligencia artificial. Incluso tareas cotidianas, como procesar imágenes o analizar grandes volúmenes de información, dependen cada vez más de arquitecturas con múltiples núcleos, unidades vectoriales y aceleradores especializados. Por ese motivo, comprender sus principios ya no constituye un interés restringido a ámbitos muy específicos, sino una parte importante de la formación en informática.

Estudiar paralelismo implica aprender a reconocer cómo se divide un problema, qué costos introduce la coordinación entre tareas, qué límites impone la arquitectura disponible y de qué manera se interpreta el rendimiento obtenido. Dicho de otro modo, no alcanza con observar que una implementación funciona: conviene entender bajo qué condiciones mejora su desempeño y cómo se evalúan sus resultados.

Con ese marco, el recorrido propuesto combina definiciones, ejemplos, implementaciones y métricas. A lo largo de los capítulos se desarrollan los conceptos necesarios para pasar de una comprensión general del campo a una aproximación más concreta a sus principales estrategias y herramientas de trabajo.

## Objetivos del libro

Al finalizar este recorrido se espera que el estudiante pueda:

- distinguir computación secuencial, concurrente, paralela y distribuida;
- reconocer las principales arquitecturas, modelos de memoria y criterios básicos de organización del cómputo paralelo;
- interpretar métricas como speed-up y eficiencia al analizar resultados experimentales;
- identificar modelos y APIs de programación paralela adecuados para distintos tipos de problemas;
- desarrollar implementaciones introductorias en Python para explorar paralelismo explícito en CPU, reformulación sobre arreglos y ejecución sobre GPU;
- analizar críticamente las ventajas y los límites de distintas estrategias de paralelización.

## Organización del recorrido

El libro sigue una secuencia progresiva que va de los fundamentos conceptuales a las estrategias de implementación. En los primeros capítulos se introducen las distinciones básicas entre computación secuencial, concurrencia, paralelismo y distribución, y luego se presentan las arquitecturas, los modelos de memoria y las métricas que permiten analizar rendimiento. Esa base resulta necesaria para comprender por qué ciertas decisiones de diseño escalan mejor que otras y qué límites impone cada plataforma.

Sobre ese marco se desarrollan después los modelos clásicos de programación paralela y algunas APIs históricas del área, como Pthreads, OpenMP y MPI. Estas referencias no aparecen solo como repertorio técnico, sino como formas de organizar problemas, comunicación y sincronización según el tipo de arquitectura disponible.

La segunda mitad se concentra en Python como lenguaje de trabajo para explorar distintos niveles de abstracción. Primero se estudia el paralelismo explícito en CPU mediante hilos, procesos y compilación JIT. Luego se introduce una estrategia complementaria: reformular el cálculo sobre arreglos y tensores completos mediante vectorización, broadcasting y trabajo con bibliotecas como NumPy y PyTorch en CPU. A continuación se analiza el paso hacia GPU, primero desde un modelo más cercano al hardware y luego desde herramientas de más alto nivel.

El cierre del libro recupera esa progresión para sintetizar criterios de elección, límites de escalabilidad y relaciones entre estructura del problema, forma de implementación y arquitectura de ejecución.

## Cómo trabajar con este libro

Conviene recorrer el libro en orden. Los capítulos posteriores retoman definiciones, métricas, ejemplos y criterios introducidos al comienzo, de modo que saltear secciones suele dificultar la comprensión global del recorrido. Antes de profundizar en bibliotecas o APIs, resulta importante comprender qué problema intenta resolver el paralelismo y por qué su rendimiento no depende solamente de agregar más hilos, más procesos o más hardware.

La lectura se aprovecha mejor cuando se combina con implementación y medición. Muchos de los conceptos desarrollados en el libro se vuelven más claros al comparar una versión secuencial con una versión paralela, al registrar tiempos de ejecución y al analizar por qué dos soluciones correctas pueden exhibir desempeños muy diferentes.

También conviene prestar atención al tipo de problema que se trabaja en cada capítulo. En algunos casos, el interés estará puesto en repartir tareas de manera explícita; en otros, en reorganizar el cálculo para aprovechar mejor la memoria y las bibliotecas optimizadas; y en otros, en reconocer cuándo una GPU ofrece una ventaja real. Mantener esa perspectiva ayuda a evitar una lectura reducida a herramientas aisladas.

Por último, resulta importante documentar el contexto de ejecución. En sistemas paralelos, variables como la cantidad de cores, el sistema operativo, la disponibilidad de GPU, la memoria y las bibliotecas instaladas influyen directamente sobre los resultados. Registrar esas condiciones forma parte del análisis técnico y permite interpretar con mayor cuidado las comparaciones que aparecen a lo largo del libro.

## Herramientas mínimas para empezar

Para trabajar con este libro alcanza, como base, con una instalación funcional de Python y un editor de código. A lo largo del recorrido se incorporarán bibliotecas como NumPy, Numba y PyTorch, según el tipo de problemas y ejemplos que se desarrollan en los capítulos.

Siempre que sea posible, conviene trabajar en un entorno nativo y, de preferencia, en Linux, aunque buena parte de las prácticas también puede realizarse en otros sistemas operativos. Cuando no se disponga de una GPU local, algunas pruebas vinculadas con aceleración por hardware podrán ejecutarse en servicios como Google Colab o en otros entornos equivalentes.

En el contexto de la asignatura, también podrán utilizarse recursos institucionales disponibles para ciertas actividades específicas, como el nodo de alta performance de la UNTDF.

## Sobre el autor

Federico Gonzalez Brizzio es profesor adjunto en la carrera de Informática de la UNTDF, donde además de la asignatura Sistemas Paralelos, tiene a su cargo las cátedras de Laboratorio de Software, y Desarrollo Web I y II. Es Licenciado en Informática por la Universidad Nacional de la Patagonia San Juan Bosco, con un Máster en Smart Cities por la Universidad de Girona, un posgrado en Gobierno Abierto por la Organización de los Estados Americanos (OEA) y actualmente realiza su doctorado en Inteligencia Artificial en la Universidad de Barcelona. Es cofundador de Panalsoft, una empresa con sede en Ushuaia, Argentina, orientada a la transformación digital de organizaciones públicas y privadas. Trabaja en el Institute of Science and Technology Austria (ISTA), un centro internacional de investigación científica ubicado en Klosterneuburg, a las afueras de Viena.

## Ilustraciones y revisión

Las ilustraciones incluidas en el libro fueron diseñadas íntegramente con ChatGPT 5.4. En su elaboración no hubo intervención humana sobre la construcción visual propiamente dicha más allá del prompt inicial que orientó cada imagen y de la posterior decisión editorial de incorporarla al capítulo correspondiente. Las figuras deben leerse como parte de una metodología de producción asistida, integrada deliberadamente al proceso de escritura.

La revisión del libro también se realizó mediante una modalidad de trabajo de a pares. Ese equipo de revisión estuvo formado por el autor, Federico Gonzalez Brizzio, y por GitHub Copilot, utilizando para esa tarea modelos Claude Sonnet 4.6 y GPT 5.4. Esta revisión se aplicó a la relectura técnica y editorial de los capítulos, con el propósito de detectar inconsistencias, ajustar formulaciones, mejorar la claridad expositiva y controlar la coherencia del recorrido pedagógico. La responsabilidad autoral final sobre el contenido, su selección y su organización permanece, en todos los casos, en la figura del autor.

## Reporte de errores y sugerencias

Si encuentra errores, inconsistencias o tiene sugerencias para mejorar el contenido, puede reportarlas por alguno de estos canales:

- Correo electrónico: fgonzalez@untdf.edu.ar
- GitHub: https://github.com/fedegonzal/books
- Website: https://fedegonzalez.com
