#Aldo López Barrios
#21310106
#--------------------------
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Cargar el conjunto de datos de dígitos escritos a mano
digits = datasets.load_digits()

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.2, random_state=42)

# Crear un clasificador k-NN
knn = KNeighborsClassifier(n_neighbors=3)

# Entrenar el clasificador
knn.fit(X_train, y_train)

# Predecir las etiquetas de los datos de prueba
y_pred = knn.predict(X_test)

# Calcular la precisión del modelo
accuracy = accuracy_score(y_test, y_pred)
print("Precisión del modelo:", accuracy)
