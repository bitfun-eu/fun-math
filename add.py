def add_one(n):
    return n + 1 

def sub_one(n):
    return n - 1 

def add(x, y): 
    while True:
        if y == 0:
            return x
        else:
            return add(add_one(x), sub_one(y))

def mult(x, y): 
    r = 0 
    for i in range(y):
        r = add(r, x)
    return r

print("add(3,4) = ", add(3,4))
print("mult(4, 5) = ", mult(4,5))
