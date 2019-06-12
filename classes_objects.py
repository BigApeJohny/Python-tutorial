lottery_player_dict = {
    'name': 'Rolf',
    'numbers': (5,3,4,43,12)
}

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def avarage(self):
        return sum(self.marks) / len(self.marks)

    @classmethod
    def go_to_school(cls):
        print("I am going to school.")
        print("I am a{}".format(cls))

anna = Student("Anna", "UŚ")
anna.marks.append(5)
anna.marks.append(3.4)
anna.go_to_school()
