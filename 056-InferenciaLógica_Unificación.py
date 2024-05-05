def unify(var, x, theta):
    """
    Función para unificar dos términos.

    Args:
    - var: variable
    - x: término
    - theta: sustitución

    Returns:
    - Sustitución actualizada
    """

    if theta is None:
        return None
    elif var == x:
        return theta
    elif isinstance(var, str) and var[0].islower():
        return unify_var(var, x, theta)
    elif isinstance(x, str) and x[0].islower():
        return unify_var(x, var, theta)
    elif isinstance(var, list) and isinstance(x, list):
        if len(var) != len(x):
            return None
        for v, t in zip(var, x):
            theta = unify(v, t, theta)
        return theta
    elif isinstance(var, list):
        return unify_list(var, x, theta)
    elif isinstance(x, list):
        return unify_list(x, var, theta)
    else:
        return None

def unify_var(var, x, theta):
    """
    Función para unificar una variable con un término.

    Args:
    - var: variable
    - x: término
    - theta: sustitución

    Returns:
    - Sustitución actualizada
    """

    if var in theta:
        return unify(theta[var], x, theta)
    elif x in theta:
        return unify(var, theta[x], theta)
    else:
        theta[var] = x
        return theta

def unify_list(var_list, x, theta):
    """
    Función para unificar una lista con un término.

    Args:
    - var_list: lista
    - x: término
    - theta: sustitución

    Returns:
    - Sustitución actualizada
    """

    if tuple(var_list) in theta:
        return unify(theta[tuple(var_list)], x, theta)
    elif x in theta:
        return unify(var_list, theta[x], theta)
    else:
        theta[tuple(var_list)] = x
        return theta

# Ejemplo de uso
theta = unify('x', 'a', {})
print(theta)  # Output: {'x': 'a'}

theta = unify(['x', 'a'], 'b', theta)
print(theta)  # Output: {'x': 'b'}

theta = unify(['x', 'y'], ['a', 'b'], {})
print(theta)  # Output: {'x': 'a', 'y': 'b'}
