"""
Módulo para la gestión del historial de conversiones mediante listas en memoria.
"""

historial_lista = []


def agregar_registro(entrada: str, origen: str, destino: str, resultado: str):
    """Agrega un registro válido al historial."""
    historial_lista.append({
        "entrada": entrada,
        "origen": origen,
        "destino": destino,
        "resultado": resultado
    })


def obtener_historial() -> list[dict]:
    """Retorna la lista completa del historial."""
    return historial_lista


def eliminar_registro(indice: int):
    """Elimina un registro del historial según el índice base cero."""
    if 0 <= indice < len(historial_lista):
        historial_lista.pop(indice)


def vaciar_historial():
    """Limpia todo el historial de la sesión."""
    historial_lista.clear()