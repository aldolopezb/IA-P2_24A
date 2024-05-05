from sympy import symbols, Or, And, Not, parse_expr

def to_cnf_resolution(expression):
    # Convertir la expresión de cadena a una expresión lógica de SymPy
    expr = parse_expr(expression)

    # Aplicar la distributividad
    def distribute_or_over_and(expr):
        if expr.is_Or:
            args = [distribute_or_over_and(arg) for arg in expr.args]
            result = []
            for arg in args:
                if arg.is_And:
                    result.extend(arg.args)
                else:
                    result.append(arg)
            return And(*[Or(*arg) for arg in zip(*result)])
        elif expr.is_And:
            return And(*[distribute_or_over_and(arg) for arg in expr.args])
        else:
            return expr

    # Convertir la expresión a CNF
    expression_cnf = distribute_or_over_and(expr)

    return expression_cnf

# Expresión original
expression = "(P | Q) & (~P | R)"

# Convertir a CNF usando la resolución
cnf_expression = to_cnf_resolution(expression)

print("Expresión original:", expression)
print("Expresión en CNF:", cnf_expression)
