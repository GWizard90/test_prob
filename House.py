class House:
    def __init__(self, name: str, number_floor: int):
        self.name = name
        self.number_floor = number_floor

    def to_go_(self, new_floor):
        for floor in range(new_floor):
            if floor > self.number_floor:
                print('None floor')
            else:
                print(floor)

    def __str__(self):
        return f'{self.name} and {self.number_floor}'


h_ = House('New_build', 19)
print(h_)
h_.to_go_(21)