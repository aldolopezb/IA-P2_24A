#Aldo López Barrios
#21310106
#--------------------------

import numpy as np

# Definir las funciones de transición y recompensa
def transicion_estado_accion(estado, accion):
    # Define las transiciones de estado según la acción
    pass

def recompensa(estado):
    # Define las recompensas por estado
    pass

# Iteración de políticas
def iteracion_politicas(num_iteraciones):
    politica = np.random.choice(['Arriba', 'Abajo', 'Izquierda', 'Derecha'], size=9)  # Política inicial
    for _ in range(num_iteraciones):
        nuevos_valores = np.zeros(9)
        for estado in range(9):
            accion = politica[estado]
            nuevo_estado = transicion_estado_accion(estado, accion)
            if nuevo_estado is not None:  # Verifica si el nuevo estado es válido
                recompensa_accion = recompensa(nuevo_estado)
                if recompensa_accion is not None:  # Verifica si la recompensa es válida
                    nuevos_valores[estado] = recompensa_accion
        # Actualiza la política basada en los nuevos valores
        politica = np.random.choice(['Arriba', 'Abajo', 'Izquierda', 'Derecha'], size=9)
    return politica

# Ejecutar la iteración de políticas
politica_final = iteracion_politicas(num_iteraciones=100)
print("Política final:", politica_final)
