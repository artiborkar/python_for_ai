# defaultdict(list) se students ko unki grade ke hisaab se group karo.

'''
1=restate= defaultdict(list) se students ko unki grade ke hisaab se group karo.
2=example= from collections import defaultdict , print(student)
3=psuedocode= 1.from collections import defaultdict
               2.student  = defaultdict(list)
               3.grade = ['A' , 'B' , 'C' ,'D'],name = ["Arti","Rohini","Shreya","Navneet"]
               4.for grade  ,name  in zip(grade  ,name):,student[grade].append(name)
               5 .print(student)
4=transalte
'''

from collections import defaultdict

student  = defaultdict(list)

grade = ['A' , 'B' , 'C' ,'D']
name = ["Arti","Rohini","Shreya","Navneet"]

for grade  ,name  in zip(grade  ,name):
    student[grade].append(name)

print(student)
