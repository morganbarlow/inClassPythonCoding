from functools import reduce

def manual_exponent(base,power):
  rules = [base]*power
  return reduce(lambda total, element: total*element, rules )


print(manual_exponent(2,3)) # 8
print(manual_exponent(10,2))# 100
print(manual_exponent(2,5))
print(manual_exponent(5,2))
print(manual_exponent(3,2))