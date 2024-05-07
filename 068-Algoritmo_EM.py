#Aldo López Barrios
#21310106
#--------------------------
import numpy as np
from sklearn.datasets import make_blobs
from sklearn.mixture import GaussianMixture

# Generar datos de muestra
X, _ = make_blobs(n_samples=300, centers=3, cluster_std=1.0, random_state=42)

# Inicializar el modelo de mezclas gaussianas
gmm = GaussianMixture(n_components=3, random_state=42)

# Ajustar el modelo a los datos
gmm.fit(X)

# Obtener las etiquetas de los clusters
labels = gmm.predict(X)

# Obtener los parámetros del modelo
means = gmm.means_
covariances = gmm.covariances_
weights = gmm.weights_

# Imprimir los parámetros del modelo
print("Medias de los clusters:")
print(means)
print("\nMatrices de covarianza de los clusters:")
print(covariances)
print("\nPesos de los clusters:")
print(weights)
