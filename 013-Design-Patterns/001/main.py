from abc import ABC, abstractmethod
from pathlib import Path


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def move(self):
        pass


class Dog(Animal):
    def make_sound(self):
        return "Woof"

    def move(self):
        return "runs"


class Cat(Animal):
    def make_sound(self):
        return "Meow"

    def move(self):
        return "sneaks"


class Cow(Animal):
    def make_sound(self):
        return "Moo"

    def move(self):
        return "walks"


class Duck(Animal):
    def make_sound(self):
        return "Quack"

    def move(self):
        return "swims"


class AnimalFactory(ABC):
    """Abstract factory: creates animals from a list of names."""

    def create_all(self, names):
        return [self.create_animal(name) for name in names]

    @abstractmethod
    def create_animal(self, name):  # factory method
        pass


class SimpleAnimalFactory(AnimalFactory):
    ANIMALS = {"dog": Dog, "cat": Cat, "cow": Cow, "duck": Duck}

    def create_animal(self, name):
        try:
            return self.ANIMALS[name.strip().lower()]()
        except KeyError:
            raise ValueError(f"Unknown animal: {name}") from None


def animals_from_file(path, factory):
    names = [line for line in Path(path).read_text(encoding="utf-8").splitlines() if line.strip()]
    return factory.create_all(names)


factory = SimpleAnimalFactory()
assert isinstance(factory.create_animal(" Dog "), Dog)
try:
    factory.create_animal("dragon")
    assert False
except ValueError:
    pass

if __name__ == "__main__":
    for animal in animals_from_file(Path(__file__).with_name("animals.txt"), factory):
        print(f"{type(animal).__name__}: {animal.make_sound()}, {animal.move()}")
