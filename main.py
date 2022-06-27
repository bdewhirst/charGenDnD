import dice
import constants as c

def gen_stats() -> list:
    """
    generate six stats using the "4d6 drop the lowest" system
    :return: a list of six integer stats

        note: assignment is up to the user
    """
    stats: list = []
    for nth_stat in range (1, c.N_STATS + 1):
        rolls_for_stat: list = dice.drop_lowest(dice.roll(quantity=4, faces=6))
        a_stat = sum(rolls_for_stat)
        stats.append(a_stat)
    return stats


if __name__ == '__main__':
    print(gen_stats())