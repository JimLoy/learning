# Los metodos de clase solo se usan con la clase sin crear una instancia
# como es un metodo de clase POR CONVENCION SE LLAMA cls (hace referencia a la clase)

class Circulo:

    pi = 3.141592

    @classmethod
    def area(cls,radio):
        return cls.pi * (radio ** 2)

res = Circulo.area(14)

print(res)