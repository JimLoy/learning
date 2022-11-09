lista = [1,2,3,4]
tupla = (10,20,30,40)

res = zip(lista,tupla) #devuelve un tipo de dato zip
res = tuple(res) #tupla de tuplas
#valido list(res) para una lista de tuplas

print(res)
#Las tuplas del zip son todas del mismo tamaño si alguna tiene valores de mas estos no son tomados en cuenta
#Se le pueden agregar mas tuplas o listas como argumentos