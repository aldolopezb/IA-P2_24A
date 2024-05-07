#Aldo López Barrios
#21310106
#--------------------------
from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Definir la estructura de la red bayesiana
model = BayesianModel([('A', 'C'), ('B', 'C'), ('C', 'D')])

# Definir las probabilidades condicionales (CPDs)
cpd_A = TabularCPD(variable='A', variable_card=2, values=[[0.6], [0.4]])
cpd_B = TabularCPD(variable='B', variable_card=2, values=[[0.7], [0.3]])
cpd_C = TabularCPD(variable='C', variable_card=2,
                   values=[[0.8, 0.9, 0.5, 0.7],
                           [0.2, 0.1, 0.5, 0.3]],
                   evidence=['A', 'B'],
                   evidence_card=[2, 2])
cpd_D = TabularCPD(variable='D', variable_card=2,
                   values=[[0.9, 0.6], [0.1, 0.4]],
                   evidence=['C'], evidence_card=[2])

# Asociar las CPDs con las variables en el modelo
model.add_cpds(cpd_A, cpd_B, cpd_C, cpd_D)

# Verificar si las CPDs están consistentes con la estructura y las restricciones
print("¿Las CPDs son consistentes?", model.check_model())

# Realizar inferencias en la red bayesiana
inference = VariableElimination(model)

# Calcular la probabilidad de D dado A=1 y B=0
q = inference.query(variables=['D'], evidence={'A': 1, 'B': 0})
print("Probabilidad de D dado A=1 y B=0:")
print(q)
