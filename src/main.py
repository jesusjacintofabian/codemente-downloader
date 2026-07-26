# ============================================
# Codemente Downloader
# Version: v0.1.0-beta
# Sprint 2
# ============================================


from menu import mostrar_menu

from downloader import (
    descargar_video,
    descargar_audio,
    descargar_playlist
)


def main():
    while True:
        opcion = mostrar_menu()

        # ============================================
        # Opción 1: Descargar video
        # Estado: IMPLEMENTADO
        # ============================================
        if opcion == "1":
            descargar_video()

        # ============================================
        # Opción 2: Descargar audio MP3
        # Estado: IMPLEMENTADO
        # ============================================
        elif opcion == "2":
            descargar_audio()

        # ============================================
        # Opción 3: Descargar playlist
        # Estado: IMPLEMENTADO
        # ============================================
        elif opcion == "3":
            descargar_playlist()

        # ============================================
        # Opción 4: Elegir resolución
        # Estado: IMPLEMENTADO
        #
        # La resolución se selecciona al iniciar
        # la descarga de un video.
        # ============================================
        elif opcion == "4":
            print(
                "\n[INFO] La resolución se selecciona "
                "al iniciar la descarga del video."
            )

        # ============================================
        # Opción 5: Mostrar progreso
        # Estado: IMPLEMENTADO
        #
        # El progreso aparece automáticamente
        # durante las descargas.
        # ============================================
        elif opcion == "5":
            print(
                "\n[INFO] El progreso se muestra "
                "automáticamente durante la descarga."
            )

        # ============================================
        # Opción 6: Salir
        # Estado: IMPLEMENTADO
        # ============================================
        elif opcion == "6":
            print("\n¡Gracias por usar Codemente Downloader!")
            break

        else:
            print("\n[ERROR] Opción no válida. Inténtalo nuevamente.")


if __name__ == "__main__":
    main()