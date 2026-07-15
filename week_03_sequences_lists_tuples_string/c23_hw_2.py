# class 23
# homework 02

# 3 students ka naam aur 3 subjects ke marks rakho; har student ka total print karo.

student  = (["Bhavesh",89,52,52],
            ["Harsha",11,56,45],
            ["Harsha",55,52,42]
            )

print(student)

for row in student:
    print(f"{row[0]} : total = {sum(row[1:4])}")