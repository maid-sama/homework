good = 0
net = 0
bad = 0
count = 0
while count < 5:
    fer = int(input("оцените нас от 100 до -100:    "))
    print("------------------------------")
    if fer >= -100 or fer <= 100:
        if fer > 0:
            count += 1
            good += 1
            print("спасибо за отзыв")
            print("------------------------------")
        elif fer == 0 :
            count += 1
            net += 1
            print("спасибо за отзыв")
            print("------------------------------")
        else:
            count += 1
            bad += 1
            print("спасибо за отзыв")
            print("------------------------------")
    else:
        print("ты чо дурак")
if good > net and good > bad:
    print("мы хорошие")
elif bad > good and bad > net:
    print("------------------------------")
    print("мы не хоршие")
    print("------------------------------")
else:
    print("хз")















