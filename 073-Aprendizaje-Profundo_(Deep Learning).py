#Aldo López Barrios
#21310106
#--------------------------
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers, models
from tensorflow.keras.datasets import fashion_mnist

# Cargar el conjunto de datos Fashion MNIST
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

# Normalizar las imágenes y convertirlas en tensores
train_images = train_images.astype('float32') / 255.0
test_images = test_images.astype('float32') / 255.0

# Definir el modelo de red neuronal profunda
model = models.Sequential([
    layers.Flatten(input_shape=(28, 28)),  # Capa de aplanamiento para convertir las imágenes 2D en un vector 1D
    layers.Dense(128, activation='relu'),  # Capa oculta con 128 neuronas y función de activación ReLU
    layers.Dense(64, activation='relu'),   # Capa oculta con 64 neuronas y función de activación ReLU
    layers.Dense(10, activation='softmax')  # Capa de salida con 10 neuronas para las 10 clases de Fashion MNIST y función de activación softmax
])

# Compilar el modelo
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Entrenar el modelo
model.fit(train_images, train_labels, epochs=10, batch_size=64, verbose=1)

# Evaluar el modelo en el conjunto de prueba
test_loss, test_acc = model.evaluate(test_images, test_labels)
print('Precisión en el conjunto de prueba:', test_acc)
