import pandas as pd
import numpy as np
import random
import venv

def asignment(personas):
    # Diccionario para almacenar las asignaciones
    asignacion = {}

    # Convertir las claves del diccionario a una lista y mezclarla
    nombres_rand = list(personas.keys())
    random.shuffle(nombres_rand)

    # Asignar a cada persona otra persona aleatoria
    for persona_a in personas.keys():
        n=len(nombres_rand)
        persona_b = nombres_rand[n-1]
        while (persona_b == persona_a):
            random.shuffle(nombres_rand)
            persona_b = nombres_rand[n-1]
        asignacion[persona_a] = persona_b
        nombres_rand.remove(persona_b)
        print(f'A {persona_a} le toca {persona_b}')
    
if __name__ == "__main__":
    #esto solo se ejecutará cuando llame la función desde la terminal
    personas = {
        'Josué Rivera': 'jjared.ro@gmail.com',
        'Iván Rivera': 'asdfasdfgasdfgh4@gmail.com',
        'Rafael Rivera': 'rafaelriveralopez@gmail.com',
        'Diego Rivera': 'diero.rivera@ciencias.com'
    }
    asignacion_personas(personas)