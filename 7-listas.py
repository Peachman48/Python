mylist = [4, 8, 9, 6, 2, 4, 1]
print(mylist)
print(mylist[2])
print(len(mylist))
mylist.append(50)
print(mylist)

mylist.sort()
for count, element in enumerate(mylist):
    print(f"contador {count} element {element}")

if 50 in mylist:
    print("Si esta el 50")

thisdict = {"brand: ford"}
