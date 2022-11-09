name = 'Jaz'
last_name = 'Loy'

full_name = name + ' ' + last_name + '.'
print(full_name)

#Porcentaje ese
full_name = '%s %s.' %(name,last_name)
print(full_name)


#{} placeholder
full_name = '{} {}.'.format(name,last_name)
print(full_name) 

full_name = '{l} {n}.'.format(n=name,l=last_name)
print(full_name) 

#Fstring
full_name = f'{name} {"Loy"}.'
print(full_name) 

print(name,last_name,'.',sep='//') 
#La funcion print divide sus valores con un espacio
#sep es el caracter que separara los vaolres