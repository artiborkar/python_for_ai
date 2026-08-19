# Ek Counter class banao jisme class attribute total ho jo har object par badhe.



# 1=reststate=Ek Counter class banao jisme class attribute total ho jo har object par badhe.
# 2=Example=class Counter:,total=0,def __init__(self,name):
# 3=psuedocode=1.class Counter:   class attribute is total=0
            #    2.def __init__(self,name):,self.name=name,Counter.total+=1
            #    3.class call and Counter("arti") ,,print(Counter.total)


print("-------Homework 3----------")

class Counter:
    total=0

    def __init__(self,name):
        self.name=name
        Counter.total+=1

Counter("arti")

Counter(21)

print(Counter.total)
