class Rule:
    def __init__(self, premises, conclusion):
        self.premises = premises
        self.conclusion = conclusion

    def match(self, facts):
        return all(premise in facts for premise in self.premises)

class KnowledgeBase:
    def __init__(self):
        self.rules = []

    def add_rule(self, rule):
        self.rules.append(rule)

    def forward_chain(self, facts):
        new_facts = set()
        for rule in self.rules:
            if rule.match(facts) and rule.conclusion not in facts:
                new_facts.add(rule.conclusion)
        return new_facts

    def backward_chain(self, goal, facts):
        if goal in facts:
            return True
        for rule in self.rules:
            if rule.conclusion == goal:
                if all(self.backward_chain(premise, facts) for premise in rule.premises):
                    return True
        return False

# Crear reglas
rule1 = Rule(['P', 'Q'], 'R')
rule2 = Rule(['S'], 'P')
rule3 = Rule(['R'], 'S')

# Crear base de conocimiento
kb = KnowledgeBase()
kb.add_rule(rule1)
kb.add_rule(rule2)
kb.add_rule(rule3)

# Hechos iniciales
facts = {'P', 'Q'}

# Encadenamiento hacia adelante
new_facts_forward = kb.forward_chain(facts)
print("Nuevos hechos por encadenamiento hacia adelante:", new_facts_forward)

# Meta para encadenamiento hacia atrás
goal = 'R'

# Encadenamiento hacia atrás
backward_result = kb.backward_chain(goal, facts)
print("¿Se puede demostrar la meta por encadenamiento hacia atrás?:", backward_result)
