
#Liana Bernt GIS 6345 Assignment 3


#Exercise 5.1

import time
epochtime = time.time()


def calctime(time):
    sec = time % 60
    mins = (time // 60) % 60
    hour = (time // 3600) % 24
    days = (time // 86400)
    print("It has been " + str(int(days)) + " days " + str(int(hour)) + " hours " + str(int(mins)) + \
          " minutes and " + str(int(sec)) + " seconds") 

calctime(epochtime)


#Exercise 5.2

def check_fermat(a, b, c, n):
    if n > 2 and a**n + b**n == c**n:
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn't work")

def fermat_input():
    print("pick a number")
    a = int(input())
    print("pick another number")
    b = int(input())
    print("and a third number")
    c = int(input())
    print("one more!")
    n = int(input())
    check_fermat(a, b, c, n)

fermat_input()


#Exercise 6.3

def first(word):
    return word[0]
def last(word):
    return word[-1]
def middle(word):
    return word[1:-1]

def is_palindrome(word):
    word = str(word)
    if len(word) <= 1:
        return True
    elif first(word) != last(word):
        return False
    else:
        return is_palindrome(middle(word))


print(is_palindrome("hello"))
print(is_palindrome("hannah"))

