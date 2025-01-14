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
"""





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