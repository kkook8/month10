# # fruits = ["りんご", "みあん", "バナナ"]
# # # print(fruits[0])
# # # print(fruits[1])
# # # print(fruits[-1])

# # # fruits.pop()
# # # print(fruits)
# # # fruits.append("なし")
# # # print(fruits)

# # # fruits.insert(0, "スイカ")
# # # print(fruits)

# # # print("なし" in fruits)

# # # fruits[0] = "いちご"
# # # print(fruits)
# # # removed = fruits.remove("バナナ")
# # # print(fruits,removed)

# # # 繰り返し処理
# # # prices = [3, 5, 9, 10]
# # # total = 0
# # # for p in prices:
# # #     total = total+p

# # # print(f"合計：{total}")

# # # for f in fruits:
# # #     print(f)

# # # スライスslice
# # # number = [10, 20, 30, 40, 50, 60]
# # # print(number[::-1])

# # # number = [1, 2, 3, 4, 5, 6, 7]
# # # mutiply = [n*2 for n in number]
# # # squares = [n**2 for n in number]
# # # evens = [n for n in number if n % 2 == 0]
# # # odd = [n for n in number if n % 2 == 1]

# # # print(mutiply)
# # # print(squares)
# # # print(evens)
# # # print(odd)

# # # scores = [45, 70, 85, 60, 95]

# # # avg_scores = sum(scores)/len(scores)
# # # max_scores = max(scores)
# # # qualified_scores = [s for s in scores if s >= 60]

# # # print(avg_scores)
# # # print(max_scores)
# # # print(qualified_scores)

# # # student = {"id": 101, "name": "田中", "score": 85}

# # # print(student["name"])
# # # print(student["score"])

# # product = {"name": "ノード", "price": 200}

# # # 追加　Create
# # product["stock"] = 30
# # print(product)

# # # 参照　Read
# # print(product["price"])
# # print(product.get("category", "未設定"))
# # print(product.get("stock", "未設定"))

# # # 更新 updete
# # product["price"] = 220
# # print(product)

# # # 削除 Delete
# # print(product.pop("stock"))
# # print(product)

# # for key in product:
# #     print(key)

# # for value in product.values():
# #     print(value)

# # for k, v in product.items():
# #     print(f"{key},{value}")

# # print("===== 簡易レジシステム Version 3.0 =====")

# # cart = []

# # while True:
# #     name = input("商品名(終了：done)：").strip()

# #     if name.lower() == "done":
# #         break

# #     if name == "":
# #         print("商品名を入力してください。")
# #         continue

# #     try:
# #         price = int(input("単価(円)："))
# #         quantity = int(input("数量："))
# #     except ValueError:
# #         print("単価と数量には整数を入力してください。")
# #         continue

# #     if price <= 0 or quantity <= 0:
# #         print("単価と数量には１以上の整数を入力してください。")
# #         continue

# #     product = {
# #         "name": name,
# #         "price": price,
# #         "quantity": quantity
# #     }
# #     cart.append(product)
# #     print(f"{name}をカードに追加しました。")

# # if not cart:
# #     print("商品が登録されていません。")
# # else:
# #     subtotal = 0
# #     print("\n===== 購入明細 =====")

# #     for index, product in enumerate(cart, start=1):
# #         line_total = product["price"]*product["quantity"]
# #         subtotal += line_total
# #         print(
# #             f"{index}.{product['namme']}"
# #             f"{product['price']:,}円 x {product['quantity']}"
# #             f"= {line_total:,}円"
# #         )

# #     tax = subtotal
# #     total = subtotal + tax

# #     print("--------------------")
# #     print(f"税抜合計：{subtotal:,}円")
# #     print(f"消費税(10%）：{tax:,}円")
# #     print(f"税込合計：{total:,}円")
# #     print(f"ご利用ありがとうございました！")

# cart = [
#     {"name": "ノード", "price": 250, "quantity": 2},
#     {"name": "ペン", "price": 120, "quantity": 3},
#     {"name": "ノード", "price": 250, "quantity": 1},
# ]

# remove_name = input("削除する商品名:").strip()
# original_count = len(cart)
# cart = [product for product in cart if product["name"] != remove_name]

# print(f"削除件数:{original_count - len(cart)}件")
# print("削除後:", cart)
