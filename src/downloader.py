import yt_dlp


def formatear_duracion(segundos):
    minutos, segundos = divmod(segundos, 60)

    horas, minutos = divmod(minutos, 60)

    if horas > 0:
        return f"{horas:02d}:{minutos:02d}:{segundos:02d}"

    return f"{minutos:02d}:{segundos:02d}"


def mostrar_progreso(d):
    if d["status"] == "downloading":
        porcentaje = d.get("_percent_str", "N/A")
        velocidad = d.get("_speed_str", "N/A")
        eta = d.get("_eta_str", "N/A")

        print(
            f"\r[PROGRESO] {porcentaje} | "
            f"Velocidad: {velocidad} | "
            f"Tiempo restante: {eta}",
            end=""
        )

    elif d["status"] == "finished":
        print("\n[INFO] Procesando archivo...")


def seleccionar_resolucion():
    print("\nSelecciona la resolución:")
    print("1. 360p")
    print("2. 720p")
    print("3. 1080p")

    opcion = input("\nSeleccione una resolución: ").strip()

    resoluciones = {
        "1": 360,
        "2": 720,
        "3": 1080
    }

    return resoluciones.get(opcion)


def descargar_video():
    url = input("\nIntroduce la URL del video: ").strip()

    if not url:
        print("\n[ERROR] La URL no puede estar vacía.")
        return

    resolucion = seleccionar_resolucion()

    if resolucion is None:
        print("\n[ERROR] Resolución no válida.")
        return

    opciones = {
        "format": f"best[height<={resolucion}]/best",
        "outtmpl": "downloads/Videos/%(title)s.%(ext)s",
        "noplaylist": True,
        "progress_hooks": [mostrar_progreso]
    }

    try:
        with yt_dlp.YoutubeDL(opciones) as ydl:
            info = ydl.extract_info(url, download=False)

            duracion = info.get("duration") or 0

            print(f"\nTítulo: {info.get('title')}")
            print(f"Duración: {formatear_duracion(duracion)}")
            print(f"Resolución máxima seleccionada: {resolucion}p")

            ydl.download([url])

        print("\n[OK] Video descargado correctamente.")

    except Exception as error:
        print("\n[ERROR] No se pudo descargar el video.")
        print(f"Detalles: {error}")


def descargar_audio():
    url = input("\nIntroduce la URL del video: ").strip()

    if not url:
        print("\n[ERROR] La URL no puede estar vacía.")
        return

    opciones = {
        "format": "bestaudio/best",
        "outtmpl": "downloads/Audio/%(title)s.%(ext)s",
        "noplaylist": True,
        "progress_hooks": [mostrar_progreso],
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
    }

    try:
        with yt_dlp.YoutubeDL(opciones) as ydl:
            info = ydl.extract_info(url, download=False)

            duracion = info.get("duration") or 0

            print(f"\nTítulo: {info.get('title')}")
            print(f"Duración: {formatear_duracion(duracion)}")

            ydl.download([url])

        print("\n[OK] Audio descargado correctamente.")

    except Exception as error:
        print("\n[ERROR] No se pudo descargar el audio.")
        print(f"Detalles: {error}")


def descargar_playlist():
    url = input("\nIntroduce la URL de la playlist: ").strip()

    if not url:
        print("\n[ERROR] La URL no puede estar vacía.")
        return

    opciones = {
        "format": "best[ext=mp4]/best",
        "outtmpl": (
            "downloads/Playlists/"
            "%(playlist_title)s/"
            "%(playlist_index)s - %(title)s.%(ext)s"
        ),
        "noplaylist": False,
        "progress_hooks": [mostrar_progreso]
    }

    try:
        with yt_dlp.YoutubeDL(opciones) as ydl:
            ydl.download([url])

        print("\n[OK] Playlist descargada correctamente.")

    except Exception as error:
        print("\n[ERROR] No se pudo descargar la playlist.")
        print(f"Detalles: {error}")