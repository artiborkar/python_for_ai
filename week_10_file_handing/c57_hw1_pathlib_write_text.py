# pathlib se ek folder banano aur usme ek file likho(write_text).

'''
1= restate= pathlib se ek folder banano aur usme ek file likho(write_text).
2=example= from pathlib  import Path
3=psudocode=1.from pathlib  import Path , folder = Path("new_folder")
            2.folder.mkdir(exist_ok=True), file = folder /  "my_new_folder.txt"
            3.file.write_text("This is my pathilb file and folder name is new_folder and file name is my_new_folder.txt" , encoding="utf-8")
4=translate=

'''

from pathlib  import Path

folder = Path("new_folder")

folder.mkdir(exist_ok=True)

file = folder /  "my_new_folder.txt"

file.write_text("This is my pathilb file and folder name is new_folder and file name is my_new_folder.txt" , encoding="utf-8")

# r = file.read_text()

# print(r)



# 5=dry run=













