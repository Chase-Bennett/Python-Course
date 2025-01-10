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
"""




def introduction(first_name, last_name="Smith"):
     print("Hello, my name is", first_name, last_name)




introduction("James", "Doe")

def add_numbers(a, b=2, c):
    print(a + b + c)
 
add_numbers(a=1, c=3)
 
