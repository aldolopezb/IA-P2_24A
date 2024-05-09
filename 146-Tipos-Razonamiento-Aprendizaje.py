#Aldo López Barrios
#21310106
#--------------------------
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# Datos de ejemplo: características y etiquetas
features = [[5, 2], [7, 3], [8, 2], [3, 6], [2, 3], [3, 4]]
labels = [1, 1, 1, 0, 0, 0]  # Etiquetas: 1 para "positivo", 0 para "negativo"

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

# Crear el clasificador Naive Bayes
clf = GaussianNB()

# Entrenar el clasificador
clf.fit(X_train, y_train)

# Predecir las etiquetas para el conjunto de prueba
predicted_labels = clf.predict(X_test)

# Calcular la precisión del clasificador
accuracy = accuracy_score(y_test, predicted_labels)
print("Precisión del clasificador Naive Bayes:", accuracy)
