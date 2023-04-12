azzz1 = 12
azzz2 = 22 
azzz3 = 32



for i in range(1, 4):
    print(locals()["azzz" + str(i)])
