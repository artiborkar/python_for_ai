# 3.Append mode se ek 4th goal add karo , phir dobara file padho.

'''
1= restate=.Append mode se ek 4th goal add karo , phir dobara file padho.
2=example= with open("mygoals.text" , "a") as f,with open("mygoals.text" , "r") as f:
3=psuedocode=1.with open("mygoals.text" , "a") as f:
             2.goal = "\nMy 4th Goal is To Become Agentic AI Engineer"
             3. print(f.write(goal)
             4.with open("mygoals.text" , "r") as f:
             5.goal = f.read()
             6.print(goal)
4=transalte=

'''

with open("mygoals.text" , "a") as f:

    goal = "\nMy 4th Goal is To Become Agentic AI Engineer"

    print(f.write(goal))

with open("mygoals.text" , "r") as f:

    goal = f.read()

    print(goal)
