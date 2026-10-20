"""
Módulo del Modo de Práctica con ejercicios aleatorios entre 0 y 255.
"""

import random
from validaciones import BASES
from conversiones import realizar_conversion

aciertos = 0
respondidos = 0


def obtener_estadisticas() -> tuple[int, int, float]:
    """Retorna los aciertos, ejercicios respondidos y el porcentaje."""
    porcentaje = (aciertos / respondidos * 100) if respondidos > 0 else 0.0
    return aciertos, respondidos, porcentaje


def reiniciar_estadisticas():
    """Reinicia la puntuación del modo práctica."""
    global aciertos, respondidos
    aciertos = 0
    respondidos = 0


def generar_ejercicio() -> tuple[str, str, str, str]:
    """Genera un ejercicio aleatorio con su valor de origen, origen, destino y respuesta esperada."""
    num_decimal = random.randint(0, 255)
    nombres_bases = list(BASES.keys())
    origen = random.choice(nombres_bases)
    destino = random.choice([b for b in nombres_bases if b != origen])

    if origen == "Decimal":
        val_origen = str(num_decimal)
    else:
        val_origen, _ = realizar_conversion(str(num_decimal), "Decimal", origen)

    respuesta_esperada, _ = realizar_conversion(val_origen, origen, destino)

    return val_origen, origen, destino, respuesta_esperada


def registrar_respuesta(es_correcta: bool):
    """Suma al contador de respuestas de la sesión."""
    global aciertos, respondidos
    respondidos += 1
    if es_correcta:
        aciertos += 1