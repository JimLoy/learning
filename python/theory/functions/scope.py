animal = 'Fox' #Global

def print_animal():
    global animal #Para indicarle a python que no queremos crear una variable sino que usar la que esta
    animal = 'Wolf'#Local
    print(animal,id(animal))

print_animal()
print(animal,id(animal))

#nonlocal para variables no globales pero de un scoupe superior