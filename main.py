for i in range(1,10):
    for r in range(1,i):
        print(end='\t')
    for j in range(i,10):
        print(f"{i:d}x{j:<2d}={i*j:2d}",end=' ')
    print()
input("Please enter any key to exit...")