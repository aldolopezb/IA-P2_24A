#Aldo López Barrios
#21310106
#--------------------------
import numpy as np

class Factor:
    def __init__(self, variables, values):
        self.variables = variables
        self.values = values

class HaciaAdelanteAtras:
    def __init__(self, modelo):
        self.modelo = modelo
        self.factores = modelo  # Utilizar el diccionario de factores directamente
        self.variables_ocultas = list(modelo.keys())
        self.numero_variables = len(self.variables_ocultas)
        self.alpha = [None] * self.numero_variables
        self.beta = [None] * self.numero_variables
        self.norm_const = 0.0

    def hacia_adelante(self):
        # Paso hacia adelante
        for i, var in enumerate(self.variables_ocultas):
            if i == 0:
                # Inicialización
                self.alpha[i] = np.ones_like(self.factores[var].values)
            else:
                # Recursión
                phi = self.factores[var]
                phi_values = phi.values
                alpha_values = self.alpha[i - 1]
                self.alpha[i] = np.dot(phi_values, alpha_values)
                # Normalización
                self.alpha[i] /= np.sum(self.alpha[i])
        # Calcular la constante de normalización
        self.norm_const = np.sum(self.alpha[-1])


    def hacia_atras(self):
        # Paso hacia atrás
        for i in range(self.numero_variables - 1, -1, -1):
            if i == self.numero_variables - 1:
                # Inicialización
                self.beta[i] = np.ones_like(self.factores[self.variables_ocultas[i]].values)
            else:
                # Recursión
                phi = self.factores[self.variables_ocultas[i + 1]]
                phi_values = phi.values[np.newaxis, :]
                beta_values = self.beta[i + 1][:, np.newaxis]
                self.beta[i] = np.dot(beta_values, phi_values).flatten()
                # Normalización
                self.beta[i] /= np.sum(self.beta[i])

    def inferencia_posterior(self, variable_oculta):
        # Calcular la probabilidad posterior de la variable oculta dada las observaciones
        indice_variable = self.variables_ocultas.index(variable_oculta)
        posterior = (self.alpha[indice_variable] * self.beta[indice_variable]) / self.norm_const
        return posterior

# Definir el modelo como un diccionario de factores
modelo = {
    'A': Factor(['A'], np.array([0.6, 0.4])),
    'B': Factor(['B'], np.array([0.5, 0.5])),
    'C': Factor(['A', 'B', 'C'], np.array([[0.3, 0.9], [0.7, 0.1]])),
    'D': Factor(['C', 'D'], np.array([[0.2, 0.8], [0.4, 0.6]]))
}

# Crear una instancia del algoritmo hacia adelante-atrás
inference = HaciaAdelanteAtras(modelo)

# Realizar el paso hacia adelante
inference.hacia_adelante()

# Realizar el paso hacia atrás
inference.hacia_atras()

# Realizar inferencia posterior para una variable oculta dada las observaciones
posterior_C = inference.inferencia_posterior('C')
print("Probabilidad posterior de C:", posterior_C)
