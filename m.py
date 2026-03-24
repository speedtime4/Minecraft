print("hello from Speed_Time4")
for i in range(1,10)
print(i)
# a=["Даниэль",10,"Эйлат","майнкрафт и роблокс"]
# print("меня зовут ",a[0],".мне ",a[1])
# b={"Name":"Daniel","age":10,}
# print(b)
# b["hobby"]="roblox"
# print(b)
# b["age"]=18
# del b["hobby"]
# print(b)


# grades = {
#     "Bohdan": 8,
#     "Oleh": 12,
#     "Iryna": 9
# }
# print(grades["Bohdan"])
# grades["Eric"]=11
# print(grades)
# grades["Anna"]=12
# print(grades)
a=("Minecraft is a sandbox game developed and published by "
"Mojang Studios." 
" Following its initial public alpha release in 2009, it was "
"formally released in 2011 for personal computers."
" The game has since been ported to numerous platforms, including mobile devices"
" and various video game consoles.")

b={"a":0}
for i in a.lower():
    print(i)
    if i.isalpha():
        if i in b:
            b[i]+=1
        else:
            b[i]=1
for d,aa in b.items():
    print("letter",d,"found",aa)
