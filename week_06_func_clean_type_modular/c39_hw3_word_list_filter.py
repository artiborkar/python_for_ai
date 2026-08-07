# Words ki list ["hi","hello","hey","welcome"] mein se sirf 4+ letter waale filter se rakho.


word_lst = ["hi","hello","hey","welcome"]

fil_word = list(filter(lambda word : len(word) > 4 ,word_lst))

print(fil_word)