# ============================================
# Codemente Downloader
# Configuration
# Sprint 3
# ============================================

from pathlib import Path


VERSION = "0.1.0-beta"

CARPETA_VIDEOS = "downloads/Videos"
CARPETA_AUDIO = "downloads/Audio"
CARPETA_PLAYLISTS = "downloads/Playlists"


def crear_carpetas():
    """Crea las carpetas necesarias para las descargas."""

    Path(CARPETA_VIDEOS).mkdir(parents=True, exist_ok=True)
    Path(CARPETA_AUDIO).mkdir(parents=True, exist_ok=True)
    Path(CARPETA_PLAYLISTS).mkdir(parents=True, exist_ok=True)

