y=0
def add(x):
    global y
    y=x+y
    return y

for x in range(0,10):
        print(add(x))
