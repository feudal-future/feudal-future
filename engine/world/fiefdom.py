from engine.world.hamlets import Hamlets
from engine.world.resources import Resources

class Fiefdom:
    def __init__(self, player_id: str, resources: Resources, hamlets: Hamlets):
        self.player_id = player_id
        self.hamlets = hamlets
        self.resources = resources

    def recruit_villagers(self, villagers: int):
        food_needed = villagers * 10

        if not self.resources.has_enough(food_needed, 0, 0):
            raise ValueError("Not enough resources")
        if not self.hamlets.has_space_for(villagers):
            raise ValueError("Not enough space for villagers")
            
        self.resources.consume(food_needed, 0, 0)
        self.hamlets.add_villagers(villagers)

    def upgrade_hamlet(self):
        wood_needed = self.hamlets.level * 100
        iron_needed = self.hamlets.level * 50

        if not self.resources.has_enough(0, wood_needed, iron_needed):
            raise ValueError("Not enough resources")
        
        self.resources.consume(0, wood_needed, iron_needed)
        self.hamlets.upgrade()
