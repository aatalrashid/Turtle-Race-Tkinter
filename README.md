# Turtle-Race-Tkinter

Turtle Race!

Introduction
------------------------------------------------------------

In this project you will use loops to create a racing turtle game and draw a race
track.

================================================================
Step 1: Race track

You’re going to create a game with racing turtles. First they’ll need a race track.
Activity Checklist
Open the blank Python template Trinket: jumpto.cc/python-new.
Add the following code to draw a line using the ‘turtle’:


############################
1
The turtle write function writes text to the screen.
Try it:
There’s a better way of doing this in Python. You can use a for loop.
Update your code to use a for loop:
Now let’s use the turtle to draw some track markings for the race.
Now you need to fill in the numbers in between to create markings:
Did you notice that your code is very repetitive? The only thing that
changes is the number to write.
Hmm, that only prints numbers up to 4. In Python range(5) returns five
numbers, from 0 up to 4. To get it to also return 5 you’ll need to use
range(6) :


##############################
2
Move the turtle to the top left instead:
right(90) makes the turtle turn right 90 degrees (a right angle.) Moving forward(10)
Now we can draw some track markings. The turtle starts at coordinates
(0,0) in the middle of the screen.
Ah, you’ll want to lift the pen up first!
Instead of drawing a line horizontally, let’s draw vertical lines to create a
track:


#################################
3
before putting the pen down leaves a small gap between the number and the
start of the line. After drawing the line you lift up the pen and go backward(160) the
length of the line plus the gap.


Save Your Project
Challenge: More lines
Can you change your code so that the track lines go right
across the screen?
It looks neater if you centre the numbers:
And you can speed up the turtle so it draws faster:


####################################
4
If you want to make the turtle go even faster you can use
speed(0) .




================================================= STEP 2 ============================================================


Step 2: Racing turtles
Now for the fun bit. Let’s add some racing turtles. It would be really boring if the
turtles did the same thing every time so they will move a random number of steps
each turn. The winner is the turtle that gets the furthest in 100 turns.

Activity Checklist
The first line creates a turtle called ‘ada’. The next lines set the colour and shape
of the turtle. Now it really looks like a turtle!
When you use commands like forward(20) you are using a single turtle.
But you can create more turtles. Add the following code to the end of
your script (but make sure it’s not indented):
Let’s send the turtle to the starting line:


#######################################
5
Now you need to make the turtle race by moving a random number of
steps at a time. You’ll need the randint function from the Python random
library. Add this import line to the top of your script:
The randint function returns a random integer (whole number) between
the values chosen. The turtle will move forward 1, 2, 3, 4, or 5 steps at
each turn.
One turtle isn’t much of a race! Let’s add another one:


######################################
6
Note that the code for moving the blue turtle needs to be inthe same for loop as
the code for moving the red turtle so that they each make a move every turn.

Save Your Project
Challenge: Race time!
Now you’re ready to race. Pick a turtle and an opponent and
see who wins.
Can you add more turtles so you can race with more friends?
Colours include: orange, purple, violet, tomato, turquoise,
magenta and brown - or you can go to jumpto.cc/colours and
pick any colour you like!


#######################################
7
Save Your Project
Challenge: Do a twirl
Can you use a for turn in range(): loop to make each turtle do a
360 degree twirl after they get to the starting line? You’ll need
to make sure they are facing in the right direction at the start
of the race!
ada.right(36) will turn the red turtle right by 36 degrees.

Hint: A full turn is 360 degrees. A turtle could turn right 10
degrees 36 times, or left 5 degrees 72 times, or any other
numbers make 360!
Challenge: Dashed lines
Can you use a loop to make the track lines dashed instead of
solid?
Hint: Find the code that draws a straight line. Try using:for ,
forward() , penup() and pendown()

#################################################

Email: trevor@code4missions.com
Twitter: @trevornathan
LinkedIn: atwijukire-trevor-a10b5b184
Facebook: Trevor Nathan
