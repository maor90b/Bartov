from Package_2.Rectangle import Rectangle


class Box(Rectangle):
    def __init__(self, length, width, height):
        Rectangle.__init__(self,length,width)
        self.height=height


    def area(self):
        return super().area()*2 + self.width*self.height*2+self.length*self.height*2


    def volume(self):
        return super().area()*self.height

    def print(self):
        super().print()
        print("height: ",self.height)


