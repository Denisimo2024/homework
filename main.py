class Bird():
    def __init__(self, name, voice, color ):
        self.name = name
        self.voice = voice
        self.color = color

    def fly(self):
        print(f"{self.name} летает")

    def eat(self):
        print(f"{self.name} кушает")

    def sing(self):
        print(f"{self.name} поет {self.voice}")

    def info(self):
        print(f"{self.name} - имя")
        print(f"{self.voice} - голос")
        print(f"{self.color} - окрас")



class Pigeon(Bird):
    def __init__(self, name, voice, color, favorie_food):
        super().__init__(name, voice, color)
        self.favorite_food = favorie_food

bird1 = Pigeon("Гоша", "курлык", "серый", "хлебные крошки")

bird1.sing()

bird1.info()