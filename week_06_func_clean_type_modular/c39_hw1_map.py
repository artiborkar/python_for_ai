# map + lambda se [1,2,3,4] ke har number ka cube banao.


lst = [1,2,3,4] 

cube_lst = list(map(lambda num : num **3 ,lst))

print(cube_lst)

print("---------------")

# set = {1,2,3,4} 

# cube_set = set(map(lambda num : num **3 ,set))

# print(cube_set)

# print("-------------")

tup = [1,2,3,4] 

cube_tup = tuple(map(lambda num : num **3 ,tup))

print(cube_tup)