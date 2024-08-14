class House:
    house_history = []

    def __new__(cls, *args, **kwargs):
        cls.house_history.append(args[0])
        return cls.house_history

    def __init__(self, name, number_floor):
        self.name = name
        self.number_floor = number_floor

    def to_go_(self, new_floor: int):
        for floor in range(new_floor):
            if floor > self.number_floor:
                print('None floor')
            else:
                print(floor)

    def __len__(self):
        return self.number_floor

    def __str__(self):
        return f'Name house: {self.name} and {self.number_floor} floor'

    def __eq__(self, other):
        return self.number_floor == other.number_floor

    def __le__(self, other):
        return self.number_floor <= other.number_floor

    def __gt__(self, other):
        return self.number_floor > other.number_floor

    def __ge__(self, other):
        return self.number_floor >= other.number_floor

    def __ne__(self, other):
        return self.number_floor != other.number_floor

    def __add__(self, values: int):
        return self.number_floor + values

    def __del__(self):
        return f'{self.name}, снесён, но он останется в истории'


h1 = House('ЖК Эльбрус', 10)
print(House.house_history)
h2 = House('ЖК Акация', 20)
print(House.house_history)
h3 = House('ЖК Матрёшки', 20)
print(House.house_history)
del h1
print(House.house_history)
