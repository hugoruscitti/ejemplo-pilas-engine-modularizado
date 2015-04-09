import pilasengine
import escena_menu
import escena_juego
import actores

pilas = pilasengine.iniciar()
pilas.reiniciar_si_cambia(__file__)


pilas.escenas.vincular(escena_menu.EscenaMenu)
pilas.escenas.vincular(escena_juego.EscenaJuego)

pilas.actores.vincular(actores.gallina.Gallina)

pilas.escenas.EscenaMenu()


pilas.ejecutar()
