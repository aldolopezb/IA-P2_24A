#Aldo López Barrios
#21310106
#--------------------------
# Función para calcular la probabilidad conjunta utilizando la regla de la cadena
def probabilidad_conjunta(variables, evidencias, prob_table):
    """
    variables: lista de variables en orden
    evidencias: diccionario de evidencias {variable: valor}
    prob_table: tabla de probabilidades condicionales P(variable | padres)
    """
    joint_prob = 1
    for variable in variables:
        parents = prob_table[variable]['parents']
        if not parents:  # Si no tiene padres
            joint_prob *= prob_table[variable]['prob'][()]
        else:
            parent_values = tuple(evidencias[parent] for parent in parents)
            joint_prob *= prob_table[variable]['prob'][parent_values]
    return joint_prob

# Definir la tabla de probabilidades condicionales
prob_table = {
    'A': {'parents': [], 'prob': {(): 0.3}},
    'B': {'parents': [], 'prob': {(): 0.6}},
    'C': {'parents': ['A', 'B'], 'prob': {(0, 0): 0.1, (0, 1): 0.5, (1, 0): 0.8, (1, 1): 0.9}}
}

# Calcular la probabilidad conjunta P(C=1, A=0, B=1)
variables = ['C', 'A', 'B']
evidencias = {'A': 0, 'B': 1}
joint_prob = probabilidad_conjunta(variables, evidencias, prob_table)
print("Probabilidad conjunta P(C=1, A=0, B=1):", joint_prob)
