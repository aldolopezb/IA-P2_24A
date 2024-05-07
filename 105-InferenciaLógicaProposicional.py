#Aldo López Barrios
#21310106
#--------------------------
import itertools

def evaluate(expression, assignment):
    """
    Evalúa una expresión lógica dada una asignación de variables.
    :param expression: Expresión lógica en forma de string.
    :param assignment: Asignación de variables representada como un diccionario.
    :return: Resultado de evaluar la expresión.
    """
    local_assignment = assignment.copy()
    for var, value in assignment.items():
        exec(f"{var} = {value}", {}, local_assignment)
    return eval(expression, {}, local_assignment)

def generate_truth_table(variables):
    """
    Genera todas las posibles asignaciones de valores para las variables dadas.
    :param variables: Lista de variables.
    :return: Lista de todas las posibles asignaciones de valores como diccionarios.
    """
    truth_values = [0, 1]
    assignments = list(itertools.product(truth_values, repeat=len(variables)))
    return [dict(zip(variables, assignment)) for assignment in assignments]

def truth_table(expression):
    """
    Genera una tabla de verdad para la expresión lógica dada.
    :para m expression: Expresión lógica en forma de string.
    :retur n: Lista de diccionarios representando la tabla de verdad.
    """
    variables = sorted(set([char for char in expression if char.isalpha()]))
    table = []

    for assignment in generate_truth_table(variables):
        row = assignment.copy()
        row['result'] = evaluate(expression, assignment)
        table.append(row)

    return table

def print_truth_table(table):
    """
    Imprime la tabla de verdad.
    :para m table: Lista de diccionarios representando la tabla de verdad.
    """
    headers = list(table[0].keys())
    print(" | ".join(headers))
    print("-" * (len(headers) * 4 - 1))
    for row in table:
        print(" | ".join(str(row[key]) for key in headers))

# Ejemplo de uso
if __name__ == "__main__":
    expression = "(A and B) or (C and not D)"
    table = truth_table(expression)
    print_truth_table(table)
