"""
print("Enter a value: ")
a = int(input())

print("Enter a value: ")
b = int(input())

print("Enter a value: ")
c = int(input())


def message():
    print("Enter a value please : ")
message()
a = int(input())
message()
b = int(input())
message()
c = int(input())








def message():
    print("Enter a value: ")

 
print("We start here.")
message()
print("We end here.")


def message(number):
    print("Enter a number:", number)
 
number = 1234
message(1)
print(number)




def message(what, number):
    print("Enter", what, "number", number)
 
message("telephone", 11)
message("price", 5)
message("number", "number")


def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)
 
introduction("Luke", "Skywalker")
introduction("Jesse", "Quick")
introduction("Clark", "Kent")
 



def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)
 
introduction(first_name = "James", last_name = "007")
introduction(last_name = "Skywalker", first_name = "Luke")





def introduction(first_name, last_name="Smith"):
     print("Hello, my name is", first_name, last_name)




introduction("James", "Doe")




def boring_function():
    return 123456789
 
x = boring_function(), '987654321'
 
print("The boring_function has returned its result. It's:", x)
#print(None + 2)


value = None
if value is None:
    print("Sorry, you don't carry any value")


def strange_function(n):
    if(n % 2 == 0):
        return True


print(strange_function(2))
print(strange_function(1))
 





def list_sum(lst):
    s = 0
 
    for elem in lst:
        s += elem
 
    return s
 
 
print(list_sum([5, 4, 3]))
 
def strange_list_fun(n):
    strange_list = []
    
    for i in range(0, n):
        strange_list.insert(0, i)
    
    return strange_list

print(strange_list_fun(5))






def is_year_leap(year):
    if year % 4 !=0:
        return False
    elif year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    else:
        return True
    
    
    

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr,"->",end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")

from unittest import TextTestRunner


month_lengths_non_leap = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month_lengths_leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def is_year_leap(year):
   
    if year % 4 !=0:
        return False
    elif year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    else:
        return True

def days_in_month(year, month):
   if is_year_leap(year):
        return month_lengths_leap[month - 1]  # Use the leap year list
   else:
        return month_lengths_non_leap[month - 1]  # Use the non-leap year list
    

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")




def is_year_leap(year):
    # Check if a year is a leap year
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_in_month(year, month):
    # Return the number of days in a given month for a specific year
    if month < 1 or month > 12:
        return None  # Invalid month
    month_lengths_non_leap = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month_lengths_leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if is_year_leap(year):
        return month_lengths_leap[month - 1]
    else:
        return month_lengths_non_leap[month - 1]

def day_of_year(year, month, day):
    # Calculate the day of the year for the given date
    if month < 1 or month > 12 or day < 1:
        return None  # Invalid month or day
    
    total_days = 0
    for m in range(1, month):  # Add days for all preceding months
        days_in_current_month = days_in_month(year, m)
        if days_in_current_month is None:
            return None
        total_days += days_in_current_month

    # Add days for the current month
    days_in_current_month = days_in_month(year, month)
    if day > days_in_current_month:  # Check if day is valid
        return None

    total_days += day
    return total_days

# Testing the functions
print(day_of_year(2000, 12, 31))  # Output: 366 (Leap year)
print(day_of_year(2001, 12, 31))  # Output: 365 (Non-leap year)
print(day_of_year(2024, 2, 29))   # Output: 60 (Leap year, February 29)
print(day_of_year(2023, 2, 29))   # Output: None (Non-leap year, invalid date)
print(day_of_year(2023, 13, 1))   # Output: None (Invalid month)
print(day_of_year(2023, 0, 1))    # Output: None (Invalid month)
print(day_of_year(2023, 6, 15))   # Output: 166 (Valid date)
"""










def is_prime(num):
    for i in range(2,int(1+num**.5)):
     if num%i==0:
         return False
     return True

    

for i in range(1, 200000):
       if is_prime(i + 1):
        print(i + 1, end=" ")


print()