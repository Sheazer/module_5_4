from functools import total_ordering
@total_ordering

class House:
    houses_history = []
    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __init__(self, name='Name', floors='0'):
        self.name = name
        self.number_of_floors = int(floors)

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей {self.number_of_floors}'

    def __len__(self):
        return self.number_of_floors

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print('Такого этажа нет')
        else:
            for i in range(new_floor):
                print(i + 1, 'floor')

    def __eq__(self, other):
        if not isinstance(other, House):
            other = House()
        return other.number_of_floors == self.number_of_floors

    def __lt__(self, other):
        if not isinstance(other, House):
            other = House()
        return other.number_of_floors > self.number_of_floors

    def __le__(self, other):
        if not isinstance(other, House):
            other = House()
        return other.number_of_floors >= self.number_of_floors

    def __add__(self, other):
        if not isinstance(other, House):
            return House(self.name, self.number_of_floors + other)

    def __radd__(self, other):
        return self.__add__(other)


# h1 = House('ЖК Эльбрус', 10)
# h2 = House('ЖК Акация', 20)
#
# print(h1)
# print(h2)
#
# print(h1 == h2) # __eq__
#
# h1 = h1 + 10 # __add__
# print(h1)
# print(h1 == h2)
#
# h1 += 10 # __iadd__
# print(h1)
#
# h2 = 10 + h2 # __radd__
# print(h2)
#
# print(h1 > h2) # __gt__
# print(h1 >= h2) # __ge__
# print(h1 < h2) # __lt__
# print(h1 <= h2) # __le__
# print(h1 != h2) # __ne__

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)

