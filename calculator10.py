#Simple calculator with basic arithmetic operations using Python
  
import math
import time

def add(x,y):
    return x+y

def subtract(x,y):
    if(x >= y):
        return x-y
    else:
        return y-x

def multiply(x,y):
    return x*y

def divide(x,y):
    if y != 0:
      return x/y

    else:
      return ('Invalid Division')

def exponential(x,y):
    return x**y

def modulus(x,y):
    return x%y

def floorDivision(x,y):
    return x//y

def ceilDivision(x,y):
    return math.ceil(x/y)

if __name__ == "__main__":
    while True:
     print("Simple Calculator\n")
     print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Exponential\n6.Modulus\n7.floorDivision\n8.ceilDivision\n\n")
     choice = int(input("Enter your choice: "))
     
     if 1<= choice <= 8:
      a = float(input("Enter the 1st number: "))
      b = float(input("Enter the 2nd number: "))

      result = None

      if choice == 1:
        result = add(a,b)

      elif choice == 2:  
        result = subtract(a,b)

      elif choice == 3:
        result = multiply(a,b)

      elif choice == 4:
        result = divide(a,b)

      elif choice == 5:
        result = exponential(a,b)

      elif choice == 6:
        result = modulus(a,b)

      elif choice == 7:
        result = floorDivision(a,b)

      elif choice == 8:
        result = ceilDivision(a,b)
        
      print('Result:', result)
      time.sleep(1)

     else:
        print('Invalid choice')
        break
  
    



