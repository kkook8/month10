# # with open("diary.txt", "w", encoding="utf-8") as file:
# #     file.write("今日はPythonのファイル操作を勉強したした。\n")
# #     file.write("withを使うとファイルを自動で閉じます。\n")
# # print("保存しました。")


# # with open("diary.txt", "r", encoding="utf-8") as file:
# #     content = file.read()

# # print(content)

# # with open("diary.txt", "a", encoding="utf-8") as file:
# #     file.write("明日続けます。\n")

# import json
# import csv
# from pathlib import Path

# base_dir = Path(__file__).resolve().parent
# print(base_dir)

# data_dir = base_dir/"data"

# data_dir.mkdir(exist_ok=True)

# file_path = data_dir/"memo.txt"
# file_path.write_text("パス操作の練習。\n", encoding="utf-8")

# print(file_path.exists())
# print(file_path.read_text(encoding="utf-8"))


# sales = [
#     {"product": "ノート", "quantity": 2, "price": 250},
#     {"product": "ペン", "quantity": 3, "price": 120},
# ]

# with open("D:\\BaiduNetdiskDownload\\pythoncode_10\\data\\sales.csv", "w", newline="", encoding="utf-8-sig") as file:
#     writer = csv.DictWriter(file, fieldnames=["product", "quantity", "price"])
#     writer.writeheader()
#     writer.writerows(sales)

#     print("sales.csvを作成しました。")

#     amount = 0
#     with open("D:\\BaiduNetdiskDownload\\pythoncode_10\\data\\sales.csv", "r", newline="", encoding="utf-8-sig") as file:
#         reader = csv.DictReader(file)
#         for row in reader:
#             amount = amount+int(row["quantity"])*int(row["price"])
#     print(f"税抜売上合計：{amount}円")


# # --

# students = [
#     {"name": "田中", "score": 80},
#     {"name": "佐藤", "score": 90},
#     {"name": "鈴木", "score": 70},
# ]

# total = 0
# row_amount = 0
# with open("students", "w", newline="", encoding="utf-8-sig") as file:
#     writer = csv.DictWriter(file, fieldnames=["name", "score"])
#     writer.writeheader()
#     writer.writerows(students)

# with open("students", "r", newline="", encoding="utf-8-sig") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         total = total+int(row["score"])
#         row_amount += 1

# print(f"学生の平均点：{total / row_amount}点")


# student = [{"name": "田中", "age": 25, "skills": ["Python", "SQL"]}
#            {"name": "鈴木", "age": 28, "skills": ["Python", "SQL", "JavaScript"]}]

# # student = {"name": "田中", "age": 25, "skills": ["Python", "SQL"]}
# with open("student.json", "w", encoding="utf-8") as f:
#     json.dump(student, f, ensure_ascii=False, indent=2)

# with open("student.json", "r", encoding="utf-8") as f:
#     loaded = json.load(f)

# print(loaded["name"])
# print(loaded["skills"])

# try:
#     number = int(input("整数を入力してください。"))
# except ValueError:
#     print("整数を入力してください。")
# else:
#     print(f"入力値の2倍:{number*2}")
# finally:
#     print("入力処理を終了しました。")

# from pathlib import Path
# path = Path("not_found.txt")

import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    encoding="utf-8",
    format="%(asctime)s %(levelname)s %(message)s",
    force=True,
)

logging.info("アプリケーション起動")
logging.warning("在庫が少なくなっています")
logging.info("商品登録に失敗しました")

print("ログを入力しました。")
