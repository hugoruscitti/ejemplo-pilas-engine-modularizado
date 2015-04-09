import pilasengine

class Gallina(pilasengine.actores.Actor):

    def iniciar(self):
        self.imagenes = [
            self.pilas.imagenes.cargar('data/juego/gallina_1.png'),
            self.pilas.imagenes.cargar('data/juego/gallina_2.png'),
            self.pilas.imagenes.cargar('data/juego/gallina_3.png'),
        ]
        self.imagen = self.imagenes[0]

    def actualizar(self):
        pass
