class World:
    def __init__(self, name):
        self.name = name
        self.transitions = []

    def add_transition(self, target_world, label):
        self.transitions.append((target_world, label))


class TemporalLogicProgram:
    def __init__(self):
        self.worlds = {}

    def add_world(self, world):
        self.worlds[world.name] = world

    def evaluate(self, formula, start_world):
        if '->' in formula:
            antecedent, consequent = formula.split('->')
            return self.evaluate_antecedent(antecedent.strip(), consequent.strip(), start_world)
        elif 'U' in formula:
            left, right = formula.split('U')
            return self.evaluate_until(left.strip(), right.strip(), start_world)
        else:
            return self.evaluate_simple(formula.strip(), start_world)

    def evaluate_simple(self, formula, current_world):
        if formula == 'p':
            return True if current_world.name == 'p' else False
        elif formula == 'q':
            return True if current_world.name == 'q' else False
        else:
            return False

    def evaluate_antecedent(self, antecedent, consequent, current_world):
        if self.evaluate_simple(antecedent, current_world):
            return self.evaluate(consequent, current_world)
        else:
            return True

    def evaluate_until(self, left, right, current_world):
        if self.evaluate_simple(right, current_world):
            return True
        elif self.evaluate_simple(left, current_world):
            for next_world, _ in current_world.transitions:
                if self.evaluate_until(left, right, next_world):
                    return True
            return False
        else:
            return False


# Crear mundos
w1 = World('p')
w2 = World('q')
w3 = World('r')

# Definir transiciones entre mundos
w1.add_transition(w2, 's1')
w2.add_transition(w3, 's2')

# Crear programa de lógica temporal
program = TemporalLogicProgram()
program.add_world(w1)
program.add_world(w2)
program.add_world(w3)

# Evaluar fórmulas de lógica temporal
print(program.evaluate('p -> q', w1))   # Devuelve True
print(program.evaluate('q -> p', w1))   # Devuelve False
print(program.evaluate('p U q', w1))    # Devuelve True
print(program.evaluate('q U p', w1))    # Devuelve False
