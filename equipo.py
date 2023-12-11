from jugador import *
from entrenador import Entrenador

class Equipo:
    # Metodo constructor
    def __init__(self, nombre, jugadores, entrenador):
        self.nombre = nombre
        self.jugadores = jugadores
        self.entrenador = entrenador

    # Metodo para calcular la valoracion total del equipo

    def valoracion_total(self):
        players = [jugador1, jugador2, jugador3]
        valoracion_jugadores = round(sum(style.habilidad(player) for style in PlayerStyle.all_style() for player in players) / len(players),2)

        if all(jugador.sucio == True for jugador in self.jugadores) or all(jugador.sucio == False for jugador in self.jugadores):
            valoracion_jugadores += 10

        valoracion_final = valoracion_jugadores * self.entrenador.multiplicador_habilidad

        return valoracion_final
    
    # Metodo para verificar si un equipo es un dream team
    def es_dream_team(self):
        valor = any(jugador.es_leyenda() for jugador in self.jugadores)
        if valor:
            print("El equipo PdeP es un dream team")

        else:
            print("El equipo PdeP no es un dream team")
        return ""
    



# Creacion de los jugadores
jugador1 = Jugador("Juan", 180, 60, 30, 60)
jugador2 = Jugador("Aye", 167, 35, 80, 85)
jugador3 = Jugador("Franco", 200, 10, 70, 70, True)

# Creacion del entrenador
entrenador = Entrenador("Felipe", "Scarpa", 25, 1.20)

# Creacion del equipo
equipo_pdep = Equipo("equipo PdeP", [jugador1, jugador2, jugador3], entrenador)

# Impresion de las habilidades de los jugadores

print('\n')
print("**************************************************************")
print("Habilidades de los jugadores")
print("**************************************************************")
print('\n')
print(f"Habilidad de {jugador1.nombre}:", round(Tiradores().habilidad(jugador1),2))
print()
print(f"Habilidad de {jugador2.nombre}:", round(Pasadores().habilidad(jugador2),2))
print()
print(f"Habilidad de {jugador3.nombre}:", round(Reboteadores().habilidad(jugador3),2))
print()


# Impresion de los resultados de entrenamiento de los jugadores

print("**************************************************************")
print("Entrenamiento de los jugadores")
print("**************************************************************")
print('\n')
entrenador.entrenar_jugador(jugador1)
print(f"Nueva eficacia de {jugador1.nombre}: {round(jugador1.eficacia, 2)}")
print(f"Nuevo talento de {jugador1.nombre}: {round(jugador1.talento,2)}")
print()
entrenador.entrenar_jugador(jugador2)
print(f"Nueva eficacia de {jugador2.nombre}: {round(jugador2.eficacia)}")
print(f"Nuevo talento de {jugador2.nombre}: {round(jugador2.talento,2)}")
print()
entrenador.entrenar_jugador(jugador3)
print(f"Nueva eficacia de {jugador3.nombre}: {round(jugador3.eficacia,2)}")
print(f"Nuevo talento de {jugador3.nombre}: {round(jugador3.talento,2)}")
print()
print()

# Impresion de las nuevas habilidades de los jugadores

print('\n')
print("**************************************************************")
print("Nuevas habilidades de los jugadores")
print("**************************************************************")
print('\n')
print(f"Habilidad de {jugador1.nombre}:", round(Tiradores().habilidad(jugador1),2))
print()
print(f"Habilidad de {jugador2.nombre}:", round(Pasadores().habilidad(jugador2),2))
print()
print(f"Habilidad de {jugador3.nombre}:", round(Reboteadores().habilidad(jugador3),2))
print()

# Impresion de la verificacion de si un jugador es crack o no

print("**************************************************************")
print("Verificacion de cracks")
print("**************************************************************")
print('\n')
print(f"{jugador1.nombre} es una crack" if jugador1.es_crack(Tiradores()) else f"{jugador1.nombre} no es una crack")
print(f"{jugador2.nombre} es una crack" if jugador2.es_crack(Pasadores()) else f"{jugador2.nombre} no es una crack")
print(f"{jugador3.nombre} es una crack" if jugador3.es_crack(Reboteadores()) else f"{jugador3.nombre} no es una crack")
print()

# Impresion de la verificacion de si un jugador es leyenda o no

print("**************************************************************")
print("Verificacion de leyendas")
print("**************************************************************")
print('\n')
print(f"{jugador1.nombre} es una leyenda" if jugador1.es_leyenda() else f"{jugador1.nombre} no es una leyenda")
print(f"{jugador2.nombre} es una leyenda" if jugador2.es_leyenda() else f"{jugador2.nombre} no es una leyenda")
print(f"{jugador3.nombre} es una leyenda" if jugador3.es_leyenda() else f"{jugador3.nombre} no es una leyenda")
print()
print()

# Impresion de la valoracion total de un equipo

print("**************************************************************")
print("Valoracion total del equipo")
print("**************************************************************")
print('\n')
print(f"Valoracion total del equipo PdeP: {(equipo_pdep.valoracion_total())}")
print()

# Impresion de la verificacion de si un equipo es o no un dream team

print("**************************************************************")
print("Verificacion de dream teams")
print("**************************************************************")
print('\n')
print(f"{equipo_pdep.es_dream_team()}")
print()
