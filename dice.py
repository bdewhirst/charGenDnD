import random

# import constants as c


# def setup(seed: int=317325) -> None:
#     """
#     specify a seed for repeatability during development only
#
#     :param seed: optional argument to specify a different seed value
#     :return: returns nothing
#     """
#     random.seed(a=seed)


def roll(quantity: int=1, faces: int=6, ) -> list:
    """
    roll a specified number of dice with specified number of faces and return rolls as a list

    :param quantity: specify the number of dice to roll
    :param faces: specify the number of die faces-- for example if we're rolling 2d6 this would be 2
    :return: return a list with [quantity] ints (each between 1 and [faces])
    """
    if (quantity < 1 or faces < 1):
        raise ValueError("invalid parameters passed")
    # setup()
    output: list=[]
    for rolls in range(0, quantity):
        die = random.randint(1, faces)
        output.append(die)
    return output


def drop_lowest(rolls: list) -> list:
    """
    Given a list of ints, sort and drop the lowest, then return the result
    :param rolls: list of integer-value die rolls
    :return: list of N-1 rolls
    """
    n_rolls = len(rolls)
    if n_rolls < 2:
        raise ValueError("to meaningfully drop the lowest, there must be two or more rolls")
    rolls.sort()
    rolls_to_keep: int = rolls[1:n_rolls]
    return rolls_to_keep
