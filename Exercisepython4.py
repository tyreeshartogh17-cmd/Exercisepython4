# Question 1: Using a for loop with a list

# TODO: Create a list of fruits
fruits = ["apple", "banana", "cherry", "apple" ]
# TODO: Use a for loop to print each fruit in the list
print(fruits)


#-------------------------------------------------------------------------
# Question 2: Using a while loop for countdown

# TODO: Use a while loop to create a countdown from 5 to 1
count = 5 
while count > 0: 
    print(count)
    count-= 1

#-------------------------------------------------------------------------
# Question 3: Using a for loop with range()

# TODO: Use a for loop to print the first 10 square numbers
for i in range(1,11):
    square = i ** 2
    print(f"The square of {i} is {square}")
#-------------------------------------------------------------------------

# Question 4: Using the random module

# TODO: Import the random module
import random
total_gold = 0
print ("you stranger have found 3 chest! lets lock in and open them:\n")
for chest_number in range(1,4):
    gold_found = random.randint(10,50)
    total_gold = total_gold + gold_found
    print(f"chest {chest_number} contained {gold_found} gold! lets go!")
    print(f"\n Game over! you walked away with {total_gold} total gold!")
# TODO: Create a list of colors
colors = [ "purple","red","orange","blue","green","velvety"]
print(colors)

# TODO: Use a for loop to select and print 3 random colors from the list
import random
colors = [ "purple","red","orange","blue","green","velvety"]
chosen_colors = random.sample(colors,3)
print("and your colors IT speacilist is...")
print(chosen_colors)

#-------------------------------------------------------------------------
# Question 5: Creating and using a custom module

# TODO: Create a new file named 'math_operations.py' with the following content:
"""
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"
"""
# Run this block first to create the file
module_code = """def add(a, b):
    return a + b
"""

with open("math_operations.py", "w") as file:
    file.write(module_code)

print("File created!")
import random
# 1. Import your custom file
import math_operations

# 2. Pick a random number of points
bonus_points = random.randint(1, 10)
print(f"You earned a random bonus of: {bonus_points} points!")

# 3. Use YOUR custom function to add the bonus to a base score of 50
final_score = math_operations.add(50, bonus_points)

# 4. See the result
print(f"Your final score is: {final_score}")



# TODO: Import the custom module and use its functions
# 1. Import your custom module file
import math_operations

# 2. Use your custom add function
gold_earned = math_operations.add(10, 5)
print(f"You earned: {gold_earned} gold!")



# TODO: Use a while loop to create a simple calculator
import math_operations

# This variable keeps the loop running
running = True

print("Welcome to your Custom Calculator!")
print("Type 'quit' at any time to exit.\n")

while running == True:
    # 1. Ask the player for an operation
    operation = input("Choose (add, quit): ")
    
    # 2. Check if they want to exit
    if operation == "quit":
        running = False
        print("Goodbye!")
        
    # 3. If they want to add, get numbers and use your module
    elif operation == "add":
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        
        result = math_operations.add(num1, num2)
        print(f"Result: {result}\n")
        
    else:
        print("Invalid choice, try again.\n")

