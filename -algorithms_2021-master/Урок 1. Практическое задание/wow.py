db_dict = {'a': 200, 'b': 100, 'c': 4000, 'd': 1000, 'e': 250, 'f': -10000, 'g': 500}
def test(dict_obj):
    max_income = 0
    for val1 in dict_obj.values():
        max_income = val1
        for val2 in dict_obj.values():
            if val2 > max_income:
                max_income = val2

    return max_income

print(test(db_dict))