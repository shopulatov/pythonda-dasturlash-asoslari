# P1

# savol = "Yoqtirgan kitobingizni kiriting (dasturni to'xtatish uchun 'stop' deb yozing): "
# while True:
#     if input(savol) == 'stop':
#         break
# print('Rahmat!')

# P2

# print('Muzeyga kirish chiptalarining narxlarini aniqlovchi dastur.\
#       (dasturni to\'xtatish uchun "exit" yoki "quit" deb yozing)')
# savol = "Yoshingiz nechida >>>"
# while True:
#     yosh = input(savol)
#     if yosh == 'exit' or 'quit':
#         break
#     age = int (yosh)
#     if age<7:
#         narx = 2000
#     elif age<=18:
#         narx = 3000
#     elif age<=65:
#         narx =10000
#     else:
#         narx = 0
    
#     if narx == 0:
#         print ("Sizga kirish bepul")
#     else:
#         print (f"Sizga kirish {narx} so'm")

# P3

# savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
# savol += "Musbat son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

# while True:
#     qiymat = input(savol)
#     if qiymat.lower() =='exit':
#         break
#     elif float(qiymat)<0:
#         print ('Iltimos musbat son kiriting')
#     else:
#         ildiz = float(qiymat)**(0.5)
#         print(f"{qiymat} ning ildizi {ildiz} ga teng")