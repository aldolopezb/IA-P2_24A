#Aldo López Barrios
#21310106
#--------------------------
import nltk
import random

# Frases de ejemplo para la inducción gramatical
frases = [
    "los perros ladran",
    "los gatos maullan",
    "los pájaros cantan",
    "los perros persiguen a los gatos"
]

# Tokenización de las frases en palabras
tokens = [nltk.word_tokenize(frase) for frase in frases]

# Extracción de bigramas de las frases tokenizadas
bigramas = [list(nltk.bigrams(token)) for token in tokens]

# Creación del modelo de bigramas
modelo_bigramas = nltk.ConditionalFreqDist((palabra1, palabra2) for frase in bigramas for palabra1, palabra2 in frase)

# Generación de texto utilizando el modelo de bigramas
texto_generado = ["los"]

for _ in range(10):
    if modelo_bigramas[texto_generado[-1]]:
        palabra_siguiente = modelo_bigramas[texto_generado[-1]].max()
    else:
        palabras_disponibles = list(modelo_bigramas.keys())
        palabra_siguiente = random.choice(palabras_disponibles)
    texto_generado.append(palabra_siguiente)

print(" ".join(texto_generado))
