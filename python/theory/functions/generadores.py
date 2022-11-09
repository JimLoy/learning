#Funcion que retorna objetos que podemos iterar sin que esta finalice

def pares(): # Esta funcion es un generador "Lazy iterator", se usa para no guardar en memoria variables inecesariamente
    for num in range(0,100,2):
        yield num    #es como return pero no termina la ejecucion de la funcion sino que la pausa


#for par in pares():
#    print(par)

generador = pares()

#print(next(generador)) --> 0
#print(next(generador)) --> 2
#print(next(generador)) --> 4
#print(next(generador)) --> 6
# Se consume bajo demanda

while True:
    try:
        print(next(generador))
    except StopIteration: # StopIteration es el nombre del error que sale cuando se le hace un next a un generador que ya termino
        print('El generador termino.')
        break
# Esto es el try catch