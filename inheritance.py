class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def avarage(self):
        return sum(self.makrs) / len(self.marks)

    @classmethod
    def friend(cls, origin, friend_name, *args, **kwargs):
        return cls(friend_name, origin.school,*args, **kwargs)

class WorkingStudent(Student):
    def __init__(self, name, school, salary, job_title):
        super().__init__(name, school)
        self.salary = salary
        self.job_title = job_title

anna = WorkingStudent("Anna", "Oxford", salary = 3000.00, job_title = "Dev too")
friend = WorkingStudent.friend(anna, "Greg", salary = 2000, job_title = "Dev")

print(friend.salary)
