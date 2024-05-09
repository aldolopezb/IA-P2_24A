#Aldo López Barrios
#21310106
#--------------------------
from collections import Counter

class MostFrequentValue:
    def __init__(self):
        self.most_frequent_value = None

    def fit(self, data):
        counter = Counter(data)
        self.most_frequent_value = counter.most_common(1)[0][0]

    def predict(self):
        if self.most_frequent_value is None:
            raise Exception("El código está sin entrenarse, podemos ajustarlo según nuestras necesidades")
        return self.most_frequent_value

# Ejemplo de uso
data = ['A', 'B', 'B', 'C', 'C', 'C', 'D']
most_frequent_model = MostFrequentValue()
most_frequent_model.fit(data)
prediction = most_frequent_model.predict()
print("La hipótesis más frecuente es:", prediction)
