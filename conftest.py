import pytest
from health import take_damage


@pytest.fixture
def player():
    return {"health":100, "max_health":100, "alive":True}


def test_take_damage(player):
    result = take_damage(player, 30)
    assert result["health"] is 70


def test_player_dies(player):
    result = take_damage(player, 100)
    assert result["alive"] is False
