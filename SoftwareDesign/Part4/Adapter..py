from abc import ABC, abstractmethod
import time
import random

# Clone A Interface


class ICloneA(ABC):
    @abstractmethod
    def clone(self, speak, age, height):
        return

# Clone B Interface


class ICloneB(ABC):
    @abstractmethod
    def clone(self, region, birthday):
        return


# A Class human Clone  from company A
class CloneA(ICloneA):

    # a static variable indicating the last time a clone was manufactured
    last_time = int(time.time())

    def __init__(self):
        self.speak = ''
        self.age = 0
        self.height = 0

    def clone(self, speak, age, height):
        self.speak = speak
        self.age = age
        self.height = height
        # If not busy then clone a human with characheristics

        now = int(time.time())
        if now > int(CloneA.last_time + 1):
            CloneA.last_time = now
            return True
        return False

# A Class human Clone  from company B


class CloneB(ICloneB):

    # a static variable indicating the last time a cube was manufactured
    last_time = int(time.time())

    def clone(self, region, birthday):
        self.region = region
        self.birthday = birthday
        # If not busy then clone a human with characheristics

        now = int(time.time())
        if now > int(CloneB.last_time + 2):
            CloneB.last_time = now
            return True
        return False


# An adapter for CloneB so it can become like Clone A
# Implement ICloneA interface
class CloneBAdapter(ICloneA):

    def __init__(self):
        self.clone_obj = CloneB()
        self.speak = self.age = self.height = 0

    def clone(self, speak, age, height):
        self.speak = speak
        self.age = age
        self.height = height

        if self.speak == 'english':
            region = 'West'
        else:
            region = 'East'

        birthday = 2022 - age
        success = self.clone_obj.clone(region, birthday)

        return success


# Client Code


class Client():
    def __init__(self):
        return

    def clone_people(self, number_of_clones):
        COUNTER = 0
        TOTALCLONES = number_of_clones

        while COUNTER < TOTALCLONES:
            # Clone 10 ppl from the first
            # available company

            SPEAKING_LANGUAGE = ['english', 'chinnesse', 'russian']
            SPEAK_INDEX = random.randint(0, 2)
            HEIGHT = 1.5 + random.random()  # Randon height from 1.5 to 2.5
            AGE = random.randint(5, 20)
            CLONE = CloneA()
            SUCCESS = CLONE.clone(SPEAKING_LANGUAGE[SPEAK_INDEX], AGE, HEIGHT)

            if SUCCESS:
                print(
                    f"Company A Clone id: {id(CLONE)}, "
                    f"Age: {CLONE.age}, Height: {CLONE.height}, Speaks: {CLONE.speak} ")
                COUNTER += 1
            else:
                print("Company A is unavailable, trying Company B")
                CLONE = CloneBAdapter()
                SUCCESS = CLONE.clone(
                    SPEAKING_LANGUAGE[SPEAK_INDEX], AGE, HEIGHT)
                if SUCCESS:
                    print(
                        f"Company B Clone id: {id(CLONE)}, "
                        f"Age: {CLONE.age}, Height: {CLONE.height}, Speaks: {CLONE.speak} ")
                    COUNTER += 1
                else:
                    print("Company B is unavailable, trying Company A")
            time.sleep(1)
        print(f"{TOTALCLONES} clones have beed cloned!")


if __name__ == '__main__':
    client = Client()
    client.clone_people(10)
