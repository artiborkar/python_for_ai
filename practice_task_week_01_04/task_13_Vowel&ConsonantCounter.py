
# Task 13 — Vowel & Consonant Counter
# User se ek sentence lo. Ek dictionary banao jo har vowel (a,e,i,o,u) kitni baar aaya woh count kare. 
# Phir total consonants (letters jo vowel nahi) alag se print karo.

# Concepts: loop over string, dict, .get() ya in check, .lower()
# Hint: counts[ch] = counts.get(ch, 0) + 1 — yeh missing key ko safely handle karta hai.

print("======Vowel & Consonant Counter========")

sentance = input("Enter the Sentance : ")

dict ={}

count={}

for vowel in sentance:
    count.get(vowel)
    print(count)
