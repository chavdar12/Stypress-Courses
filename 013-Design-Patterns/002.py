from abc import ABC, abstractmethod
from decimal import Decimal


class Beverage(ABC):
    @abstractmethod
    def description(self):
        pass

    @abstractmethod
    def price(self):
        pass


class Coffee(Beverage):
    def description(self):
        return "Coffee"

    def price(self):
        return Decimal("2.50")


class Decaf(Beverage):
    def description(self):
        return "Decaf"

    def price(self):
        return Decimal("2.80")


class AddOn(Beverage):
    """Decorator: wraps a beverage, extends its description and price."""
    NAME = ""
    PRICE = Decimal("0")

    def __init__(self, beverage):
        self.beverage = beverage

    def description(self):
        return f"{self.beverage.description()}, {self.NAME}"

    def price(self):
        return self.beverage.price() + self.PRICE


def add_on(name, price):
    return type(name.title().replace(" ", ""), (AddOn,), {"NAME": name, "PRICE": Decimal(price)})


Cream = add_on("cream", "0.50")
VeganCream = add_on("vegan cream", "0.70")
CowMilk = add_on("cow milk", "0.30")
SoyMilk = add_on("soy milk", "0.50")
CoconutMilk = add_on("coconut milk", "0.60")
AlmondMilk = add_on("almond milk", "0.60")
Cinnamon = add_on("cinnamon", "0.20")

order = Cinnamon(AlmondMilk(Decaf()))
assert order.description() == "Decaf, almond milk, cinnamon"
assert order.price() == Decimal("3.60")
assert Cream(Cream(Coffee())).price() == Decimal("3.50")

if __name__ == "__main__":
    for drink in (Coffee(), SoyMilk(Coffee()), order, VeganCream(CoconutMilk(Coffee()))):
        print(f"{drink.description():40} {drink.price():>5} lv.")
