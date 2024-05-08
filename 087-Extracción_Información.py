#Aldo López Barrios
#21310106
#--------------------------
import re

# Texto de ejemplo
texto = """
La inteligencia artificial (IA), a veces llamada inteligencia computacional,
es la inteligencia demostrada por máquinas, en contraste con la inteligencia natural 
que muestra el ser humano. John McCarthy acuñó el término "inteligencia artificial" 
en 1956 en la Conferencia de Dartmouth.
"""

# Definir patrones de expresiones regulares para buscar nombres propios y fechas
patron_nombre = re.compile(r'[A-Z][a-z]+ [A-Z][a-z]+')
patron_fecha = re.compile(r'\d{4}')

# Buscar nombres propios en el texto
nombres = patron_nombre.findall(texto)

# Buscar fechas en el texto
fechas = patron_fecha.findall(texto)

# Imprimir los nombres y fechas encontrados
print("Nombres encontrados:", nombres)
print("Fechas encontradas:", fechas)
