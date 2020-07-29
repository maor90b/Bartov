from Package_2.Rectangle import Rectangle
from Package_2.Box import Box

shapes=[]


type=int(input("enter shape type: 1-rec 2-box 0-exit: "))
while type!=0:
    if type==1:
        rec=Rectangle(7,4)
        shapes.append(rec)
    if type==2:
        box=Box(20,10,7)
        shapes.append(box)

    type = int(input("enter shape type: 1-rec 2-box 0-exit: "))



# rec1=Rectangle(7,4)
# rec2=Rectangle(10,8)
#
# box1=Box(10,7,5)
# box2=Box(15,10,9)
# #
# # shapes.append(rec1)
# # shapes.append(box1)
# # shapes.append(rec2)
# # shapes.append(box2)

# shapes.append(5)

for item in shapes:
    item.print()

