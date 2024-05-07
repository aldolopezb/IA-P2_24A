#Aldo López Barrios
#21310106
#--------------------------
def bayes_rule(prior_A, prob_B_given_A, prob_B):
    """
    Calcula la probabilidad posterior de A dado B utilizando la regla de Bayes.
    
    Args:
    prior_A: Probabilidad a priori de A.
    prob_B_given_A: Probabilidad de B dado A.
    prob_B: Probabilidad de B.
    
    Returns:
    La probabilidad posterior de A dado B.
    """
    return (prior_A * prob_B_given_A) / prob_B

# Ejemplo de uso
prior_A = 0.3  # Probabilidad a priori de que llueva
prob_B_given_A = 0.8  # Probabilidad de que haya tráfico si llueve
prob_B = 0.5  # Probabilidad de que haya tráfico (sin considerar si llueve o no)

# Calculamos la probabilidad posterior de que llueva dado que hay tráfico
posterior_A_given_B = bayes_rule(prior_A, prob_B_given_A, prob_B)
print("La probabilidad de que llueva dado que hay tráfico es:", posterior_A_given_B)
