# Backoff calculate karke print karo: 4 attempts ke liye wait times (delay=1).



# 1=restate=Backoff calculate karke print karo: 4 attempts ke liye wait times (delay=1).
# 2=example=for attempt in range(1,5):
# 3=psuedocode=1.for attempt in range(1,5):
#              2.wait = 2 ** (attempt - 1)
#              3.print(f"Attempt {attempt}:wait {wait} seconds")
# 4=translate in python=


for attempt in range(1,5):
    wait = 2 ** (attempt - 1)
    print(f"Attempt {attempt}:wait {wait} seconds")

# 5=dryrun