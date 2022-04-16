from abc import ABC, abstractmethod

# The shoe interface


class IShoe(ABC):
    # Abstract interface method
    @abstractmethod
    def get_type():
        return


# BasketBall shoe concrete class implements IShoe interface
class BasketballShoe(IShoe):
    def __init__(self):
        self.size = 20
        self.type = "Basket"

    def get_type(self):
        return self.type


# FootBall shoe concrete class implements IShoe interface
class FootballShoe(IShoe):
    def __init__(self):
        self.size = 15
        self.type = "Football"

    def get_type(self):
        return self.type


# Running shoe concrete class implements IShoe interface
class RunningShoe(IShoe):
    def __init__(self):
        self.size = 25
        self.type = "Running"

    def get_type(self):
        return self.type


# The Factory Class
class ShoeFactory:

    @staticmethod
    def get_shoe(shoe):
        # Static method to get show
        if shoe == "BasketballShoe":
            return BasketballShoe()
        if shoe == "FootballShoe":
            return FootballShoe()
        if shoe == "RunningShoe":
            return RunningShoe()
        return None


# The client Code
class Client():
    def __init__(self):
        return

    def get_factory_shoe_type(self, factory, shoe):
        return factory.get_shoe(shoe)


if __name__ == '__main__':
    shoe_factory = ShoeFactory()

    client = Client()

    shoe1 = "BasketballShoe"
    shoe2 = "FootballShoe"

    print(client.get_factory_shoe_type(shoe_factory, shoe1).get_type())
    print(client.get_factory_shoe_type(shoe_factory, shoe2).get_type())
