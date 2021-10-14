from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)

timmy.shape('turtle')
timmy.color('IndianRed4')

# move the turtle forward 25 steps
timmy.forward(100)

my_screen = Screen()
my_screen.exitonclick()