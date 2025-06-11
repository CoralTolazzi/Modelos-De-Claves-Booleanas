Trabajo Práctico N.º 7 - Modelo de Claves Booleanas
Nombre: Coral Tolazzi
Materia: Procesamiento del Lenguaje Natural
Tema: Recuperación de la Información
Profesora: Yanina Ximena Scudero
Cuatrimestre: 1.º Cuatrimestre del 2025
Instituto: Instituto Tecnológico Beltrán

Descripción
Este trabajo práctico consiste en la implementación de un sistema de búsqueda booleana utilizando Python, NLTK y Whoosh. Se simulan consultas del tipo AND, OR, NOT sobre documentos de texto relacionados con civilizaciones antiguas y temas de inteligencia artificial. El objetivo es comprender el funcionamiento de los modelos de recuperación de información basados en operadores booleanos.

Funcionalidades
Preprocesamiento de texto:

Tokenización y limpieza con NLTK.

Eliminación de palabras vacías (stopwords) en español.

Indexación de documentos con Whoosh.

Búsquedas booleanas del tipo:

AND: intersección de términos.

OR: unión de términos.

NOT: diferencia de conjuntos.

Selección interactiva de corpus:

Civilizaciones antiguas.

Inteligencia artificial y aprendizaje automático.

Resultados en tiempo real de documentos que coinciden con la consulta.

Corpus de Ejemplo
 Civilizaciones Antiguas
text
Copiar
Editar
doc1: Los egipcios construyeron las pirámides y desarrollaron una escritura jeroglífica.  
doc2: La civilización romana fue una de las más influyentes en la historia occidental.  
doc3: Los mayas eran expertos astrónomos y tenían un avanzado sistema de escritura.  
doc4: La antigua Grecia sentó las bases de la democracia y la filosofía moderna.  
doc5: Los sumerios inventaron la escritura cuneiforme y fundaron las primeras ciudades.
Ejemplos de consulta:
egipcios AND pirámides → 📄 {'doc1'}

escritura OR astrónomos → 📄 {'doc1', 'doc3', 'doc5'}

romana NOT griegos → 📄 {'doc2'}

Inteligencia Artificial
text
Copiar
Editar
doc1: La inteligencia artificial está revolucionando la tecnología.  
doc2: El aprendizaje automático es clave en la inteligencia artificial.  
doc3: Procesamiento del lenguaje natural y redes neuronales.  
doc4: Las redes neuronales son fundamentales en deep learning.  
doc5: El futuro de la IA está en el aprendizaje profundo.
Ejemplos de consulta:
inteligencia AND artificial → 📄 {'doc1', 'doc2'}

redes OR aprendizaje → 📄 {'doc2', 'doc3', 'doc4', 'doc5'}

inteligencia NOT automático → 📄 {'doc1'}

Estructura del Código
Importaciones:

nltk, whoosh para procesamiento y búsqueda.

Carga de documentos:

Diccionarios documentosDeHistoria y documentosDeIa.

Preprocesamiento:

Tokenización, conversión a minúsculas, eliminación de stopwords.

Creación del índice:

Con Whoosh y esquema title y content.

Búsqueda interactiva:

Consola para ingresar consultas booleanas y devolver resultados.

Ejecución principal:

Selección de tema y ejecución de búsqueda.

Conclusión
Este trabajo práctico permite aplicar conceptos de recuperación de información mediante consultas booleanas simples y eficientes. Se explora el preprocesamiento con NLTK y la búsqueda con Whoosh, abordando dos temáticas de interés: historia e inteligencia artificial. Se logra una comprensión práctica de cómo se construyen motores de búsqueda básicos y cómo se representa la información para ser consultada eficientemente.
