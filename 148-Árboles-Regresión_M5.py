#Aldo López Barrios
#21310106
#--------------------------
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Datos de ejemplo: características y etiquetas
X = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
y = [3, 5, 7, 9, 11]  # Etiquetas

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar el árbol de decisión de regresión
tree_regressor = DecisionTreeRegressor()
tree_regressor.fit(X_train, y_train)

# Entrenar el modelo de regresión lineal
linear_regressor = LinearRegression()
linear_regressor.fit(X_train, y_train)

# Realizar predicciones
y_pred_tree = tree_regressor.predict(X_test)
y_pred_linear = linear_regressor.predict(X_test)

# Calcular el error cuadrático medio (MSE)
mse_tree = mean_squared_error(y_test, y_pred_tree)
mse_linear = mean_squared_error(y_test, y_pred_linear)

print("Error cuadrático medio del árbol de decisión:", mse_tree)
print("Error cuadrático medio del modelo de regresión lineal:", mse_linear)
