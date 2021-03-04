
def fizzbuzz(n):
    for n in range(1, n+1): 

        if n % 15 == 0: 
            print("FizzBuzz")                                         
            continue

        elif n % 3 == 0:     
            print("Fizz")                                         
            continue
    

        elif n % 5 == 0:         
            print("Buzz")                                     
            continue

        else:
            print (n)
            continue