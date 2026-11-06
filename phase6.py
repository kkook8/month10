class Student:
    school = "百人町小学"

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def introduce(self):
        print(f"私は{self.name}です。{self.school}の小学校、今回の得点は{self.score}です。")


s1 = Student("田中", 98)
s2 = Student("佐藤", 72)

s1.introduce()
s2.introduce()


class BankAccount():
    bank = "瑞穂銀行"
    # コンストラクタメーソット

    def __init__(self, name, balance=0):
        if balance < 0:
            raise ValueError("初期残高0以上にしてください。")
        self.name = name
        self._balance = balance

    @property
    def balance(self):
        print("残高を読み込んでいまます")
        return self._balance

    @balance.setter
    def balance(self, amount):
        self._balance = amount

    def dispodal(self, amount):
        if amount <= 0:
            raise ValueError("入金額は1以上にしてください。")
        self._balance += amount

    def show_balance(self):
        # print(f"お客様{self.name}の残高は{self.balance}")
        return f"お客様{self.name}の残高は{self._balance}"

    def payment(self, amount):
        if amount <= 0:
            raise ValueError("出金額は1以上にしてください。")
        if amount > self._balance:
            raise ValueError("残高が不足しています。")
        self._balance -= amount


b1 = BankAccount("洋子", 1000)
# b1 = BankAccount("洋子")

b1.dispodal(500)
print(b1.show_balance())
b1.dispodal(300)
print(b1.show_balance())
b1.payment(400)
print(b1.show_balance())
print("======================")
# b1.balance = 400
print(b1.balance)

print(f"{b1.bank}{b1.show_balance()}")


class Product:
    def __init__(self, name, price):
        if price < 0:
            raise ValueError("価格は0円以上です。")
        self.name = name
        self.__price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, amount):
        self.__price = amount


p1 = Product("ノード", 250)
print(p1.name)
# print(p1.price())
print(p1.price)
# print(p1.__price)
# p1.__price = 18
p1.price = 18
print(p1.price)


class Employee:
    def __init__(self, name):
        self.name = name

    def describe(self):
        return f"社員名：{self.name}"


class FullTimeEmployee(Employee):
    def __init__(self, name, monthly_salary):
        super().__init__(name)
        self.monthly_salary = monthly_salary

    def calculate_pay(self):
        return self.monthly_salary


class PartTimeEmployee(Employee):
    def __init__(self, name, hourly_rate, hours):
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours = hours

    def calculate_pay(self):
        return self.hourly_rate*self.hours


f1 = FullTimeEmployee("田中", 350000)
f2 = FullTimeEmployee("鈴木", 520000)
p1 = PartTimeEmployee("佐藤", 1200, 58)
p2 = PartTimeEmployee("山田", 1200, 58)

print(f"{f1.name}の給料：{f1.calculate_pay()}")
print(f"{p1.name}の給料：{p1.calculate_pay()}")

print(f1.describe())
print(p1.describe())

# 多態性
employee = [
    f1, p1, f2, p2
]

for employee in employee:
    print(f"{employee.name}:{employee.calculate_pay():,}円")
