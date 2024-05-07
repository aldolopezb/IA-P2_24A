#Aldo López Barrios
#21310106
#--------------------------
class Marco:
    def __init__(self, nombre, atributos=None):
        self.nombre = nombre
        self.atributos = atributos if atributos else {}

    def agregar_atributo(self, nombre, valor):
        self.atributos[nombre] = valor

    def obtener_atributo(self, nombre):
        return self.atributos.get(nombre)


# Definir algunos marcos
accion_comer = Marco("AccionComer")
accion_dormir = Marco("AccionDormir")
situacion_cena = Marco("SituacionCena")
evento_despertar = Marco("EventoDespertar")

# Agregar atributos a los marcos
accion_comer.agregar_atributo("sujeto", "yo")
accion_comer.agregar_atributo("objeto", "una pizza")
accion_dormir.agregar_atributo("lugar", "en la cama")
situacion_cena.agregar_atributo("lugar", "en el restaurante")
evento_despertar.agregar_atributo("hora", "7:00 a.m.")

# Mostrar los marcos y sus atributos
def mostrar_marco(marco):
    print(f"Marco: {marco.nombre}")
    for atributo, valor in marco.atributos.items():
        print(f"  {atributo}: {valor}")

mostrar_marco(accion_comer)
mostrar_marco(accion_dormir)
mostrar_marco(situacion_cena)
mostrar_marco(evento_despertar)
