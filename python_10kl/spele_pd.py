import random

def skaitlis():
    print("Uzmini skaitli no 1 līdz 100") #ši funkcja parāda, kas lietotājm jādara.
izvelies_skaitli = random.randint(1, 100) #šī funkcija saglabā skaitļus no 1 līdz 100 tos nemainot

while True:
    
    minejums = int(input("Ievadi skaitli(no 1 līdz 100):"))
    
    if minejums == izvelies_skaitli: #funkcija pārbauda vai lietotājs ir uzminējis skaitli
        print("Apsveicu tu uzminēji skaitli!") #ja spēlētājs uzminēja skaitli tad viņu apsveic


        atkartot = input ("Vai vēlies spēli sākt velreiz? (jā/nē): ")
        if atkartot.lower() == "jā":
          skaitlis()
        else:
          print("Paldies par spēli!")


          break #šī funkcija pārtrauc spēli, lai spēletajs varētu spēli sākt no jauna  
    elif minejums < izvelies_skaitli:  #šī funkcija pārbauda vai minējums ir lielāks vai mazāks
        print("Minētais skaitlis ir lielāks. Meiģini velreiz.")
    else:
        print("Minētais skaitlis ir mazāks. Meiģini velreiz.")

skaitlis()
