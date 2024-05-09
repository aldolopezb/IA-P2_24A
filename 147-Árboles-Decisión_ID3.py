#Aldo López Barrios
#21310106
#--------------------------
import numpy as np

class NodoArbolDecision:
    def __init__(self, atributo=None, valor=None, resultado=None):
        self.atributo = atributo  # Atributo utilizado para dividir
        self.valor = valor  # Valor del atributo utilizado para dividir
        self.resultado = resultado  # Etiqueta de clasificación si es un nodo hoja
        self.hijos = {}  # Diccionario de hijos (valor del atributo: nodo hijo)

class ID3:
    def __init__(self):
        pass

    def entropia(self, y):
        clases, counts = np.unique(y, return_counts=True)
        probs = counts / len(y)
        return -np.sum(probs * np.log2(probs))

    def ganancia_informacion(self, X, y, atributo, valor):
        subconjunto_indices = np.where(X[:, atributo] == valor)
        subconjunto_clases = y[subconjunto_indices]
        entropia_total = self.entropia(y)
        entropia_subconjunto = self.entropia(subconjunto_clases)
        proporcion_subconjunto = len(subconjunto_clases) / len(y)
        ganancia = entropia_total - proporcion_subconjunto * entropia_subconjunto
        return ganancia

    def mejor_atributo(self, X, y):
        num_atributos = X.shape[1]
        ganancias = []
        for atributo in range(num_atributos):
            for valor in np.unique(X[:, atributo]):
                ganancias.append(self.ganancia_informacion(X, y, atributo, valor))
        if not ganancias:  # Si no se calcularon ganancias
            return -1, -1  # Valor predeterminado
        mejor_atributo_valor = np.argmax(ganancias)
        mejor_atributo, mejor_valor = divmod(mejor_atributo_valor, num_atributos)
        return mejor_atributo, mejor_valor

    def construir_arbol(self, X, y, atributos):
        if len(np.unique(y)) == 1:  # Todos los ejemplos tienen la misma etiqueta
            return NodoArbolDecision(resultado=y[0])

        if len(atributos) == 0:  # No quedan atributos para dividir
            clase_mas_comun = np.argmax(np.bincount(y))
            return NodoArbolDecision(resultado=clase_mas_comun)

        mejor_atributo, mejor_valor = self.mejor_atributo(X, y)
        nodo = NodoArbolDecision(atributo=mejor_atributo, valor=mejor_valor)

        atributos_restantes = [atributo for atributo in atributos if atributo != mejor_atributo]

        for valor in np.unique(X[:, mejor_atributo]):
            subconjunto_indices = np.where(X[:, mejor_atributo] == valor)
            subconjunto_X = X[subconjunto_indices]
            subconjunto_y = y[subconjunto_indices]
            nodo.hijos[valor] = self.construir_arbol(subconjunto_X, subconjunto_y, atributos_restantes)

        return nodo

    def entrenar(self, X, y):
        atributos = list(range(X.shape[1]))
        self.raiz = self.construir_arbol(X, y, atributos)

    def predecir(self, x):
        nodo_actual = self.raiz
        while nodo_actual.resultado is None:
            valor = x[nodo_actual.atributo]
            nodo_actual = nodo_actual.hijos[valor]
        return nodo_actual.resultado

# Ejemplo de uso
if __name__ == "__main__":
    # Ejemplo de conjunto de datos (atributos categóricos)
    X = np.array([
        ['sol', 'caliente', 'alta', 'débil'],
        ['sol', 'caliente', 'alta', 'fuerte'],
        ['nublado', 'caliente', 'alta', 'débil'],
        ['lluvia', 'templado', 'alta', 'débil'],
        ['lluvia', 'frío', 'normal', 'débil'],
        ['lluvia', 'frío', 'normal', 'fuerte'],
        ['nublado', 'frío', 'normal', 'fuerte'],
        ['sol', 'templado', 'alta', 'débil'],
        ['sol', 'frío', 'normal', 'débil'],
        ['lluvia', 'templado', 'normal', 'débil'],
        ['sol', 'templado', 'normal', 'fuerte'],
        ['nublado', 'templado', 'alta', 'fuerte'],
        ['nublado', 'caliente', 'normal', 'débil'],
        ['lluvia', 'templado', 'alta', 'fuerte']
    ])

    y = np.array([0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0])  # Etiquetas (0: No jugar, 1: Jugar)

    # Crear y entrenar el clasificador ID3
    id3 = ID3()
    id3.entrenar(X, y)

    # Ejemplo de predicción
    ejemplo = np.array(['sol', 'caliente', 'alta', 'débil'])  # Ejemplo a predecir
    prediccion = id3.predecir(ejemplo)
    print("Predicción:", "Jugar" if prediccion == 1 else "No jugar")
