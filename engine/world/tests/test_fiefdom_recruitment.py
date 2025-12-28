import pytest
from engine.world.fiefdom import Fiefdom
from engine.world.resources import Resources
from engine.world.hamlets import Hamlets

class TestFiefdomRecruitment:
    @pytest.fixture
    def fiefdom(self):
        resources = Resources(food=1000, wood=1000, iron=1000)
        hamlets = Hamlets(level=10, villagers=10) # capacity 50
        return Fiefdom(player_id="p1", resources=resources, hamlets=hamlets)

    def test_recruit_villagers_success(self, fiefdom):
        # 1 villager costs 10 food
        initial_food = fiefdom.resources.food
        initial_villagers = fiefdom.hamlets.villagers
        
        fiefdom.recruit_villagers(5)
        
        assert fiefdom.resources.food == initial_food - 50
        assert fiefdom.hamlets.villagers == initial_villagers + 5

    def test_recruit_villagers_insufficient_resources(self, fiefdom):
        fiefdom.resources.food = 0
        
        with pytest.raises(ValueError, match="Not enough resources"):
            fiefdom.recruit_villagers(1)
            
        # Ensure no side effects
        assert fiefdom.hamlets.villagers == 10

    def test_recruit_villagers_no_space(self, fiefdom):
        fiefdom.hamlets.villagers = fiefdom.hamlets.population_limit()
        
        with pytest.raises(ValueError, match="Not enough space for villagers"):
            fiefdom.recruit_villagers(1)
       
        # Ensure no side effects - resources should NOT be consumed if space check fails
        # This assumes we implement the check-before-act logic
        assert fiefdom.resources.food == 1000 
