'''
collections.Counter()
A counter is a container that stores elements as dictionary keys, and their counts are stored as dictionary values.
Task
is a shoe shop owner. His shop has  number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are  number of customers who are willing to pay  amount of money only if they get the shoe of their desired size.
Your task is to compute how much money Raghu earned.
Input Format
The first line contains , the number of shoes.
The second line contains the space separated list of all the shoe sizes in the shop.
The third line contains , the number of customers.
The next  lines contain the space separated values of the shoe size desired by the customer and , the price of the shoe.
'''

from collections import Counter
number_of_shoes = int(input())
shoe_sizes = map(int, input().split())
number_of_customers = int(input())

shoes = Counter(shoe_sizes)
income = 0
for i in range(number_of_customers):
    size, price = map(int, input().split())
    if shoes[size]:
        income += price
        shoes[size] -= 1
print(income)
