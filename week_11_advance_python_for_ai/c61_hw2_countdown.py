# Ek generator countdown(n) jo n se 1 tak yield kare.


'''
1=restate= Ek generator countdown(n) jo n se 1 tak yield kare.
2=example=countdown(n),
3=psuedocode= 1.function def countdown(n)
              2. for num in range(n, 0, -1):
              3.yield num
              4.for num in countdown(5):
              5. print(num)
4=transalte in python=
'''

def countdown(n):
    for num in range(n, 0, -1):
        yield num

for num in countdown(5):
    print(num)

# dry run:
# print(num)
# for num in countdown(5)
# countdown(n)
# for num in range(n, 0, -1):
# yield num