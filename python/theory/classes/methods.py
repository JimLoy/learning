# Para que una funcion sea considerada un metodo tiene que tener un parametro que haga referencia al propio objeto, en este caso los user1 y user2 (osea this)
# POR CONVENCION ES self

class User:

    def __init__(self, name, password): # Sobreescribiendo el metodo init heredado del objeto Object
        self.name = name
        self.password = password
    # Esta es la forma de fuerza bruta de hacer esto
    #def inicializar(self, name, password):
    #    self.name = name
    #    self.password = password


user1 = User('Carlos',21424)
user2 = User('Roberto', 6540)

print(user1.__dict__)
print(user2.__dict__)

#user1.inicializar('Carlos',21424)
#user2.inicializar('Roberto', 6540)

#print(user1.__dict__)
#print(user2.__dict__)