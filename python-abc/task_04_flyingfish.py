#!/usr/bin/python3


class Fish:
    """Fish class with methods for swimming and habitat."""
    def swim(self):
        """Method to simulate fish swimming."""
        print("The fish is swimming")

    def habitat(self):
        """Method to describe fish habitat."""
        print("The fish lives in water")


class Bird:
    """Bird class with methods for flying and habitat."""
    def fly(self):
        """Method to simulate bird flying."""
        print("The bird is flying")

    def habitat(self):
        """Method to describe bird habitat."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """FlyingFish class that inherits from Fish and Bird."""
    def fly(self):
        """Method to simulate flying fish soaring."""
        print("The flying fish is soaring!")

    def swim(self):
        """Method to simulate flying fish swimming."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Method to describe flying fish habitat."""
        print("The flying fish lives both in water and the sky!")


# Testing and MRO Exploration
if __name__ == "__main__":
    from task_04_flyingfish import FlyingFish

    flying_fish = FlyingFish()
    flying_fish.swim()
    flying_fish.fly()
    flying_fish.habitat()

    print(FlyingFish.mro())
