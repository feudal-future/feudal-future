from engine.world.resources import Resources

class TestResources:
    def test_has_enough_true(self):
        res = Resources(100, 100, 100)
        assert res.has_enough(50, 50, 50) is True

    def test_has_enough_false(self):
        res = Resources(10, 10, 10)
        assert res.has_enough(50, 50, 50) is False

    def test_consume_success(self):
        res = Resources(100, 100, 100)
        res.consume(50, 20, 10)
        assert res.food == 50
        assert res.wood == 80
        assert res.iron == 90
    
    def test_consume_blindly(self):
        res = Resources(10, 10, 10)
        res.consume(50, 0, 0)
        assert res.food == -40
