class Animal: #класс родитель для зверушек
    def __init__(self, name):
        self.alive = True
        self.fed = False
        self.name = name


class Plant:#клас родитель для растений
    def __init__(self, name, edible=False):
        self.edible = edible
        self.name = name


class Mammal(Animal):#млекопитающие-класс наследник зверушек
    def eat(self, food):
        if isinstance(food, Plant):
            if food.edible:
                print(f"{self.name} съел {food.name}")
                self.fed = True
            else:
                print(f"{self.name} не стал есть {food.name}")
                self.alive = False
        else:
            print(f"{food.name} не является растением. {self.name} не может это съесть.")


class Predator(Animal):#хищники-класс наследник зверушек
    def eat(self, food):
        if isinstance(food, Plant):
            if food.edible:
                print(f"{self.name} съел {food.name}")
                self.fed = True
            else:
                print(f"{self.name} не стал есть {food.name}")
                self.alive = False
        else:
            print(f"{food.name} не является растением. {self.name} не может это съесть.")


class Flower(Plant):#цветы-класс наследник растений
    def __init__(self, name):
        super().__init__(name, edible=False)


class Fruit(Plant):#фрукты-класс наследний растений
    def __init__(self, name):
        super().__init__(name, edible=True)


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
