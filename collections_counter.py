from collections import Counter

shoes = int(input())
shoe_size_list = Counter(input().split())
customers = int(input())
total_price = 0
for i in range(customers):
    customer_size, customer_price = input().split()
    if shoe_size_list[customer_size]:
        total_price += int(customer_price)
        shoe_size_list[customer_size] -= 1
print(total_price)
