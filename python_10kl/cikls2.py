mainigais = [1,2,3] 
for elements in mainigais:
   print(elements)

for skaitlis in range(15):
    print(skaitlis)

for skaitlis in range(4, 15):
    print(skaitlis)

for skaitlis in range(4, 15, 3):
    print(skaitlis)



mainigais = [1, 2, 3, 4]
for elements in mainigais:
    print(elements)


mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
for x in mylist:
    print(x)


for _ in mylist:
    print("Sveiki!")


for skaitlis in mylist:
    if skaitlis % 2 == 0:
        print(skaitlis)
    else:
        print(f"Nepāra skaitlis: {skaitlis}")


mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
summa = 0

for sk in mylist:
    summa = summa + sk
    print(f"Pēc {sk} skiaitļu saskaitīšanas summa ir {summa}")
    print(summa)


mystring = "Sveika, Pasaule!"
for burts in mystring:
    print(burts)

for burts in "programma":
    print(burts, end=" ")

    


