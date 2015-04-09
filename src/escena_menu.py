import pilasengine

class EscenaMenu(pilasengine.escenas.Escena):

    def iniciar(self):
        # Cargando el fondo
        self.pilas.fondos.Fondo("data/menu/fondo.png")
        # Creacion del titulo principal
        self.titulo = self.pilas.actores.Actor()
        self.titulo.imagen = "data/menu/titulo.png"
        self.titulo.escala = [0.5]
        self.titulo.x = [-150]
        self.titulo.y = [120]
        self.menu = self.pilas.actores.Menu([
            ('iniciar juego', self.iniciar_juego),
            ('salir', self.salir_del_juego)
        ])

    def iniciar_juego(self):
        self.pilas.escenas.EscenaJuego()

    def salir_del_juego(self):
        import sys
        sys.exit(0)
