# 2. Use padho aur print karo.

'''
1=restate= pichle code ko Use padho aur print karo.
2=example= read mode use , or variable mai store kare 
3=psuedocode=1.with open("mygoal.text" , "r") as f:
             2. goal = f.read()
             3.print(goal)
4=translate=


'''

with open("mygoals.text" , "r") as f:
    
    goal = f.read()

    print(goal)
    
# dry run:
# print(goal)
# goal = f.read()
# with open("mygoal.text" , "r") as f: