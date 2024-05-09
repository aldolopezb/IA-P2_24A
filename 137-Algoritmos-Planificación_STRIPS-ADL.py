#Aldo López Barrios
#21310106
#--------------------------
(define (domain robot)
    (:requirements :strips :typing)
    (:types location)
    (:predicates
        (at ?loc - location)
        (robot-at ?loc - location)
        (connected ?loc1 - location ?loc2 - location)
        (free ?loc - location)
    )
    (:action move
        :parameters (?from - location ?to - location)
        :precondition (and (at ?from) (free ?to) (connected ?from ?to))
        :effect (and (not (at ?from)) (at ?to) (not (free ?to)) (free ?from))
    )
)

(define (problem robot-transport)
    (:domain robot)
    (:objects room1 room2 - location)
    (:init
        (at room1)
        (free room1)
        (free room2)
        (connected room1 room2)
        (connected room2 room1)
    )
    (:goal (at room2))
)

from pddlpy import DomainProblem

# Cargar el dominio y el problema desde archivos
with open("domain.pddl", "r") as f:
    domain_pddl = f.read()

with open("problem.pddl", "r") as f:
    problem_pddl = f.read()

# Crear el problema y resolverlo
pddl = DomainProblem(domain_pddl, problem_pddl)
solution = pddl.solve()

if solution:
    print("Planificación exitosa:")
    for action in solution:
        print(action)
else:
    print("No se encontró solución.")
