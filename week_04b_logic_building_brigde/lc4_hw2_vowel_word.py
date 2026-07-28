
# logic class homework 
# Check karo ek word mein koi vowel hai kya.

words = "arti"
word_found = False

for word in words:
    if word in "aeiou":
        word_found = True
print(word_found)