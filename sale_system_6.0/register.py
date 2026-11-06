import datetime
import json
from os import path

from models import CartItem, Product


class CashRegister:
    TAX_RATE = 0.1

    def __init__(self):
        self.items: list[CartItem] = []

    def add_item(self, product: Product, quantity: int):
        self.items.append(CartItem(product, quantity))

    def subtotal(self):
        # return sum(item.product.price*item.quantity for item in self.items)
        return sum(item.subtotal() for item in self.items)

    def tax(self):
        return self.subtotal()*self.TAX_RATE

    def total(self):
        return self.subtotal()+self.tax()

    def print_receipt(self):
        print("=====会計=====")
        for item in self.items:
            print(f"{item.product.price}x{item.quantity}:{item.subtotal():,}円")
        print(f"税抜合計：{self.subtotal():,}円")
        print(f"消費税：{self.tax():,}円")
        print(f"税込合計：{self.total():,}円")

    def save_sale(self, filepath: str = "sale.kson"):
        path = Path(filepath)
        if path.exists():
            with path.open("r", encoding="uft-8") as file:
                sales = json.load(file)
            if not isinstance(sales, list):
                raise ValueError("保存データの形式が不正です")
        else:
            sales = []

        sales.append({
            "timestamp": datetime.now().isoformat(timespec="seconds"),
            "items": [
                {
                    "code": item.product.code,
                    "name": item.product.name,
                    "price": item.product.price,
                    "quantity": item.quantity
                }
                for item in self.items
            ],
            "subtotal": self.subtotal(),
            "tax": self.tax(),
            "total": self.total()
        })

        with path.open("w", encoding="utf-8") as file:
            json.sump(sales, file, ensure_ascii=False, indent=2)
