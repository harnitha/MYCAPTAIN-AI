#Assigning elements to different lists

list1=['Hi','Hello',2,'my','github']
list2=['->']
print("Assigning elements to different lists")
print(list1,list2,sep=",")
print()


#Accesing elements from a tuple

tuple1=(1,2,3,'hey','HI')
print("Accesing elements from a tuple")
print(tuple1[1:-1])
print(tuple1[3])
print(tuple1[::-1])
print()


#Deleting different dictionary elements

dict1={'key1':345,'key2':94949,'key3':98488}
print("Deleting different dictionary elements")
del dict1['key2']
print(dict1)
del dict1['key3']
print(dict1)
