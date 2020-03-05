# Dictionaries use curly brackets
monthCOnversions = {"Jan": "January", "Feb": "February"}
# Key is unique and is before the : and works as the index finder
print(monthCOnversions["Feb"])
# Another method is get but get is usefull as you can add default value next to the key you want
print(monthCOnversions.get("O", "October"))


# TO make a function
def name_of_function(x):
    if x > 10:
        print("Number bigger than 10")
    elif x < 10:
        print("Number smaller than 10 ")
    else:
        print("Number is 10")


name_of_function(10)

# in python we have the and
x = "DAve"
y = "Batissta"
if x == "DAve" and y == "Batista":
    print("Batista Bomb")
else:
    print("Wrestler")


# how to make a class
class Student:
    # this is how to create a constructor it has to take self as a argument evrytime and in all its functions
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation
        # Self is an argument in all class related methods unlike php

    def checkGpa(self):
        if self.gpa > 3.0:
            return "this boy good"
        return "this boy bad"
