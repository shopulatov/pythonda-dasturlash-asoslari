# P1

# izohli_lugat = {
#     'int':'butun son',
#     'float':"o'nlik son",
#     'bolean':'mantiqiy amallar',
#     'string':'matnlar',
#     'for': 'takrorlash operatori',
#     'list': 'jadvallar',
#     'input': 'mijozdan kiritigan ma\'lumot',
#     'print':"e'lon qilish",
#     'tuples':"o'zgarmas jadval",
#     'del':"o'chirish",
#     "get": 'olish'
#     }

# for lugat in sorted(izohli_lugat.keys()):
#     print(lugat)

# P2

poytaxtlar = {
    'usa' : 'washington',
    'canada' : 'ottava',
    'uk' : 'london',
    'china': 'beijing',
    'japan': 'tokio',
    'germany': 'berlin',
    'france': 'paris',
    'uae':'dubai',
    'uzbekistan':'tashkent'
    }

# print("Lug'atimizda quyidagi davlatlar bor:")
# for davlat in sorted(poytaxtlar.keys()):
#     print(davlat.title())

# print("Lug'atimizda quyidagi davlatlarning poytaxlari bor:")
# for poytaxt in sorted(poytaxtlar.values()):
#     print(poytaxt.title())
   
# P3

# davlat = input ("Istalgan davlatingizni kiriting >>>").lower()
# poytaxt = poytaxtlar.get(davlat)
# if davlat == 'usa' or 'uk' or 'uae':
#     davlat= davlat.upper()
# else:
#     davlat = davlat.title()
# if poytaxt == None:
#     print("Kechirasiz, bizda bu davlatning poytaxti ma'lumoti yo'q")
# else:
#     print(f"{davlat}ning poytaxti {poytaxt.title()}.")
    
# P4

# menu = {
#         'osh':20000,
#         "lag'mon":22000,
#         'non':4000,
#         'choy':5000,
#         'shashlik':12000,
#         'somsa':6000,
#         'tabaka':15000
#         }

# buyurtmalar = []
# for n in range(5):
#     buyurtmalar.append(input(f"{n+1}-taomingizni kiriting >>>").lower())
# for buyurtma in buyurtmalar:
#     if buyurtma in menu:
#         print(f"{buyurtma}ning narxi {menu[buyurtma]}")
#     else:
#         print(f"Kechirasiz bizda {buyurtma} yo'q")