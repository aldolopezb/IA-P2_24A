from modal_logic_parser import Formula, World, ModalSystem, SystemLabel
from modal_logic_parser.syntax import AtomicProposition

# Definir las fórmulas
p = AtomicProposition('p')
q = AtomicProposition('q')
r = AtomicProposition('r')

# Crear mundos
w1 = World(['p'])
w2 = World(['q'])
w3 = World(['r'])

# Crear sistema modal
system = ModalSystem()

# Definir relaciones entre mundos
system.add_relation(w1, w2, SystemLabel('M'))  # w1 tiene acceso a w2
system.add_relation(w2, w3, SystemLabel('M'))  # w2 tiene acceso a w3

# Crear fórmulas de lógica modal
formula1 = Formula('[]p')  # Necesariamente p
formula2 = Formula('<>r')  # Posiblemente r
formula3 = Formula('[M](p -> q)')  # En todos los mundos accesibles desde este, si p entonces q

# Verificar satisfactibilidad de las fórmulas en un mundo dado
print(system.satisfies(w1, formula1))  # Devuelve True si []p es satisfacible en w1
print(system.satisfies(w1, formula2))  # Devuelve False si <>r no es satisfacible en w1
print(system.satisfies(w1, formula3))  # Devuelve True si [M](p -> q) es satisfacible en w1
