nach = int(input("начало"))
kon = int(input("конец"))
chag = int(input("введита шаг"))
if nach > kon:
    nach, kon = kon, nach
else:
    pass
if chag > 0:
    chag = -chag
else:
    pass
for x in range(kon, nach-1, chag):
    y = (x ** 3) + 2 * (x ** 2) - (4 * x) + 1
    print(f"в точке {x}, функция равна {y}")










