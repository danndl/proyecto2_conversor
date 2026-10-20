BASES = {
    "Binario": 2,
    "Octal": 8,
    "Decimal": 10,
    "Hexadecimal": 16
}

DIGITOS = "0123456789ABCDEF"


def validar_numero(texto: str, nombre_base: str) -> str:
    """Valida que el número ingresado cumpla las reglas de la base especificada."""
    if nombre_base not in BASES:
        raise ValueError("La base seleccionada no es válida.")

    if texto == "":
        raise ValueError("Debe ingresar un número.")

    if len(texto) > 128:
        raise ValueError("Se admiten como máximo 128 dígitos.")

    texto = texto.upper()
    permitidos = DIGITOS[:BASES[nombre_base]]

    for caracter in texto:
        if caracter not in permitidos:
            raise ValueError(
                f"Entrada inválida para {nombre_base}.\nCaracteres permitidos: {permitidos}"
            )

    return texto


def validar_entrada(texto: str, origen: str, destino: str) -> str:
    """Valida las bases y el número ingresado para la conversión."""
    if origen not in BASES or destino not in BASES:
        raise ValueError("Seleccione bases válidas.")

    if origen == destino:
        raise ValueError("Las bases de origen y destino deben ser distintas.")

    return validar_numero(texto, origen)


def validar_opcion(texto: str, opciones: list[str]) -> str:
    """Valida que la opción elegida se encuentre en la lista permitida."""
    if texto not in opciones:
        raise ValueError("Opción inválida. Seleccione una de las opciones válidas.")
    return texto


def validar_indice(texto: str, cantidad: int) -> int:
    """Valida el número de registro a eliminar del historial."""
    if cantidad == 0:
        raise ValueError("El historial está vacío.")

    if not texto or any(c not in "0123456789" for c in texto):
        raise ValueError("Ingrese el número del registro.")

    normalizado = texto.lstrip("0") or "0"

    if len(normalizado) > len(str(cantidad)):
        raise ValueError("El registro seleccionado no existe.")

    numero = int(normalizado)

    if numero < 1 or numero > cantidad:
        raise ValueError("El registro seleccionado no existe.")

    return numero - 1