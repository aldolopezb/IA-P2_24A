#Aldo López Barrios
#21310106
#--------------------------
class KnowledgeBase:
    def __init__(self):
        self.facts = set()
        self.rules = []

    def add_fact(self, fact):
        self.facts.add(fact)

    def add_rule(self, rule):
        self.rules.append(rule)

    def infer(self):
        inferred_facts = set()

        for rule in self.rules:
            if rule.condition.issubset(self.facts):
                inferred_facts.add(rule.consequence)

        self.facts.update(inferred_facts)

    def print_facts(self):
        print("Facts:")
        for fact in self.facts:
            print(fact)

    def print_rules(self):
        print("Rules:")
        for rule in self.rules:
            print(rule)

class Rule:
    def __init__(self, condition, consequence):
        self.condition = condition
        self.consequence = consequence

    def __str__(self):
        return f"If {self.condition} then {self.consequence}"

# Ejemplo de uso
if __name__ == "__main__":
    kb = KnowledgeBase()

    # Agregar hechos
    kb.add_fact("Sunny")
    kb.add_fact("Warm")

    # Agregar reglas
    kb.add_rule(Rule({"Sunny", "Warm"}, "PlayTennis"))
    kb.add_rule(Rule({"Rainy"}, "StayInside"))

    # Inferir nuevos hechos
    kb.infer()

    # Imprimir hechos y reglas
    kb.print_facts()
    kb.print_rules()
