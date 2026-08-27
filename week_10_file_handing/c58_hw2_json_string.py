# ek json string '{"city":"mumbai","pin":400001}' ko dict mein load karke city print karo.

# 1=restate= ek json string '{"city":"mumbai","pin":400001}' ko dict mein load karke city print karo.
# 2=example= import json 
# 3=psuedocode= 1.json ko import karna hai import json 
        #       2.variable mai dict store kare dict_str = '{"city":"mumbai","pin":400001}'
        #       3.json loads karae variable mai like json_str = json.loads(dict_str).
        #       4.then print (print(json_str['city'] )).
# 4=translate=



import json 

dict_str = '{"city":"mumbai","pin":400001}'

json_str = json.loads(dict_str)

print(json_str['city'] )

# 5=dry run=