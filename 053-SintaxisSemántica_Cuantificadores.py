from sympy import symbols, And, Or, Not

# Definición de variables
x, y = symbols('x y')

# Definición de una función que representa una expresión lógica
def P(x):
    return x > 0  # Ejemplo de función que devuelve True si x es mayor que 0

# Cuantificador Universal: Para todo x, P(x)
cuantificador_universal = And(*[P(x) for x in range(-10, 11)])
print("Cuantificador Universal:", cuantificador_universal)

# Cuantificador Existencial: Existe algún x tal que P(x)
cuantificador_existencial = Or(*[P(x) for x in range(-10, 11)])
print("Cuantificador Existencial:", cuantificador_existencial)
