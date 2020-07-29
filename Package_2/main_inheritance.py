from Package_2.Rectangle import Rectangle
from Package_2.Box import Box

rec=Rectangle(7,5)

print("area: ",rec.area())
print("perimeter: ",rec.perimeter())
rec.print()

box=Box(20,10,8)
print("area box: ", box.area())
print("volume: ", box.volume())
box.print()

