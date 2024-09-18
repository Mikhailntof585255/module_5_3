class House:
    def __init__(self,name,number_of_floors:int):
        self.name=name
        self.number_of_floors=number_of_floors

    def __str__(self):
        return f"Название: {self.name} ,количество этажей:{self.number_of_floors}"
    def __eq__(self,other):
        if isinstance(other,House):
            return self.number_of_floors==other.number_of_floors
        elif isinstance(other.int):
            return self.number_of_floors==other
        return self
    def __add__(self, value):
        if isinstance(value, House):
             self.number_of_floors += value.number_of_floors
        elif isinstance(value, int):
             self.number_of_floors += value

    def __radd__(self, other):
       return self.__add__(other)
    def __iadd__(self, other):
       return self.__add__(other)
    def __gt__(self, other):
        if isinstance(other, House):
             return self.number_of_floors > other.number_of_floors
        elif isinstance(other,int):
            return self.number_of_floors > other
    def __ge__(self,other):
        return self.__eq__(other) or self.__gt__(other)
    def __lt__(self, other):
        if isinstance(other, House):
             return self.number_of_floors < other.number_of_floors
        elif isinstance(other,int):
            return self.number_of_floors < other
    def __le__(self, other):
        return self.__eq__(other) or self.__lt__(other)
    def __ne__(self, other):
        return not self.__eq__(other)




h1=House("ЖК Эльбрус",10)
h2=House("ЖК Акация",20)
print(h1)
print(h2)
print(h1==h2)
h1.__add__(10)
print(h1)
print(h1==h2)
h1.__iadd__(10)
print(h1)
h2.__radd__(10)
print(h2)
print(h1>h2)
print(h1>=h2)
print(h1<h2)
print(h1<=h2)
print(h1!=h2)
