#Aldo López Barrios
#21310106
#--------------------------
import numpy as np

class Perceptron:
    def __init__(self, num_inputs, learning_rate=0.01, num_epochs=100):
        self.num_inputs = num_inputs
        self.learning_rate = learning_rate
        self.num_epochs = num_epochs
        self.weights = np.zeros(num_inputs + 1)  # +1 para el sesgo

    def predict(self, inputs):
        summation = np.dot(inputs, self.weights[1:]) + self.weights[0]  # Suma ponderada + sesgo
        activation = 1 if summation >= 0 else 0  # Función de activación (umbral)
        return activation

    def train(self, training_inputs, labels):
        for _ in range(self.num_epochs):
            for inputs, label in zip(training_inputs, labels):
                prediction = self.predict(inputs)
                self.weights[1:] += self.learning_rate * (label - prediction) * inputs
                self.weights[0] += self.learning_rate * (label - prediction)  # Actualizar sesgo

# Ejemplo de uso
if __name__ == "__main__":
    # Datos de entrenamiento
    training_inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    labels = np.array([0, 0, 0, 1])

    # Crear y entrenar el perceptrón
    perceptron = Perceptron(num_inputs=2)
    perceptron.train(training_inputs, labels)

    # Probar el perceptrón
    for inputs in training_inputs:
        prediction = perceptron.predict(inputs)
        print(f"Predicción para {inputs}: {prediction}")
