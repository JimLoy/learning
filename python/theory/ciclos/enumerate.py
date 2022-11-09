#Devuelve una tupla con claves indice valor

nums = [10,20,30,40,50,60]


print(tuple(enumerate(nums)))


for index,num in enumerate(nums):
    print(index,num)
