
sentance = input("Enter the any sencetane or error : ")

new = sentance.split(" ")
print(f"old data :{new}")

add_sentance = []

for text in new:
    if text:
        add_sentance.append(text)
clean_data = " ".join(add_sentance)

print(f"clean Data : {clean_data}")
