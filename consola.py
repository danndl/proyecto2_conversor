from validaciones import validar_opcion, validar_entrada, validar_indice
from conversiones import realizar_conversion
from historial import agregar_registro, obtener_historial, eliminar_registro, vaciar_historial
import practica

NOMBRES_BASES = {
    "1": "Binario",
    "2": "Octal",
    "3": "Decimal",
    "4": "Hexadecimal"
}


def seleccionar_base(titulo: str) -> str | None:
   #menu selección de bases
    while True:
        print("\n==================================================")
        print(f"{titulo}")
        print("==================================================")
        print("1. Binario")
        print("2. Octal")
        print("3. Decimal")
        print("4. Hexadecimal")
        print("5. Volver al menú principal")

        op = input("Seleccione una opción: ").strip()
        if op == "5":
            return None
        try:
            validar_opcion(op, ["1", "2", "3", "4", "5"])
            return NOMBRES_BASES[op]
        except ValueError as e:
            print(f"\n {e}")


def menu_conversion():
    #la opcion a realizar una conversión.
    origen = seleccionar_base("SELECCIONE LA BASE DE ORIGEN")
    if origen is None:
        return

    destino = seleccionar_base("SELECCIONE LA BASE DE DESTINO")
    if destino is None:
        return

    if origen == destino:
        print("\n Las bases de origen y destino deben ser distintas.")
        return

    print("\n==================================================")
    print(f"CONVERSIÓN: {origen.upper()} A {destino.upper()}")
    print("==================================================")
    print("Ingrese un entero no negativo de hasta 128 dígitos.")


    while True:
        num_str = input("Número a convertir: ").strip()
        if num_str.lower() == "volver":
            return
        try:
            num_validado = validar_entrada(num_str, origen, destino)
            resultado, pasos = realizar_conversion(num_validado, origen, destino)

            print("\n==================================================")
            print("RESULTADO")
            print("==================================================")
            print(f"Número ingresado: {num_validado}")
            print(f"Base de origen: {origen}")
            print(f"Base de destino: {destino}")
            print(f"Resultado: {resultado}")

            print("\nPROCEDIMIENTO PASO A PASO")
            print("--------------------------------------------------")
            for paso in pasos:
                print(paso)

            agregar_registro(num_validado, origen, destino, resultado)
            print("\nConversión agregada al historial.")
            input("\nPresione Enter para continuar...")
            break
        except ValueError as e:
            print(f" {e}\n")


def menu_historial():
    #historial
    while True:
        hist = obtener_historial()
        print("\n==================================================")
        print("HISTORIAL DE CONVERSIONES")
        print("==================================================")
        if not hist:
            print("El historial está vacío.")
        else:
            for idx, reg in enumerate(hist, 1):
                print(f"Registro {idx}")
                print(f"  Entrada:   {reg['entrada']}")
                print(f"  Origen:    {reg['origen']}")
                print(f"  Destino:   {reg['destino']}")
                print(f"  Resultado: {reg['resultado']}\n")
            print(f"Total de registros: {len(hist)}")

        print("\n1. Eliminar un registro")
        print("2. Vaciar historial")
        print("3. Volver al menú principal")

        op = input("Seleccione una opción: ").strip()

        if op == "1":
            if not hist:
                print("\n El historial está vacío.")
                continue
            reg_str = input("Ingrese el número del registro a eliminar: ").strip()
            try:
                idx = validar_indice(reg_str, len(hist))
                eliminar_registro(idx)
                print("\nRegistro eliminado correctamente.")
            except ValueError as e:
                print(f"\n {e}")
        elif op == "2":
            if not hist:
                print("\n El historial está vacío.")
                continue
            vaciar_historial()
            print("\nHistorial vaciado correctamente.")
        elif op == "3":
            break
        else:
            print("\n Opción inválida. Seleccione 1, 2 o 3.")


def menu_practica():
    #modo de practica
    while True:
        aciertos, respondidos, porcentaje = practica.obtener_estadisticas()
        print("\n==================================================")
        print("MODO DE PRÁCTICA")
        print("==================================================")
        print(f"Aciertos: {aciertos}")
        print(f"Ejercicios respondidos: {respondidos}")
        print(f"Porcentaje de aciertos: {porcentaje:.1f}%")
        print("\n1. Resolver un nuevo ejercicio")
        print("2. Reiniciar puntuación")
        print("3. Volver al menú principal")

        op = input("Seleccione una opción: ").strip()

        if op == "1":
            val_origen, origen, destino, resp_esperada = practica.generar_ejercicio()
            print("\n--------------------------------------------------")
            print("EJERCICIO DE PRÁCTICA")
            print("--------------------------------------------------")
            print(f"Convierta {val_origen} de {origen} a {destino}.")
            print("Ingrese únicamente el número de la respuesta.")

            while True:
                resp_usuario = input("Su respuesta: ").strip()
                try:
                    num_validado = validar_entrada(resp_usuario, destino, origen)
                    if num_validado == resp_esperada:
                        print("\n¡Respuesta correcta!")
                        practica.registrar_respuesta(True)
                    else:
                        print(f"\nRespuesta incorrecta. La respuesta esperada era: {resp_esperada}")
                        practica.registrar_respuesta(False)

                    input("\nPresione Enter para continuar...")
                    break
                except ValueError as e:
                    print(f" {e}")
        elif op == "2":
            practica.reiniciar_estadisticas()
            print("\nPuntuación reiniciada.")
        elif op == "3":
            break
        else:
            print("\n Opción inválida.")


def iniciar_programa():
    #menu principal
    while True:
        print("\n==================================================")
        print("CONVERSOR DE SISTEMAS NUMÉRICOS")
        print("==================================================")
        print("1. Realizar una conversión")
        print("2. Consultar el historial")
        print("3. Iniciar el modo de práctica")
        print("4. Salir")

        op = input("Seleccione una opción: ").strip()

        if op == "1":
            menu_conversion()
        elif op == "2":
            menu_historial()
        elif op == "3":
            menu_practica()
        elif op == "4":
            print("\n¡Programa finalizado!")
            break
        else:
            print("\n Opción inválida. Seleccione una opción entre 1 y 4.")