#Aldo López Barrios
#21310106
#--------------------------
from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Definir la estructura del modelo
modelo = BayesianModel([('A', 'C'), ('B', 'C'), ('C', 'D'), ('D', 'E')])

# Definir las distribuciones de probabilidad condicional (CPDs)
cpd_A = TabularCPD(variable='A', variable_card=2, values=[[0.5], [0.5]])
cpd_B = TabularCPD(variable='B', variable_card=2, values=[[0.5], [0.5]])
cpd_C = TabularCPD(variable='C', variable_card=2, values=[[0.3, 0.4, 0.7, 0.8],
                                                          [0.7, 0.6, 0.3, 0.2]],
                    evidence=['A', 'B'], evidence_card=[2, 2])
cpd_D = TabularCPD(variable='D', variable_card=2, values=[[0.9, 0.6], [0.1, 0.4]],
                    evidence=['C'], evidence_card=[2])
cpd_E = TabularCPD(variable='E', variable_card=2, values=[[0.9, 0.2], [0.1, 0.8]],
                    evidence=['D'], evidence_card=[2])

# Añadir los CPDs al modelo
modelo.add_cpds(cpd_A, cpd_B, cpd_C, cpd_D, cpd_E)

# Realizar eliminación de variables
inferencia = VariableElimination(modelo)
resultado = inferencia.query(variables=['C', 'D'], evidence={'A': 0, 'B': 1})

print(resultado)
