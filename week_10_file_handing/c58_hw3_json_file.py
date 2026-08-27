
# Apni week 4 ki content book(list of dicts) ko json file mein save aur me load karo.



'''
1=restate= Apni week 4 ki content book(list of dicts) ko json file mein save aur me load karo.
2=example=import json
3=psuedocode=
4=Translate
5=dry run
'''
import json

lst_dict     = {
                    "name" : "Arti" ,
                    "age" : 20 ,
                    "city" : "Wardha" , 
                    "favourite_subject" : "math",
                    "student_info" : True
                }


with open("week4.json", "w") as f:
    json.dump(lst_dict, f, indent=2)

print("Data successfully saved!")


with open("week4.json", "r") as f:
    data = json.load(f)

print("Loaded data:")
print(data)





