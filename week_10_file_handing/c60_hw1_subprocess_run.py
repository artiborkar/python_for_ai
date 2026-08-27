# subprocess.run se python --version chalao (list form) aur output print karo.


'''
1=restate=  subprocess.run se python --version chalao (list form) aur output print karo.
2=example=  import subprocess
3=psuedocode= 1.import subprocess
              2. result  = subprocess.run(["python" , "--version"] , capture_output = True ,text =True )
              3.print(result.stdout)
4=translate in python =
'''


import subprocess

result  = subprocess.run(["python" , "--version"] , capture_output = True ,text =True )

print(result)

print(result.stdout)