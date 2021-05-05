# i am infinite
# hello!
class student:
    pass
import rpr
harr = student
larr = student
print(harr,larr)
harr.name = "hello"
print(harr.name)
larr.manliness = "name"
print(larr.manliness)
print(student)
print(student())
print(student.__name__)
print(__name__)
print(rpr.__name__)
# hello now we are going to learn about instance and class variables
class Employ:
    hello = "man"
    pass
shiva = Employ()
manliness = Employ()
shiva.valour = "trishul"
shiva.state = "almighty"
manliness.definition = "the state of being a man"
print(shiva.valour)
print(shiva.hello)
print(manliness.definition)
print(manliness.hello)
Employ.hello="the highest man"
print(Employ.hello)
print(shiva.hello)
shiva.hello="the infinite"
print(Employ.hello)
print(shiva.hello)
# class variables can be  change using only class name
# using objects you cannot change class variables
from playsound import playsound
playsound("")