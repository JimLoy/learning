'''
dic.keys()                  retorna un lista de las keys del dic
dic.values()                retorna un lista de los valores del dic
dic.items()                 retorna un tupla de los items del dic
dic.get(value1,value2)      retorna el valor de la key value o 'none' o value2 si no existe la key
dic.setdefault(key,value)   si la key no existe la crea con el valor
del dic['key']              borra el valor rompe si la key no existe
dic.pop(key)                borra el valor rompe si la key no existe
dic.clear()                 limpia el diccionario
'''


dic = {'a':1,'b':2}

print(tuple(dic.keys()))
print(tuple(dic.values()))
print(tuple(dic.items()))

