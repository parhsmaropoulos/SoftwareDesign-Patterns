from abc import ABC, abstractmethod

# The abstract car factory interfcae


class ICarFactory(ABC):
    # Abstraact car factory interface method
    @abstractmethod
    def get_car_stats(car):
        return


# Normal Car interface
class INormalCar(ABC):
    @abstractmethod
    def get_stats():
        return


# Sedan class implement Normal car Interface
class Sedan(INormalCar):
    def __init__(self):
        self._top_speed = 100
        self._zero_to_100 = 10
        self._weight = 5

    def get_stats(self):
        return {
            'top speed (km/h)': self._top_speed,
            '0-100 (s)': self._zero_to_100,
            'Weight (tones)': self._weight,
        }


# Jeep class implement Normal car Interface
class Jeep(INormalCar):
    def __init__(self):
        self._top_speed = 150
        self._zero_to_100 = 12
        self._weight = 10

    def get_stats(self):
        return {
            'top speed (km/h)': self._top_speed,
            '0-100 (s)': self._zero_to_100,
            'Weight (tones)': self._weight,
        }


# Roadster class implement Normal car Interface
class Roadster(INormalCar):
    def __init__(self):
        self._top_speed = 200
        self._zero_to_100 = 5
        self._weight = 3

    def get_stats(self):
        return {
            'top speed (km/h)': self._top_speed,
            '0-100 (s)': self._zero_to_100,
            'Weight (tones)': self._weight,
        }


# Factory Class
class NormalCarFactory:
    @staticmethod
    def get_car(normalcar):
        try:
            if normalcar == 'Sedan':
                return Sedan()
            if normalcar == 'Jeep':
                return Jeep()
            if normalcar == 'Roadster':
                return Roadster()
            raise Exception("Normal Car not Found")
        except Exception as e:
            print(e)
        return None


# The electric car interface
class IECar(ABC):
    @abstractmethod
    def get_stats():
        return


# Hybrid class implement Electric car Interface
class Hybrid(IECar):
    def __init__(self):
        self._top_speed = 100
        self._zero_to_100 = 8
        self._weight = 6

    def get_stats(self):
        return {
            'top speed (km/h)': self._top_speed,
            '0-100 (s)': self._zero_to_100,
            'Weight (tones)': self._weight,
        }


# E_Roadster class implement Electric car Interface
class E_Roadster(IECar):
    def __init__(self):
        self._top_speed = 180
        self._zero_to_100 = 6
        self._weight = 3

    def get_stats(self):
        return {
            'top speed (km/h)': self._top_speed,
            '0-100 (s)': self._zero_to_100,
            'Weight (tones)': self._weight,
        }


# E_Jeep class implement Electric car Interface
class E_Jeep(IECar):
    def __init__(self):
        self._top_speed = 140
        self._zero_to_100 = 10
        self._weight = 11

    def get_stats(self):
        return {
            'top speed (km/h)': self._top_speed,
            '0-100 (s)': self._zero_to_100,
            'Weight (tones)': self._weight,
        }


# Factory Class
class ElectricCarFactory:
    @staticmethod
    def get_car(electriccar):
        try:
            if electriccar == 'Hybrid':
                return Hybrid()
            if electriccar == 'E_Roadster':
                return E_Roadster()
            if electriccar == 'E_Jeep':
                return E_Jeep()
            raise Exception("Normal Car not Found")
        except Exception as e:
            print(e)
        return None


# Abstract Car Fuctory Concrete calss
class CarFactory(ICarFactory):
    @staticmethod
    def get_car(car):
        try:
            if car in ['Sedan', 'Jeep', 'Roadster']:
                return NormalCarFactory().get_car(car)
            if car in ['Hybrid', 'E_Roadster', 'E_Jeep']:
                return ElectricCarFactory().get_car(car)
            raise Exception("No compat factory found")
        except Exception as e:
            print(e)
        return None


# Client Code
class Client():

    def __init__(self):
        return

    def get_stats_from_car(self, car):
        car = CarFactory.get_car(car)
        print(f"{car.__class__} : {car.get_stats()}")


if __name__ == '__main__':
    client = Client()

    n_car_1 = 'Sedan'
    n_car_2 = 'Roadster'

    e_car_1 = 'Hybrid'
    e_car_2 = 'E_Jeep'

    cars = []
    cars.append(n_car_1)
    cars.append(n_car_2)
    cars.append(e_car_1)
    cars.append(e_car_2)

    for i in range(len(cars)):
        client.get_stats_from_car(cars[i])
