
# current folder ki saari .text files list karo (glob)

'''
1=restate= current folder ki saari .text files list karo (glob)
2=example= ye from pathlib import Path
3=psuedocode=1.from pathlib import Path
             2.parent_folder = Path("week_10_file_handing")
             3.txt_file = parent_folder.glob("*.text")
             4.for file in txt_file:
             5.print(file.name)
4=transalte =


'''
from pathlib import Path

parent_folder = Path("week_10_file_handing")

txt_file = parent_folder.glob("*.text")

for file in txt_file:

    print(file.name)


# 5=dry run=