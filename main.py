from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.title("Welcome to the turtle zoo!")
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "Black", "green", "blue", "gray"]

y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

# Create 6 turtles
for turtle_index in range(0, 6):
	new_turtle = Turtle(shape="turtle")
	new_turtle.penup()
	new_color = random.choice(colors)
	new_turtle.color(new_color)
	new_turtle.goto(x=-230, y=y_positions[turtle_index])
	all_turtles.append(new_turtle)
	colors.remove(new_color)
print(colors)
if user_bet:
	is_race_on = True

while is_race_on:
	for turtle in all_turtles:
		# 230 is 250 - half the width of the turtle.
		if turtle.xcor() > 230:
			is_race_on = False
			winning_color = turtle.pencolor()
			if winning_color == user_bet:
				print(f"You won! The {winning_color} turtle is the winner!")
			else:
				print(f"You lost! The {winning_color} turtle is the winner!")

		# Make each turtle move a random amount.
		rand_distance = random.randint(0, 10)
		turtle.forward(rand_distance)

screen.exitonclick()
