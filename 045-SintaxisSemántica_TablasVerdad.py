#Aldo López Barrios
#21310106
#--------------------------
import itertools

def truth_table(expression):
    variables = sorted(set(c for c in expression if c.isalpha()))
    table = []
    
    for assignment in itertools.product([False, True], repeat=len(variables)):
        row = dict(zip(variables, assignment))
        row['result'] = eval(expression, {}, row)
        table.append(row)
    
    return table

# Ejemplo de uso
expression = "(A and B) or (not A and C)"
table = truth_table(expression)

# Imprimir la tabla de verdad
print("Tabla de Verdad para la expresión:", expression)
print("-" * (len(expression) + 22))
for row in table:
    assignments = ", ".join(f"{var}={int(val)}" for var, val in row.items() if var != 'result')
    print(f"{assignments} => Resultado: {int(row['result'])}")
