class Hamlets:
    def __init__(self, level: int, villagers: int):
        self.level = level
        self.villagers = villagers

    def population_limit(self) -> int:
        return self.level * 5
    
    def has_space_for(self, villagers: int) -> bool:
        return self.villagers + villagers <= self.population_limit()
    
    def add_villagers(self, villagers: int):
        self.villagers += villagers
