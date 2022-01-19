print("Keling o'ylagan sonni topish o'yinini o'ynaymiz")

import random as r

def sontop(x=10):
    a = r.randint(1,x)
    print (f"1 dan {x} gacha bitta son o'yladim. Topa olasizmi?")
    taxminlar = 0
    while True:
        taxminlar+=1
        t1= int(input(">>>"))
        if t1>a:
            print("Xato men o'ylagan son bundan kichikroq. Yana harakat qiling: ")
        elif t1<a:
            print("Xato men o'ylagan son bundan kattaroq. Yana harakat qiling: ")
        else:
            break
    print(f"TOPDINGIZ! {a} sonini o'ylagan edim. {taxminlar} ta taxmin bilan topdingiz. Tabriklayman!!!")
    return taxminlar

def sontop_pc(x=10):
    input(f"1 dan {x} gacha son o'ylang men topishga harakat qilaman. Boshlash uchun ixtiyoriy tugmani bosing")
    a=1
    b=x
    taxminlar1 = 0
    while True:
        taxmin = r.randint(a,b)
        taxminlar1+=1
        javob = input(f"Siz {taxmin} sonini o'yladingiz to'g'rimi? To'g'ri (T), men o'ylagan son bundan kattaroq (+), yoki kichikroq (-)")
        if javob == '+':
            a=taxmin+1
        elif javob == '-':
            b=taxmin-1
        else:
            break
    print (f"Soningizni {taxminlar1} ta taxmin bilan topdim")
    return taxminlar1

def play(x=10):
    man = sontop(x)
    pc = sontop_pc(x)
    while True:
        if man<pc:
            print(f"Siz {man} ta taxmin bilan topdingiz va YUTDINGIZ")
        elif man>pc:
            print(f"Afsuski men {pc} ta taxmin bilan topdim va yutdim!")
        else:
            print(f"Durrang Ikkalamiz ham {pc} ta taxmin bilan topdik")
        
        response = input("Yana o'ynaymizmi? (ha/yo'q) ")
        if response != 'ha':
            break

play()

    

