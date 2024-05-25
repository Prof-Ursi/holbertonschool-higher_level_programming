from abc import ABC, abstractmethod

class Animal(ABC):
    """
    Abstract base class for animals.
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method to be implemented by subclasses.
        Returns the sound made by the animal.
        """
        pass

class Dog(Animal):
    """
    Concrete subclass of Animal representing a dog.
    """

    def sound(self):
        """
        Implementation of the sound method for dogs.
        Returns the string "Bark".
        """
        return "Bark"

class Cat(Animal):
    """
    Concrete subclass of Animal representing a cat.
    """

    def sound(self):
        """
        Implementation of the sound method for cats.
        Returns the string "Meow".
        """
        return "Meow"
