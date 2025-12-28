from engine.world.hamlets import Hamlets

class TestHamlets:
    def test_population_limit(self):
        hamlet = Hamlets(level=1, villagers=0)
        assert hamlet.population_limit() == 5

    def test_has_space_for_true(self):
        hamlet = Hamlets(level=1, villagers=0)
        assert hamlet.has_space_for(5) is True

    def test_has_space_for_false(self):
        hamlet = Hamlets(level=1, villagers=4)
        assert hamlet.has_space_for(2) is False

    def test_add_villagers_success(self):
        hamlet = Hamlets(level=1, villagers=0)
        hamlet.add_villagers(5)
        assert hamlet.villagers == 5

    def test_add_villagers_blindly(self):
        hamlet = Hamlets(level=1, villagers=4)
        hamlet.add_villagers(2)
        assert hamlet.villagers == 6
