num = 1483496854
dig_num = 0

while num >= 1:
    dig_num += 1
    num = num / 10
else:
    print('Fin del while', dig_num)

#cuando la condicion del while sea false, se ejecuta el else