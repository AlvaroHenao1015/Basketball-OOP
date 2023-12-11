class PlayerStyle:
    def all_style():
        return [Tiradores(), Pasadores(), Reboteadores()]

class Tiradores(PlayerStyle):
    def habilidad(self, player):
        score = (player.eficacia * 2 + (player.inteligencia + player.talento) / 2 + player.altura / 2) / 2
        if player.sucio == False:
            return score
        return score - (score * 15 / 100) 


class Pasadores(PlayerStyle):
    def habilidad(self, player):
        return ((player.inteligencia + player.talento) / 2 + player.altura * 0.80 + player.eficacia * 0.30) / 5


class Reboteadores(PlayerStyle):
    def habilidad(self, player):
        score = (player.eficacia * 2 + (player.inteligencia + player.talento) / 2 + player.altura / 2) / 2
        if player.sucio == False:
            return score
        return score + (score * 20 / 100) 


class Jugador:
    def __init__(self, nombre, altura, eficacia, inteligencia, talento, sucio=False):
        self.nombre = nombre
        self.altura = altura
        self.eficacia = eficacia
        self.inteligencia = inteligencia
        self.talento = talento
        self.sucio = sucio

    def habilidad(self, style):
        return style.habilidad(self)
    
    def entrenar(self):
        self.eficacia *= 1.10
        self.talento *= 1.10

    def es_crack(self, style):
        return self.habilidad(style) >= 90

    def es_leyenda(self):
        for style in PlayerStyle.all_style():
            if not self.es_crack(style):
                return False
        return True

