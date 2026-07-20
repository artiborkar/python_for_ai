
# Homework  Q1
# 3 dicts ki list banao (naam, age) aur age ke hisaab se sort karke print karo.

print("==========Q1.=========")

stu_info = [

            {"name":"Arti","age":21},
            {"name":"Navneet","age":14},
            {"name":"Vaishnav","age":16}

           ]


stu_info.sort(key=lambda s:s['age'])

print(stu_info)


# sorted_age = sorted(stu_info , key=lambda s:s['age'])

# print(sorted_age)