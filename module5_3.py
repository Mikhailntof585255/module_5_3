class House:
    def __init__(self,name,number_of_floors:int):
        self.name=name
        self.number_of_floors=number_of_floors

    def __str__(self):
        return f"Название: {self.name} ,количество этажей:{self.number_of_floors}"
    def __eq__(self,other):
        return self.number_of_floors==other.number_of_floors
    def __lt__(self, other):
        return self.number_of_floors==other.number_of_floors
    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors
    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors
    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors
    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors
    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors
    def __add__(self, value):
        return self.number_of_floors+value
    def __radd__(self, other):
        return self+other
    def __iadd__(self, other):
        self.number_of_floors+=other.number_of_floors
        return self

h1=House("ЖК Эльбрус",10)
h2=House("ЖК Акация",20)

print(h1)
print(h2)
print(h1==h2)#eq
h1.number_of_floors=h1.__add__(10)
print(h1)
print(h1==h2)
h1.number_of_floors+=10
print(h1)
h2.number_of_floors=h2.__radd__(10)
print(h2)
print(h1<h2)#lt
print(h1<=h2)#le
print(h1>h2)#gt
print(h1>=h2)#ge
print(h1!=h2)#ne



