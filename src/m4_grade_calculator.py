###############################################################################
# DONE: 1.
#
#   In this module, we are going to create a script that helps you calculate
#   your score in this course.
#
#   First, we need a function that we can call to ask the user what their
#   current score is in a particular category.
#
#   Write a function called gather_score() that takes one arguement:
#     - category_name
#
#   This function should prompt the user to input their current score in the
#   category. So, if the function is called and given the "Participation"
#   category, it would prompt the user saying:
#
#       'What is your current grade in the Participation category? '
#
#   The user should then input their grade as a decimal (if they have a 95%,
#   they should put 0.95).
#
#   The function should return whatever score the user put as a float.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
def gather_score(category_name):
    return float(input(f"What is your current grade in {category_name} category?"))

###############################################################################
# DONE: 2.
#
#   Now we need a function that will calculate the user's grade in the course.
#
#   Write a function called calculate_final_grade() that takes 5 keyword
#   arguments (each indicate the current score that the user has in that
#   category):
#     - participation
#     - exam1
#     - exam2
#     - exam3
#     - final_project
#
#   It should then use those arguments to calculate the final grade in the
#   course. As a reminder, the weights for each of the categories in this
#   course are:
#
#   Participation: 20%
#   Exam 1:        10%
#   Exam 2:        15%
#   Exam 3:        20%
#   Final Project: 35%
#
#   As another reminder, you can calculate your final grade using this formula
#   (this example below only has two categories):
#
#       (category1_score * weight1) + (category2_score * weight2)
#
#   Remember, each of the scores and weights above should be written as
#   decimals (so, a 95% should be written as 0.95).
#
#   The function should return the result of the final grade calculation.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
def calculate_final_grade(participation, exam1, exam2, exam3, final_project):
    return (participation * 0.2) + (exam1 * 0.1) + (exam2 * 0.15) + (exam3 * 0.2) + (final_project * 0.3)

###############################################################################
# TODO: 3.
#
#   Now, let's put it all together.
#
#   Write a function called main() that will start everything off. The function
#   should do the following (make sure to use the functions you defined above):
#
#     1. Print 'Let's calculate your grade in CSC-141!'
#     2. Prompt the user to enter their current grade in the Participation
#        category and save that value to a variable (as a float)
#     3. Repeat step 2 for all of the categories in this course (see the list
#        in _TODO_ #2)
#     4. Calculate the final score using keyword arguments in the arguments of
#        the function you defined above and save the result to a variable
#     5. Convert the decimal score back to a percentage (HINT: multiply by
#        100) and save it to a variable
#     5. Print 'You currently have a <score>% in CSC-141.'
#
#   Don't forget to call your main() function to start things off.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
def main():
    print("Let's calculate your grade in CSC-141!")
    participation = float(input("What is your grade in the Participation category"))
    exam1 = float(input("What is your grade in the exam1 category"))
    exam2 = float(input("What is your grade in the exam2 category"))
    exam3 = float(input("What is your grade in the exam3 category"))
    final_project1 = float(input("What is your grade in the Final Project category"))
    calculate_final_grade(final_project = final_project1)


main()