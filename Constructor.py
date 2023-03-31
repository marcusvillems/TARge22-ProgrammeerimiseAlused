"""Constructor exercise."""


class Empty:
    """An empty class without constructor."""
    pass


class Person:
    """Represent person with firstname, lastname and age."""
    def __init__(self):
        """Person constructor."""
        self.firstname = ""
        self.lastname = ""
        self.age = 0


class Student:
    """Represent student with firstname, lastname and age."""
    def __init__(self, firstname: str, lastname: str, age: int):
        """Student constructor."""
        self.firstname = firstname
        self.lastname = lastname
        self.age = age


if __name__ == '__main__':
    # empty usage
    empty = Empty()
    print(empty)
    # 3 x person usage
    person = Person()
    person.firstname = "Tõnis"
    person.lastname = "Niinemets"
    person.age = 60
    print(person.firstname)
    print(person.lastname)
    print(person.age)
    # 3 x student usage
    student = Student("Jeesus", "Kristus", 3000)
    print(student.firstname)
    print(student.lastname)
    print(student.age)
