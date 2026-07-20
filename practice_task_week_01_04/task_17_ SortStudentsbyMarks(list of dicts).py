
# Task 17 — Sort Students by Marks (list of dicts)
# Ek list of dicts banao: [{"name": "Asha", "marks": 85}, ...] (kam se kam 4 students).
#  Unhe marks ke descending order mein sort karke print karo (rank ke saath). Original list ko mat badlo.

# Concepts: sorted(key=lambda ...), reverse=True, enumerate, nested access
# Hint: sorted(students, key=lambda s: s["marks"], reverse=True). Rank ke liye enumerate(..., start=1).

print("=========Sort Students by Marks (list of dicts)==========")

dicts = [
            {"name": "Asha", "marks": 82}, 
            {"name": "Rohini", "marks": 90} , 
            {"name": "Shreya", "marks": 80} , 
            {"name": "Asha", "marks": 85}
        ] 

sort_dict = sorted(dicts , key=lambda s : s["marks"],reverse=True)

print(sort_dict)

for key , index in enumerate (sort_dict, start=1):
    print(key , index)