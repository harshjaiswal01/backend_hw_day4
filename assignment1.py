import random
# 1. The Range Riddle
# Objective: The aim of this assignment is to deepen your understanding of Python's range() function and its application in loops. 
# You will correct a code snippet, simulate moods for different days, and create a countdown timer.

# Task 1: Every Other Day Write a program that prints each day of the week, but only if that day is on an even index.

# Example Outcome: An example output could be "Sunday", "Tuesday", "Thursday"

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

user_break = ""

while user_break != "Yes":
    user_break = input("Please say 'Yes' to break the loop :")

# Task 2: Conditional Exit Create a while loop that will terminate after 5 iterations, and 
# each iteration you print which iteration it is on. (use a control variable)

i = 1

while i <= 5:
    print(i)
    i = i+1