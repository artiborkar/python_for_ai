# ek dict banao aur use json.dumps(indent=2) se sundar print karo.



'''
1=restate= ek dict banao aur use json.dumps(indent=2) se sundar print karo.
2=example=import json
3=psuedocode= 1.create dict new_dict = {
             "name" : "Arti" ,
             "age" : 21 ,
             "city" : "Wardha" , 
             "contry" : "India" , 
             "pincode" : 442102 ,
             "is_info" : True
            }
            2.dict_to_json  = json.dumps(new_dict , indent = 2)
            3.print(dict_to_json)
4=transalte =

'''
import json

new_dict = {
             "name" : "Arti" ,
             "age" : 21 ,
             "city" : "Wardha" , 
             "contry" : "India" , 
             "pincode" : 442102 ,
             "is_info" : True
            }

dict_to_json  = json.dumps(new_dict , indent = 2)

print(dict_to_json)






# dry run 






