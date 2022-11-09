
#POR CONVENCION: EL NOMBRE EN CAMELCASE Y EN SINGULAR


'''
Existen dos tipos de atributos
de clase: los tiene todas las instancias
de instancia: solo lo tiene esa instancia
'''
class User:
    # atributos de clase
    name = '-' 
    email = '-'

#print(User.name)
#User.name = 'New Value'
#print(User.name)

user_1 = User()
user_1.name = 'Loy'
print(user_1.__dict__) # Los atributos del objeto (meta atributo dict)

