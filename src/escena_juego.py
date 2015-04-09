import pilasengine
from actores import gallina

class EscenaJuego(pilasengine.escenas.Escena):

    def iniciar(self):
        self.pilas.avisar("Pulsa ESC para regresar al menu")
        self.gallina = self.pilas.actores.Gallina()
        self.pilas.eventos.pulsa_tecla_escape.conectar(self.regresar)

    def ejecutar(self):
        pass

    def regresar(self, evento):
        self.pilas.escenas.EscenaMenu()
