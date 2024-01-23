# # 1-masala boshlandi ::::

list = [1, 3, 4, 5, 6, 7, 8, 9, 10]
number = []
def tushib_qoldirilgan_son(list, num):
    for x in range(1, 10 + 1):
        if x not in list:
            num.append(x)
            print(x)
tushib_qoldirilgan_son(list, num)

def moshina(odamlar):
    moshina = 6
    cars_needed = (odamlar + moshina) // moshina
    return cars_needed

total_people = int(input("kiriting: "))
cars = moshina(total_people)
# #
print(f"qilay moshina {total_people} dostlar siz uchun {cars} moshina.")

a = int(input("son:"))
xisoblash = 1/2

def calc():
    c = a + xisoblash
    print(f"hisobladi 50% ni kritgan son:{a} va javobi:{c}")
calc()

a = int(input("son:"))
xisoblash = 3/4

def calc():
    c = a + xisoblash
    print(f"hisobladi 50% ni kritgan son:{a} va javobi:{c}")
calc()

a = int(input("son:"))
xisoblash = 9/20

def calc():
    c = a + xisoblash
    print(f"hisobladi 50% ni kritgan son:{a} va javobi:{c}")
calc()