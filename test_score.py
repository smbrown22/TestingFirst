from score import * 

def test_add_points():
    game = {"score": 0, "multiplier": 1, "active": True}
    add_points(game, 10)
    assert game["score"] == 10


def test_add_points_with_multiplier():
    game = {"score": 0, "multiplier": 2, "active": True}
    add_points(game, 5)
    assert game["score"] == 10


def test_add_points_inactive_game():
    game = {"score": 0, "multiplier": 2, "active": False}
    add_points(game, 5)
    assert game["score"] == 0


def test_apply_multiplier():
    game = {"score": 0, "multiplier": 1, "active": True}
    apply_multiplier(game, 3)
    assert game["multiplier"] == 3


def test_apply_multiplier_invalid():
    game = {"score": 0, "multiplier": 1, "active": True}
    try:
        apply_multiplier(game, 0)
        assert False
    except ValueError:
        assert True


def test_reset_score():
    game = {"score": 50, "multiplier": 3, "active": True}
    reset_score(game)
    assert game["score"] == 0
    assert game["multiplier"] == 1


def test_is_high_score_true():
    game = {"score": 20, "multiplier": 1, "active": True}
    assert is_high_score(game, 10)


def test_is_high_score_false():
    game = {"score": 5, "multiplier": 1, "active": True}
    assert not is_high_score(game, 10)


def test_is_high_score_invalid_threshold():
    game = {"score": 10, "multiplier": 1, "active": True}
    try:
        is_high_score(game, -1)
        assert False
    except ValueError:
        assert True