#historial de conversiones

historial_lista = []


def agregar_registro(entrada: str, origen: str, destino: str, resultado: str):
    #Agrega un registro valido al historial
    historial_lista.append({
        "entrada": entrada,
        "origen": origen,
        "destino": destino,
        "resultado": resultado
    })


def obtener_historial() -> list[dict]:
    #devueleve la lista del historial
    return historial_lista


def eliminar_registro(indice: int):
    #Elimina un registro del historial
    if 0 <= indice < len(historial_lista):
        historial_lista.pop(indice)


def vaciar_historial():
    #Limpia todo el historial
    historial_lista.clear()