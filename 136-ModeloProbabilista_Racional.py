#Aldo López Barrios
#21310106
#--------------------------
import numpy as np

# Definir las probabilidades iniciales
probabilidad_lluvia = 0.3  # P(lluvia)
probabilidad_paraguas = 0.9  # P(paraguas | lluvia)
probabilidad_no_paraguas = 0.2  # P(no_paraguas | lluvia)

# Calcular la probabilidad condicional de llevar un paraguas dado que llueve
probabilidad_lluvia_paraguas = (probabilidad_paraguas * probabilidad_lluvia) / probabilidad_lluvia
print("P(paraguas | lluvia) =", probabilidad_lluvia_paraguas)

# Calcular la probabilidad condicional de no llevar un paraguas dado que llueve
probabilidad_lluvia_no_paraguas = (probabilidad_no_paraguas * probabilidad_lluvia) / probabilidad_lluvia
print("P(no_paraguas | lluvia) =", probabilidad_lluvia_no_paraguas)
