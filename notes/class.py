# Classes and Objects in Python

sentence = "the quick brown fox jumped over the lazy dog"

print(sentence.upper()) 

class Subject:
    def __init__(self, content, period, teacher, room):
        self.content = content 
        self.period = period
        self.teacher = teacher
        self.room = room
    def __str__(self):
        return f"Name: {self.content}\nPeriod: {self.period}\nTeacher: {self.teacher}\nRoom: {self.room}"

first = Subject("Math", 1, "Mr. Smith", 101)
second = Subject("English", 2, "Ms. Johnson", 102)
third = Subject("History", 3, "Mr. Brown", 103)

print(first)
print(second)

class Pokemon:
    def __init__(self, name, species, hp, dmg):
        self.name = name
        self.species = species
        self.hp = hp
        self.dmg = dmg

    def __str__(self):
        return f"{self.name} is a{self.species}\n and they have {self.hp} HP and do {self.dmg} amount of damage in battle"
    
    def battle(self, opponent):
        while self.hp > 0 and opponent.hp > 0:
            print(f"{self.name} attacks {opponent.name} for {self.dmg} and {opponent.name} has {opponent.hp} HP left.")
            opponent.hp -= self.dmg
            if opponent.hp <= 0:
                print(f"{opponent.name} has fainted! {self.name} wins!")
            else:
                print(f"{opponent.name} attacks {self.name} for {opponent.dmg} and {self.name} has {self.hp} HP left.")
                self.hp -= opponent.dmg
                if self.hp <= 0:
                    print(f"{self.name} has fainted! {opponent.name} wins!")
                    break

fluffy = Pokemon("Fluffy", "Arcanine", 280, 110)
Slimy = Pokemon("Slimy", "Ditto", 100, 70)
Spiky = Pokemon("Spiky", "Jolteon", 150, 100)

Slimy.battle(Spiky)

# What is a class in python?
    # Class is a blueprint for creating objects
# What is an object in python?
    # Object is an instance of a class
# How do python classes relate to python objects?
    # Classes are used to create objects
# How do you create a python class?
    # A class is created using the class keyword followed by the class name
# What are methods?
    # Methods are functions defined inside a class
# How do you create a python object?
    # An object is created by calling the class name followed by parentheses
# How to you call a method for an object?
    # You call a method by using the dot operator followed by the method name
# Why do we use python classes?
    # Classes are used to create objects that can have attributes and methods