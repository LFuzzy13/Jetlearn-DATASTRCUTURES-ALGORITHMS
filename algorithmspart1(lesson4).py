#LINEAR SEARCH

list = [10,34,20,90,40,1,30,87,200,489,19,2090,3984,4809,5987,9879,87979,2345,2345678,8765,3456,9876,4567,54,43,5647465,43546,456,34,46,34,678,86,3,4356,9,654,32,4,788,9,786,763,42,3,67,8567457,45,9,9789,789,2334,24234234,56,86,74,354,868,6556,81,852,856,8]
target = 24234234

found = False
for i in range(len(list)):
    if list[i] == target:
        print ("Element Found At Index", i)
        found = True
        break

if found == False:
    print("Element Not Found")

