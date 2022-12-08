class Person:
    def __init__(self):
        self.name = None
        self.position = None
        self.date_of_birth = None
    def __str__(self):
        return f'{self.name} born on {self.date_of_birth} works at {self.position}'

    def new(self):
        return PersonBuilder()

class PersonBuilder:
    def __init__(self):
        self.person = Person()

    def build(self):
        return self.person

class PersonalInfoBuilder(PersonBuilder):
    def called(self,name):
        self.person.name = name
        return self

class PersonalJobBuilder(PersonalInfoBuilder):
    def works_as_a(self,position):
        self.person.position = position
        return self

class PersonBirthDateBuilder(PersonalJobBuilder):
    def born(self,date_of_birth):
        self.person.date_of_birth = date_of_birth
        return self

if __name__ == '__main__':
    pb = PersonBirthDateBuilder()
    me = pb.called("Bipin").works_as_a("software Developer").born("11/07/1989").build()
    print(me)
