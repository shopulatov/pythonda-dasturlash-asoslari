# P1

print("Buyurtmalar ro'yxatini tuzamiz")
buyurtmalar = []
flag = True
while flag:
    buyurtma = input("Buyurtmangizni kiriting >>>")
    buyurtmalar.append(buyurtma)
    
    javob = input("Yana buyurtma qo'shishni hohlaysizmi? (ha\yo'q) ")
    if javob != 'ha':
        flag = False

# print("Buyurtmalar ro'yxati:")
# for buyum in buyurtmalar:
#     print(buyum)

# P2

print("Elektron bozor uchun mahsulotlar va ularning narxlari lug'ati")
mahsulotlar = {}
while True:
    mahsulot = input ("Mahsulotning nomini kiriting:  ")
    narx = input(f"{mahsulot.title()}ning narxi:  ")
    mahsulotlar[mahsulot]=int(narx)
    
    javob = input("Yana mahsulot qo'shishni hohlaysizmi? (ha\yo'q) ")
    if javob != 'ha':
        break

# for mahsulot,narx in mahsulotlar.items():
#     print(f"{mahsulot}ning narxi {narx} so'm")

# P3

# buyurtmalar = ['olma','anjir','uzum','qovun']
# mahsulotlar = {'olma':20000,
#                'shaftoli':25000,
#                'tarvuz':18000,
#                'uzum':22000}

while buyurtmalar:
    buyurtma=buyurtmalar.pop()
    if buyurtma in mahsulotlar.keys():
        print(f"{buyurtma.title()}ning narxi {mahsulotlar[buyurtma]} so'm.")
    else:
        print(f"Bizda {buyurtma}dan yo'q")