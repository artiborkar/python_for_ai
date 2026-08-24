# retry function ko ek aise task par chalao jo pehle 2 baar fail kare phir success de.


# 1=restate= retry function ko ek aise task par chalao jo pehle 2 baar fail kare phir success de.
# 2=example=def retry(attempt):,for attempt in range(1,4):
# 3=psuedocode=1.def retry(attempt):,if attempt < 3:
            #  2.raise ConnectionError("Failed Network Error"),return "Sucessful !"
#              3.for attempt in range(1,4):
#              4.try:,result = retry(attempt), print(f"Attempt {result}")
    #          5. except ConnectionError as e:, print(f"Error : {e}")
# 4=translate=


print("-----------homework------------")

def retry(attempt):
    if attempt < 3:
        raise ConnectionError("Failed Network Error")

    return "Sucessful !"


for attempt in range(1,4):

    try:
        result = retry(attempt)
        print(f"Attempt {result}")
    except ConnectionError as e:
        print(f"Error : {e}")



# 5=dry run