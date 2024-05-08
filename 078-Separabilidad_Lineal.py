#Aldo López Barrios
#21310106
#--------------------------
import numpy as np
import matplotlib.pyplot as plt

# Generar datos linealmente separables
np.random.seed(0)
num_samples = 100
mean_class1 = [2, 4]
mean_class2 = [5, 2]
cov = [[1, 0], [0, 1]]
class1 = np.random.multivariate_normal(mean_class1, cov, num_samples)
class2 = np.random.multivariate_normal(mean_class2, cov, num_samples)

# Trazar los datos
plt.scatter(class1[:, 0], class1[:, 1], marker='o', label='Class 1')
plt.scatter(class2[:, 0], class2[:, 1], marker='x', label='Class 2')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')

# Calcular la línea de separación (hiperplano)
A = np.vstack([class1, class2])
B = np.hstack([np.ones(num_samples), -np.ones(num_samples)])
w = np.linalg.solve(np.dot(A.T, A), np.dot(A.T, B))

# Verificar la forma de w
print("Forma de w:", w.shape)

# Si la forma de w es (2,), expandirla a (3,) para tener una constante
if w.shape == (2,):
    w = np.concatenate([w, [0]])

# Calcular la línea de separación
xx = np.linspace(0, 6, 100)
yy = -w[0]/w[1] * xx - w[2]/w[1]

# Trazar la línea de separación
plt.plot(xx, yy, 'k-')
plt.title('Datos Linealmente Separables con la Línea de Separación')
plt.legend()
plt.grid(True)
plt.show()
