# OPEN/CLOSED PRINCIPLE

from abc import ABC, abstractmethod

# Every subclass of type Person must implement the abstractmethods


class Person(ABC):

    @abstractmethod
    def Speak(self):
        pass

#  Implements class Person


class Greek(Person):

    # Initialize greek object
    def __init__(self):
        self.goodmorning = "καλημέρα"
        self.country = "Greece"
        pass

    # overriding abstract method
    def Speak(self):
        print("In", self.country, "we say", self.goodmorning, " !")
        return

#  Implements class Person


class English(Person):

    # Initialize greek object
    def __init__(self):
        self.goodmorning = "goodmorning"
        self.country = "England"
        pass

    # overriding abstract method
    def Speak(self):
        print("In", self.country, "we say", self.goodmorning, " !")
        return


class Russian(Person):
    # Initialize greek object
    def __init__(self):
        self.goodmorning = "доброе утро"
        self.country = "Russia"
        pass

    # overriding abstract method
    def Speak(self):
        print("In", self.country, "we say", self.goodmorning, " !")
        return

# Class that call the speak func of a given list of persons


class Greeter:
    def __init__(self):
        pass

    def World_Speak(self, persons):
        for i in range(len(persons)):
            persons[i].Speak()
        return


if __name__ == '__main__':
    greeter = Greeter()
    persons = []

    gr1 = Greek()
    eng1 = English()
    rus1 = Russian()

    persons.append(gr1)
    persons.append(eng1)
    persons.append(rus1)

    print("Lets hear everyone! :")
    greeter.World_Speak(persons)
