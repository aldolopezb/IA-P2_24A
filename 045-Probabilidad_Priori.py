#Aldo López Barrios
#21310106
#--------------------------
# Datos de ejemplo: aprobados y reprobados
datos = [
    {'edad': 20, 'genero': 'Femenino', 'aprobado': True},
    {'edad': 22, 'genero': 'Masculino', 'aprobado': False},
    {'edad': 21, 'genero': 'Femenino', 'aprobado': True},
    {'edad': 19, 'genero': 'Masculino', 'aprobado': True},
    {'edad': 23, 'genero': 'Femenino', 'aprobado': True},
    # Agrega más datos si es necesario
]

# Contar el número de estudiantes que aprobaron
total_aprobados = sum(1 for estudiante in datos if estudiante['aprobado'])

# Contar el número total de estudiantes
total_estudiantes = len(datos)

# Calcular la probabilidad a priori de aprobar
probabilidad_priori_aprobado = total_aprobados / total_estudiantes

print("La probabilidad a priori de aprobar el examen es:", probabilidad_priori_aprobado)
