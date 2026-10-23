"""
Módulo de Conversiones de Sistemas Numéricos.
Implementa el algoritmo de Notación Posicional y Divisiones Sucesivas.
"""

from validaciones import DIGITOS, BASES


def a_decimal(texto: str, base: int) -> tuple[int, list[str]]:
    """Convierte una cadena validada a un entero decimal"""
    total = 0
    pasos = []

    for posicion, caracter in enumerate(reversed(texto)):
        valor = DIGITOS.index(caracter)
        aporte = valor * (base ** posicion)
        total += aporte

        pasos.append(
            f"{caracter} (valor {valor}) x {base}^{posicion} = {aporte}"
        )

    pasos.append(f"Suma de los aportes: {total}")
    return total, pasos


def desde_decimal(numero: int, base: int) -> tuple[str, list[str]]:
    """Convierte un entero no negativo mediante divisiones sucesivas."""
    if numero == 0:
        return "0", ["El número es cero.", "Su representación en la base de destino es 0."]

    resultado = ""
    pasos = []

    while numero > 0:
        cociente = numero // base
        residuo = numero % base
        simbolo = DIGITOS[residuo]

        pasos.append(
            f"{numero} / {base}: cociente = {cociente}, residuo = {residuo}, dígito = {simbolo}"
        )

        resultado = simbolo + resultado
        numero = cociente

    pasos.append(
        "Leer los residuos del último al primero: " + resultado
    )

    return resultado, pasos


def realizar_conversion(texto: str, origen_nombre: str, destino_nombre: str) -> tuple[str, list[str]]:
    """
    Orquesta las 12 conversiones utilizando Decimal como base intermedia si corresponde.
    """
    base_origen = BASES[origen_nombre]
    base_destino = BASES[destino_nombre]
    pasos = []

    # Origen es Decimal
    if base_origen == 10:
        num_decimal = int(texto)
        resultado, pasos_proc = desde_decimal(num_decimal, base_destino)
        pasos.extend(pasos_proc)
        return resultado, pasos

    # Destino es Decimal
    if base_destino == 10:
        num_decimal, pasos_proc = a_decimal(texto, base_origen)
        pasos.extend(pasos_proc)
        return str(num_decimal), pasos

    #Ambas distintas de decimal
    pasos.append(f"ETAPA 1: {origen_nombre.upper()} A DECIMAL")
    num_decimal, pasos_etapa1 = a_decimal(texto, base_origen)
    pasos.extend(pasos_etapa1)

    pasos.append(f"\nETAPA 2: DECIMAL A {destino_nombre.upper()}")
    resultado, pasos_etapa2 = desde_decimal(num_decimal, base_destino)
    pasos.extend(pasos_etapa2)

    return resultado, pasos