from rdflib import Graph, URIRef, Literal, Namespace
from rdflib.namespace import RDF, RDFS, OWL

# Crear un nuevo grafo RDF
g = Graph()

# Definir los espacios de nombres
my_ontology = Namespace("http://www.ejemplo.com/ontologia#")
g.bind("my_ontology", my_ontology)

# Definir las clases
g.add((my_ontology.Persona, RDF.type, OWL.Class))
g.add((my_ontology.Coche, RDF.type, OWL.Class))

# Definir las propiedades
g.add((my_ontology.tieneNombre, RDF.type, RDF.Property))
g.add((my_ontology.tieneNombre, RDFS.domain, my_ontology.Persona))
g.add((my_ontology.tieneNombre, RDFS.range, RDFS.Literal))

g.add((my_ontology.tieneEdad, RDF.type, RDF.Property))
g.add((my_ontology.tieneEdad, RDFS.domain, my_ontology.Persona))
g.add((my_ontology.tieneEdad, RDFS.range, RDFS.Literal))

g.add((my_ontology.tieneCoche, RDF.type, RDF.Property))
g.add((my_ontology.tieneCoche, RDFS.domain, my_ontology.Persona))
g.add((my_ontology.tieneCoche, RDFS.range, my_ontology.Coche))

# Agregar instancias
g.add((my_ontology.Juan, RDF.type, my_ontology.Persona))
g.add((my_ontology.Juan, my_ontology.tieneNombre, Literal("Juan")))
g.add((my_ontology.Juan, my_ontology.tieneEdad, Literal(30)))

g.add((my_ontology.Ford, RDF.type, my_ontology.Coche))
g.add((my_ontology.Juan, my_ontology.tieneCoche, my_ontology.Ford))

# Serializar el grafo RDF en formato Turtle
print(g.serialize(format="turtle").decode("utf-8"))
