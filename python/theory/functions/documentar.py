# Docstring: es un comentario que se pone en la primera linea de la funcion 

def suma(n_1,n_2):
    """
    La funcion suma 2 numeros enteros

    Args:
    n_1 (int)
    n_2 (int)

    Se retorna la suma de los argumentos

    >>> suma(10,20)
    300

    >>> suma(100,200)
    300
    """
    return n_1 + n_2

# Se almacena en la propiedad __doc__
# Solo los Modulos, Clases, Metodos y Funciones tiene esta propiedad (porque son los objetos documentables)
#print(suma.__doc__)
#print(help(suma))
# Las dos formas te retornan la "documentacion" de la funcion suma

#POR CONVENCION SE HACE CON COMILLAS DOBLES


# python -m doctest documentar.py  para ejecutar los test (la primera va a fallar)