# Date class banao with from_string("2026-06-28") classmethod (year, month, day mein todo).

# 1=restate=# Date class banao with from_string("2026-06-28") classmethod (year, month, day mein todo).
# 2=example=class Date:,   def __init__(self,year,month,day):,  @classmethod,def from_string(cls,text):
# 3=psuedocode=1.write the class Date: method     def __init__(self,year,month,day) ,attribute  self.year=year,  self.month=month,  self.day=day
#              2.decorator @classmethod  method def from_string(cls,text):
#              3.year,month,day=text.split("-"), return cls(int(year),int(month),int(day))
#              4. object d=Date.from_string("2026-06-28"),print(d.year,d.month,d.day)
# 4=translate python=

print("---------homework 1---------")

class Date:
    def __init__(self,year,month,day):
        self.year=year
        self.month=month
        self.day=day

    @classmethod

    def from_string(cls,text):
        year,month,day=text.split("-")
        return cls(int(year),int(month),int(day))


# date=Date(2026,6,28)

# print(date)

d=Date.from_string("2026-06-28")

print(d.year,d.month,d.day)

# 5=dry run =
# 1.d=Date.from_string("2026-06-28")
# 2.class Date:
#     def __init__(self,year,month,day):
#         self.year=year
#         self.month=month
#         self.day=day
# 3.print(d.year,d.month,d.day)
# 4. @classmethod

#     def from_string(cls,text):
#         year,month,day=text.split("-")
#         return cls(int(year),int(month),int(day))