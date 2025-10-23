def cube (num):
    print (num**3)
def by_3(number):
 if number % 3 == 0: 
  return cube(number)
 else:
   print("The number is not divisible by 3")
print (by_3(9))