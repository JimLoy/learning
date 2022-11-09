#Los decoradores son funciones que reciben como argumento una funcion y retorna una funcion
#Es para extender funcionalidades de funciones que no podemos/queremos modificar

'''
a -> funcion principal
b -> funcion a decora
c -> funcion decorada
'''

def a_function(b_function):

    def c_function(*args, **kwargs):
        print(*args, **kwargs)
        res = b_function(*args, **kwargs)
        return res

    return c_function

#le dice a python que a_function va a resivir como arg la funcion saludar
@a_function
def saludar():
    print('hi')


@a_function
def suma(n_1,n_2):
    return n_1 + n_2

#a_function() rompe

saludar()
result = suma(12,10)
print(result)
#ejecutan la funcion a_function