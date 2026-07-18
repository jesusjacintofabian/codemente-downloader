from menu import mostrar_menu


def main():
  while True:
    opcion = mostrar_menu()
    
    if opcion == "1":
        print("Descarga de video: proximamnente disponible...")

    elif opcion == "2":
        print("Descarga de audio: proximamnente disponible...")         
    elif opcion == "3":
        print("Descarga de playlist: proximamnente disponible...")
    elif opcion == "4":
        print("Elegir resolución: proximamnente disponible...")
    elif opcion == "5":
        print("Mostrar progreso: proximamnente disponible...")
    elif opcion == "6":
        print("Gracias por usar Codemente Downloader. ")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")  
        break

if __name__ == "__main__":
    main()
