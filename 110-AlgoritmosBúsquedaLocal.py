#Aldo López Barrios
#21310106
#--------------------------
import random

class Objeto:
    def __init__(self, valor, peso):
        self.valor = valor
        self.peso = peso

def valor_total(solucion, objetos):
    return sum(obj.valor for obj in objetos if solucion[objetos.index(obj)])

def peso_total(solucion, objetos):
    return sum(obj.peso for obj in objetos if solucion[objetos.index(obj)])

def generar_solucion_inicial(objetos):
    return [random.choice([0, 1]) for _ in range(len(objetos))]

def vecindario(solucion):
    vecinos = []
    for i in range(len(solucion)):
        vecino = solucion[:]
        vecino[i] = 1 - vecino[i]  # Cambiar el elemento i-esimo de la solución
        vecinos.append(vecino)
    return vecinos

def mejor_vecino(vecinos, capacidad, objetos):
    mejor_valor = 0
    mejor_vecino = None
    for vecino in vecinos:
        if peso_total(vecino, objetos) <= capacidad:
            valor = valor_total(vecino, objetos)
            if valor > mejor_valor:
                mejor_valor = valor
                mejor_vecino = vecino
    return mejor_vecino

def busqueda_local(objetos, capacidad, iteraciones):
    solucion_actual = generar_solucion_inicial(objetos)
    valor_actual = valor_total(solucion_actual, objetos)

    for _ in range(iteraciones):
        vecinos = vecindario(solucion_actual)
        mejor_vecino_actual = mejor_vecino(vecinos, capacidad, objetos)
        
        if mejor_vecino_actual:
            valor_mejor_vecino_actual = valor_total(mejor_vecino_actual, objetos)
            if valor_mejor_vecino_actual > valor_actual:
                solucion_actual = mejor_vecino_actual
                valor_actual = valor_mejor_vecino_actual

    return solucion_actual

# Ejemplo de uso
objetos = [Objeto(valor=60, peso=10), Objeto(valor=100, peso=20), Objeto(valor=120, peso=30)]
capacidad_mochila = 50
iteraciones = 100

mejor_solucion = busqueda_local(objetos, capacidad_mochila, iteraciones)
print("Mejor solución encontrada:", mejor_solucion)
print("Valor total:", valor_total(mejor_solucion, objetos))
print("Peso total:", peso_total(mejor_solucion, objetos))
