# Ek text se saare hashtags (#word) nikaalo.

'''
1=restate=  Ek text se saare hashtags (#word) nikaalo.
2=example= import re write the any text 
3=psuedocode= 1.import re
              2.write the any text  like sentance = ""My Gmail pass123#gmail.com  Mobile Number is 4455667788 , another one gamil is arti#56gmail.com"
              3.create object and store the hashtags_text = sentance.split(" ")
              4.check condtion for hash in hashtags_text:,if "#" in hash:
              5.print hash
4=translate in python


'''
import re

sentance = "My Gmail pass123#gmail.com  Mobile Number is 4455667788 , another one gamil is arti#56gmail.com"

hashtags_text = sentance.split(" ")

for hash in hashtags_text:
    if "#" in hash:
        print(hash)