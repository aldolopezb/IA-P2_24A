#Aldo López Barrios
#21310106
#--------------------------
import nltk

# Oración de ejemplo
sentence = "I am learning Natural Language Processing."

# Tokenización de la oración en palabras
tokens = nltk.word_tokenize(sentence)

# Etiquetado de las palabras
tagged = nltk.pos_tag(tokens)

# Impresión de las palabras etiquetadas
print(tagged)
