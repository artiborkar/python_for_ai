def avarage(num:list[int])->float:
    '''
        return :
            float:avarage value of given list of number

        args:
            nums:list[int] - list of numbers.
        
        returns:
            float - average value of given list of number.

    '''

    return sum(num)/len(num)

def modian(num:list[int])->float:
    '''
        return :
            given the return value of the list of number.
        args:
            nums(list[int]) list of number.

    '''
    return sorted(num)[len(num)//2]


def mode(num:list[int])->float:
    '''  
        return:
            given the mode value of given list of numbers
        args:
            num(list[int]): list of numbers
        return:
            int:mode value of given list of number.


    '''