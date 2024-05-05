class Rule:
    def __init__(self, condition, recommendation):
        self.condition = condition
        self.recommendation = recommendation

    def match(self, age, gender):
        return age in self.condition['age'] and gender in self.condition['gender']

class KnowledgeBase:
    def __init__(self):
        self.rules = []

    def add_rule(self, rule):
        self.rules.append(rule)

    def recommend_movie(self, age, gender):
        for rule in self.rules:
            if rule.match(age, gender):
                return rule.recommendation
        return "No recommendation available"

# Crear reglas de recomendación
rule1 = Rule({'age': range(0, 18), 'gender': 'male'}, 'Spider-Man: Into the Spider-Verse')
rule2 = Rule({'age': range(0, 18), 'gender': 'female'}, 'Interstellar')
rule3 = Rule({'age': range(18, 40), 'gender': 'male'}, 'Inception')
rule4 = Rule({'age': range(18, 40), 'gender': 'female'}, 'La La Land')
rule5 = Rule({'age': range(40, 100), 'gender': 'male'}, 'The Shawshank Redemption')
rule6 = Rule({'age': range(40, 100), 'gender': 'female'}, 'The Devil Wears Prada')

# Crear base de conocimiento y agregar reglas
kb = KnowledgeBase()
kb.add_rule(rule1)
kb.add_rule(rule2)
kb.add_rule(rule3)
kb.add_rule(rule4)
kb.add_rule(rule5)
kb.add_rule(rule6)

# Hacer recomendaciones para diferentes usuarios
print(kb.recommend_movie(25, 'male'))  # Output: Inception
print(kb.recommend_movie(15, 'female'))  # Output: Frozen
print(kb.recommend_movie(55, 'female'))  # Output: The Devil Wears Prada
