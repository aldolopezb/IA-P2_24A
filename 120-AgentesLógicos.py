#Aldo López Barrios
#21310106
#--------------------------
class AgenteLogico:
    def __init__(self, base_conocimiento):
        self.base_conocimiento = base_conocimiento

    def preguntar(self, pregunta):
        propiedad, objeto = pregunta
        return objeto in self.base_conocimiento.get(propiedad, [])

# Ejemplo de uso
base_conocimiento = {"puede_volar": ["pájaro", "avión"],
                     "es_comestible": ["manzana", "pera", "pájaro"]}

agente = AgenteLogico(base_conocimiento)

print(agente.preguntar(("puede_volar", "pájaro")))  # True
print(agente.preguntar(("es_comestible", "avión")))  # False
