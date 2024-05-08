#Aldo López Barrios
#21310106
#--------------------------
import nltk
from nltk.corpus import treebank

# Obtener las producciones del corpus treebank
productions = []
for tree in treebank.parsed_sents():
    productions.extend(tree.productions())

# Contar la frecuencia de cada producción
production_counts = nltk.FreqDist(productions)

# Construir una PCFG asignando probabilidades a las producciones
productions_with_prob = {}
for production in production_counts:
    prob = production_counts[production] / len(productions)
    if production.lhs() not in productions_with_prob:
        productions_with_prob[production.lhs()] = []
    productions_with_prob[production.lhs()].append((production.rhs(), prob))

# Definir el símbolo inicial como el primer símbolo izquierdo de las producciones
start = productions[0].lhs()

# Crear la gramática PCFG
grammar = nltk.PCFG(start, productions_with_prob)

# Crear un parser Viterbi con la gramática PCFG
parser = nltk.ViterbiParser(grammar)

# Ejemplo de análisis sintáctico
sentence = "the dog saw a cat"
tokens = nltk.word_tokenize(sentence)
parsed_trees = parser.parse(tokens)

# Mostrar los árboles de análisis sintáctico
for tree in parsed_trees:
    print(tree)
