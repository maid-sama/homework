count = 0
zzz = 0
jnd = 0
while count != 8:
    tyr = int(input("сколько задач тебе дали на этот час?"))
    zzz += tyr
    count += 1
    nyt = input("ответил жене")
    if nyt == "да":
        jnd += 1
    elif nyt == "нет":
        pass
print(f"за сегодня ты выполнил {zzz} задач")
if jnd > 0:
    print("незабудь сходить в магаз")
else:
    print("кабзда тебе")


