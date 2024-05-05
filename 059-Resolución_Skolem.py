from sympy import symbols, Not, Or, And, Exists, ask
from sympy.abc import x, y, z

# Definir las variables
P = symbols('P', cls=Function)
Q = symbols('Q', cls=Function)
a, b, c = symbols('a b c')

# Definir las cláusulas
clausula1 = Or(P(x), Not(Q(x)))
clausula2 = Exists(x, P(x))
clausula3 = Not(P(a))

# Resolver
resultado = ask(And(clausula1, clausula2, clausula3))
print(resultado)
