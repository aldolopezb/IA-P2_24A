#Aldo López Barrios
#21310106
#--------------------------
import numpy as np
import matplotlib.pyplot as plt
import noise

# Definir las dimensiones de la textura
width = 512
height = 512

# Generar la textura procedural utilizando ruido de Perlin
scale = 50.0  # Escala del ruido
octaves = 6   # Número de octavas
persistence = 0.5  # Persitencia del ruido
lacunarity = 2.0   # Lacunaridad del ruido

world = np.zeros((height, width))
for i in range(height):
    for j in range(width):
        world[i][j] = noise.pnoise2(i / scale, 
                                     j / scale, 
                                     octaves=octaves, 
                                     persistence=persistence, 
                                     lacunarity=lacunarity, 
                                     repeatx=width, 
                                     repeaty=height, 
                                     base=0)

# Mostrar la textura generada
plt.figure(figsize=(8, 8))
plt.imshow(world, cmap='gray', interpolation='nearest')
plt.axis('off')
plt.title('Textura generada con ruido de Perlin')
plt.show()
