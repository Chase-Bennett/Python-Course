
"""

#n = int(input("num:"))
#print( n >= 100) 



# Read two numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
 
# Choose the larger number
if number1 > number2: larger_number = number1
   
else:
    larger_number = number2
 
# Print the result
print("The larger number is:", larger_number)






# Read three numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))
 
# We temporarily assume that the first number
# is the largest one.
# We will verify this soon.
largest_number = number1
 
# We check if the second number is larger than the current largest_number
# and update the largest_number if needed.
if number2 > largest_number:
    largest_number = number2
 
# We check if the third number is larger than the current largest_number
# and update the largest_number if needed.
if number3 > largest_number:
    largest_number = number3
 
# Print the result
print("The largest number is:", largest_number)
 


input = input("what kills harmfull objects: ")

if input == "Spathiphyllum":
    print("Yes - Spathiphyllum is the best plant ever!")

elif input == "spathiphyllum":
  print("No, I want a big Spathiphyllum!")

else:
    print("Spathiphyllum! Not "+ input);
    
    """







