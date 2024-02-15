###############################################################################
#
#   This is NOT a todo. I have provided you with a function that you will use
#   later. You do NOT have to understand how it works, but you will have to
#   call it, so read this carefully.
#
#   This function called date_from_now() takes one parameter
#       num_of_days     <-- this is an int
#   and it returns the date that is that many days from now. So, if you put 2
#   in for its parameters it would return the date of the day that is 2 days
#   from now as a string.
#
#   For example, if today is February 06, 2024 and we gave the number 2 as its
#   parameter, the function would return:
#
#       "February 08, 2024"
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

import datetime

def date_from_now(num_of_days):
    today = datetime.date.today()
    end_date = today + datetime.timedelta(days=num_of_days)
    return end_date.strftime('%B %d, %Y')

###############################################################################
# DONE: 1.
#
#   Write a function called book_info() that takes four keyword arguments:
#     - title
#     - author
#     - genre
#     - num_of_pages
#   and prints them like so:
#
#   Title: The Hobbit
#   Author: J.R.R. Tolkien
#   Genre: Fantasy/Adventure
#   Number of Pages: 300
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
def book_info(title, author, genre, num_of_pages):
    print(f'Title: {title}\nAuthor: {author}\nGenre: {genre}\nNumber of Pages: {num_of_pages}')

###############################################################################
# DONE: 2.
#
#   Write a function called reading_plan() that takes two parameters
#     - num_of_pages
#     - num_of_days
#   and returns a string that describes a reading plan to the user.
#
#   For example, if I have a book that has 300 pages, I want to finish it in
#   10 days and today is February 6, 2024, the function would return:
#
#       To read this book in 10 days starting tomorrow, you will have to read
#       30 pages per day. You will finish the book on February 16, 2024. Happy
#       reading!
#
#   Hint: Use the function I gave you
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
def reading_plan(num_of_pages, num_of_days):
    d = date_from_now(num_of_days)
    pnum = num_of_pages / num_of_days
    return f'To read {num_of_pages} pages in {num_of_days} days, you will need to read {pnum} pages per day. You will finish these pages on {d}. Have fun!'

###############################################################################
# TODO: 3.
#
#   Now write a function called main() that will start everything off.
#
#     1. First, create 5 different variables and give them a value (you do NOT
#        need to use user input, just give them your own values in the code):
#       - title
#       - author
#       - genre
#       - num_of_pages
#       - num_of_days
#     2. Using the function you defined earlier, print the book information
#        (using keyword arguments in your function). Make sure you use the
#        variables you created.
#     3. Using the other function you defined, print the reading plan. Make
#        sure you use the variables you created.
#
#   Don't forget to call your main() function to start things off.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
def main():
    title1 = "The Hobbit"
    author1 = "J.R.R. Tolkien"
    genre1 = "Adventure/Fantasy"
    num_of_pages1 = int("300")
    num_of_days = 5
    book_info(title=title1, author=author1, genre=genre1, num_of_pages=num_of_pages1)
    print(reading_plan(num_of_pages1, num_of_days))
main()
    
# def book_author(**info):
#     print(info["author"])

# book_author(title="The Swiss Family Robinson", author="Johann David Wyss",
# num_of_pages=533)