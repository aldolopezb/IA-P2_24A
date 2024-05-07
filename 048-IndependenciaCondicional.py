#Aldo López Barrios
#21310106
#--------------------------
# Función para calcular la probabilidad condicional P(A|B)
def prob_condicional(evento_A, evento_B, datos):
    count_A_and_B = sum(1 for d in datos if d[0] == evento_A and d[1] == evento_B)
    count_B = sum(1 for d in datos if d[1] == evento_B)
    if count_B == 0:
        return 0
    return count_A_and_B / count_B

# Función para verificar la independencia condicional
def independencia_condicional(evento_A, evento_B, datos):
    p_A = sum(1 for d in datos if d[0] == evento_A) / len(datos)
    p_B = sum(1 for d in datos if d[1] == evento_B) / len(datos)
    p_A_given_B = prob_condicional(evento_A, evento_B, datos)
    return abs(p_A_given_B - p_A) < 1e-6 and abs(p_A_given_B - p_A * p_B) < 1e-6

# Datos de ejemplo
datos = [('Soleado', 'Calor'), ('Nublado', 'Templado'), ('Lluvioso', 'Frío'),
         ('Soleado', 'Templado'), ('Nublado', 'Frío'), ('Lluvioso', 'Frío'),
         ('Lluvioso', 'Frío'), ('Nublado', 'Templado'), ('Lluvioso', 'Templado'),
         ('Soleado', 'Calor')]

# Eventos a verificar
evento_A = 'Soleado'
evento_B = 'Calor'

# Verificar independencia condicional
if independencia_condicional(evento_A, evento_B, datos):
    print(f"Los eventos {evento_A} y {evento_B} son independientes.")
else:
    print(f"Los eventos {evento_A} y {evento_B} no son independientes.")
