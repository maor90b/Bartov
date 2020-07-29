class Person:
    def __init__(self, id):
        self.id=id

    def __str__(self):
        return f'id: {self.id}, name: {self.name}, age: {self.age}'

    def __eq__(self, other):
        if self.id==other.id:
            return True
        else:
            return False

    def __gt__(self, other):
        print("__gt__is working")
        if self.age>other.age:
            return True
        else:
            return False

    def __lt__(self, other):
        print("__lt__is working")
        if self.age > other.age:
            return True
        else:
            return False