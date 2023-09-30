import time

for i in range(0,11):
    for j in range(0,11):
        print("%2d X %2d = %2d" % (j, i, (j * i)))
    # endfor
    
    time.sleep(1)
    print("_"*20)

# endfor


