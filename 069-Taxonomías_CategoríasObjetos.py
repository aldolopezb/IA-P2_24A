#Aldo López Barrios
#21310106
#--------------------------
class Categoria:
    def __init__(self, nombre, subcategorias=None):
        self.nombre = nombre
        self.subcategorias = subcategorias if subcategorias else []

    def agregar_subcategoria(self, subcategoria):
        self.subcategorias.append(subcategoria)


# Crear la taxonomía
animalia = Categoria("Animalia")
vertebrados = Categoria("Vertebrados")
invertebrados = Categoria("Invertebrados")
mamiferos = Categoria("Mamíferos")
aves = Categoria("Aves")
reptiles = Categoria("Reptiles")
anfibios = Categoria("Anfibios")
peces = Categoria("Peces")
artropodos = Categoria("Artrópodos")
moluscos = Categoria("Moluscos")

# Agregar subcategorías
animalia.agregar_subcategoria(vertebrados)
animalia.agregar_subcategoria(invertebrados)
vertebrados.agregar_subcategoria(mamiferos)
vertebrados.agregar_subcategoria(aves)
vertebrados.agregar_subcategoria(reptiles)
vertebrados.agregar_subcategoria(anfibios)
vertebrados.agregar_subcategoria(peces)
invertebrados.agregar_subcategoria(artropodos)
invertebrados.agregar_subcategoria(moluscos)

# Mostrar la taxonomía
def mostrar_taxonomia(categoria, nivel=0):
    print("  " * nivel + categoria.nombre)
    for subcategoria in categoria.subcategorias:
        mostrar_taxonomia(subcategoria, nivel + 1)

mostrar_taxonomia(animalia)
