

"""
print("pq")
n = int(input("num:"))
print( n >= 100) 



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






"""
money= float(input("how much do you make: "))

if money < 85528:
    
    money = money * .18
    money = money-556.02
    

else:
    money = ((money-85528)*.32)+14839.02



if money<0:
    money=0

money = round(money,0)
print("your taxes are ", money)


year = int(input("Enter a year: "))

if year < 1582:
	print("Not within the Gregorian calendar period")
else:
	if year % 4 != 0:
		print("Common year")
	elif year % 100 != 0:
		print("Leap year")
	elif year % 400 != 0:
		print("Common year")
	else:
		print("Leap year")



   






# Store the current largest number here.
largest_number = -999999999
 
# Input the first value.
number = int(input("Enter a number or type -1 to stop: "))
 
# If the number is not equal to -1, continue.
while number != -1:
    # Is number larger than largest_number?
    if number > largest_number:
        # Yes, update largest_number.
        largest_number = number
    # Input the next number.
    number = int(input("Enter a number or type -1 to stop: "))
 
# Print the largest number.
print("The largest number is:", largest_number)





# A program that reads a sequence of numbers
# and counts how many numbers are even and how many are odd.
# The program terminates when zero is entered.
 


odd_numbers = 0
even_numbers = 0
 
# Read the first number.
number = int(input("Enter a number or type 0 to stop: "))
 
# 0 terminates execution.
while number != 0:
    # Check if the number is odd.
    if number % 2 == 1:
        # Increase the odd_numbers counter.
        odd_numbers += 1
    else:
        # Increase the even_numbers counter.
        even_numbers += 1
    # Read the next number.
    number = int(input("Enter a number or type 0 to stop: "))
 
# Print results.
print("Odd numbers count:", odd_numbers)
print("Even numbers count:", even_numbers)




counter = 5
while counter:
    print("Inside the loop.", counter)
    counter -= 1
print("Outside the loop.", counter)

"""




"""
secret_number = 4545

print(
""""""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
"""#)

"""S

guess= int(input("Try to guess my number: " ))


while guess != secret_number:
    print(" your stuck in my loop now")
    guess = int(input("try again "))

print("Well done, muggle! You are free now.")
"""

for i in range(2, 8):
    print("The value of i is currently", i)


for i in range(1,80, 10):
    print("The value of i is currently", i)



for i in range(1, 1):
    print("The value of i is currently", i)
 



power = 1
for expo in range(16):
    print("2 to the power of", expo, "is", power)
    power *= 2






from ast import Break
import time
from tkinter import WORD
# Write a for loop that counts to five.
    # Body of the loop - print the loop iteration number and the word "Mississippi".
    # Body of the loop - use: time.sleep(1)
"""
# Write a print function with the final message.


for i in range(0,6):
    print(i,"Mississppi")
    time.sleep(1)
print("Ready or not, here I come!")
"""
"""




print("Inside the loop.", i)
print("Outside the loop.")


# continue - example

print("\nThe continue instruction:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Inside the loop.", i)
print("Outside the loop.")



largest_number = -99999999
counter = 0

while True:
    number = int(input("Enter a number or type -1 to end the program: "))
    if number == -1:
        break
    counter += 1
    if number > largest_number:
        largest_number = number

if counter != 0:
    print("The largest number is", largest_number)
else:
    print("You haven't entered any number.")


    """
"""
Word= input("guess your word: ")

while True:
   if Word == "dog":
      break
   Word= input("guess your word: ")


print("You've successfully left the loop.")
"""
"""


user_word = input("Word:")
user_word = user_word.upper()
word_without_vowels = ""
# Prompt the user to enter a word
# and assign it to the user_word variable.

for letter in user_word:
    # Complete the body of the for loop.
    if letter  in "AEIOU":
        word_without_vowels = word_without_vowels + letter
        continue

    else: print(letter)

print ("Vowels " + word_without_vowels) 
"""



Num_Block = int(input("Number of blocks: "))
Block_Used = 0
Height = 1
for i in (range(1,Num_Block+1)):
    print(i)
    Block_Used = Block_Used + i
    if Block_Used > Num_Block:
        Height =  i-1
        break

print("the height is " + str(Height))
 



