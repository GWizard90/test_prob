class House:
    def __init__(self, name: str, number_floor: int):
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


h_ = House('New_build', 19)
h_2 = House('Serpika', 12)
print(h_), print(h_2)
h_.to_go_(21), h_2.to_go_(14)
print(len(h_)), print(len(h_2))
h_ = h_ + 12
h_2 = h_2 + 5
print(h_)
print(h_2)
print(h_ > h_2)
