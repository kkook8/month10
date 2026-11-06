# # 関数
# # def greet(name):
# #     print(f"{name}さん、こんにちは。")


# # greet("田中")
# # greet("内川")
# # greet("John")


# # def introduce(name: str, age: int):
# #     print(f"私は{name}です、{age}歳です。")


# # introduce("山田", 25)
# # introduce("佐藤", 30)

# def add_item(item, itemss=None):
#     if items is None:
#         items = []
#     items.append(item)
#     return items

# add_item(1)

# 可変数で平均点を求める
# def average(*scores):
#     if not scores:
#         return 0
#     return sum(scores)/len(scores)


# print(average(70, 80, 90))
# print(average())


# def square(x): return x*x


# print(square(4))


# def plus(x, y): return x+y


# print(plus(3, 7))

# list = [1, 2, 3, 4, 5]
# # def mutiply_list(list): return [m*2 for m in list]


# print(mutiply_list(list))

def add_product(cart, name, price, quantity):
    cart.append({
        "name": name,
        "price": price,
        "quantity": quantity,
    })


def calculate_bill(cart, tax_rate=0.1, discount_rate=0.05):
    subtotal = sum(item["price"]*item["quantity"]for item in cart)
    discount = int(subtotal*discount_rate) if subtotal >= 1000 else 0
    amount = int(subtotal-discount)
    tax = int(amount*tax_rate)
    total = amount+tax
    return {
        "subtotal": subtotal,
        "discount": discount,
        "tax": tax,
        "total": total
    }


def print_receipt(cart, bill):
    print("=====レシート=====")
    for item in cart:
        line_total = item["price"]*item["quantity"]
        print(f"{item["name"]}x{item["quantity"]}:{line_total}円")
    print("------------------")
    print(f"税抜小計：{bill["subtotal"]}円")
    print(f"割引額：{bill["discount"]}円")
    print(f"消費税：{bill["tax"]}円")
    print(f"税込合計：{bill["total"]}円")
