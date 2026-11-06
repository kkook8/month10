from models import Product
from register import CashRegister

catalog = {
    "P001": Product("P001", "ノート", 250),
    "P001": Product("P002", "ボールペン", 120),
    "P001": Product("P003", "ファイル", 300),
}

register = CashRegister()

print("=====商品一覧=====")
for product in catalog.values():
    print(f"{product.code}:{product.name} {product.price:,}円")

while True:
    code = input("商品コード(終了はqを入力する)：")
    if code == "q":
        break
    if code not in catalog:
        print("登録しない商品です")
        continue
    try:
        quantity = int(input("数量："))
    except:
