from tokenize import Number


j = 22
i=1


"""
bit = i &j
print(bit)

bitneg = ~i
print(bitneg)
print(11111)


var = 17
var_right = var >> 1
var_left = var << 2
print(var, var_left, var_right)
numbers = [10, 5, 7, 2, 1]
print(numbers)


print("Source file edit test")
print(".sln edit test")

numbers = [10, 5, 7, 2, 1]
print("Original list content:", numbers)  # Printing original list content.

numbers[0] = 111
print("\nPrevious list content:", numbers)  # Printing previous list content.

numbers[1] = numbers[4]  # Copying value of the fifth element to the second.
print("Previous list content:", numbers)  # Printing previous list content.

print("\nList's length:", len(numbers))  # Printing previous list length.

###

del numbers[1]  # Removing the second element from the list.
print("New list's length:", len(numbers))  # Printing new list length.
print("\nNew list content:", numbers)  # Printing current list content.

###




numbers = [111, 7, 2, 1]
print(numbers[-2])



hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

# Step 1: write a line of code that prompts the user
# to replace the middle number with an integer number entered by the user.
hat_list[2]=int(input("Num: "))
# Step 2: write a line of code that removes the last element from the list.
del hat_list[4]
# Step 3: write a line of code that prints the length of the existing list.
print(len(hat_list))
print(hat_list)
"


numbers = [1,2,3,4,5,6,7,8,9]
numbers.append(4)

print(len(numbers))
print(numbers)

###
while i < 20000:
    numbers.insert(0, 222)
    print(len(numbers))
    print(numbers)
    numbers.insert(1, 333)
    print(len(numbers))
    print(numbers)
    i+=1

#


my_list = []  # Creating an empty list.

for i in range(25):
    my_list.append(i + 1)

print(my_list)


my_list = []  # Creating an empty list.
 
for i in range(25):
    my_list.insert(0, i + 1)
 
print(my_list)



numbers=[]
while i <-89:
    numbers.insert(0, 222)
    print(len(numbers))
    print(numbers)
    numbers.insert(1, 333)
    print(len(numbers))
    print(numbers)
    i+=1


    my_list=[1,2]
    length = my_list.length

for i in range(length // 2):
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]
 
print(my_list)


"""


"""


# step 1
beatles = []
print("Step 1:", beatles)

# step 2
beatles.append("John lennon")
beatles.append( "Paul McCartney" )
beatles.append( "George Harrison")

print("Step 2:", beatles)



# Step 3: Prompt the user to add Stu Sutcliffe and Pete Best to the list
for member in ["Stu Sutcliffe", "Pete Best"]:
    beatles.append(input(f"Add {member} to the list: "))  # Prompts user to type names
print("Step 3:", beatles)

# Step 4: Remove Stu Sutcliffe and Pete Best from the list
del beatles[-2:]  # Removes the last two members
print("Step 4:", beatles)

# Step 5: Add Ringo Starr to the beginning of the list
beatles.insert(0, "Ringo Starr")
print("Step 5:", beatles)


# testing list legth
print("The Fab", len(beatles))




my_list = [8, 10, 6, 2, 41,2,3,4,32,1,233,2,32,12,2,2,2,3,4,2,4,]  # list to sort
swapped = True  # It's a little fake, we need it to enter the while loop.
print (my_list)
while swapped:
    swapped = False  # no swaps so far
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True  # a swap occurred!
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
 
print(my_list)


my_list = []
swapped = True
num = int(input("How many elements do you want to sort: "))

for i in range(num):
    val = float(input("Enter a list element: "))
    my_list.append(val)

while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print("\nSorted:")
print(my_list)


"""
# Copying the entire list.
list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)

# Copying some part of the list.
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:-1]
print(new_list)

