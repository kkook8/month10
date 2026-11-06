# print("こんにちは")

# # str int float bool
# system_name1 = "weChat"
# system_name2 = "人事管理システム"

# # print(system_name1)
# # print(system_name2)

# ticket_id = 101
# air_temperature = 36.8

# flag = False

# print(f"system_name1のタイプ：{type(system_name1)}")
# print(f"ticket_idのタイプ:{type(ticket_id)}")
# print(f"air_temperatureのタイプ:{type(air_temperature)}")
# print(f"flagのタイプ:{type(flag)}")


# name = input("お名前を入力してください：")
# print(f"ようこそ、{name}")

# impact_count = int(input("影響人数:"))
# print(f"impact_countタイプ:{type(impact_count)}")

# is_urgent = True
# if is_urgent:
#     print("至急対応してください。")
# else:
#     print("通常の優先度")

# impact_count = 8
# もしimpact_countは10以上、URGENTを印刷する
# もしimpact_countは10以下~5以上、HIGHを印刷する
# もしimpact_countは他の場合、NOEMALを印刷する

# if impact_count >= 10:
#     priority = "URGENT"
# elif impact_count >= 5:
#     priority = "HIGH"
# else:
#     priority = "NOEMAL"
# print(priority)

# 切り捨て除算　// 四捨五入ですか？
# print(13/5)
# print(13//5)

# print(13/0)
# height = float(input("身長を入力してください(cm):"))
# weight = float(input("体重を入力してください(kg):"))

# height_M = height/100
# bmi = weight/height_M**2
# print(f"あなたのBMIは：{bmi:.2f}です。")


# message = "python"
# # ->["p","y","t","h","o","n"] 右からインデックスと左からインデックス
# print(len(message))
# print(message[0])
# print(message[1])
# print(message[2])
# print(message[-1])
# print(message[-2])
# print(message[-3])

# # 文字列操作
# message_show = " Python$Good"
# print(message_show.upper())
# print(message_show.lower())
# print(message_show.strip())
# print(message_show.replace("$", "-"))
# print(message_show.split("$"))

# total = 825
# payment = int(input("お預かり金額："))
# change = payment - total

# if change < 0:
#     print("金額が足りない")
# else:
#     print(f"お支払い金額：{total}円")
#     # print(f"お預かり金額：{payment}円")
#     print(f"お釣り：{change}円")

# age = int(input("年齢を入力してください："))

# if age >= 20:
#     print("成人になった、飲酒でいます。")
# elif age >= 18:
#     print("成人になったが、飲酒でいません。")
# else:
#     print("未成年、飲酒できません。")


# goods_price = 2500
# delivery_pay = 500
# payment = int(input("購入金額を入力してください："))

# if payment < 0:
#     print("負の金額ができない。")
# else:
#     if payment >= 3000:
#         delivery_pay = 0
#         print(f"購入金額:{payment}")
#         print(f"送料:{delivery_pay}円")
#         print(f"お支払い金額:{payment+delivery_pay}円")
#     else:
#         delivery_pay = 500
#         print(f"購入金額:{payment}")
#         print(f"送料:{delivery_pay}円")
#         print(f"お支払い金額:{payment+delivery_pay}円")

# for i in range(5):
#     print(i+1)

# for i in range(1, 6, 2):
#     print(i)

# total = 0
# for i in range(1, 101, 1):
#     total = total + i
# print(total)

# count = 1

# while count <= 5:
#     print(count)
#     count += 1


# for i in range(1, 11):
#     if i == 6:
#         break
#     print(i)

# for i in range(1, 11):
#     if i == 6:
#         continue
#     print(i)

# while True:
#     command = input("終了する場合はqを入力:")
#     if command.lower() == "q":
#         print("終了します。")
#         break
#     print("続きます。")

# passwprd = "123"

# for i in range(3):
#     enter = input("パスワードを入力してください：")
#     if enter == passwprd:
#         print("正しくパスワードを入力しました。")
#         break
#     else:
#         print("間違っているパスワードを入力しまいました。")
#         print("もう一回入力してください(上限3回)。")
# else:
#     print("上限に達しました。")

# for dan in range(1, 10):
#     for number in range(1, 10):
#         print(f"{dan}x{number}={dan*number}", end=" ")
#     print()

# for dan in range(1, 10):
#     for number in range(1, dan+1):
#         print(f"{dan}x{number}={dan*number}", end=" ")
#     print()

# import random

# target = random.randint(1, 100)
# attempts = 0

# print("1~100の数字を当ててください!")


# while True:
#     answer_text = input("予想した数字(qで終了):")

#     if answer_text.lower() == "q":
#         print(f"ゲームを終了します。正解は{target}でした。")
#         break
#     try:
#         answer = int(answer_text)
#     except ValueError:
#         print("整数を入力してください")
#         continue

#     if not 1 <= answer <= 100:
#         print("1~100の範囲で入力してください")
#         continue

#     attempts += 1

#     if answer < target:
#         print("入力した数字は小さいです。")
#     elif answer > target:
#         print("入力した数字は大きいです。")
#     else:
#         print(f"正解!{attempts}回で当てました。")
#         break

# print("=====簡易レジシステム v2=====")

# total = 0
# item_count = 0

# while True:
#     product_name = input("商品名(qで会計):").strip()

#     if product_name == "q":
#         print("レジ退出しました。")
#         break
#     if product_name == " ":
#         print("商品名を入力してください。")
#         continue

#     price_text = input("単価:")
#     quantity_text = input("数量:")

#     if not price_text.isdecimal() or not quantity_text.isdecimal():
#         print("単価と数量は正の数値で入力してください")
#         continue

#     price = int(price_text)
#     quantity = int(quantity_text)

#     if price <= 0 or quantity <= 0:
#         print("単価の数量は１以上で入力してください。")
#         continue

#     item_total = price*quantity
#     total += item_total
#     item_count = item_count+1

#     print(f"小計:{item_total}")

# if item_count == 0:
#     print("商品は登録しないため、会計終了しました。")

#     discount = total*0.1 if total > 5000 else 0
#     after_discount = total-discount
#     tax = after_discount*0.1
#     all_total = total+tax

#     print(f"税抜合計:{total}")
#     print(f"割引:{discount}")
#     print(f"消費税:{tax}")
#     print(f"お支払い金額:{all_total}")

#     while True:
#         payment_text = input("お預かり金額:")

#         if not payment_text.isdecimal():
#             print("0以上の整数を入力してください")
#             continue

#         payment = int(payment_text)

#         if payment < all_total:
#             print(f"不足している。あと{all_total-payment}円が必要です。")
#             continue

#         print(f"お釣り:{payment-all_total}")
#         print("ありがとうございました。")
#         break
