class A:
    college_name = "Mythos"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def showData(self):
        print("Name is :- ", self.name)
        print("Marks is :- ", self.marks)

    @classmethod
    def showCollegeName(cls):
        print("College Name is :- ", cls.college_name)

    @staticmethod
    def showDeveloperInfo():
        print("Md. Aasem")

a=A("Aasem",80)
a.showCollegeName()
a.showData()
a.showDeveloperInfo()
