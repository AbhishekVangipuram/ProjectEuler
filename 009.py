for i in range(1,1000):
    for j in range(1,1000):
        if (1000*(i+j-500)) == (i*j):
            k=1000-i-j
            print(i,j,k)
            print(i**2+j**2, k**2)
            print(i*j*k)
