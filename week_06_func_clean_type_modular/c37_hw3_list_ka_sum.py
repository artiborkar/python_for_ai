# recursion se ek list [1,2,3,4,5]ka sum nikaalo(loop use na kro)

def list_sum(lst, index=0):
    if index == len(lst):      # Base Case
        return 0

    return lst[index] + list_sum(lst, index + 1)


numbers = [1, 2, 3, 4, 5]
print(list_sum(numbers))


# dry run 
# [1, 2, 3, 4, 5]
# if 0==5:
# 1+(1,0+1=1)=1
# if 1==5:
# 1+2+(2,2)=3
# if 2==5:
# 1+2+3+(3,3)=6
# if 3==5:
# 1+2+3+4+(4,4)=10
# if 4==5:
# 1+2+3+4+5(5,5)=15
# if 5==5:
# return 0