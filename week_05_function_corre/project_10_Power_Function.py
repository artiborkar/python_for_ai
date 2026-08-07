# Project 10 — Power Function (default exponent)
# EN: Write power(base, exp=2) that returns base ** exp. By default it squares; but power(2, 3) should give 8.
# हिंदी: power(base, exp=2) बनाओ जो base ** exp return करे। Default में यह square करे; पर power(2, 3) का जवाब 8 आए।
# Concepts: default value, ** operator
# Hint: return base ** exp. power(5) → 25.

print("========Power Function (default exponent)=======")
'''
1= Write power(base, exp=2) that returns base ** exp. By default it squares; but power(2, 3) should give 8.
2= return base ** exp ,print(power(5))->25
3=1.create a function power   arggument is(base, exp=2)
  2.return base ** exp
  3.print the power(5) etc.
4=translate.
5=dryrun
def power(base, exp=2):
power(5)
return base ** exp
25

'''
def power(base, exp=2):
    return base ** exp

print(power(5))

print(power(2,3))