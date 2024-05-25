#!/usr/bin/python3

class SwimMixin:
    """SwimMixin class with method for swimming"""
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """FlyMixin class with method for flying"""
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class inheriting from SwimMixin & FlyMixin,
    able to swim, fly and roar."""
    def roar(self):
        print("The dragon roars!")


# Testing the Dragon's Abilities
if __name__ == "__main__":
    draco = Dragon()
    draco.swim()
    draco.fly()
    draco.roar()
