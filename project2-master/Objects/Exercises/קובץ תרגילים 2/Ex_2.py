class Bus:
    def __init__(self,size):
        self.size=size
        self.num_of_passangers=0
        self.seats=['free' for i in range(self.size)]


    def getOn(self,name):
        for i in range(self.size):
            if self.seats[i]=='free':
                self.seats[i]==name
                self.num_of_passangers+=1
                break
            else:
                print('the bus is full')

    def getOf(self,name):
        for i in range(self.size):
            if self.seats[i] ==name:
                self.seats[i] == 'free'
                self.num_of_passangers -=1
                break
            else:
                print(name+ 'is not on the bus')




    def __str__(self):
        return f'size: {self.size}, number of passangers: {self.num_of_passangers}'

bus=Bus(10)
bus.getOn('aa')

bus.getOn('bb')

bus.getOn('cc')
print(bus)

