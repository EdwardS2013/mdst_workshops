"""
MDST Workshop 1 - Python Basics Starter Code
"""

# Add any imports you need here:
import random
import base64

def part1(num):
    """
    Ask the user for a number. Depending on whether the number is even or odd,
    print out an appropriate (i.e. "even" or "odd") message to the user.
    """
    if num % 2 == 1:
        print("odd!")
    else:
        print("even!")


def part2():
    """
    Generate a random number between 1 and 9 (including 1 and 9). Ask the user
    to guess the number, then tell them whether they guessed too low, too high,
    or exactly right.
    (Hint: remember to use the user input lessons from the very first
    exercise).
    Keep the game going until the user types "exit".
    [ try checking the random module in python on google. Concepts: Infinite
    loops, if, else, loops and user/input].
    """
    x = random.randint(1,9)
    while(True):
        print("Guess: ")
        guess = input()
        if guess == 'exit':
            return
        elif int(guess) > x:
            print("Too high\n")
        elif int(guess) < x:
            print("Too low\n")
        elif int(guess) == x:
            print("You got it!")
            return


def part3(string):
    """
    Ask the user for a string and print out whether this string is a palindrome
    or not. (A palindrome is a string that reads the same forwards and
    backwards.)
    """
    for i in range(0, int(len(string)/2)):
        lo = string[i]
        hi = string[-(i+1)]
        if(lo != hi):
            print("False")
            return
    print("True")

def part4a(filename, username, password):
    """
    Encrypt your username and password using base64 module
    Store your encrypted username on the first line and your encrypted password
    on the second line.
    """
    f = open(filename, "w");
    f.write(base64.b64encode(username.encode()).decode())
    f.write("\n")
    f.write(base64.b64encode(password.encode()).decode())
    f.close()

def part4b(filename, password=None):
    """
    Create a function to read the file with your login information.
    Print out the decrypted username and password.
    If a password is specified, update the file with the new password.
    """
    f = open(filename, "r")
    username = base64.b64decode(f.readline()[:-1].encode()).decode()
    print("Username:", username)
    print("Password:", base64.b64decode(f.readline().encode()).decode())
    f.close()
    if password != None:
        part4a(filename, username, password)        


if __name__ == "__main__":
    part1(3)  # odd!
    part1(4)  # even!
    part2()
    part3("ratrace")  # False
    part3("racecar")  # True
    part4a("secret.txt", "naitian", "p4ssw0rd")
    part4b("secret.txt")
    part4b("secret.txt", password="p4ssw0rd!")
    part4b("secret.txt")
