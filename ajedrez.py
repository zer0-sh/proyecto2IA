import pygame
import validaciones as val

# Inicialización de Pygame
pygame.init()

# Dimensiones de la ventana
ANCHO_VENTANA = 600
ALTO_VENTANA = 600

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AZUL = (0, 0, 255)

# Tamaño de cada cuadro del tablero
TAM_CUADRO = 75

# Tamaño deseado para las imágenes de las piezas
TAM_PIEZA = (30, 30)

# Inicialización de la ventana
ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Ajedrez")

# Función para dibujar el tablero de ajedrez
def dibujar_tablero():
    for fila in range(8):
        for columna in range(8):
            color = BLANCO if (fila + columna) % 2 == 0 else NEGRO
            pygame.draw.rect(ventana, color, (columna * TAM_CUADRO, fila * TAM_CUADRO, TAM_CUADRO, TAM_CUADRO))

# Función principal del juego
def jugar_ajedrez():
    # Posición inicial del tablero
    tablero = [
        ["r", "n", "b", "q", "k", "b", "n", "r"],
        ["p", "p", "p", "p", "p", "p", "p", "p"],
        ["", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", ""],
        ["P", "P", "P", "P", "P", "P", "P", "P"],
        ["R", "N", "B", "Q", "K", "B", "N", "R"]
    ]

    # Variables para el control del juego
    seleccionado = None
    turno_blanco = True

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                return

            if evento.type == pygame.MOUSEBUTTONDOWN:
                columna = evento.pos[0] // TAM_CUADRO
                fila = evento.pos[1] // TAM_CUADRO
                pieza_seleccionada = tablero[fila][columna]

                if seleccionado is None:
                    if pieza_seleccionada != "":
                        if (turno_blanco and pieza_seleccionada.isupper()) or (not turno_blanco and pieza_seleccionada.islower()):
                            seleccionado = (fila, columna)
                else:
                    fila_seleccionada, columna_seleccionada = seleccionado
                    if mover_pieza(fila_seleccionada, columna_seleccionada, fila, columna, tablero):
                        tablero[fila][columna] = tablero[fila_seleccionada][columna_seleccionada]
                        tablero[fila_seleccionada][columna_seleccionada] = ""
                        turno_blanco = not turno_blanco
                    seleccionado = None

        ventana.fill(AZUL)
        dibujar_tablero()

        for fila in range(8):
            for columna in range(8):
                pieza = tablero[fila][columna]
                if pieza != "":
                    if pieza.islower():
                        imagen = pygame.image.load(f"imagenes/{pieza}2.png")
                    else:
                        imagen = pygame.image.load(f"imagenes/{pieza}.png")
                    imagen = pygame.transform.scale(imagen, TAM_PIEZA)
                    ventana.blit(imagen, (columna * TAM_CUADRO, fila * TAM_CUADRO))

        if seleccionado is not None:
            fila, columna = seleccionado
            pygame.draw.rect(ventana, AZUL, (columna * TAM_CUADRO, fila * TAM_CUADRO, TAM_CUADRO, TAM_CUADRO), 3)

        pygame.display.update()

# Función para validar y mover una pieza
def mover_pieza(fila_origen, columna_origen, fila_destino, columna_destino, tablero):
    pieza = tablero[fila_origen][columna_origen]
    if not val.validar_movimiento(pieza, fila_origen, columna_origen, fila_destino, columna_destino, tablero):
        return False

    tablero[fila_destino][columna_destino] = pieza
    tablero[fila_origen][columna_origen] = ""
    return True

# Ejecución del juego
jugar_ajedrez()
