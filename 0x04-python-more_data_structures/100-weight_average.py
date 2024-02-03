#!/usr/bin/python3
def weight_average(my_list=[]):
    score_weight, weight_sum = 0, 0
    if not my_list:
        return score_weight
    for i in my_list:
        score_weight += (i[0] * i[1])
        weight_sum += i[1]
    return score_weight / weight_sum
