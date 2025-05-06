from abc import ABC, abstractmethod

from abc import ABC, abstractmethod

class Beverage(ABC):
    @abstractmethod
    def get_description(self):
        pass
    @abstractmethod
    def cost(self):
        pass

class Espresso(Beverage):
    def get_description(self):
        return "Еспресо"
    def cost(self):
        return 2.0

class BeverageDecorator(Beverage):
    def __init__(self, beverage):
        self._beverage = beverage
    def get_description(self):
        return self._beverage.get_description()
    def cost(self):
        return self._beverage.cost()

class MilkDecorator(BeverageDecorator):
    def get_description(self):
        return f"{self._beverage.get_description()} з молоком"
    def cost(self):
        return self._beverage.cost() + 0.5

# Конкретний декоратор: Цукор
class SugarDecorator(BeverageDecorator):
    def get_description(self):
        return f"{self._beverage.get_description()} з цукром"
    
    def cost(self):
        return self._beverage.cost() + 0.2

# Запуск програми
if __name__ == "__main__":
    # Створюємо базовий напій
    espresso = Espresso()
    
    # Додаємо декоратори
    espresso_with_milk = MilkDecorator(espresso)
    espresso_with_milk_and_sugar = SugarDecorator(espresso_with_milk)
    
    # Виводимо результати
    print(
        f"Напій: {espresso.get_description()}," 
        f"ціна: ${espresso.cost()}"
    )
    print(
        f"Напій: {espresso_with_milk.get_description()}," 
        f"ціна: ${espresso_with_milk.cost()}"
    )
    print(
        f"Напій: {espresso_with_milk_and_sugar.get_description()}," 
        f"ціна: ${espresso_with_milk_and_sugar.cost()}"
    )