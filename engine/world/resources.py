class Resources:
    def __init__(self, food: int, wood: int, iron: int):
        self.food = food
        self.wood = wood
        self.iron = iron

    def has_enough(self, food: int, wood: int, iron: int) -> bool:
        return self.food >= food and self.wood >= wood and self.iron >= iron

    def consume(self, food: int, wood: int, iron: int):
        self.food -= food
        self.wood -= wood
        self.iron -= iron
