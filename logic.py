import random
from decouple import config


def start():
    print("Добро пожаловать в казино!")
    balanse = int(config('MY_MONEY'))
    while True:
        commond = input("1-выход\n"
                        "2-играть\n")
        if commond == "1":
            print("До свидания ")
            break
        elif commond == "2":
            print(f"ваш баланс - {balanse}$")
            num = list(range(1, 31))
            print(num)
            stavka = int(input("введите сумму ставки"))
            if stavka > balanse:
                print("у вас не достаточно денег")
                break

            user_num = int(input("выберите число "))
            print(f"ваше число - {user_num}")
            rang = random.randint(1, 31)
            print(f"число казино - {rang}")

            if user_num >= 31:
                print("только числа от 1 до 30!")
                continue


            elif user_num == rang:
                print(f"паздравляем! вы выиграли {stavka * 2}$")
            else:
                print(f"вы проиграли {stavka}$")
                balanse -= stavka



        elif balanse <= 0:
            print("у вас закончились деньги")
            break

