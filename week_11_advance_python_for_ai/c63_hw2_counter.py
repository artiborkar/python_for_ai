# Ek sentence mein har word ki frequency Counter se nikaalo.


'''
1=restate= Ek sentence mein har word ki frequency Counter se nikaalo
2=example= from collections import Counter  ,print(fre)
3=psuedocode= 1. from collections import Counter
              2. sentence = "I am learning Python and Agentic AI and I am also practice daily".split()
              3. fre = Counter(sentence)
              4.print(f"Sentence : {sentence}")
              5. print(fre)
4=translate=

'''
from collections import Counter

sentence = "I am learning Python and Agentic AI and I am also practice daily".split()

fre = Counter(sentence)

print(f"Sentence : {sentence}")

print(fre)

# dry run 
# print(fre)
# fre = Counter(sentence)
# from collections import Counter
# sentence = "I am learning Python and Agentic AI and I am also practice daily".split()
# print(f"Sentence : {sentence}")
# print(fre)