# make_counter() banao jo har call par badhta number de (closure se).

# not clear  

def make_counter():
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter


c = make_counter()

print(c())   # 1
print(c())   # 2
print(c())   # 3