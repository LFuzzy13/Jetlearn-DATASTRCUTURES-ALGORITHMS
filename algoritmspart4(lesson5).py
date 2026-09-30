#bubble sort

mylist = [1,54,23,65,9,24]

for i in range(0, len(mylist)):
    for j in range (i, len(mylist)):
        if mylist[i] > mylist[j]:
            mylist[i],mylist[j] = mylist[j],mylist[i]

print(mylist)

#insertion sort

mylist = [1,54,23,65,9,24]

for i in range(0,len(mylist)):
    minElement = 1000000
    minLocation = -1

    for j in range(i,len(mylist)):
        if minElement > mylist[j]:
            minElement = mylist[j]
            minLocation = j

    mylist[i], mylist[minLocation] = mylist[minLocation], mylist[i]

print(mylist)
