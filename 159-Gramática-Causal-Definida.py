#Aldo López Barrios
#21310106
#--------------------------
# Definición de la gramática causal
# Definición de la gramática causal
def relacion_causal(X, Y):
    return (X == 'lluvia' and Y == 'humedad_alta') or \
           (X == 'humedad_alta' and (Y == 'frio' or Y == 'neblina')) or \
           (X == 'viento_fuerte' and Y == 'lluvia') or \
           (X == 'temperatura_baja' and Y == 'frio')

# Reglas para determinar si una causa implica otra
def implica(X, Y):
    return relacion_causal(X, Y) or any(relacion_causal(X, Z) and implica(Z, Y) for Z in ['humedad_alta', 'frio', 'neblina', 'lluvia'])

# Ejemplos de uso
causas_directas = [(X, Y) for X in ['lluvia', 'humedad_alta', 'viento_fuerte', 'temperatura_baja'] 
                          for Y in ['humedad_alta', 'frio', 'neblina', 'lluvia'] if relacion_causal(X, Y)]

print("Causas directas:")
for causa in causas_directas:
    print(causa[0], "causa", causa[1])

print("\nImplicaciones causales:")
print("La lluvia implica frío:", implica('lluvia', 'frio'))
print("La temperatura baja implica lluvia:", implica('temperatura_baja', 'lluvia'))
