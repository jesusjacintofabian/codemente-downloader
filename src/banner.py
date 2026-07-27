"""
Banner ASCII para Codemente Downloader.

Requiere:
    pip install wcwidth

Uso:
    from banner import mostrar_banner
    mostrar_banner()
"""
from wcwidth import wcswidth

# Colores ANSI
AZUL = "\033[94m"
VERDE = "\033[92m"
AMARILLO = "\033[93m"
CIAN = "\033[96m"
RESET = "\033[0m"
NEGRITA = "\033[1m"

TITULO_CODEMENTE = r""" █▀▀ █▀█ █▀▄ █▀▀ █▀▄▀█ █▀▀ █▄░█ ▀█▀ █▀▀
 █▄▄ █▄█ █▄▀ ██▄ █░▀░█ ██▄ █░▀█ ░█░ ██▄ """

TITULO_DOWNLOADER = r""" █▀▄ █▀█ █░█░█ █▄░█ █░░ █▀█ █▀█ █▀▄ █▀▀ █▀█
 █▄▀ █▄█ ▀▄▀▄▀ █░▀█ █▄▄ █▄█ █▀▄ █▄▀ ██▄ █▀▄ """

ANCHO = 66  # ancho interior del marco


def _centrar(linea, ancho=ANCHO):
    """Centra respetando el ancho visual real (los emojis ocupan 2 columnas)."""
    pad = ancho - wcswidth(linea)
    izq = pad // 2
    der = pad - izq
    return " " * izq + linea + " " * der


def _fila(texto="", color=""):
    contenido = _centrar(texto)
    if color:
        return f"║{color}{contenido}{RESET}║"
    return f"║{contenido}║"


def mostrar_banner():
    """Imprime el banner completo, con marco y estado de los módulos."""
    top = "╔" + "═" * ANCHO + "╗"
    bottom = "╚" + "═" * ANCHO + "╝"
    vacio = _fila()

    print(CIAN + top + RESET)

    for linea in TITULO_CODEMENTE.split("\n"):
        print(_fila(linea, AZUL))

    print(vacio)

    for linea in TITULO_DOWNLOADER.split("\n"):
        print(_fila(linea, VERDE))

    print(vacio)
    print(_fila("DESCARGA VIDEOS, AUDIOS Y PLAYLISTS DE YOUTUBE", VERDE))
    print(vacio)

    print(_fila("┌───────────────┐ ┌───────────────┐ ┌───────────────┐", CIAN))
    print(_fila("│   🎬 VIDEO    │ │   🎵 AUDIO    │ │  📂 PLAYLIST  │", CIAN))
    print(_fila("│    READY      │ │    READY      │ │    READY      │", CIAN))
    print(_fila("└───────────────┘ └───────────────┘ └───────────────┘", CIAN))

    print(vacio)
    print(_fila("⚡ RAPIDO    ✓ SENCILLO    ◆ POTENTE", AMARILLO))
    print(vacio)
    print(_fila("VERSION 0.1.0-BETA", NEGRITA + AZUL))

    print(CIAN + bottom + RESET)


if __name__ == "__main__":
    mostrar_banner()