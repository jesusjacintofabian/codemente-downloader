import yt_dlp

from urllib.parse import urlparse, parse_qs, urlencode, urlunparse

from config import (
    CARPETA_VIDEOS,
    CARPETA_AUDIO,
    CARPETA_PLAYLISTS,
)


def formatear_duracion(segundos):
    minutos, segundos = divmod(segundos, 60)
    horas, minutos = divmod(minutos, 60)

    if horas > 0:
        return f"{horas:02d}:{minutos:02d}:{segundos:02d}"

    return f"{minutos:02d}:{segundos:02d}"


def limpiar_url_video(url):
    """
    Elimina los parámetros de playlist de una URL de video.

    Ejemplo:

    https://www.youtube.com/watch?v=ABC123&list=RDABC123&start_radio=1

    Se convierte en:

    https://www.youtube.com/watch?v=ABC123
    """

    partes = urlparse(url)
    parametros = parse_qs(partes.query)

    video_id = parametros.get("v")

    if not video_id:
        return url

    nueva_query = urlencode({
        "v": video_id[0]
    })

    return urlunparse(
        (
            partes.scheme,
            partes.netloc,
            partes.path,
            partes.params,
            nueva_query,
            "",
        )
    )


def mostrar_progreso(d):
    if d["status"] == "downloading":
        porcentaje = d.get("_percent_str", "N/A")
        velocidad = d.get("_speed_str", "N/A")
        eta = d.get("_eta_str", "N/A")

        print(
            f"\r[PROGRESO] {porcentaje} | "
            f"Velocidad: {velocidad} | "
            f"Tiempo restante: {eta}",
            end="",
        )

    elif d["status"] == "finished":
        print("\n[INFO] Procesando archivo...")


def seleccionar_resolucion():
    print("\nSelecciona la resolución máxima:")
    print("1. 360p")
    print("2. 720p")
    print("3. 1080p")

    opcion = input("\nSeleccione una resolución: ").strip()

    resoluciones = {
        "1": 360,
        "2": 720,
        "3": 1080,
    }

    return resoluciones.get(opcion)


def obtener_resolucion_real(info):
    """
    Obtiene la mayor resolución de video disponible.
    """

    formatos = info.get("formats", [])

    alturas = [
        formato.get("height")
        for formato in formatos
        if formato.get("vcodec") != "none"
        and formato.get("height")
    ]

    if not alturas:
        return None

    return max(alturas)


def descargar_video():
    url = input("\nIntroduce la URL del video: ").strip()

    if not url:
        print("\n[ERROR] La URL no puede estar vacía.")
        return

    # Limpia parámetros como list= y start_radio=
    url = limpiar_url_video(url)

    resolucion = seleccionar_resolucion()

    if resolucion is None:
        print("\n[ERROR] Resolución no válida.")
        return

    opciones = {
        # Busca el mejor video hasta la resolución seleccionada
        # y el mejor audio disponible.
        "format": (
            f"bestvideo[height<={resolucion}]"
            f"+bestaudio/"
            f"best[height<={resolucion}]"
        ),

        "outtmpl": f"{CARPETA_VIDEOS}/%(title)s.%(ext)s",

        # Evita descargar una playlist accidentalmente.
        "noplaylist": True,

        # Combina video + audio en MP4.
        "merge_output_format": "mp4",

        # Muestra progreso.
        "progress_hooks": [mostrar_progreso],
    }

    try:
        with yt_dlp.YoutubeDL(opciones) as ydl:

            info = ydl.extract_info(url, download=False)

            duracion = info.get("duration") or 0
            resolucion_real = obtener_resolucion_real(info)

            print(f"\nTítulo: {info.get('title')}")
            print(f"Duración: {formatear_duracion(duracion)}")
            print(f"Resolución solicitada: {resolucion}p")

            if resolucion_real:
                print(
                    f"Resolución máxima disponible: "
                    f"{resolucion_real}p"
                )

                if resolucion_real < resolucion:
                    print(
                        f"[INFO] El video no tiene {resolucion}p. "
                        f"Se utilizará {resolucion_real}p como máximo."
                    )

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

    # Limpia parámetros como list= y start_radio=
    url = limpiar_url_video(url)

    opciones = {
        "format": "bestaudio/best",

        "outtmpl": f"{CARPETA_AUDIO}/%(title)s.%(ext)s",

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

    # IMPORTANTE:
    # Aquí NO limpiamos la URL porque necesitamos
    # conservar el parámetro list= para descargar
    # la playlist completa.

    opciones = {
        "format": "best[ext=mp4]/best",

        "outtmpl": (
            f"{CARPETA_PLAYLISTS}/"
            "%(playlist_title)s/"
            "%(playlist_index)s - %(title)s.%(ext)s"
        ),

        "noplaylist": False,

        "progress_hooks": [mostrar_progreso],
    }

    try:
        with yt_dlp.YoutubeDL(opciones) as ydl:
            ydl.download([url])

        print("\n[OK] Playlist descargada correctamente.")

    except Exception as error:
        print("\n[ERROR] No se pudo descargar la playlist.")
        print(f"Detalles: {error}")