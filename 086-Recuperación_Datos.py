#Aldo López Barrios
#21310106
#--------------------------
import numpy as np

# Lista de documentos
documentos = [
    "El cielo es azul",
    "El sol brilla en el cielo",
    "La naturaleza es hermosa",
    "Los pájaros cantan en los árboles",
    "El sol ilumina el día",
    "El agua es clara y fresca",
    "Las flores son coloridas y hermosas",
    "Los árboles dan sombra en el parque",
]

# Lista de consultas
consultas = [
    "cielo azul",
    "sol brillante",
    "naturaleza hermosa",
    "pájaros cantando",
    "agua clara",
    "flores coloridas",
    "árboles sombra",
]

# Función para preprocesar el texto
def preprocesar(texto):
    texto = texto.lower()  # Convertir a minúsculas
    texto = texto.split()  # Dividir en palabras
    return texto

# Preprocesar documentos y consultas
documentos_preprocesados = [preprocesar(doc) for doc in documentos]
consultas_preprocesadas = [preprocesar(consulta) for consulta in consultas]

# Calcular la matriz de términos de documentos (binaria)
matriz_documentos = np.zeros((len(documentos), len(consultas)), dtype=int)
for i, doc in enumerate(documentos_preprocesados):
    for j, term in enumerate(consultas_preprocesadas):
        if set(term).issubset(set(doc)):
            matriz_documentos[i, j] = 1

# Mostrar la matriz de términos de documentos
print("Matriz de términos de documentos (binaria):")
print(matriz_documentos)
