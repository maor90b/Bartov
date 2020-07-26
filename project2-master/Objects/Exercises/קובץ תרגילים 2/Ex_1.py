class Animal:
    def __init__(self,name):
        self.name=name
        self.hungry=5
        self.energy=5

    def __str__(self):
        return f'name of animal = {self.name},energy={int(self.energy)},hunger={int(self.hungry)}'

    def eat(self,gr):
        count=0
        while self.hungry>0 and gr>=50:
            self.hungry-=1
            gr-=50
            count+=1
            if count%2==0:
                self.energy-=1


        if self.hungry<=0:
            self.hungry=0
            print('the animal is not hungry anymore')
        if self.energy<=0:
            self.energy=0


    def play(self,tp):
        while tp>=10 and self.energy>=0:
            tp-=10
            self.energy-=2
            self.hungry+=2
        if self.energy<=0:
            self.energy=0
            print('the animal has no power')
        if self.hungry>=10:
            self.hungry=10


    def rest(self,tr):

        if self.energy+tr//20>=10 and self.hungry+tr//30<10:
            self.energy=10
            self.hungry+=tr//30
        if self.hungry+tr//30>=10 and self.energy+tr//20<10:
            self.hungry=10
            self.energy+=tr//20
        if self.hungry+(tr//30)>=10 and self.energy+(tr//20)>=10:
            if (10-self.energy)*20>(10-self.hungry)*30:
                self.energy+=(((10-self.hungry)*30)//20)
                self.hungry=10
            if(10-self.hungry)*30 > (10-self.energy)*20:
                self.energy=10
                self.hungry+=(((10-self.energy)*20)//30)
        if self.energy+tr//20<10 and self.hungry+tr//30<10:
            self.energy += tr // 20
            self.hungry += tr // 30




Animal_1=Animal(input('enter name of animal: '))

action = int(input("enter action: "))
while action!=0:
    if action>3 or action<0:
        print('invalid action')

    if action == 1:
        Animal_1.eat(int(input('enter grams amount: ')))
        print(Animal_1)

    if action==2:
        Animal_1.play(int(input('enter play time:')))
        print(Animal_1)

    if action==3:
        Animal_1.rest(int(input('enter time rest:')))
        print(Animal_1)
    action = int(input("enter action: "))
