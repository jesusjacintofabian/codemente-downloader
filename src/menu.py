def mostrar_menu():
    print("=" * 40)
    print("      Codemente Downloader")
    print("          v0.1.0-beta")
    print("=" * 40)

    print("\n1. Descargar video")
    print("2. Descargar audio")
    print("3. Descargar playlist")
    print("4. Elegir resolución")
    print("5. Mostrar progreso")
    print("6. Salir")
    
    opcion=input("Seleccione una opcion : ")
    return opcion

if __name__ == "__main__":
    mostrar_menu()

