#Aldo López Barrios
#21310106
#--------------------------
class ExplanationGenerator:
    def __init__(self, data, target):
        self.data = data
        self.target = target

    def generate_explanation(self, instance):
        relevant_attributes = self.get_relevant_attributes(instance)
        explanation = {}
        for attr in relevant_attributes:
            explanation[attr] = instance[attr]
        return explanation

    def get_relevant_attributes(self, instance):
        relevant_attributes = []
        for attr, value in enumerate(instance):
            if self.is_relevant(attr, value):
                relevant_attributes.append(attr)
        return relevant_attributes

    def is_relevant(self, attr, value):
        # Aquí puedes implementar la lógica para determinar la relevancia del atributo
        # Esta es solo una implementación de ejemplo
        if value == 1:  # Consideramos relevantes solo los atributos con valor 1
            return True
        return False

# Ejemplo de uso
data = [
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 1, 1, 0],
    [0, 0, 1, 1],
    [1, 0, 0, 0]
]
target = [1, 0, 1, 0, 1]

generator = ExplanationGenerator(data, target)

# Generar explicaciones para cada instancia
for i, instance in enumerate(data):
    explanation = generator.generate_explanation(instance)
    print("Explicación para la instancia {}: {}".format(i+1, explanation))
