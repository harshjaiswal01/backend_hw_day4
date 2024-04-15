import random
# 1. The Range Riddle
# Objective: The aim of this assignment is to deepen your understanding of Python's range() function and its application in loops. 
# You will correct a code snippet, simulate moods for different days, and create a countdown timer.

# Task 1: Every Other Day Write a program that prints each day of the week, but only if that day is on an even index.

# Example Outcome: An example output could be "Sunday", "Tuesday", "Thursday"
print("Question 1")

days_in_week = ["Sunday", "Monday", "Teusday", 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

for index in range(len(days_in_week)):
    if index % 2 == 0:
        print('"', days_in_week[index], '"')



# 2. Nested Loops
# Objective: The aim of this assignment is to practice using nested loops in Python. 
# You will correct a nested loop code snippet, simulate a mood tracker, and generate a multiplication table.

# Task 1: Meal Planner Simulate a meal planner that picks a random meal from a meal list for 
# breakfast lunch and dinner for each day of the week. Use nested loops to implement this: 
# the outer loop should iterate over the days, and the inner loop should iterate over the meals of the day. 
# For each time, randomly select a meal from a predefined list and print it. 

# Output: ..."Tuesday for Breakfast I'm having Yogurt" "Tuesday for Lunch I'm having Chicken" 
# "Tuesday for Dinner I'm having Pizza" "Wednesday for Breakfast I'm having Tacos" ...

print("Question 2")

time_of_day = ["Breakfast", "Lunch", "Dinner"]
meal_options = ['Yogurt', 'Butter Chicken and Rice', 'Tandoori Chicken', 'Lasagne', 'Sandwich', 'Burger', 'Tacos', "Qdoba's", "Taco Bell", "Subway", "Denny's"]

for day in days_in_week:
    for meal_time in time_of_day:
        meal_name = random.choice(meal_options)
        print(day, "for", meal_time, "I'm having", meal_name)


# 3. Loop Condition Logic
# Objective: The aim of this assignment is to explore the importance of the loop condition in while loops. 
# You will create loops with different conditions to see how they influence the behavior of the loop.

# Task 1: Loop Condition Exploration Write a while loop with a condition that will never be true (an infinite loop). 
# Ask the user a series of questions until their answer triggers a break statement.

print("Question 3, Task 1")

user_break = ""

while user_break != "Yes":
    user_break = input("Please say 'Yes' to break the loop :")

# Task 2: Conditional Exit Create a while loop that will terminate after 5 iterations, and 
# each iteration you print which iteration it is on. (use a control variable)

print("Question 3, Task 2")

i = 1

while i <= 5:
    print(i)
    i = i+1

# 4. Python's Random Game Night
# Objective: The aim of this assignment is to explore the random package in Python and understand 
# how it can be used with loops to introduce randomness into your programs.

# Task 1: Random Choice Game Create a game where a player has a list of items. 
# They have to guess which item in the list was selected. Use random.choice() to select the item and take the user's guess via input. 
# Provide feedback on whether they guessed correctly or not keep them playing until they guess correctly.

print("Question 4")

random_choice_options = ["Yes", "No"]

i = 0
while i == 0:
    user_input = input("Please input either 'Yes' or 'No': ")
    if user_input == random.choice(random_choice_options):
        print("You an computer chose the same")
        ask_for_continue = input("Would you like to continue? Y or N ")
        if ask_for_continue == "N":
            i = 1
    else:
        print("Please Try Again")

# 5.Advanced Looping Techniques (BONUS)
# Objective: Advance your looping skills by exploring more complex list manipulations. 
# You will learn to selectively loop through parts of a list, use list comprehensions for concise code, 
# and generate numerical lists with Python's range and len function.

# Task 1: Ice Cream BO-GO Your local ice cream shop is running a buy-one-get-one on scoops today, 
# create a list of your five favorite scoops. Using a nested for loop print out all the combinations you can make

print("Question 5, Task 1")

scoops = ["Chocolate", 'Vanilla', 'Strawberry', 'Banana Caramel', 'Hot Fudge']

print("BOGO SPECIALS")

for option_one in scoops:
    for option_two in scoops:
        if option_one == option_two:
            pass
        else:
            print("BOGO Offer, Buy", option_one, "Get", option_two, "Free")

# Task 2: Double UP! If you land on a the same flavor print "Double <that flavor>" instead of repeating that flavor

print("Question 5, Task 2")

for option_one in scoops:
    for option_two in scoops:
        if option_one == option_two:
            print("Double", option_one)
        else:
            print("BOGO Offer, Buy", option_one, "Get", option_two, "Free")

# Task 3: No Repeats!  Make it to where you never print the same combinations of flavors, 
# If your printed "Vanilla Chocolate" you shouldn't see "Chocolate Vanilla" . 
# Hint: this can be done by gradually slicing off previous flavors from the inner loops list.

print("Question 5, Task 3")

second_scoop = scoops.copy()

for option_one in scoops:
    for option_two in second_scoop:
        if option_one == option_two:
            print("Double", option_one)
        else:
            print("BOGO Offer, Buy", option_one, "Get", option_two, "Free")
    second_scoop.remove(option_one)




