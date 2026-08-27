# Ek CSV file 3 students ke naam+marks ke saath banao aur DictReader se padho.

# name    marks
# Arti    77
# Rohini  88
# Shreya  66

'''
1=restate= Ek CSV file 3 students ke naam+marks ke saath banao aur DictReader se padho.
2=example= import csv create dictionary
3=psuedocode= 1.import csv or create dict 
              2.write the file like with open("student_info.csv" , "w" , newline="",encoding="utf-8") as f:
              3.writer = csv.writer(f), writer.writerows(student_info)
              4.read the file with open("student_info.csv" , "r" , encoding= "utf-8" ) as f:
              5.reader = csv.DictReader(f), for row_dict in reader:
              6. print  print(row_dict["Name"] , row_dict["Marks"])
4=transalte in python 
'''

# import csv

# student_info = [
#                 ["Name" , "Marks"],
#                 ["Arti " ,  77],
#                 ["Rohini" , 88],
#                 ["Shreya " , 66]
# ]


# with open("student_info.csv" , "w" , newline="",encoding="utf-8") as f:
#     writer = csv.writer(f)
#     writer.writerows(student_info)
                

# with open("student_info.csv" , "r" , encoding= "utf-8" ) as f:
#     reader = csv.DictReader(f)
#     for row_dict in reader:
#         print(row_dict["Name"] , row_dict["Marks"])



with open("my_first_file.txt" , "w" , encoding="utf-8") as f:
    f.write(" नमस्ते! 🙏  Hello Python")


with open("my_first_file.txt" , "r" , encoding="utf-8") as f:
    r = f.read()
    print(r)

