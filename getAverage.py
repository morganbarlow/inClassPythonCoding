from functools import reduce

my_list = [1, 2, 3, 4, 5, 6]
list_two = [2, 3, 6, 9, 12]


def get_average(list_to_average):
    total = reduce(lambda total, element: total + element, list_to_average)
    average = total / len(list_to_average)
    return average


# def get_average(list_to_average):
#   total =  sum(list_to_average)
#   average = total / len(list_to_average)
#   return average

print(get_average(my_list))
print(get_average(list_two))