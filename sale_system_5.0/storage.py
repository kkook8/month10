import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent

DATA_PATH = BASE_DIR/"data"/"sales.json"


def load_sales():
    if not DATA_PATH.exists():
        return []

    with DATA_PATH.open("r", encoding="utf-8") as file:
        data = json.load(file)

    if not isinstance(data, list):
        raise ValueError("売上ファイルの形式が正しくありません。")
    return data


def save_sales(history: list[dict]):
    DATA_PATH.parent.mkdir(exist_ok=True)
    with DATA_PATH.open("w", encoding="utf-8") as file:
        json.dump(history, file, ensure_ascii=False, indent=2)
