# class 23
# homework
# Ek 3x3 grid ke saare items nested loop se print karo.


grids = [ [5,6,7],
        [4,3,2],
        [1,8,9]
]


for i in grids:
        for row in i:
                print(row , end=" ")
        print()