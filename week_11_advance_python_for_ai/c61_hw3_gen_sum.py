# generator expression se 1-100 ke square ka  sum nikaale.


'''
1=restate =generator expression se 1-100 ke square ka  sum nikaale.
2=Example = def sum_num(): ,gen_sum = sum_num() , print(sum(gen_sum))
3=psuedocode= 1. create the function def sum_num():
              2.check the for condtion for num in range(1,100):
              3.yield num ** 2.
              4.gen_sum = sum_num()
              5.print(sum(gen_sum))
4=translate=

'''

def sum_num():
    for num in range(1,100):

        yield num ** 2

gen_sum = sum_num()

print(sum(gen_sum))


# dry run:
# print(sum(gen_sum))
# gen_sum = sum_num()
# def sum_num()
#  for num in range(1,100)
#     yield num
# print(sum(gen_sum))
#  for num in range(1,100)
#   yield num