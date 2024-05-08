#Aldo López Barrios
#21310106
#--------------------------
class Particle:
    def __init__(self, initial_position, initial_velocity):
        self.position = initial_position
        self.velocity = initial_velocity

    def move(self, time):
        self.position += self.velocity * time

# Parámetros
initial_position = 0
initial_velocity = 2  # Unidades de distancia por unidad de tiempo (por ejemplo, metros por segundo)
time = 1  # Unidad de tiempo (por ejemplo, segundos)

# Crear la partícula
particle = Particle(initial_position, initial_velocity)

# Mover la partícula
particle.move(time)

# Imprimir la nueva posición
print("Nueva posición de la partícula:", particle.position)
