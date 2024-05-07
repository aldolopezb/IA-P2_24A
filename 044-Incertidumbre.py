#Aldo López Barrios
#21310106
#--------------------------
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Definir los antecedentes y consecuentes
edad = ctrl.Antecedent(np.arange(0, 101, 1), 'edad')
ingreso = ctrl.Antecedent(np.arange(0, 100001, 1), 'ingreso')
aceptacion_credito = ctrl.Consequent(np.arange(0, 101, 1), 'aceptacion_credito')

# Definir las funciones de membresía
edad['joven'] = fuzz.trimf(edad.universe, [0, 25, 50])
edad['adulto'] = fuzz.trimf(edad.universe, [25, 50, 75])
edad['anciano'] = fuzz.trimf(edad.universe, [50, 75, 100])

ingreso['bajo'] = fuzz.trimf(ingreso.universe, [0, 25000, 50000])
ingreso['medio'] = fuzz.trimf(ingreso.universe, [25000, 50000, 75000])
ingreso['alto'] = fuzz.trimf(ingreso.universe, [50000, 75000, 100000])

aceptacion_credito['baja'] = fuzz.trimf(aceptacion_credito.universe, [0, 25, 50])
aceptacion_credito['media'] = fuzz.trimf(aceptacion_credito.universe, [25, 50, 75])
aceptacion_credito['alta'] = fuzz.trimf(aceptacion_credito.universe, [50, 75, 100])

# Visualización de las funciones de membresía
edad.view()
ingreso.view()
aceptacion_credito.view()

# Definir las reglas difusas
regla1 = ctrl.Rule(edad['joven'] & ingreso['bajo'], aceptacion_credito['baja'])
regla2 = ctrl.Rule(edad['joven'] & ingreso['medio'], aceptacion_credito['baja'])
regla3 = ctrl.Rule(edad['joven'] & ingreso['alto'], aceptacion_credito['media'])

regla4 = ctrl.Rule(edad['adulto'] & ingreso['bajo'], aceptacion_credito['baja'])
regla5 = ctrl.Rule(edad['adulto'] & ingreso['medio'], aceptacion_credito['media'])
regla6 = ctrl.Rule(edad['adulto'] & ingreso['alto'], aceptacion_credito['alta'])

regla7 = ctrl.Rule(edad['anciano'] & ingreso['bajo'], aceptacion_credito['media'])
regla8 = ctrl.Rule(edad['anciano'] & ingreso['medio'], aceptacion_credito['alta'])
regla9 = ctrl.Rule(edad['anciano'] & ingreso['alto'], aceptacion_credito['alta'])

# Sistema de control difuso
sistema_control = ctrl.ControlSystem([regla1, regla2, regla3, regla4, regla5, regla6, regla7, regla8, regla9])
sistema = ctrl.ControlSystemSimulation(sistema_control)

# Evaluación del sistema de control difuso
sistema.input['edad'] = 40
sistema.input['ingreso'] = 60000
sistema.compute()

print("Nivel de aceptación de crédito:", sistema.output['aceptacion_credito'])
aceptacion_credito.view(sim=sistema)
