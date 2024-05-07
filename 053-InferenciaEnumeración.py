#Aldo López Barrios
#21310106
#--------------------------
from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Definir la estructura de la red bayesiana
model = BayesianModel([('A', 'C'), ('B', 'C')])

# Definir las distribuciones de probabilidad condicional (CPDs)
cpd_a = TabularCPD(variable='A', variable_card=2, values=[[0.6], [0.4]])
cpd_b = TabularCPD(variable='B', variable_card=2, values=[[0.7], [0.3]])
cpd_c = TabularCPD(variable='C', variable_card=2, 
                   values=[[0.8, 0.6, 0.3, 0.1], [0.2, 0.4, 0.7, 0.9]],
                   evidence=['A', 'B'], evidence_card=[2, 2])

# Añadir las CPDs al modelo
model.add_cpds(cpd_a, cpd_b, cpd_c)

# Verificar la consistencia del modelo
assert model.check_model()

# Realizar inferencia por enumeración
infer = VariableElimination(model)
posterior_c = infer.query(variables=['C'])

# Imprimir los resultados
print(posterior_c)
