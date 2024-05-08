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

def is_equivalent(expression1, expression2):
    """
    Verifica si dos expresiones lógicas son equivalentes.
    :param expression1: Primera expresión lógica en forma de string.
    :param expression2: Segunda expresión lógica en forma de string.
    :return: True si las expresiones son equivalentes, False de lo contrario.
    """
    variables = sorted(set([char for char in expression1 + expression2 if char.isalpha()]))
    for assignment in generate_truth_table(variables):
        if evaluate(expression1, assignment) != evaluate(expression2, assignment):
            return False
    return True

def is_valid(expression):
    """
    Verifica si una expresión lógica es válida (siempre verdadera).
    :param expression: Expresión lógica en forma de string.
    :return: True si la expresión es válida, False de lo contrario.
    """
    variables = sorted(set([char for char in expression if char.isalpha()]))
    for assignment in generate_truth_table(variables):
        if not evaluate(expression, assignment):
            return False
    return True

def is_satisfiable(expression):
    """
    Verifica si una expresión lógica es satisfactible (al menos una vez verdadera).
    :param expression: Expresión lógica en forma de string.
    :return: True si la expresión es satisfactible, False de lo contrario.
    """
    variables = sorted(set([char for char in expression if char.isalpha()]))
    for assignment in generate_truth_table(variables):
        if evaluate(expression, assignment):
            return True
    return False

# Ejemplo de uso
if __name__ == "__main__":
    expression1 = "(A and B) or (not C)"
    expression2 = "not (A or B) or (not C)"
    print("¿Las expresiones son equivalentes?", is_equivalent(expression1, expression2))
    print("¿La expresión 1 es válida?", is_valid(expression1))
    print("¿La expresión 2 es válida?", is_valid(expression2))
    print("¿La expresión 1 es satisfactible?", is_satisfiable(expression1))
    print("¿La expresión 2 es satisfactible?", is_satisfiable(expression2))
