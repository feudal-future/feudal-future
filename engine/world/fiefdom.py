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
