from turtle import *
from random import randint

''' #use turtle to draw track markings for the race:
write(0)
forward(100)
write(5) '''

''' #fill in numbers in-btn to create markings:
write(0)
forward(20)
write(1)
forward(20)
write(2)
forward(20)
write(3)
forward(20)
write(4)
forward(20)
write(5)
forward(20) '''

speed(10) #speed up the turtle so it draws faster:

penup()  #you'll want to lift the pen up first!

goto(-140, 140) #move the turtle to the top left:

''' #use a for-loop for a shorter code:
for step in range(6):
    write(step)
    forward(20) '''

#lets draw vertical lines to create a track:
for step in range(17):
    write(step, align='center') #center the numbers
    right(90)
    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(20)
'''right(90) makes the turtle turn right 90 degrees. Moving foward(10) before putting the pen down leaves a small gap between the number and the
start of the line. After drawing the line you lift up the pen and go backward(160) the
length of the line plus the gap. '''

#RACING TURTLES:
#commands forward(20), you are using a single turtle:
#forward(20)
  #(1)
trevor = Turtle() #name of turtle
trevor.color('red') #color
trevor.shape('turtle') #shape

#lets send the turtle to the starting line:
trevor.penup()
trevor.goto(-160, 100)
trevor.pendown()
'''
Now you need to make the turtle race by moving a random number of
steps at a time. You’ll need the randint function from the Python random
library. The randint function returns a random integer (whole number) between
the values chosen. The turtle will move forward 1, 2, 3, 4, or 5 steps at
each turn.
'''

#for turn in range(100):
 #   trevor.forward(randint(1, 5))

#ADD ANOTHER TURTLE
   #(2)
bruce = Turtle()
bruce.color('blue')
bruce.shape('turtle')

bruce.penup()
bruce.goto(-160, 70)
bruce.pendown()

    #(3)
nico = Turtle()
nico.color('green')
nico.shape('turtle')

nico.penup()
nico.goto(-160, 40)
nico.pendown()

    #(4)
benja = Turtle()
benja.color('black')
benja.shape('turtle')

benja.penup()
benja.goto(-160, 10)
benja.pendown()

'''
code for mov'g blue turtle needs to br in same for-loop as the code for
moving the red turtlleso that they each make a move every turn.'''

for turn in range(100):
    trevor.forward(randint(1, 5))
    bruce.forward(randint(1, 5))
    nico.forward(randint(1, 5))
    benja.forward(randint(1, 5))











 












