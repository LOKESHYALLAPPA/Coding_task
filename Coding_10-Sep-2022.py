print("--------------Program 1-------------------")
print(" ------Get ODD NUMBERS -----")
print(" ------- 1.a. List Comprehension ------ ")

# Step1: Initialization of list
# Step2: list Comprehension format
# step 3: For loop for iterations
# Step 4: If condition to check value is odd number or not
# Step 5: print those values in list format
odd_list = [element for element in range(1, 11) if element % 2 == 1 ]
print(odd_list)

print(" ------- 1.b. Normal For Loop -------")

# Step1: Minimum and Maximum values Initialization
# Step2: for loop for number of Iterations
# Step3: if statement for to check if value is odd number or not
# Step4: if value is odd it will print

# Dynamic Initialization
maxi_mum = 11
# Iteration purpose
for number in range(1, maxi_mum + 1):
    # To check if a value odd or not
    if(number % 2 != 0):
        # Printing odd numbers
        print("{0}".format(number))

print(" ------- 1.c. Generator mechanism ----")
# This topic is still pending

print("------- 1. Implement palindrome using iterator(for loop) and generator mechanism. ----------")
print(" --------- Palindrome program = A ----------")

# Step1: Dynamic Initialization
# Step2: Reverse give string
# Step3: Compare that previous string to reversed string
# Step4: If both are same, output will be "The string is a palindrome"

my_str = input("Enter the String: ")
# make it suitable for caseless comparison
my_str = my_str.casefold()

# reverse the string
rev_str = reversed(my_str)

# check if the string is equal to its reverse
if list(my_str) == list(rev_str):
   print("The string is a palindrome.")
else:
   print("The string is not a palindrome.")

print(" --------- Palindrome program = B ----------")
print("Generator Mechanism concept still pending")

print("------------- 2. Sum of 2 digits into output -------------------- ")
'''
Sum of 2 digits into output
		n1 = 1234 # int(input("Enter number1 :" ))
		n2 = 9999 # int(input("Enter number2 :" ))
		Output: 9+1 2+9 3+9 4+9 
		         10 + 11 + 12 + 13
				 46
'''
# Step1: Dynamic initialization
# Step2: Addition two inputs by index
# Step3: Add those index addition values in to one variable
# Step4: Print the output

n1 = input("Enter first 4 digit numbers: ")
n2 = input("Enter second 4 digit numbers: ")
a, b, c, d = n1[0], n1[1], n1[2], n1[3]
e, f, g, h = n2[0], n2[1], n2[2], n2[3]

a1 = int(a) + int(e)
a2 = int(b) + int(f)
a3 = int(c) + int(g)
a4 = int(d) + int(h)

addition = a1 + a2 + a3 + a4
print(addition)

print("----------  3. Reverse string considering only alphabets. Symobls should not be reversed -------------------")
'''
st = "ab@#cd!ef"
   Reverse string considering only alphabets. Symobls should not be reversed
   # Output: fe@#dc!ba

'''
# Step1: String initialization
# Step2: Find length of string and store it in other variable for check condition
# Step3: while loop for number of iterations
# Step4: Check the value by using isalpha() function in if statement where it is a alpha or not
# Step5: Increment and decrement to check all the characters in a given string
# Step6: Printing only alpha bets
st = "ab@#cd!ef"
# convert string into list
listSample = list(st)
i = 0
j = len(listSample) - 1
while i < j:
    if not listSample[i].isalpha():
        i += 1
    elif not listSample[j].isalpha():
        j -= 1
    else:
        # swap the element in the list
        # if both elements are alphabets
        listSample[i], listSample[j] = listSample[j], listSample[i]
        i += 1
        j -= 1

# convert list into string
# by concatinating each element in the list
strOut = ''.join(listSample)
print(strOut)

print("---------------- 4. findout elements duplicate count output in  dict format ------------")
'''
4. some_list = ["a", "b", "c", "d", "n", "a", "b", "m", "n", "m"]
   #findout elements duplicate count output in  dict format
'''

# Step1: Fist import counter module
# Step2: List initialization
# Step3: Count the list
# Step4: Find the duplicate values in a list
# Step5: Print them in dictionar format

# Counter import
from collections import Counter
# List Initialization
some_list = ["a", "b", "c", "d", "n", "a", "b", "m", "n", "m"]
# elements count
d = Counter(some_list)

# List Comprehension
r_list = list([num for num in d if d[num]>1])
# Printing elements in dict format by using List Comprehension
print("Duplicate integers: ",{r_list[i]:r_list[i+1] for i in range(0,len(r_list),2)})

print(" ---------- 5. Output: (10,10,10,'ab','cd') ------------------")
'''
# t1 = (1, 2, 3, "a", "c") 
   # t2 = ("b", "d", 9, 8, 7)
   # Output: (10,10,10,"ab","cd")
'''

def combine_list(t1, t2):
    t1 = list(t1)
    t2 = list(t2)
    t3 = []
    for i in t1:

        for j in range(len(t2)):
            if(type(i) is type(t2[j])):
                t3.append(i + t2[j])
                t2.remove(t2[j])
                break
    return tuple(t3)
t1 = (1, 2, 3, "a", "c")
t2 = ("b", "d", 9, 8, 7)
print(combine_list(t1,t2))

print("--------------- 6. Write a Python program to remove leading zeros from an IP address. ---------------")
'''
#Write a Python program to remove leading zeros from an IP address.
			  inp = "216.08.094.196"
			# o/p =  216.8.94.196
'''
# Step1: Import re module to remove value in IP address
# Step2: Static Initialization
# Step3: Remove leading zeros from IP address
# Step4: Output Print

import re
inp = "216.08.094.196"
string = re.sub('\.[0]*', '.', inp)
print(string)

print("--------- 7. output= [1,2,3,4,5,6,7,8,9,10] ----------------")
'''
l = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]]
   #output= [1,2,3,4,5,6,7,8,9,10]
'''
# Step1: Nested list creation
# Step2: Split() and lamda function
# Step3: Printing values
l = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]]
print(list(map(lambda x:int(x),str(l).replace('[','').replace(']','').split(', '))))

