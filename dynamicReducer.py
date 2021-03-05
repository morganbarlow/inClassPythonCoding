import operator
from functools import reduce

def dynamic_reducer(list_to_reduce, operator_to_use):
    operators = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
    }

    return reduce((lambda total, element: operators[operator_to_use](total, element)), list_to_reduce)

print(dynamic_reducer([1,2,3], "+"))
print(dynamic_reducer([1,2,3], "-"))
print(dynamic_reducer([1,2,3], "*"))
print(dynamic_reducer([1,2,3], "/"))

