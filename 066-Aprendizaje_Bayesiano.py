#Aldo López Barrios
#21310106
#--------------------------
import numpy as np
import pymc3 as pm

# Datos observados (0 = cara, 1 = sello)
data = np.array([0, 1, 1, 0, 0, 1, 0, 1, 0, 1])

# Definir el modelo bayesiano
with pm.Model() as coin_flip_model:
    # Priori Beta para la probabilidad de obtener una cara
    p_heads = pm.Beta('p_heads', alpha=1, beta=1)
    
    # Distribución binomial para el proceso de lanzamiento de moneda
    coin_flips = pm.Bernoulli('coin_flips', p=p_heads, observed=data)
    
    # Realizar el muestreo de la posterior utilizando MCMC
    trace = pm.sample(1000, tune=1000)

# Obtener los resultados del muestreo
pm.summary(trace)
