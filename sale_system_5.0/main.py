from datetime import datetime
import json
import logging
from pathlib import Path
from register import calculate_total
from storage import load_sales, save_sales

BASE_DIR = Path(__file__).resolve().parent

LOG_DIR = BASE_DIR/"logs"
LOG_DIR.mkdir(exist_ok=True)

logging.basicConfig(
    filename=LOG_DIR/"register.log",
    level=logging.INFO,
    encoding="utf-8",
    format="%(asctime)s %(levelname)s %(message)s"
)


def read_non_negative_integer(message: str):
    while True:
        try:
            value = int(input(message))
            if value < 0:
                raise ValueError("0以上の値が必要です。")
            return value
        except ValueError:
            print("0以上の整数を入力してください。")


def create_sale():
    items = []
    while True:
        name = input("商品名(修了は'q'を押す：)").strip()
        if name == "q":
            break

        price = read_non_negative_integer("単価：")
        quantity = read_non_negative_integer("数量：")

        if quantity == 0 or price == 0:
            print("数量又は価格0の商品は登録しません。")
            continue
        items.append({"name": name, "price": price, "quantity": quantity})

    if not items:
        print("商品が登録されていません。")
        return

    amounts = calculate_total(items)
    print(f"税抜：{amounts["subtotal"]:,}円")
    print(f"消費税：{amounts["tax"]:,}円")
    print(f"税込：{amounts["total"]:,}円")

    sale = {"timestamp": datetime.now().isoformat(timespec="seconds"),
            "items": items,
            **amounts,
            }
    try:
        history = load_sales()
        history.append(sale)
        save_sales(history)
    except (OSError, json.JSONDecodeError, ValueError) as error:
        logging.exception("購入履歴の保存失敗しました。")
        print(f"保存できませんでした：{error}")

    logging.info(f"購入履歴を保存、合計=%s", amounts["total"])
    print("購入履歴を保存しました。")


def show_history():
    try:
        history = load_sales()
    except (OSError, json.JSONDecodeError, ValueError) as error:
        logging.exception("購入履歴の保存失敗しました。")
        print(f"保存できませんでした：{error}")
        return
    if not history:
        print("購入履歴はありません。")
        return

    for index, sale in enumerate(history, start=1):

        print(
            f"{index}.税抜{sale["subtotal"]}、消費税{sale["tax"]}、{sale["total"]:,}円")


def main():
    while True:
        print("\n======レジシステム Version 5.0 ======")
        print("1.新しい会計")
        print("2.購入履歴")
        print("0.終了")
        choice = input("以上の番号を選択：")

        if (choice == "1"):
            create_sale()
        elif (choice == "2"):
            show_history()
        elif (choice == "0"):
            print("終了します。")
            break
        else:
            print("0,1,2のいずれかを入力してください。")


if __name__ == "__main__":
    main()
