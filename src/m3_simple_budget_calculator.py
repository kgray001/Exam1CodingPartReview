###############################################################################
# DONE: 1.
#
#   In this module, we are going to create a simple budget calculator.
#
#   First, we need a function to deduct taxes out of our gross monthly income
#   (that is the amount before taxes are taken out). The amount that is left is
#   called our net monthly income (that is how much you actually get to spend
#   each month).
#
#   Write a function called calculate_net_income() that takes two parameters:
#     - gross_pay
#     - tax_percentage
#   and calculates the net income. As a reminder, you calculate net income by:
#
#       gross income multiplied by the percentage of tax taken out (as a
#       decimal) and subtracting that from the original gross income
#
#   So, if I made $10,000 each month and 25% of my income was taken out by
#   taxes, I would calculate my net income by doing the following calculation:
#
#       10000 - (10000 * 0.25)
#
#   The function should return the net income that it calculates.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
def calculate_net_income(gross_pay, tax_percentage):
    net_income = gross_pay - (gross_pay * tax_percentage)
    return net_income

###############################################################################
# DONE: 2.
#
#   Now, let's write a function that will help us deduct certain categories out
#   of our budget.
#
#   Write a function called expense() that takes two parameters:
#     - total               <-- the amount we have left to spend in our budget
#     - amount_budgeted     <-- the amount we typically spend in this category
#
#   This function should simply subtract the amount budgeted from the amount we
#   have left to budget.
#
#   It should then return the amount that we have left after we have budgeted
#   that category.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
def expense(total, amount_budgeted):
     leftover = total - amount_budgeted 
     return leftover 

###############################################################################
# DONE: 3.
#
#   Write a simple function that prints how much the user has left to budget.
#   This funciton should be called current_amount() and it takes one parameter:
#     - amount
#
#   It should simply print a statement saying how much the user has left in
#   their budget. For example, if it is given the amount 100, it will print:
#
#       'You have $100 left in your budget'
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
def current_amount(amount):
     return print(f"You have ${amount} left in your budget.")

###############################################################################
# TODO: 4.
#
#   Write a function called main() that starts things off. This function should
#   do the following (make sure you use the functions you defined above):
#
#     1. Prints 'Let's do some budgeting!'
#     2. Gives the user this prompt:
#           'What is your monthly income (before taxes)? '
#        allows them to enter a value (as a float), and saves the amount to a
#        variable.
#     3. Calculates how much they have left in their budget after taxes and
#        saves it to a variable
#     4. Updates the user on how much they have left in their budget
#     5. Gives the user this prompt:
#           'How much do you spend on groceries each month? '
#        allows them to enter a value (as a float), and saves the amount to a
#        variable
#     6. Calculates how much they have left in their budget after that expense
#        and saves it to a variable
#     7. Updates the user on how much they have left in their budget
#     8. Repeat steps 5-7 but this time give the user this prompt:
#           'How much do you spend on gas each month? '
#        and updates the values accordingly.
#     9. Prints 'Congratulations! You have $<AMOUNT LEFT> left in your budget!'
#
#   Don't forget to call your main() function to start things off.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
def main():
     print("Let's do some budgeting!")
     income = float(input("What is your monthly income?"))
     budget_amount = calculate_net_income(income,.50)
     current_amount(budget_amount)
     groceries = float(input("How much do you spend on groceries every month?"))
     after_groceries = expense(budget_amount, groceries)
     current_amount(after_groceries)
     gas = float(input("How much money do you spend on gas per month?"))
     after_gas = expense(after_groceries, gas)
     print(f"Congratulations! You have ${after_gas} left in your budget!")
main()