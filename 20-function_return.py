# P1

# def mijoz_info(ism,familya,tyil,tjoy,email = '',tel=None,yosh=''):
#     mijoz= {'ism':ism,
#             'familya':familya,
#             'tyil':tyil,
#             'tjoy':tjoy,
#             'email':email,
#             'tel':tel 
#         }
#     return mijoz

# print("\nEndi siz haqingizda ba'zi narsalar haqida gaplashamiz: ")
# mijozlar=[]
# while True:
#     ism = input("Ismingiz nima?  ")
#     familya = input("Familyangiz nima?  ")
#     tyil = input(f"Hurmatli {ism.title()} {familya.title()} qachon tug'ilgansiz?  ")
#     tjoy = input("Va qayerda?  ")
#     email = input("Elektron pochtangizni qoldira olasizmi? ")
#     tel = input("Telefon raqamingiznichi?  ")
#     mijozlar.append(mijoz_info(ism,familya,tyil,tjoy,email,tel))
    
#     javob = input("Davom etamizmi? (ha/yo'q)  ")
#     if javob != 'ha':
#         break

# P2

# print("Mijozlar: ")
# for mijoz in mijozlar:
#     print (f"{mijoz['ism'].title()} {mijoz['familya'].title()} {2022-int(mijoz['tyil'])} yoshda tel raqami: {mijoz['tel']}")

# P3

# def engkatta(son1,son2,son3):
#     max = 1
#     if son1>son2:
#         if son1>son3:
#             max = son1
#         else:
#             max=son3
#     elif son1<son2:
#         if son2>son3:
#             max= son2
#         else:
#             max=son3
#     else:
#         if son1>son3:
#             max= son1
#         else:
#             max = son3
#     print ( f"\nBu sonlar ichida eng kattasi {max}.")


# P4

# son1 = int(input("1-sonni kiriting: "))
# son2 = int(input("2-sonni kiriting: "))
# son3 = int(input("3-sonni kiriting: "))
# engkatta(son1,son2,son3)

# def aylana_info(radius, pi=3.14159):
#     aylana = {'radius':radius,
#               'diametr':2*radius,
#               'uzunlik': 2*pi*radius,
#               'yuza': pi*radius**2}
#     return aylana

# aylana_info(5)

# P5

# def tson_top(min,max):
#     tsonlar = []
#     for n in range (min,max+1):
#         tub = True
#         if n == 1:
#             tub = False
#         elif n == 2:
#             tub = True
#         for x in range (2,n):
#             if (n%x == 0):
#                 tub = False
            
#         if tub:
#             tsonlar.append(n)
            
#     return tsonlar

# print(tson_top(100,200))

# def fibonacci(n):
#     sonlar = []
#     for x in range(n):
#         if x==0 or x==1:
#             sonlar.append(1)        
#         else:
#             sonlar.append(sonlar[x-1]+sonlar[x-2])
#     return sonlar

# print(fibonacci(10))