import random

def skaitlis():
    print("Uzmini skaitli no 1 līdz 100")
izvelies_skaitli = random.randint(1, 100)

while True:
    minejums = int(input("Ievadi minēto skaitli(no 1 līdz 100):"))
    if minejums == izvelies_skaitli:
        print("Apsveicu tu uzminēji skaitli!") 
        break
    elif minejums < izvelies_skaitli: 
        print("Minētais skaitlis ir lielāks. Meiģini velreiz.")
    else:
        print("Minētais skaitlis ir mazāks. Meiģini velreiz.")

skaitlis()
