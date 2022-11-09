num = [1,2,3,4,5]
#num = (1,2,3,4,5) va con las dos

u,d,t,cu,ci = num

print(u)
print(d)
print(t)
print(cu)
print(ci)

#Si los valores de la lista son mas rompe a menos que pongas * en el ultimo valor que tomara el resto

u,d,*todo_el_resto,ci = num
#Si no se van a usar esos valores por convencion *_ como nombre de variable

print(u)
print(d)
print(todo_el_resto) # el * crea una lista con los valores sobrantes
print(ci)
