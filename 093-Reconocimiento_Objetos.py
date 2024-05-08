#Aldo López Barrios
#21310106
#--------------------------
import cv2

# Cargar la imagen
ruta = (r"C:\Users\Aldo\Desktop\Rostros.jpg")
image = cv2.imread(ruta)

# Convertir la imagen a escala de grises
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Cargar el clasificador Haar para detección de rostros
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Detectar rostros en la imagen
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

# Dibujar un rectángulo alrededor de los rostros detectados
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 4)

# Mostrar la imagen con los rostros detectados
cv2.imshow('Object Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
