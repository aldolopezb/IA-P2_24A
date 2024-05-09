#Aldo López Barrios
#21310106
#--------------------------
import numpy as np

# Definir las longitudes de los eslabones
L1 = 1
L2 = 1

# Función para calcular la cinemática directa
def forward_kinematics(theta1, theta2):
    x = L1 * np.cos(theta1) + L2 * np.cos(theta1 + theta2)
    y = L1 * np.sin(theta1) + L2 * np.sin(theta1 + theta2)
    return x, y

# Función para calcular la cinemática inversa utilizando el método de Jacobiano Pseudo-Inverso
def inverse_kinematics(x, y, theta1_guess, theta2_guess, max_iterations=100, tolerance=1e-6):
    theta = np.array([theta1_guess, theta2_guess])
    for i in range(max_iterations):
        x_fk, y_fk = forward_kinematics(theta[0], theta[1])
        error = np.array([x - x_fk, y - y_fk])
        if np.linalg.norm(error) < tolerance:
            print("Convergió después de {} iteraciones.".format(i+1))
            return theta
        J = np.array([
            [-L1 * np.sin(theta[0]) - L2 * np.sin(theta[0] + theta[1]), -L2 * np.sin(theta[0] + theta[1])],
            [L1 * np.cos(theta[0]) + L2 * np.cos(theta[0] + theta[1]), L2 * np.cos(theta[0] + theta[1])]
        ])
        theta += np.linalg.pinv(J) @ error
    print("No se pudo converger después de {} iteraciones.".format(max_iterations))
    return None

# Definir la posición deseada
x_deseado = 1.5
y_deseado = 0.5

# Adivinanza inicial para los ángulos
theta1_guess = np.pi / 4
theta2_guess = np.pi / 4

# Calcular la cinemática inversa
theta_solucion = inverse_kinematics(x_deseado, y_deseado, theta1_guess, theta2_guess)

# Imprimir la solución
if theta_solucion is not None:
    print("Solución encontrada:")
    print("Theta1 = {:.4f} rad".format(theta_solucion[0]))
    print("Theta2 = {:.4f} rad".format(theta_solucion[1]))
    x_fk, y_fk = forward_kinematics(theta_solucion[0], theta_solucion[1])
    print("Posición calculada: ({:.4f}, {:.4f})".format(x_fk, y_fk))
else:
    print("No se encontró solución.")
