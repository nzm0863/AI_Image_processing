from pathlib import Path
import shutil
import sys
import tempfile


def resource_path(relative_path: str) -> Path:
    """
    開発環境 / PyInstaller(EXE) の両方でリソースパスを取得する。
    """
    if getattr(sys, "frozen", False):
        base_path = Path(sys._MEIPASS)
    else:
        base_path = Path(__file__).resolve().parent.parent

    return base_path / relative_path


def get_temp_model(relative_path: str) -> Path:
    """
    日本語パス対策としてモデルを Temp にコピーして返す。
    """
    source = resource_path(relative_path)
    temp_dir = Path(tempfile.gettempdir())
    destination = temp_dir / source.name

    if not destination.exists():
        shutil.copy2(source, destination)

    return destination