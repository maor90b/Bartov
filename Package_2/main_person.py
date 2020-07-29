from Package_2.Person import Person

p1 = Person(10)
p1.name = 'Moshe'
p1.age = 32

p2 = Person(10)
p2.name = "Moshe"
p2.age = 32

print(p1 == p2)
