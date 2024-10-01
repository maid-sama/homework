num = int(input("до какого числа считаем"))
su = 0
for n in range(0, num + 1):
    elem = (-1)**n*1/(2**n)
    su += elem
    print(f"значение числа {n} по формуле = {elem} ")
    print("---------------------------------------------")
print(f"сумма = {su}")





