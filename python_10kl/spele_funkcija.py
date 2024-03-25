#importē bibliotēkas
from random import randint, shuffle

# print(randint(1, 100))
# saraksts = [1,2,3,4,5]
# shuffle(saraksts)

# print(saraksts)



#metode try excpet - pārbauda vai tiek ievadīts prasītais

# while True:
#     x = input("Ievadi veselu skaitli: ")
#     try:
#         if int(x):
#             break
#     exept:
#     print(f"{x} nav vesels skaitlis!")

#     print(f"Tu ievadiji {x}")

    #pārbaude vai tiek ievadīts prasītais

# x = input("Ievadi 1, 2 vai 3: ")
# while x not in ["1", "2", "3"]:
#      x = input("Ievadi 1, 2 vai 3: ")


#-----------------------------------

glazite = ["🌹", "🌹", "💖"]
print(*glazite)


def sajauc(glazite):
    shuffle(glazite)
    return glazite 

# print(sajauc(glazite))

#pajautā minējumu
def mans_minejums():
    minejums= ""
    while minejums not in ["1","2","3"]:
        minejums = input("Kurā glāzītē ir bumbiņa (ievadi 1,2 vai 3)?: ")
    return int(minejums)

# print(mans_minejums())

#pārbaudu vai minējums ir pareizs
def parbaudi_minejumu(glazite, minejums):
    if glazite[minejums-1]=="💖":
        print("Uzvarēji!🎉")
    else:
        print("Zaudēji...😥")
        print(*glazite)



#pa soļiem sauc visas funkcijas
  #sajaucu glazites
        
sajauktais = sajauc(glazite)


#speletaja minejums
speletaja_minejums = mans_minejums()


#parbauda speletaja minejumu
parbaudi_minejumu(sajauktais, speletaja_minejums)