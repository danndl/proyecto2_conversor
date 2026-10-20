from consola import iniciar_programa

if __name__ == "__main__":
    try:
        iniciar_programa()
    except (KeyboardInterrupt, EOFError):
        print("\nPrograma finalizado.")