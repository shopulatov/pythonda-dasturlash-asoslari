# P1

# def tugilgan_yil(ism, yosh):
#     """"Foydalanuvchining ismini va yoshini so'rab undan tug'ilgan yilini aniqlaydigan dastur"""
#     print(f"Hurmatli {ism.title()}. Siz {2022-yosh}-yilda tug'ilganga o'xshaysiz")

# ism = input("Assalomu alaykum, ismingizni bilsam bo'ladimi?  ")
# yosh = int(input(f"{ism.title()} yoshingizni kiriting:  "))
# tugilgan_yil(ism, yosh)

# P2

# def kvadrat(son):
#     """"Kiritilgan sonning kvadratini hisoblaydigan funksiya"""
#     print(f"{son} ning kvadrati {son**2} ga teng")

# def kub(son):
#     """"Kiritilgan sonning kubini hisoblaydigan funksiya"""
#     print(f"{son} ning kubi {son**3} ga teng")
    
# son = int(input("Biror son kiriting:  "))
# kvadrat(son)
# kub(son)

# P3

# def juft_yoki_toq(son):
#     """Kiritilgan sonning juft yoki toqligini aniqlovchi funksiya"""
#     if son%2 == 0:
#         print(f"{son} soni juft son.")
#     else:
#         print(f"{son} soni toq son.")

# son = int(input("Biror son kiriting:  "))
# juft_yoki_toq(son)

# P4

# def taqqosla(son1, son2):
#     """Berilgan sonlarning katta, kichik yoki tengligini aniqlovchi funksiya"""
#     if son1==son2:
#         print("Kiritilgan sonlar teng")
#     elif son1>son2:
#         print(f"Bu sonlardan {son1} kattaroq")
#     else:
#         print(f"Bu sonlardan {son2} kattaroq")

# son1= int(input("1-sonni kiriting >>>"))
# son2= int(input("2-sonni kiriting >>>"))
# taqqosla(son1, son2)

# P5

# def daraja_hisobla(x,y=2):
#     """Berilgan asos va uning darajasidan shu sonni hisoblaydigan funksiya"""
#     print (f"{x} ning {y}-darajasi {x**y} ga teng.")

# x = int(input("Sonning asosi >>>"))
# y = int(input("Sonning darajasi >>>"))
# daraja_hisobla(x, y)

# daraja_hisobla(5)

# P7

# def boluvchi_top(son):
#     """Kiritilgan sonning 2 dan 10 gacha qaysi sonlarga qoldiqsiz bo'linishini aniqlovchi dastur"""
#     boluvchilar = []
#     for n in range(2,11):
#         if son%n == 0:
#             boluvchilar.append(n)
    
#     if not boluvchilar:
#         print(f"{son} soni 2 dan 10 gacha xech qanday songa qoldiqsiz bo'linmaydi")
        
#     for boluvchi in boluvchilar:
#         print(f"{son} {boluvchi} ga bo'linadi")
        
# boluvchi_top(370)
