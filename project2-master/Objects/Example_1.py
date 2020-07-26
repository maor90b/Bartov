# object oriented programing
# OOP
# class= דבר כללי object= דבר ספציצפי בכללי
#class cr
#attributes: type, id, color, fuel, km
#operations: beep, addfuel


class car:
    #constructor
    def __init__(self,type,color):
        self.type=type
        self.color=color
        self.id=int(input("enter id: "))
        self.fuel=10
        self.km=0



    def beep(self):
        print(f'i am a {self.color} {self.type}: id={self.id} fuel={self.fuel} km={self.km} ')


    def addfuel(self, amount):
        self.fuel+=amount
#main
car1 = car('kia','red')

car1.addfuel(25)
# car1.type = input("enter type: ")
# car1.color = input('enter color: ')
# car1.id = int(input("enter id: "))
# car1.fuel = int(input("enter fuel: "))
# car1.km = int(input("enter km: "))


car1.beep()