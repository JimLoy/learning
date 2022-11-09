#Cuando el return tiene mas de un valor devuelve los valores como una tupla
def suma(n1, n2):
    return 'The result is:',n1 + n2

num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))

mes,num = suma(num1, num2)
print(mes,num)

#por convencion cuando se declara un valor por defecto no se usan espacios
def area_circulo(radio,pi=3.14):
    return pi * (radio ** 2) # ** es elevar

print(area_circulo(pi=3.1415,radio=20)) 


