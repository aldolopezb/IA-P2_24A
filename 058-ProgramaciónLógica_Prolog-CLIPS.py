from pyDatalog import pyDatalog

# Definir las relaciones
pyDatalog.create_terms('es_mamifero, tiene_pelo, da_leche, X')

# Definir los hechos
+es_mamifero('perro')
+es_mamifero('gato')
+es_mamifero('elefante')

# Definir las reglas
tiene_pelo(X) <= es_mamifero(X)
da_leche(X) <= es_mamifero(X)

# Consultas
print(tiene_pelo.unify('perro'))     # Devuelve True
print(da_leche.unify('gato'))        # Devuelve True
print(es_mamifero.unify('elefante')) # Devuelve True
print(tiene_pelo.unify('gato'))      # Devuelve True
print(da_leche.unify('perro'))       # Devuelve True
