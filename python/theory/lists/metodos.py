'''
len(value)                    len() == length ==  longitud 
list.append(value)            agrega el valor al final de la lista
list.insert(index,value)      inserta el valor en el indice especificado (los otros valores se corren, nada se borra)
list1.extend(list2)           agrega la lista2 al final de la lista1 (concat)
list.remove(value)            elimina el elemento de la lista igual al value pasado
del lista[0]                  elimina el primer valor de la lista
list.clear()                  vacia la lista
list.sort()                   ordena la lista de forma asendente
lista.sort(reverse=True)      ordena la lista de forma desendente
min(list)                     devuelve el valor mas chico
max(list)                     devuelve el valor mas grande
value in list                 devuelve True si el valor se encuentra en la lista 
value not in list             es la forma correcta del inverso del in
list.index(value)             retorna el primer indice del elemento value, si el valor no esta en la lista rompe
'''


lista = [0,1,42,35,4,5056,6,27,854,92]

lista.sort(reverse=True)

print(4 in lista)
