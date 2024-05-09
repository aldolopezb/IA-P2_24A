#Aldo López Barrios
#21310106
#--------------------------
import re

class AnalizadorLexico:
    def __init__(self, texto, tokens):
        self.texto = texto
        self.tokens = tokens

    def analizar(self):
        resultados = []
        for token, patron in self.tokens.items():
            coincidencias = re.findall(patron, self.texto)
            for coincidencia in coincidencias:
                resultados.append((token, coincidencia))
        return resultados

# Ejemplo de uso
texto = "if (x == 5) { y = 10; }"
tokens = {
    'IF': r'\bif\b',
    'NUMERO': r'\b\d+\b',
    'PARENTESIS_ABIERTO': r'\(',
    'PARENTESIS_CERRADO': r'\)',
    'LLAVE_ABIERTA': r'\{',
    'LLAVE_CERRADA': r'\}',
    'IGUAL': r'==',
    'ASIGNACION': r'=',
    'PUNTO_Y_COMA': r';',
    'VARIABLE': r'\b[a-zA-Z_][a-zA-Z0-9_]*\b',
    'ESPACIO': r'\s+'
}

analizador = AnalizadorLexico(texto, tokens)
resultados = analizador.analizar()

print("Tokens encontrados:")
for token, lexema in resultados:
    print("{}: {}".format(token, lexema))
