import turtle
from turtle import *
t = Turtle()
t.speed(100)

# turtle.done()
#define the functin name then pass arguements/parameter
# def add(x,y):
#     print(x+y)
# def square(x):
#     t.forward(125)
#     t.left(90)
#     t.forward(100)
#     t.left(90)

# square(50)
# turtle.done()
# for i in range(1,4):
#     print(i)

# for i in range(0,3):
#     t.forward(90)
#     t.right(120)

""" for i in range (0,60):
    t.forward(100)
    t.left(90)
    t.right(5)
    t.speed(100)
    t.forward(200)
    t.left(120) """

# for i in range(60):
#     def square(x):
#         t.forward(x)
#         t.left(90)
#         t.forward(x)
#         t.left(90)
#         t.forward(x)
#         t.left(90)
#         t.forward(x)
#         t.left(90)
#         t.right(5)
#     square(200)


"""         t.forward(x)
        t.left(90)
        t.forward(x)
        t.left(90)
        t.forward(x)
        t.left(90)
        t.forward(x)
        t.left(90)
        square(200) """

# sidelength = 100
# rotate = 90
# def square(x,y):
#     for i in range(60):
#         t.forward(x)
#         t.left(y)
# square(100,90)
# def doubleSquares(iRange):
#     length = 25
#     for i in range(iRange):
#         square(length, 90)
#         length = length + 5
# doubleSquares(5)

# for i in range(60):
#     def square(x):
#         t.forward(x)
#         t.left(90)
#         t.forward(x)
#         t.left(90)
#         t.forward(x)
#         t.left(90)
#         t.forward(x)
#         t.left(90)
#         t.right(5)
#     square(200)
# y=input("whats your name")
# # turtle.done()
# print(y)
# def add(x,y):
#     return(x+y)
# bill=add(5,10)
# print(bill)
# sidelength=5
# def square(x,y):
#     for i in range(60):
#         t.forward(100)
#         t.left(90)
#         t.right(5)
#     for i in range(60):
#         length=5
#         length= length + 5
# square(200,100)
# for i in range(60):
#     def square(x):
#         t.forward(x)
#         t.right(90)
#         t.forward(x)
#         t.right(90)
#         t.forward(x)
#         t.right(90)
#         t.forward(x)
#         t.right(90)
#         t.left(5)
#         length=5
#         length= length + 5
#     square(200)

def manySquares(x):
    y=10
    for i in range(x):
        square(y)
        y=y+5
        t.left(5)
manySquare(3)
turtle.done()