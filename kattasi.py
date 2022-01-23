def kattalashtir(toplam):
    new_toplam=[]
    for word in toplam:
        word = word.title()
        new_toplam.append(word)
        
    return new_toplam

# print(kattalashtir(['bir', 'ikki', 'uch']))                                  