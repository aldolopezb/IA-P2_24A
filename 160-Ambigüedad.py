#Aldo López Barrios
#21310106
#--------------------------
import nltk
from nltk import CFG

# Definición de la gramática ambigua
gramatica_ambigua = CFG.fromstring("""
    S -> NP VP | VP NP
    NP -> Det N | Det N PP
    VP -> V | V NP | V NP PP
    Det -> 'el' | 'la' | 'los' | 'las'
    N -> 'perro' | 'gato' | 'gata' | 'casa' | 'puerta'
    V -> 'persigue' | 'abre' | 'cierra'
    PP -> P NP
    P -> 'en' | 'por'
""")

# Frase ambigua
frase = "el perro persigue la gata en la casa por la puerta"

# Crear un parser para la gramática
parser = nltk.ChartParser(gramatica_ambigua)

# Mostrar todos los árboles de análisis posibles para la frase
for arbol in parser.parse(frase.split()):
    print(arbol)
