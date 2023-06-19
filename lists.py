# Write a Python program that takes a list of strings as input and outputs the number of times each string appears 
# in the list, using a dictionary and conditional statements.
str_lists = ["bananas","Avocados","oranges","bananas","bananas"]
str_counts ={}
for str in str_lists:
    str_counts[str]=1
    str_counts[str]+=1
    print(str,"appears","times")
    
# Write a Python program that takes a list of numbers as 
# input and outputs the median of the numbers 
def median(numbers):
        sorted_numbers = sorted(numbers)
        if length % 2 == 0:
            mid = length/2
            # else:
        mid = length / 2
        
        numbers = [2,3,4,,6,8,10]
print(median(numbers))

# Write a Python program that takes a list of numbers as input and outputs 
# the second largest number in the list using conditional statements and a for loop.
numbers = []
for i in range(n):
    num=int(input("Enter number"))
    numbers.append
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            second_largest= largest
            largest = num
            elif num= largest and (second_largest is None or num>second_largest):
    second_largest = num
    print("There is no second largest number")
       
    
# Write a Python program that takes a year as input and determines if it is a leap year.

year = int(input("Enter a year: "))
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
# Write a Python program that takes a string as input and 
# checks if it is a palindrome (reads the same forwards and backwards), ignoring spaces and punctuation.
input_string = input("Enter a string")
if is_palindrome(input_string):
    print("The string is palindrome")
else:
    print("The is not palindrome")    
    