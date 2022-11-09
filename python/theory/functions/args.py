#Convencion: * sin espacios y tambien el nombre "args"
def promedio(*args):
    print(args)
    print(type(args))#tuple
    return sum(args) / len(args) # ** es elevar

print(promedio(3,54,4,9,2,48)) 
#Convencion: las funciones se eparan por dos espacios entre ellas


#Kwargs
#Adivina POR CONVENCION ese nombre
def users(**kwargs):
    print(kwargs)
    print(type(kwargs))#dict

users(mumei=[5,7,0,10,5],bae=[1,2,3,1,2])


def combinacion(*args,**kwargs):
    print(args)
    print(kwargs)

combinacion(1,2,85,4,9,5,8,fauna='nice',kroni='flower')