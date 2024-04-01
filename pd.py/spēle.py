import random

def skaitlis():
    print("Uzmini skaitli no 1 līdz 100") #ši funkcja parāda, kas lietotājm jādara.
izvelies_skaitli = random.randint(1, 100) #šī funkcija saglabā skaitļus no 1 līdz 100 tos nemainot

while True:
    minejums = int(input("Ievadi minēto skaitli(no 1 līdz 100):"))
    if minejums == izvelies_skaitli: #funkcija pārbauda vai lietotājs ir uzminējis skaitli
        print("Apsveicu tu uzminēji skaitli!") #ja spēlētājs uzminēja skaitli tad viņu apsveic

        atkartot = input ("Vai vēlies spēli sākt velreiz? (jā/nē): ")
        if atkartot.lower() == "jā":
          skaitlis()
        else:


          break #šī funkcija pārtrauc spēli, lai spēletajs varētu spēli sākt no jauna  
    elif minejums < izvelies_skaitli:  #šī funkcija pārbauda vai minējums ir lielāks vai mazāks
        print("Minētais skaitlis ir lielāks. Meiģini velreiz.")
    else:
        print("Minētais skaitlis ir mazāks. Meiģini velreiz.")

skaitlis()



def skaitlis():
    print("Uzmini skaitli no 1 līdz 100")
    izvelies_skaitli = random.randint(1, 100)
    while True:
        minejums = input("Ievadi minēto skaitli (no 1 līdz 100) vai raksti 'ne', lai pārtrauktu spēli: ")
        if minejums.lower() == "ne":
            print("Labprāt spēlējam nākamreiz! Paldies par spēli!")
            break
        else:
            minejums = int(minejums)
            if minejums == izvelies_skaitli:
                print("Apsveicu, tu uzminēji skaitli!")
                atkartot = input("Vai vēlies spēli sākt vēlreiz? (jā/nē): ")
                if atkartot.lower() == "jā":
                    skaitlis()
                else:
                    print("Paldies par spēli!")
                    break
            elif minejums < izvelies_skaitli:
                print("Minētais skaitlis ir lielāks. Mēģini vēlreiz.")
            else:
                print("Minētais skaitlis ir mazāks. Mēģini vēlreiz.")

skaitlis() 
    
