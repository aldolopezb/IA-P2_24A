#Aldo López Barrios
#21310106
#--------------------------
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Cargar una imagen en escala de grises
ruta = (r"C:\Users\Aldo\Desktop\Im.jpg")
image = cv2.imread(ruta, cv2.IMREAD_GRAYSCALE)

# Aplicar el operador Sobel para detectar bordes en la imagen
sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

# Calcular la magnitud de los gradientes
gradient_magnitude = np.sqrt(np.square(sobel_x) + np.square(sobel_y))

# Normalizar la magnitud de los gradientes a valores entre 0 y 255
gradient_magnitude *= 255.0 / gradient_magnitude.max()

# Convertir los valores de punto flotante a enteros sin signo de 8 bits
gradient_magnitude = np.uint8(gradient_magnitude)

# Mostrar la imagen original y la detección de bordes
plt.figure(figsize=(10, 6))
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Imagen Original')
plt.axis('off')
plt.subplot(1, 2, 2)
plt.imshow(gradient_magnitude, cmap='gray')
plt.title('Detección de Bordes (Operador Sobel)')
plt.axis('off')
plt.show()
