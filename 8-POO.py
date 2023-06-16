class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def saludo(self):
        print(f"Hola mi nombre es {self.name} y  mi edad es {self.age}")


p1 = person("Christian", 20)
p2 = person("Joaquin", 15)

print(p1.name)
print(p1.age)
print(p2.name)
print(p2.age)

p1.saludo()
p2.saludo()
