#Aldo López Barrios
#21310106
#--------------------------

import numpy as np

# Definir la función de transición y la función de recompensa
def transicion_estado_accion(estado, accion):
    # Define las transiciones de estado según la acción
    pass

def recompensa(estado):
    # Define las recompensas por estado
    pass

# Iteración de valores
def iteracion_valores(num_iteraciones):
    valores = np.zeros(9)  # Valores iniciales
    for _ in range(num_iteraciones):
        nuevos_valores = np.zeros(9)
        for estado in range(9):
            valores_acciones = []
            for accion in ['Ir arriba', 'Ir abajo', 'Ir izquierda', 'Ir derecha']:
                nuevo_estado = transicion_estado_accion(estado, accion)
                if nuevo_estado is not None:  # Verifica si el nuevo estado es válido
                    valor_accion = recompensa(nuevo_estado)
                    if valor_accion is not None:  # Verifica si la recompensa es válida
                        valor_accion += valores[nuevo_estado]
                        valores_acciones.append(valor_accion)
            if valores_acciones:  # Verifica si hay valores en la lista
                nuevos_valores[estado] = np.max(np.array(valores_acciones))
        valores = nuevos_valores
    return valores

# Ejecutar la iteración de valores
valores_finales = iteracion_valores(num_iteraciones=100)
print("Valores finales:", valores_finales)
