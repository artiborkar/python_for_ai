# Q12
# EN: Trace the built O/E string. HI: O/E string trace karo.

result = ""
for n in [1, 2, 3, 4]:
    if n % 2 == 0:
        result = result + "E"
    else:
        result = result + "O"
print(result)