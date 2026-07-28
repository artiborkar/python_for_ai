
#logic class homework 3

# Ek list mein sabse chhota number dhoondho (bina min()).

list = [2,6,8,10,4,12]
count = list[0]
for i in list:
    if i < count:
        count=i
print(count)
    