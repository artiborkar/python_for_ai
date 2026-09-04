# @lru_cache ek fibonacci function par lagao aur speed mehsoos karo.

'''
1=restate= @lru_cache ek fibonacci function par lagao aur speed mehsoos karo.
2=example= 
3=psuedocode=
4=translate in python=

'''

from functools import lru_cache

@lru_cache

def fibonacci(num):
    if num <= 1:
        return num

    return fibonacci(num-1)+fibonacci(num-2)

print(fibonacci(3))

#dry run 
# print(fibonacci(3))
# 3<=1
# return (3-1)+(3-2)
# return 2+1=3
