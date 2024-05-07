#Aldo López Barrios
#21310106
#--------------------------
# Datos de ejemplo: clima y si se jugó al tenis
datos = [
    {'clima': 'Soleado', 'jugar_tenis': 'Sí'},
    {'clima': 'Soleado', 'jugar_tenis': 'Sí'},
    {'clima': 'Lluvioso', 'jugar_tenis': 'No'},
    {'clima': 'Nublado', 'jugar_tenis': 'Sí'},
    {'clima': 'Nublado', 'jugar_tenis': 'Sí'},
    {'clima': 'Lluvioso', 'jugar_tenis': 'Sí'},
    {'clima': 'Lluvioso', 'jugar_tenis': 'No'},
    {'clima': 'Nublado', 'jugar_tenis': 'No'},
    {'clima': 'Soleado', 'jugar_tenis': 'Sí'},
    {'clima': 'Lluvioso', 'jugar_tenis': 'Sí'}
]

# Contar el número de veces que se jugó al tenis dado un cierto clima
# y el número total de veces que ocurrió ese clima
contadores = {}
total_clima = {}

for entrada in datos:
    clima = entrada['clima']
    jugar_tenis = entrada['jugar_tenis']
    
    if clima not in contadores:
        contadores[clima] = {'Sí': 0, 'No': 0}
        total_clima[clima] = 0
        
    contadores[clima][jugar_tenis] += 1
    total_clima[clima] += 1

# Calcular la probabilidad condicionada de jugar al tenis dado un cierto clima
probabilidad_condicionada = {}
for clima, valores in contadores.items():
    probabilidad_condicionada[clima] = {}
    for jugar_tenis, cantidad in valores.items():
        probabilidad_condicionada[clima][jugar_tenis] = cantidad / total_clima[clima]

# Normalizar la probabilidad condicionada
for clima, valores in probabilidad_condicionada.items():
    total = sum(valores.values())
    for jugar_tenis in valores:
        probabilidad_condicionada[clima][jugar_tenis] /= total

# Imprimir resultados
print("Probabilidad condicionada de jugar al tenis dado un cierto clima:")
for clima, valores in probabilidad_condicionada.items():
    print(clima + ":")
    for jugar_tenis, probabilidad in valores.items():
        print("  Jugar al tenis =", jugar_tenis, "-> Probabilidad:", probabilidad)
