#Aldo López Barrios
#21310106
#--------------------------
class AnalizadorSemantico:
    def __init__(self):
        self.tabla_simbolos = {}

    def agregar_variable(self, nombre, tipo):
        self.tabla_simbolos[nombre] = tipo

    def verificar_tipo(self, expresion):
        partes = expresion.split()
        tipo = None
        for parte in partes:
            if parte.isdigit():
                if tipo is None:
                    tipo = 'ENTERO'
                elif tipo != 'ENTERO':
                    print("Error semántico: La expresión contiene tipos inconsistentes.")
                    return False
            elif parte in self.tabla_simbolos:
                tipo_variable = self.tabla_simbolos[parte]
                if tipo is None:
                    tipo = tipo_variable
                elif tipo != tipo_variable:
                    print("Error semántico: La expresión contiene tipos inconsistentes.")
                    return False
            elif parte in ('+', '-', '*', '/'):
                continue
            else:
                print("Error semántico: La expresión contiene un identificador no declarado.")
                return False
        return True

# Ejemplo de uso
analizador = AnalizadorSemantico()

# Declarar variables
analizador.agregar_variable('a', 'ENTERO')
analizador.agregar_variable('b', 'ENTERO')
analizador.agregar_variable('c', 'REAL')

# Verificar expresiones
expresion1 = "a + b"
expresion2 = "a * c"
expresion3 = "a + c"

print("Verificación de expresiones:")
print("Expresión 1:", analizador.verificar_tipo(expresion1))
print("Expresión 2:", analizador.verificar_tipo(expresion2))
print("Expresión 3:", analizador.verificar_tipo(expresion3))
