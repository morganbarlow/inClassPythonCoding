sale_prices = [100, 83, 220, 40, 45, 108, 95, 100, 400]

sorted_sale_prices = sorted(sale_prices)

print(sorted_sale_prices)

left_prices = sorted_sale_prices[:len(sorted_sale_prices) // 2]
print(left_prices)

right_prices = sorted_sale_prices[len(sorted_sale_prices) // 2:]
print(right_prices)

right_flip=right_prices[::-1]
print(right_flip)

median=right_flip.pop()
print(median)

