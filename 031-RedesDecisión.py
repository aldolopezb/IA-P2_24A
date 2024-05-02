#Aldo López Barrios
#21310106
#--------------------------

class NodoDecision:
    def __init__(self, pregunta, si_nodo, no_nodo):
        self.pregunta = pregunta
        self.si_nodo = si_nodo
        self.no_nodo = no_nodo

def tomar_decision(nodo_actual):
    respuesta = input(nodo_actual.pregunta + " (s/n): ")
    if respuesta.lower() == 's':
        if isinstance(nodo_actual.si_nodo, NodoDecision):
            return tomar_decision(nodo_actual.si_nodo)
        else:
            return nodo_actual.si_nodo
    else:
        if isinstance(nodo_actual.no_nodo, NodoDecision):
            return tomar_decision(nodo_actual.no_nodo)
        else:
            return nodo_actual.no_nodo

# Construir el árbol de decisión
nodo4 = NodoDecision("¿Está el paciente mareado?", "Gripe", "Resfriado")
nodo3 = NodoDecision("¿Tiene el paciente fiebre?", nodo4, "Gripe")
nodo2 = NodoDecision("¿Tiene el paciente tos?", nodo3, "Resfriado")
nodo1 = NodoDecision("¿Tiene el paciente dolor de garganta?", nodo2, "Resfriado")

# Tomar una decisión basada en el árbol de decisión
resultado = tomar_decision(nodo1)
print("Diagnóstico:", resultado)
