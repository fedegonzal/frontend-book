# Presentación

La computación paralela ocupa hoy un lugar central en el desarrollo de software, el procesamiento de datos, la simulación científica y la inteligencia artificial. Incluso tareas cotidianas, como procesar imágenes o analizar grandes volúmenes de información, dependen cada vez más de arquitecturas con múltiples núcleos, unidades vectoriales y aceleradores especializados. Por ese motivo, conviene estudiar el paralelismo no solo como un conjunto de técnicas de implementación, sino también como una forma de analizar problemas, distribuir trabajo y evaluar resultados con criterio.

Este libro fue elaborado para la asignatura Sistemas Paralelos de la Universidad Nacional de Tierra del Fuego (UNTDF). Está dirigido a estudiantes universitarios que necesitan una introducción ordenada a los fundamentos del procesamiento paralelo, sus arquitecturas, sus modelos de programación y sus herramientas de implementación.

En términos generales, el enfoque del libro parte de una idea simple: en sistemas paralelos no alcanza con que un programa funcione. También es importante comprender cómo se divide el trabajo, qué costos introduce la coordinación entre tareas y de qué manera se interpreta la mejora de rendimiento observada. Por eso, a lo largo del libro se combinan definiciones, ejemplos, implementaciones y métricas.

## Objetivos del libro

Al finalizar este recorrido se espera que el estudiante pueda:

- distinguir computación secuencial, concurrente, paralela y distribuida;
- reconocer las principales arquitecturas y modelos de memoria involucrados en el procesamiento paralelo;
- interpretar métricas como speed-up y eficiencia al analizar resultados experimentales;
- identificar modelos y APIs de programación paralela adecuados para distintos tipos de problemas;
- desarrollar implementaciones introductorias en Python para explorar paralelismo en CPU, vectorización y GPU;
- analizar críticamente las ventajas y los límites de distintas estrategias de paralelización.

## Organización del recorrido

El libro sigue una secuencia progresiva. En una primera etapa se introducen los conceptos básicos del paralelismo, las arquitecturas de hardware y las métricas que permiten evaluar rendimiento. Esa base resulta necesaria para comprender por qué ciertas estrategias escalan mejor que otras y qué restricciones impone cada tipo de sistema.

Sobre ese marco se presentan luego los principales modelos de programación paralela y algunas de las APIs clásicas del área. Más adelante se incorporan herramientas prácticas en Python, con el propósito de ofrecer una puerta de entrada accesible sin perder de vista los fundamentos del campo.

En la parte final se desarrollan temas especialmente relevantes en la computación contemporánea, como la vectorización, el broadcasting y el cómputo con GPU. El cierre del libro está dado por trabajos prácticos integradores, pensados para relacionar teoría, implementación y medición en problemas concretos.

## Cómo trabajar con este material

Conviene recorrer el libro en orden. Los capítulos posteriores retoman definiciones, métricas y herramientas introducidas al comienzo, de modo que saltear secciones suele dificultar la comprensión global del recorrido. Antes de profundizar en bibliotecas o APIs, resulta importante comprender qué problema intenta resolver el paralelismo y por qué su rendimiento no depende solamente de agregar más hilos o más procesos.

La mejor forma de aprovechar este material es combinar lectura, implementación y medición. En esta asignatura, entender un concepto suele requerir también ejecutarlo, registrar tiempos, comparar variantes y analizar por qué dos soluciones correctas pueden exhibir desempeños muy diferentes.

También conviene documentar el contexto de ejecución. En sistemas paralelos, variables como la cantidad de cores, el sistema operativo, la disponibilidad de GPU, la memoria y las bibliotecas instaladas influyen directamente sobre los resultados. Registrar esas condiciones no es un detalle accesorio, sino parte del aprendizaje técnico.

## Herramientas mínimas para empezar

Para trabajar con este libro se necesita, como base, una instalación funcional de Python y un editor de código. A lo largo del recorrido se incorporarán bibliotecas como NumPy, Numba y PyTorch, entre otras herramientas necesarias para los distintos ejercicios y experiencias de laboratorio.

Siempre que sea posible, conviene trabajar en un entorno nativo y preferentemente Linux, aunque buena parte de las prácticas también puede realizarse en otros sistemas operativos. Cuando no se disponga de una GPU local, será posible recurrir a servicios como Google Colab para ejecutar pruebas específicas vinculadas con aceleración por hardware, también algunos ejercicios podrán ser resueltos utilizando recursos disponibles en el nodo de alta performance de la UNTDF.

## Sobre el autor

Federico Gonzalez Brizzio es profesor adjunto en la carrera de Informática de la UNTDF, donde además de la asignatura Sistemas Paralelos, tiene a su cargo las cátedras de Laboratorio de Software, y Desarrollo Web I y II. Es Licenciado en Informática por la Universidad Nacional de la Patagonia San Juan Bosco, con un Máster en Smart Cities por la Universidad de Girona, un posgrado en Gobierno Abierto por la Organización de los Estados Americanos (OEA) y actualmente realiza su doctorado en Inteligencia Artificial en la Universidad de Barcelona. Es cofundador de Panalsoft, empresa orientada a la transformación digital de organizaciones públicas y privadas. Trabaja en el Institute of Science and Technology Austria (ISTA), un centro internacional de investigación científica ubicado en Klosterneuburg, a las afueras de Viena.

## Reporte de errores y sugerencias

Si encuentra errores, inconsistencias o tiene sugerencias para mejorar el contenido, puede reportarlas por alguno de estos canales:

- Correo electrónico: fgonzalez@untdf.edu.ar
- GitHub: https://github.com/fedegonzal/books
- Website: https://fedegonzalez.com
