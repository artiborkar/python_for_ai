# homework 4
# Ek list of names mein "Asha" hai kya, aur agar hai toh us par kaunse index par hai (hint: enumerate).

lsts = ["Arti","Rohini","Asha","Shreya"]

for index , lst in enumerate (lsts):
    if lst == "Asha":
        # print(index)
        print(f"Index no.: {index}\nName : {lst}")
    