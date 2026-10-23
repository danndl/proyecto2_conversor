#practica con ejercicios random entre 0 y 255

import random
from validaciones import BASES
from conversiones import realizar_conversion

aciertos = 0
respondidos = 0


def obtener_estadisticas() -> tuple[int, int, float]:
    #devueleve los aciertos, ejercicios respondidos y el porcentaje
    porcentaje = (aciertos / respondidos * 100) if respondidos > 0 else 0.0
    return aciertos, respondidos, porcentaje


def reiniciar_estadisticas():
    #reinicia la puntuaci[on del modo prcctica
    global aciertos, respondidos
    aciertos = 0
    respondidos = 0


def generar_ejercicio() -> tuple[str, str, str, str]:
    #genera un ejercicio aleatorio con su valor de origen, destino y la respuesta que le corresponde
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
    #suma al contador de respuestas de la sesion del user
    global aciertos, respondidos
    respondidos += 1
    if es_correcta:
        aciertos += 1