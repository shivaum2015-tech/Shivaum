Lower=int(input("Enter the lower bound " ))
Upper=int(input("Enter the upper bound " ))
print ("Ther prime numbers are " )
for number in range (Lower,Upper+1):
    if number >1:
        for i in range (2,number):
            if (number%i)==0:
                break
        else:
         print (number)
