
# Task 14 — Word Frequency Counter
# Ek paragraph string lo (multi-word). Har word kitni baar aaya, ek dictionary mein count karo (case-insensitive). 
# Phir sabse zyada aane wala word batao.

# Concepts: .lower(), .split(), dict counting, max(..., key=...)
# Hint: max(counts, key=counts.get) sabse badi value waali key deta hai.

print("============== Word Frequency Counter===========")

paragraph = input("Enter a paragraph: ").lower()

words = paragraph.split()

counts = {}

for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

most_common = max(counts, key=counts.get)

print("Word Frequency:")
for word, count in counts.items():
    print(word, ":", count)

print("Most Frequent Word:", most_common)
print("Count:", counts[most_common])



# copy peast code