def tri(n):
    spacein = 1
    spaceout = n - 2
    first = n - 1
    last = (n - 1) + n
    print((first*" ")+"x"+(first*" "))
    for i in range(0,n-2):
        print(((spaceout)*" ")+"x"+((spacein)*" ")+"x"+((spaceout)*" "))
        spacein +=2
        spaceout -=1

    print("x"*(last))

tri(10)