#Aldo López Barrios
#21310106
#--------------------------
from collections import defaultdict
import nltk
from nltk.tokenize import word_tokenize
import random

class LanguageModel:
    def __init__(self, corpus):
        # Diccionarios para almacenar conteos de unigramas, bigramas y trigramas
        self.unigrams = defaultdict(int)
        self.bigrams = defaultdict(lambda: defaultdict(int))
        self.trigrams = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
        # Construir el modelo a partir del corpus proporcionado
        self.build_model(corpus)

    def build_model(self, corpus):
        # Iterar sobre cada oración en el corpus
        for sentence in corpus:
            # Tokenizar la oración y agregar marcadores de inicio y final
            tokens = ['<s>'] + word_tokenize(sentence.lower()) + ['</s>']
            # Contar unigramas, bigramas y trigramas
            for i in range(len(tokens)):
                self.unigrams[tokens[i]] += 1
                if i > 0:
                    self.bigrams[tokens[i-1]][tokens[i]] += 1
                if i > 1:
                    self.trigrams[tokens[i-2]][tokens[i-1]][tokens[i]] += 1

    def generate_sentence(self, max_length=20):
        sentence = ['<s>']  # Comenzar con un marcador de inicio
        # Generar la oración palabra por palabra hasta que se alcance la longitud máxima o se encuentre un marcador de final
        while len(sentence) < max_length and sentence[-1] != '</s>':
            # Elegir la siguiente palabra basada en el modelo de n-gramas
            if len(sentence) == 1:
                next_word = self.choose_next_word(self.unigrams)
            elif len(sentence) == 2:
                next_word = self.choose_next_word(self.bigrams[sentence[-1]])
            else:
                next_word = self.choose_next_word(self.trigrams[sentence[-2]][sentence[-1]])
            sentence.append(next_word)
        return ' '.join(sentence[1:-1])  # Concatenar las palabras de la oración generada

    def choose_next_word(self, word_counts):
        # Elegir aleatoriamente una palabra basada en las frecuencias de ocurrencia en el diccionario de conteo de palabras
        total_count = sum(word_counts.values())  # Calcular el total de ocurrencias
        rand_value = random.randint(1, total_count)  # Elegir un valor aleatorio dentro del rango total
        cumulative_sum = 0
        # Iterar sobre las palabras y determinar cuál se elige basada en el valor aleatorio generado
        for word, count in word_counts.items():
            cumulative_sum += count
            if rand_value <= cumulative_sum:
                return word

# Ejemplo de uso
corpus = [
    "El gato come pescado",
    "El perro ladra mucho",
    "El gato es gris",
    "El perro es negro",
    "El gato y el perro son amigos"
]

# Crear un modelo de lenguaje basado en el corpus
lm = LanguageModel(corpus)

# Generar y mostrar una oración aleatoria utilizando el modelo
print("Generando una oración:")
print(lm.generate_sentence())
