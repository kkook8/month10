from phase4 import add_product, calculate_bill, print_receipt

# print(plus(3, 11))

cart = []
while True:
    name = input("商品名(終了する場合はq)：").strip()
    if name == "q":
        break
    try:
        price = int(input("単価（円）："))

        if price <= 0:
            print("単価は１以上で入力してください。")
            continue

        quantity = int(input("数量："))

        if quantity <= 0:
            print("数量は１以上で入力してください。")
            continue

    except ValueError:
        print("単位と数量は整数を入力してください。")
        continue

    if price <= 0:
        print("単価は１以上で入力してください。")
        continue
    if quantity <= 0:
        print("数量は１以上で入力してください。")
        continue

    add_product(cart, name, price, quantity)
    print("商品を登録しました。")

if not cart:
    print("商品を追加されていません。")

else:
    bill = calculate_bill(cart)
    print_receipt(cart, bill)
