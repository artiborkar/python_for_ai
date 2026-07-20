# Q11
# EN: How many even numbers are counted? HI: Kitne even numbers gine gaye?

count = 0
for n in [1, 2, 3, 4, 5, 6]:
    if n % 2 == 0:
        count = count + 1
print(count)