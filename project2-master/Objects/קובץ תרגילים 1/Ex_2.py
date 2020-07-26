class Circle:
    def __init__(self,radius):
        self.R=radius
        self.PI=3.14


    def S(self):
        return (self.R**2)*self.PI


    def P(self):
       return 2*self.PI*self.R



c=Circle()
c.R=5

print(c.P())
print(c.S())
