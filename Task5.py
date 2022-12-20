# Реализуйте алгоритм перемешивания списка.

import random

def get_list(numbers, negative_range, positive_range):
    return [random.randint(negative_range, positive_range) for i in range(numbers)]


def shuffle_list(list1):
    return random.shuffle(list1)


numbers = 5 
negative_range = -10
positive_range = 10

sh_list = get_list(numbers, negative_range, positive_range)
print(sh_list)
shuffle_list(sh_list)
print(sh_list)
