class Rule:
    def __init__(self, antecedents, consequent):
        self.antecedents = antecedents
        self.consequent = consequent

class KnowledgeBase:
    def __init__(self, rules):
        self.rules = rules

    def forward_chain(self, known_facts):
        new_facts = set()
        for rule in self.rules:
            if all(antecedent in known_facts for antecedent in rule.antecedents):
                new_facts.add(rule.consequent)
        return known_facts.union(new_facts)

    def backward_chain(self, goal, known_facts):
        if goal in known_facts:
            return True
        for rule in self.rules:
            if rule.consequent == goal:
                if all(self.backward_chain(antecedent, known_facts) for antecedent in rule.antecedents):
                    return True
        return False

# Ejemplo de uso
if __name__ == "__main__":
    # Definir reglas
    rules = [
        Rule(["P", "Q"], "R"),
        Rule(["S"], "P"),
        Rule(["T"], "Q"),
        Rule(["P"], "U"),
        Rule(["R", "U"], "V")
    ]

    # Crear base de conocimiento
    kb = KnowledgeBase(rules)

    # Encadenamiento hacia adelante
    known_facts_forward = set(["S", "T"])
    new_facts_forward = kb.forward_chain(known_facts_forward)
    print("Encadenamiento hacia adelante:")
    print("Hechos conocidos:", known_facts_forward)
    print("Nuevos hechos inferidos:", new_facts_forward - known_facts_forward)

    # Encadenamiento hacia atrás
    goal_backward = "V"
    known_facts_backward = set(["S", "T"])
    result_backward = kb.backward_chain(goal_backward, known_facts_backward)
    print("\nEncadenamiento hacia atrás:")
    print("Meta:", goal_backward)
    print("Hechos conocidos:", known_facts_backward)
    print("¿La meta es alcanzable?", result_backward)
