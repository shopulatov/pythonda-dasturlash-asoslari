# with open('pi_million_digits.txt') as file:
#     PI = file.read()
#     PI = PI.rstrip()
#     PI = PI.replace ('\n','')
#     PI = float(PI)

# # bday ='14159'
# # print(bday in PI)

# import pickle

# with open('PImilliondigits','wb') as file:
#     pickle.dump(PI,file)

# with open('PImilliondigits','rb') as file:
#     pi=pickle.load(PI,file)
    
# print(pi)

filename = 'new_file.txt'

while True:
    ism = input('Keyingi odam ismingizni kiriting:  ')
    tyil= input("Keyingi odam tug'ilgan yilingizni kiriting:  ")
    with open(filename, 'a') as file:
        file.write(ism+'\n')
        file.write(tyil+'\n')
    
    javob=input('Davom etamizmi? (ha/yo\'oq)  ')
    if javob != 'ha':
        break
    
    