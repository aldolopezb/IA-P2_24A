#Aldo López Barrios
#21310106
#--------------------------
import nltk
nltk.download('comtrans')
from nltk.translate import IBMModel1
from nltk.translate import Alignment, AlignedSent

# Descargar los datos de entrenamiento
training_data = [AlignedSent(s.words, s.mots) for s in nltk.corpus.comtrans.aligned_sents()[:100]]

# Entrenar el modelo de traducción automática estadística (IBM Model 1)
ibm1 = IBMModel1(training_data, 5)

# Texto de ejemplo en inglés
english_text = "The cat is on the mat"

# Traducción automática del texto de ejemplo al francés
french_text = ibm1.translate(english_text)

print("Texto en inglés:", english_text)
print("Texto traducido al francés:", french_text)
