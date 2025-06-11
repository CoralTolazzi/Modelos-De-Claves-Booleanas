import nltk
from nltk.tokenize import word_tokenize
from whoosh.index import create_in
from whoosh.fields import Schema, TEXT
from whoosh.qparser import QueryParser

# Descargar recursos necesarios (solo la primera vez)
# nltk.download('punkt')
# nltk.download('stopwords')

documentosDeIa = {
    "doc1": "La inteligencia artificial está revolucionando la tecnología.",
    "doc2": "El aprendizaje automático es clave en la inteligencia artificial.",
    "doc3": "Procesamiento del lenguaje natural y redes neuronales.",
    "doc4": "Las redes neuronales son fundamentales en deep learning.",
    "doc5": "El futuro de la IA está en el aprendizaje profundo."
}

documentosDeHistoria = {
    "doc1": "Los egipcios construyeron las pirámides y desarrollaron una escritura jeroglífica.",
    "doc2": "La civilización romana fue una de las más influyentes en la historia occidental.",
    "doc3": "Los mayas eran expertos astrónomos y tenían un avanzado sistema de escritura.",
    "doc4": "La antigua Grecia sentó las bases de la democracia y la filosofía moderna.",
    "doc5": "Los sumerios inventaron la escritura cuneiforme y fundaron las primeras ciudades."
}

stop_words = set(nltk.corpus.stopwords.words('spanish'))

def preprocess(text):
    tokens = word_tokenize(text.lower())
    return [word for word in tokens if word.isalnum() and word not in stop_words]


def crear_indice(documents):

    schema = Schema(title=TEXT(stored=True), content=TEXT(stored=True))
    
    indice = create_in("indexdir", schema)
    
    writer = indice.writer()
    for doc_id, text in documents.items():
        words = preprocess(text)
        writer.add_document(title=doc_id, content=" ".join(words))
    
    writer.commit()
    return indice

def buscar(indice):
    with indice.searcher() as searcher:
        parser = QueryParser("content", indice.schema)

        while True:
            consulta = input("Ingrese una consulta booleana (o 'salir' para terminar): ")
            if consulta.lower() == 'salir':
                break

            query = parser.parse(consulta)
            resultados = searcher.search(query)
            encontrados = {r['title'] for r in resultados}
            if encontrados:
                print(f" Documentos encontrados: {encontrados}")
            else:
                print("No se encontró ningún documento que coincida con la consulta.")


if __name__ == "__main__":
    documentoAUtilizar = int(input("Ingrese 1 si quiere consultar utilizando los documentos sobre IA o 2 si quiere utilizar los documentos sobre Historia: "))
    if documentoAUtilizar == 1:
        documentoAUtilizar = documentosDeIa
        print("Búsqueda booleana en documentos sobre IA y aprendizaje automático")

    elif documentoAUtilizar == 2:
        documentoAUtilizar = documentosDeHistoria
        print("Búsqueda booleana en documentos sobre Historia")

    else:
        print("Opcion no Valida")
    indice = crear_indice(documentoAUtilizar)
    buscar(indice)
