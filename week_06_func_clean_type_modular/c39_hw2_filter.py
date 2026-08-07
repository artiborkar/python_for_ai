# filter + lambda se [3,8,1,9,4] mein se sirf 5 se bade rakho.

lst = [3,8,1,9,4] 

fil_num = list(filter(lambda num : num>5 ,lst))

print(fil_num)