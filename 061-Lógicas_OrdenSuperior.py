from sympy import symbols, Function, forall, exists

# Definimos los símbolos
x, y = symbols('x y')

# Definimos una función
F = Function('F')

# Definimos las fórmulas lógicas
formula1 = forall(x, F(x) | ~F(x))
formula2 = exists(x, F(x) & ~F(x))
formula3 = forall(x, exists(y, F(x) | F(y)))

# Imprimimos las fórmulas y evaluamos
print("Fórmula 1:", formula1)
print("Evaluación Fórmula 1:", formula1.simplify())

print("Fórmula 2:", formula2)
print("Evaluación Fórmula 2:", formula2.simplify())

print("Fórmula 3:", formula3)
print("Evaluación Fórmula 3:", formula3.simplify())
