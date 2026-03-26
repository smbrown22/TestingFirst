game = {
    "score": 0,       # integer, always >= 0
    "multiplier": 1,  # integer, always >= 1
    "active": True    # boolean
}


def add_points(game, amount):
    if game["active"] and amount >= 0:
        game["score"] = amount * game["multiplier"]


def apply_multiplier(game, multiplier):
    if multiplier < 1:
        raise ValueError
    game["multiplier"] = multiplier


def reset_score(game):
    game["score"] = 0
    game["multiplier"] = 1


def is_high_score(game, threshold):
    if threshold < 0:
        raise ValueError
    return game["score"] > threshold
