#Video Link: https://www.youtube.com/watch?v=tHUNg8GdRQs
#Python Array module
import array as myArray

import numpy as np
arr = myArray.array('i',[1,2,3])
arr1 = myArray.array('f',[1.2,2.4,5.3])
arr2 = myArray.array('u',['a','b','c','d'])

print(arr.typecode)
print(arr1.typecode)
print(arr2.typecode)


print(len(arr))
print(len(arr1))
print(len(arr2))


print(arr)
print(arr1)
print(arr2)

for i in  range(0,len(arr)):
  print(arr[i],end=" ")
print("\n")

for i in  range(0,len(arr1)):
  print(arr1[i],end=" ")
print("\n")

for i in  range(0,len(arr2)):
  print(arr2[i],end=" ")
print("\n")

x = list(range(1,100,2))
new_array = myArray.array('i',x)

for i in range(0,len(new_array)):
  print(new_array[i], end = " ")
print("\n")

print(new_array[25])

new_arr = myArray.array('i',[3,4,5,6,7,8,9,10])
for i in  range(0,len(new_arr)):
  print(new_arr[i],end=" ")
print("\n")

new_arr.insert(0,2)
new_arr.insert(0,1)

for i in  range(0,len(new_arr)):
  print(new_arr[i],end=" ")
print("\n")

new_arr.append(11)

for i in  range(0,len(new_arr)):
  print(new_arr[i],end=" ")
print("\n")

newarr = myArray.array('i',[1,2,2,4,5])
for i in  range(0,len(newarr)):
  print(newarr[i],end=" ")
print("\n")
newarr[2] = 3
for i in  range(0,len(newarr)):
  print(newarr[i],end=" ")
print("\n")

newarr.pop(0) #index
for i in  range(0,len(newarr)):
  print(newarr[i],end=" ")
print("\n")

newarr.remove(2) #value
for i in  range(0,len(newarr)):
  print(newarr[i],end=" ")
print("\n")

x  = list(range(0,100,3))
arr = myArray.array('i',x)
for i in  range(0,len(arr)):
  print(arr[i],end=" ")
print("\n")
arr0 = arr[10:20]

for i in  range(0,len(arr0)):
  print(arr0[i],end=" ")
print("\n")

arr1 = arr[10:-20]
for i in  range(0,len(arr1)):
  print(arr1[i],end=" ")
print("\n")

arr2 = arr[::-1]
for i in  range(0,len(arr2)):
  print(arr2[i],end=" ")
print("\n")

x = list(range(0,1000000,2))
search_array = myArray.array('i',x)

for i in range (0, len(search_array[0:10])):
  print(search_array[i], end = " ")
print("\n")

index = search_array.index(10002)
res = search_array[index]
print(index,res)

sort_array = myArray.array('i',[5,3,4,6,9,7,8])
sorted_array = sort_array.tolist()

sorted_array.sort()
print(sorted_array)

sorted_array.sort(reverse = True)
print(sorted_array)

#Numoy Arrays
arr = np.array([1,2,3,4,5])
print(arr)
zeros = np.zeros((2,2))
print(zeros)
ones = np.ones((2,2))
print(ones)
const = np.full((4,4),7)
print(const)
iden = np.eye(4)
print(iden)
rdom = np.random.random((2,2))
print(rdom)
