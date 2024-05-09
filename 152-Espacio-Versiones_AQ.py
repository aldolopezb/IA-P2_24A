#Aldo López Barrios
#21310106
#--------------------------
class VersionSpace:
    def __init__(self, X, y):
        self.X = X
        self.y = y
        self.positive_instances = []
        self.negative_instances = []
        self.attributes = set(range(len(X[0])))
        self.version_space = []

    def generate_version_space(self):
        for i, instance in enumerate(self.X):
            if self.y[i] == 1:
                self.positive_instances.append(instance)
            else:
                self.negative_instances.append(instance)
        
        for pos_instance in self.positive_instances:
            consistent_hypotheses = []
            for i, attr in enumerate(pos_instance):
                for neg_instance in self.negative_instances:
                    if neg_instance[i] != attr:
                        consistent_hypotheses.append((i, attr))
            self.version_space.append(consistent_hypotheses)

# Ejemplo de uso
X = [[1, 0, 1], [0, 1, 0], [1, 1, 1], [0, 0, 1], [1, 0, 0]]
y = [1, 0, 1, 0, 1]

vs = VersionSpace(X, y)
vs.generate_version_space()

print("Espacio de versiones:")
for hypothesis in vs.version_space:
    print(hypothesis)
