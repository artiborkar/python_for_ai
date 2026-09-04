# Ek Generator even_numbers(n) jo pehle n even number yield kare.


'''
1=restate= Ek Generator even_numbers(n) jo pehle n even number yield kare.
2=example=  def even_numbers(n) 
3=psuedocode= 1.def even_numbers(n)
              2.for num in range(n),if num % 2 == 0,yield num
              3.for num in even_numbers(10) , print(num)

4=transalte = 

'''
def even_numbers(n):

    for num in range(n):
        if num % 2 == 0:
            yield num 

for num in even_numbers(10):
    print(num)










