#homework 3
#  range(2, 30) mein saare prime numbers print karo (Concept 3 ko loop mein daalo).

for num in range(2, 30):
    prime = True
    for x in range(2,num):
        if num%x==0:
            prime = False
    if prime:
        print(num)
















# for number in range(2, 30):
#     is_prime = True
#     for i in range(2, number):
#         if number % i == 0:
#             is_prime = False
#     if is_prime:
#         print(number)