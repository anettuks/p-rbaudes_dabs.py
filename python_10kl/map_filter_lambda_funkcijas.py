#map
#izveido funkciju, kas apreiķina skaitļu kvadrātus
def kvadrati(sk):
    return sk**2


print(kvadrati(5))


skaitli = [1, 2, 3, 4, 5, 6, 36]
print(map(kvadrati, skaitli))

for i in map (kvadrati, skaitli): #pirmais variants
    print(i, end="")
print()

print(list(map(kvadrati, skaitli))) #otrais variants

#izveido funkciju, kas nosaka vai vārda garums ir pāra vai nepāra skaitlis
kautkascits = ["Ieva", "Jānis", "Katrīna"]


def garums(vards):
    if len(vards) % 2 ==0:
        return "Pāra skaitlis"
    else:
        return "Nepāra skaitlis"
    
print(garums("Anastasija"))
print(list(map(garums, kautkascits)))



#izveido funkciju, kas nosaka un izdrukā vārda garunmu
def varda_garums(vards):
    return len(vards)


print(list(map(varda_garums, kautkascits)))

#filter
#uzraksta funkciju, kas nosaka vai dotais ir pāra vai nepāra skaitlis
def paris(skaitlis):
    return skaitlis % 2 ==0


print(paris(2))
skaitli = [25, 36, 52, 45, 87, 14]
print(list(filter(paris, skaitli)))

for i in filter(paris, skaitli):
    print(i, end= " ")
print()

#apreiķina rinķa laukumu
#3.14*r*r

def r_lauk(r):
    return 3.14 * r**2 > 50

print(r_lauk(5))
radiusi = [1, 6, 0.25, 14]

print(list(filter(r_lauk, radiusi)))

#### Labda experssion (jeb anonīmā funkcija) 
#uzraksta funkcju, kas apreiķina skaitļu kvadrātus
# rez = sk**2
# return  rez

#saīsinātā funkcijas
# def svadratiL(sk):
#   return sk**2

def kvadratiL(sk):
    return sk**2

print(kvadratiL(5))

#noņem funkcijas definīciju un aistāj ar lambda
kvadr = lambda sk: sk**2
print(kvadr(6))

#sakombinē ar map
skaitli = [25, 36, 52, 45, 84, 17]
print(list(map(lambda sk: sk**2, skaitli)))

# skaombinē ar filter
print(list(filter(lambda sk: sk % 2 == 0, skaitli)))