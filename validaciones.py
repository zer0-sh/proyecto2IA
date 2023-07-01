# Función para validar si un movimiento es válido para una pieza específica
def validar_movimiento(pieza, fila_origen, columna_origen, fila_destino, columna_destino, tablero):
    # Implementa la lógica de validación para cada tipo de pieza
    # Retorna True si el movimiento es válido, False en caso contrario
    if pieza.lower() == 'p':
        return validar_movimiento_peon(fila_origen, columna_origen, fila_destino, columna_destino, tablero)
    elif pieza.lower() == 'r':
        return validar_movimiento_torre(fila_origen, columna_origen, fila_destino, columna_destino, tablero)
    elif pieza.lower() == 'n':
        return validar_movimiento_caballo(fila_origen, columna_origen, fila_destino, columna_destino, tablero)
    elif pieza.lower() == 'b':
        return validar_movimiento_alfil(fila_origen, columna_origen, fila_destino, columna_destino, tablero)
    elif pieza.lower() == 'q':
        return validar_movimiento_reina(fila_origen, columna_origen, fila_destino, columna_destino, tablero)
    elif pieza.lower() == 'k':
        return validar_movimiento_rey(fila_origen, columna_origen, fila_destino, columna_destino, tablero)
    else:
        return False

# Función para validar el movimiento de un peón
def validar_movimiento_peon(fila_origen, columna_origen, fila_destino, columna_destino, tablero):
    # Movimiento hacia adelante
    if columna_origen == columna_destino:
        if tablero[fila_destino][columna_destino] == "":
            dif_filas = fila_destino - fila_origen
            if dif_filas == 1:
                return True
            elif dif_filas == 2 and fila_origen == 1:
                return True
        else:
            return False

    # Movimiento de captura en diagonal
    if abs(columna_destino - columna_origen) == 1 and fila_destino - fila_origen == 1:
        if tablero[fila_destino][columna_destino] != "":
            return True

    return False

# Función para validar el movimiento de una torre
def validar_movimiento_torre(fila_origen, columna_origen, fila_destino, columna_destino, tablero):
    # Movimiento vertical
    if columna_origen == columna_destino:
        inicio_fila = min(fila_origen, fila_destino) + 1
        fin_fila = max(fila_origen, fila_destino)
        for fila in range(inicio_fila, fin_fila):
            if tablero[fila][columna_origen] != "":
                return False
        return True

    # Movimiento horizontal
    if fila_origen == fila_destino:
        inicio_columna = min(columna_origen, columna_destino) + 1
        fin_columna = max(columna_origen, columna_destino)
        for columna in range(inicio_columna, fin_columna):
            if tablero[fila_origen][columna] != "":
                return False
        return True

    return False

# Función para validar el movimiento de un caballo
def validar_movimiento_caballo(fila_origen, columna_origen, fila_destino, columna_destino, tablero):
    dif_filas = abs(fila_destino - fila_origen)
    dif_columnas = abs(columna_destino - columna_origen)
    return (dif_filas == 2 and dif_columnas == 1) or (dif_filas == 1 and dif_columnas == 2)

# Función para validar el movimiento de un alfil
def validar_movimiento_alfil(fila_origen, columna_origen, fila_destino, columna_destino, tablero):
    dif_filas = abs(fila_destino - fila_origen)
    dif_columnas = abs(columna_destino - columna_origen)
    return dif_filas == dif_columnas

# Función para validar el movimiento de una reina
def validar_movimiento_reina(fila_origen, columna_origen, fila_destino, columna_destino, tablero):
    return (
        validar_movimiento_torre(fila_origen, columna_origen, fila_destino, columna_destino, tablero) or
        validar_movimiento_alfil(fila_origen, columna_origen, fila_destino, columna_destino, tablero)
    )

# Función para validar el movimiento de un rey
def validar_movimiento_rey(fila_origen, columna_origen, fila_destino, columna_destino, tablero):
    dif_filas = abs(fila_destino - fila_origen)
    dif_columnas = abs(columna_destino - columna_origen)
    return (dif_filas == 1 and dif_columnas == 0) or (dif_filas == 0 and dif_columnas == 1) or (dif_filas == 1 and dif_columnas == 1)