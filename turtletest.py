import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Hello World with Turtle")
screen.title("My Turtle Program") 
screen.bgcolor("white")

# Create a turtle object
pen = turtle.Turtle()

# Write "Hello World" on the screen
pen.write("Hello World", align="center", font=("Arial", 24, "normal"))

# Hide the turtle
pen.hideturtle()

# Keep the window open until it is closed by the user
turtle.done()