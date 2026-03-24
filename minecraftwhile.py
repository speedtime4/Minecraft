# a=0
# while True:
#     print(a)
#     a+=1
#     print("aa")
#     if a==5000:
#         break
# while True:
#     b = input('Как тебя зовут?')
#     if b=="2":
#         print("пока")
#         break
#     else:
#         print("привет",b)
import random
h=1
p=3
a=random.randint(1,10)
y=0
while True:
    b = int( input("ведите какое-то число"))
    if a==b:
        y=y+100
        print("вы угадали 😎")
        print("у вас",y)
        p=p+1
        a=random.randint(1,10)
    else:
        print("вы не угадали 😭")
        p=p-1
    if p==0:
        if y>200:
            h = input("хотите ли вы купить попытку")
            if h=="no":

                print("у вас не осталось попыток")
                print("вы заработали",y)
                break 
            elif h=="yes":
                p=p+1
                y=y-200
            else:
                break
        else:
            break
    print(p)