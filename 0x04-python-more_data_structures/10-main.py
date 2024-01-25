#!/usr/bin/python3
best_score = __import__('10-best_score').best_score

my_dict = { 'John': 16, 'Alex': 12, 'Bob': 8, 'Mike': 14, 'Molly': 14 }
best_key = best_score(my_dict)
print("Best: {}".format(best_key))
