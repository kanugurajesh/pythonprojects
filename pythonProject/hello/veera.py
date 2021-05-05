# i am infinite

# hello guys today we are going to create a program based on constructor let's go with it

class student:
    no_of_leaves = 10

    def __init__(self,man,god,nothing,languages,skills,thing):
        self.man = man
        self.god = god
        self.nothing = nothing
        self.languages = ["python", "java", "c++", "html", "css,javascript", "sql", "c"]
        self.skills = ["fast_typing", "creating dramatic applications", "hacking", "web development",
                       "creating algorithms ", "creating new machine learning,deep learning,ai and data structures"]
        self.thing = ["entrepreneur", "programmer", "technologist", "science", "mathematics", "builder", "thinker",
                      "philosophist", "polymath"]
        # leonardo da vinci
    @classmethod
    def printed_list(cls,string):
        cls.no_of_leaves = string
    @classmethod
    def printed(cls,sting):
        return cls(*sting.split("-"))
    @staticmethod
    def print(yes):
        if yes>7:
            print("you are unbelievable")
        else:
            print("great")

kambesh = student.printed("ori-shunya-anant-0-0-0")
print(kambesh.thing[1])
kambesh.print(8)
kambesh.printed_list(36)
print(kambesh.no_of_leaves)
# see guys we can programs static method only takes the parameters we give to it and in response it gives the value or thing we wrote in the function
# learn this code quicker