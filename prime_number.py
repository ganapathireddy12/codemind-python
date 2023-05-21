def PrimeChecker(a):  
    if a > 1:  
        for j in range(2, int(a/2) + 1):  
            if (a % j) == 0:  
                print("not a prime")  
                break  
        else:  
            print("prime")  
    else:  
        print("not a prime")  
a = int(input())  
PrimeChecker(a)  