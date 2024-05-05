class Rule:
    def __init__(self, antecedents, consequent):
        self.antecedents = antecedents
        self.consequent = consequent

    def fire(self, facts):
        if all(fact in facts for fact in self.antecedents):
            return self.consequent
        else:
            return None

class DiagnosticSystem:
    def __init__(self, rules):
        self.rules = rules

    def diagnose(self, facts):
        for rule in self.rules:
            result = rule.fire(facts)
            if result:
                return result
        return "No diagnosis found"

# Ejemplo de uso
# Supongamos que tenemos un sistema de diagnóstico de enfermedades
# con dos reglas simples: si hay fiebre y tos, entonces es gripe,
# y si hay dolor de cabeza y fatiga, entonces es resfriado.

rule1 = Rule(["fiebre", "tos"], "gripe")
rule2 = Rule(["dolor_de_cabeza", "fatiga"], "resfriado")

diagnostic_system = DiagnosticSystem([rule1, rule2])

# Supongamos que el paciente presenta fiebre y tos
patient_facts = ["fiebre", "tos"]
diagnosis = diagnostic_system.diagnose(patient_facts)
print("Diagnóstico para el paciente:", diagnosis)
