#Aldo López Barrios
#21310106
#--------------------------
class AnalizadorSintactico:
    def __init__(self, tokens):
        self.tokens = tokens
        self.posicion = 0
        self.actual = None

    def avanzar(self):
        if self.posicion < len(self.tokens):
            self.actual = self.tokens[self.posicion]
            self.posicion += 1
        else:
            self.actual = None

    def emparejar(self, tipo):
        if self.actual['tipo'] == tipo:
            self.avanzar()
        else:
            print("Error de sintaxis. Se esperaba '{}', se encontró '{}'.".format(tipo, self.actual['valor']))

    def factor(self):
        if self.actual['tipo'] == 'ENTERO':
            self.emparejar('ENTERO')
        elif self.actual['tipo'] == 'PARENTESIS_ABIERTO':
            self.emparejar('PARENTESIS_ABIERTO')
            self.expresion()
            self.emparejar('PARENTESIS_CERRADO')
        else:
            print("Error de sintaxis. Se esperaba 'ENTERO' o '(', se encontró '{}'.".format(self.actual['valor']))

    def termino(self):
        self.factor()
        while self.actual['tipo'] in ('MULTIPLICACION', 'DIVISION'):
            self.emparejar(self.actual['tipo'])
            self.factor()

    def expresion(self):
        self.termino()
        while self.actual['tipo'] in ('SUMA', 'RESTA'):
            self.emparejar(self.actual['tipo'])
            self.termino()

    def analizar(self):
        self.avanzar()
        self.expresion()
        if self.actual is not None:
            print("Error de sintaxis. Tokens adicionales al final del análisis.")

# Ejemplo de uso
tokens = [
    {'tipo': 'ENTERO', 'valor': '5'},
    {'tipo': 'SUMA', 'valor': '+'},
    {'tipo': 'ENTERO', 'valor': '3'},
    {'tipo': 'MULTIPLICACION', 'valor': '*'},
    {'tipo': 'ENTERO', 'valor': '2'},
    {'tipo': 'PARENTESIS_ABIERTO', 'valor': '('},
    {'tipo': 'ENTERO', 'valor': '4'},
    {'tipo': 'SUMA', 'valor': '+'},
    {'tipo': 'ENTERO', 'valor': '2'},
    {'tipo': 'PARENTESIS_CERRADO', 'valor': ')'},
]

analizador = AnalizadorSintactico(tokens)
analizador.analizar()
