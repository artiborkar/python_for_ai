# Ek sentence se saare numbers re.findall(r"\d+") se nikaalo.


'''
1=restate= Ek sentence se saare numbers re.findall(r"\d+") se nikaalo.
2=example= import re write the any text 
3=psuedocode= 1.import re
              2.write the any text  like sentance = "My Gmail pass123@gmail.com  Mobile Number is 4455667788 , another one is 9955118822"
              3.craete object and store the num_text = re.findall(r"\d+",sentance )
              print th object p
4=translate in python


'''
import re

sentance = "My Gmail pass123@gmail.com  Mobile Number is 4455667788 , another one is 9955118822"


num_text = re.findall(r"\d+",sentance )

print(num_text)