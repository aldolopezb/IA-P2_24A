#Aldo López Barrios
#21310106
#--------------------------
import numpy as np
from keras.models import Sequential
from keras.layers import Dense

# Generar datos de ejemplo
np.random.seed(0)
X = np.random.rand(1000, 10)
y = np.random.randint(2, size=(1000,))

# Definir el modelo de red neuronal
model = Sequential()
model.add(Dense(64, input_dim=10, activation='relu'))  # Capa oculta con 64 neuronas y función de activación ReLU
model.add(Dense(32, activation='relu'))  # Capa oculta con 32 neuronas y función de activación ReLU
model.add(Dense(1, activation='sigmoid'))  # Capa de salida con 1 neurona y función de activación sigmoide

# Compilar el modelo
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Entrenar el modelo
model.fit(X, y, epochs=10, batch_size=32)

# Evaluar el modelo
loss, accuracy = model.evaluate(X, y)
print("Loss:", loss)
print("Accuracy:", accuracy)
