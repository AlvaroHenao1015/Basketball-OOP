class Entrenador:
    # Metodo constructor
    def __init__(self, nombre, apellido, edad, multiplicador_habilidad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.multiplicador_habilidad = multiplicador_habilidad

    def entrenar_jugador(self, jugador):
        jugador.entrenar()