###############################################################################
# DONE: 1.
#
#   In this module, we are going to create a script that will be a system where
#   superheroes will input their information and it will create a short bio
#   about them.
#
#   First, we need to create some functions to help us out.
#   
#   Write a function called name() that asks the superhero what their superhero
#   name is.
#
#   It will prompt them with this prompt:
#
#       'What is your superhero name? '
#
#   Then, it will allow them to type their superhero name. It will then return
#   that name.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
def name():
    return input("What is your name?")

###############################################################################
# DONE: 2.
#
#   Now, lets create another function called powers() that is very similar, but
#   this time it will prompt the superhero to enter their superhero powers. It
#   will prompt them like this:
#
#       'Please list your superhero powers: '
#
#   Then it will allow them to type their superhero powers and return what they
#   typed.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
def powers():
    return input("Please list your superhero powers:")

###############################################################################
# DONE: 3.
#
#   And, create one more function called sidekick() that asks the superhero
#   what their sidekick's name is like so:
#
#       'Who is your sidekick? '
#
#   Then it will allow them to type their sidekick's name and return the
#   result.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
def sidekick():
    return input("Who is your sidekick?")

###############################################################################
# DONE: 4.
#
#   Now that we have all the pieces together, we need to put them all together.
#
#   Write a function called main() that will start things off. It should do
#   things in this order (make sure you use the functions you defined above).
#
#     1. Prints 'Hello Hero!'
#     2. Ask them for their name and save it to a variable
#     3. Prints 'Hello <THEIR NAME HERE>!
#     4. Ask them for their powers and save it to a variable
#     5. Prints 'What great powers!'
#     6. Ask them for their sidekick's name and save it to a variable
#     7. Prints 'Ah, <SIDEKICK NAME>! What a great partner!'
#     8. Then prints a bio that looks like this example below:
#
#        Each superhero has amazing powers! Superman has the powers of flight,
#        invulnerability, strength, and x-ray vision. With his sidekick,
#        Krypto, by his/her side, those bad guys don't stand a chance!
#
#   Make sure you call your main() function after you define it.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
def main():
    print("Hello Hero!")
    n = name()
    print(f'Hello {n}!')
    p = powers()
    print('What great powers!')
    s = sidekick()
    print(f"Ah, {s}! What a great partner!")
    print(f"Superheroes are awesome possum! {n} has the power to {p}! This duo of {n} and {s} is unnnstoppableee!")

main()