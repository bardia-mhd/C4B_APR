# coding: utf-8
import sys

__author__ = 'buyvich'

SUCCESS_HACK = 100
UNSUCCESS_HACK = 50
MAX_SCORES = 20000

def get_win_places(scores):
    res = []
    k = (scores//50)%475
    for _ in range(25):
        k = (k * 96 + 42)%475
        res.append(26 + k)
    return res

def find_success_hack_count(place, current_scores, min_goal):
    """
    >>> find_success_hack_count(239, 10880, 9889)
    0
    >>> find_success_hack_count(26, 7258, 6123)
    2
    >>> find_success_hack_count(493, 8000, 8000)
    24
    >>> find_success_hack_count(101, 6800, 6500)
    0
    >>> find_success_hack_count(329, 19913, 19900)
    8
    """
    goal = min_goal
    while True:
        if not (current_scores-goal)%50:
            if place in get_win_places(goal):
                break
        goal += 1
    return (max(0, goal-current_scores)+50)//100


if __name__ == '__main__':
    place, current_scores, goal = sys.stdin.readline().strip().split(' ')
    success_hacks_count = find_success_hack_count(int(place),
                                                  int(current_scores),
                                                  int(goal))
    sys.stdout.write('%s' % success_hacks_count)


# vim:ts=4:sts=4:sw=4:tw=85:et: