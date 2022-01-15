#P1

# a = int(input("Iltimos juft son kiriting: >>>"))
# if a%2 == 0:
#     print("Rahmat")
# else:
#     print("Bu juft son emas.")

#P2

# yosh = int(input('Yoshingizni kiriting: >>>'))
# if yosh<4 or yosh>60:
#     print('Sizga kirish bepul')
# elif yosh<18:
#     print("Sizga kirish 10000 so'm")
# else:
#     print("Sizga kirish 20000 so'm")

#P3

# a = float(input("Birinchi sonni kiriting >>>"))
# b = float(input("Ikkinchi sonni kiriting >>>"))
# if a>b:
#     print("Birinchi son katta.")
# elif a==b:
#     print("Bu sonlar teng.")
# else:
#     print("Ikkinchi son katta.")

#P4

# mahsulotlar = ["un", "yog'", "go'sht", 'sabzi', 'piyoz', 'kartoshka', 'tuxum', 'banan', 'pomidor', 'bodring']

# savat = []
# for n in range(5):
#     savat.append(input(f"{n+1}-mahsulotingizni kiriting >>>"))

# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         print(f"{mahsulot} do'konimizda bor.")
#     else:
#         print(f"{mahsulot} do'konimizda yo'q")

#P5

# mahsulotlar = ["un", "yog'", "go'sht", 'sabzi', 'piyoz', 'kartoshka', 'tuxum', 'banan', 'pomidor', 'bodring']

# savat = []
# for n in range(5):
#     savat.append(input(f"{n+1}-mahsulotingizni kiriting >>>"))

# bor_mahsulotlar = []
# mavjud_emas = []

# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)

# if mavjud_emas:
#     print("Bizda quyidagilar yo'q: ")
#     for mahsulot in mavjud_emas:
#         print(mahsulot)
# else:
#     print("Bizda siz so'ragan hamma mahsulot bor")
    
#P6

# foydalanuvchilar = ["abror", "asad", "sardor", "rano", "anvar"]

# y_foydalanuvchi = input("O'zingiz uchun login kiriting: >>>")
# if y_foydalanuvchi.lower() in foydalanuvchilar:
#     print(f"{y_foydalanuvchi.title()} logini band. Boshqa login kiriting.")
# else:
#     foydalanuvchilar.append(y_foydalanuvchi.lower())
#     print(f"Xush kelibsiz, {y_foydalanuvchi}!")
    
# P7

# a = int(input("Biror butun son kiriting >>>"))

# for n in range(2,11):
#     if not (a%n) :
#         print(f"{a} soni {n} ga qoldiqsiz bo'linadi")
# else:
#         print(f"{a} soni 2 dan 10 gacha xech qanday songa qoldiqsiz bo'linmaydi.")
        