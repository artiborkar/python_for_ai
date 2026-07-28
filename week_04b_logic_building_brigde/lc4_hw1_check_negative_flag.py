
# logic class homework 1
# Check karo ek list mein koi negative number hai kya (flag).



lst = [1,3,5.9,-8,7]

found = False

for i in lst:
    if i == -8:
        found = True
print(f"-8 in list {found}")