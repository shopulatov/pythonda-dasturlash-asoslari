# P1

# buxoriy = {'ism':'Abu Abdulloh Muhammad ibn Ismoil',
#            'tyil':810,
#            'vyil':870,
#            'tjoy':'Buxoro'
#            }

# qodiriy = {'ism':'Abdulla Qodiriy',
#            'tyil':1894,
#            'vyil':1938,
#            'tjoy':'Toshkent'
#            }

# vohidov = {'ism':'Erkin Vohidov',
#            'tyil':1936,
#            'vyil':2016,
#            'tjoy':"Farg'ona"
#            }

# navoiy = {'ism':'Alisher Navoiy',
#            'tyil':1441,
#            'vyil':1501,
#            'tjoy':"Xirot"
#            }

# tshaxslar = [buxoriy, qodiriy, vohidov, navoiy]
# for shaxs in tshaxslar:
#     print(f"{shaxs['ism']}\n"
#           f"{shaxs['tyil']}-yilda {shaxs['tjoy'].title()}da tug'ilgan.\n"
#           f"{shaxs['vyil']}-yilda vafot etgan.\n"
#           )
    
# P2

# buxoriy = {'ism':'Abu Abdulloh Muhammad ibn Ismoil',
#            'tyil':810,
#            'vyil':870,
#            'tjoy':'Buxoro',
#            'asarlar':["Al-Jome As-sahih", "Al-adab al-mufrad"]
#            }

# qodiriy = {'ism':'Abdulla Qodiriy',
#            'tyil':1894,
#            'vyil':1938,
#            'tjoy':'Toshkent',
#            "asarlar":["Mehrobdan chayon", "O'tgan kunlar"]
#            }

# vohidov = {'ism':'Erkin Vohidov',
#            'tyil':1936,
#            'vyil':2016,
#            'tjoy':"Farg'ona",
#            "asarlar":["Oybek", "O'zbegim"]
#            }

# navoiy = {'ism':'Alisher Navoiy',
#            'tyil':1441,
#            'vyil':1501,
#            'tjoy':"Xirot",
#            "asarlar":["Xamsa", "Lison ut-Tayr"]
#            }

# tshaxslar = [buxoriy, qodiriy, vohidov, navoiy]
# for shaxs in tshaxslar:
#     nom = shaxs['ism']
#     asarlar = shaxs['asarlar']
#     print(f"{nom}ning mashxur asarlari:"      )
#     for asar in asarlar:
#         print (asar)

# P3

# dost1 = {
#        'ism':'ali',
#        'kinolar':['avengers', 'batman', 'spiderman']
#        }
# dost2 = {
#     'ism':'vali',
#     'kinolar': ['risolat', 'umar ibn hattob', 'qimor']
#     }
# dost3 = {
#     'ism': 'soli',
#     'kinolar': ['ertugrul', 'pulat', 'muhtasham asr']
#     }

# dostlar = [dost1,dost2,dost3]
# for dost in dostlar:
#     print(f"{dost['ism'].title()}ning yaxshi ko'rgan kinolari: ")
#     kinolar=dost['kinolar']
#     for kino in kinolar:
#         print(kino.title())

# P4

# davlatlar = {
#     "o'zbekiston":{'poytaxt':"toshkent",
#                     'maydon':448978,
#                     'aholi':33_000_000,
#                     'pul birligi':"so'm"
#                     },
#     "rossiya":{'poytaxt':"moskva",
#                     'maydon':17_098_246,
#                     'aholi':144_000_000,
#                     'pul birligi':"rubl"
#                     },
#     "aqsh":{'poytaxt':"vashington",
#                     'maydon':9_631_418,
#                     'aholi':327_000_000,
#                     'pul birligi':"dollar"},
#     "malayziya":{'poytaxt':"kuala-lumpur",
#                     'maydon':329750,
#                     'aholi':25_000_000,
#                     'pul birligi':"rinngit"}
#     } 

# for davlat,info in davlatlar.items():
#     print(f"{davlat.title()} davlatining poytaxti {info['poytaxt'].title()} shahri.\n",
#           f"Maydoni {info['maydon']} kvadrat km.\n"
#           f"Aholisi {info['aholi']} kishi va pul birligi {info['pul birligi']}.")

# P5

# davlat = input("Istalgan davlatingizni kiriting >>>").lower()
# if davlat in davlatlar:
#     info = davlatlar[davlat]
#     print(f"{davlat.title()} davlatining poytaxti {info['poytaxt'].title()} shahri.\n",
#               f"Maydoni {info['maydon']} kvadrat km.\n"
#               f"Aholisi {info['aholi']} kishi va pul birligi {info['pul birligi']}.")
# else:
#     print("Bunday davlat bizning bazamizda yo'q")