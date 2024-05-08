#Aldo López Barrios
#21310106
#--------------------------
import numpy as np

# Definir la función de activación sigmoide y su derivada
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Definir la función de pérdida (MSE) y su derivada
def mean_squared_error(y_true, y_pred):
    return np.mean(np.square(y_true - y_pred))

def mean_squared_error_derivative(y_true, y_pred):
    return y_pred - y_true

# Clase para la capa de una red neuronal
class NeuralLayer:
    def __init__(self, n_inputs, n_neurons, activation_function, activation_derivative):
        self.weights = np.random.rand(n_inputs, n_neurons)
        self.bias = np.random.rand(1, n_neurons)
        self.activation_function = activation_function
        self.activation_derivative = activation_derivative

    def forward_propagation(self, inputs):
        self.inputs = inputs
        self.output = self.activation_function(np.dot(inputs, self.weights) + self.bias)

    def backward_propagation(self, error, learning_rate):
        delta = error * self.activation_derivative(self.output)
        self.weights -= learning_rate * np.dot(self.inputs.T, delta)
        self.bias -= learning_rate * np.sum(delta, axis=0, keepdims=True)

# Clase para la red neuronal
class NeuralNetwork:
    def __init__(self, layers):
        self.layers = layers

    def forward_propagation(self, inputs):
        for layer in self.layers:
            layer.forward_propagation(inputs)
            inputs = layer.output
        return inputs

    def backward_propagation(self, error, learning_rate):
        for layer in reversed(self.layers):
            layer.backward_propagation(error, learning_rate)
            error = np.dot(error, layer.weights.T)

    def train(self, X_train, y_train, epochs, learning_rate):
        for epoch in range(epochs):
            total_loss = 0
            for X, y_true in zip(X_train, y_train):
                y_pred = self.forward_propagation(X.reshape(1, -1))
                loss = mean_squared_error(y_true, y_pred)
                total_loss += loss
                error = mean_squared_error_derivative(y_true, y_pred)
                self.backward_propagation(error, learning_rate)
            print(f"Epoch {epoch + 1}/{epochs}, Loss: {total_loss / len(X_train)}")

# Datos de entrenamiento
X_train = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y_train = np.array([[0], [1], [1], [0]])

# Definir la arquitectura de la red neuronal
input_size = X_train.shape[1]
hidden_layer_size = 4
output_size = 1

# Crear las capas de la red neuronal
hidden_layer = NeuralLayer(input_size, hidden_layer_size, sigmoid, sigmoid_derivative)
output_layer = NeuralLayer(hidden_layer_size, output_size, sigmoid, sigmoid_derivative)

# Crear la red neuronal
model = NeuralNetwork([hidden_layer, output_layer])

# Entrenar la red neuronal
model.train(X_train, y_train, epochs=10000, learning_rate=0.1)
