name = 'Alice'
if name == 'Alice':
    print('Hi, Alice')
else:
    print('Hello, stranger')

name = 'Bob'
age = 5
if name == 'Alice':
    print('Hi, Alice')
elif age < 12:
    print('You are not Alice, kiddo')
else:
    print('You are neither Alice nor a little kid.')

## While Loops ##

while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello, Joe. What is the password? (It is a fish)')
    password = input()
    if password == 'swordfish':
        break
    print('Access granted.')
    

## For Loops ##

for i in range (0,10,2):
        print(i)

for i in [1,2,3,4,5]:
    if i == 3:
        break
else:
    print('only executed when no item of the list is equal to 3')

import random
for i in range (5):
    print(random.randint(1,10))

## Import ##

import sys

while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed {}'.format(response))

## Functions ##

import random
def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrare and ask again'

r = random.randint (1, 6)
fortune = getAnswer (r)
print(fortune)

def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError as e:
        print('Error: Invalid argument: {}'.format(e))

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))

## Manipulating strings ##
print('Hello there!\nHow are you?\nI\'m doing fine.')

