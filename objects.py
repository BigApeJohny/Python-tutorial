lottery_player_dict = {
    'name': 'Rolf',
    'numbers': (4,2,3,4,2,3)
}

class LotteryPlayer:
    def __init__(self, name):
        self.name = name
        self.numbers = (5,9,12,3,1,21)

    def total(self):
        return sum(self.numbers)

player_0 = LotteryPlayer("Rolf")
player_1 = LotteryPlayer("John")
# print(player_0.name == player_1.name)

####################

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def avarage(self):
        return (sum(self.marks) / len(self.marks))

anna = Student("Anna", "MIT")

anna.marks.append(4)
anna.marks.append(3)
anna.marks.append(5)
print(anna.avarage())
