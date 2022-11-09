#Por convencion son cuatro espacios para los bloques de codigo de los condicionales

res = 6

if res == 10 :
    print(True)
else:
    print(False)

# ELIF

if res == 10:
    print('Perfect')
elif  res == 9 or res == 8:
    print('Aprobadisimo')
elif  res == 7:
    print('Aprobado')
else:
    print('Desaprobado')

# TERNARIO
#si no tiene el else se rompe

color = 'Verde' if res >= 7 else 'Rojo'

print(color)