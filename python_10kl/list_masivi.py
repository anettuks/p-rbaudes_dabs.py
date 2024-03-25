myList=[1,2,3]
my_list = ['STRING', 100, 23.2]
print(my_list)
print(len(myList)) #saraksta garums
mylist=["viens", "divi", "trīs", "četri"]
print(mylist[0]) #izdrukā pirmo elementu
print(mylist[1:])

cits_list = ["pieci", "seši"]
print(mylist + cits_list) 
jauns_list = mylist + cits_list
print(jauns_list)

jauns_list[0] = "VIENS AR LIELAJIEM BURTIEM"
print(jauns_list)
jauns_list.append("septiņi")
print(jauns_list)
jauns_list.append(8)
print(jauns_list)

jauns_list.pop()
print(jauns_list)
pop_elements = jauns_list.pop()
print(pop_elements)
jauns_list.pop(0)
print(jauns_list)

new_list = ['a', 'e', 'x', 'd', 'l', 'b', 'c']
num_list = [4, 1, 8, 3]
new_list.sort() 
print(new_list)
num_list.sort() 
print(num_list)
num_list.reverse()
print(num_list)

nested_list = [1,1,[1,2]]
print(nested_list[2][1])


augli = ["banāns", "zemene", "apelsīns"]
print(augli[1])
augli.pop(1)
print(augli)
augli.append("ābols")
print(augli)

augli.insert(1, "citrons")
print(augli)
augli[0] = "bumbieris"
print(augli)
augli.sort()
print(augli)

print(f"Šajā sarakstā ir {len(augli)} augļi.")
skaitli = []
i = 20
while i <= 30:
   skaitli .append(i)
   i += 2
print(skaitli)