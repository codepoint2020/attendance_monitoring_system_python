from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("DarkOliveGreen4")


def move_forward():
    timmy.forward(10)



my_screen = Screen()

my_screen.listen()
my_screen.onkey(key="space", fun=move_forward)

print(my_screen.canvheight)
my_screen.exitonclick()

# from prettytable import PrettyTable

# table = PrettyTable()
# table.add_column("Pokemon Name", ["Pikachu","Squirtle","Charmander"])
# table.add_column("Type", ["Electric","Water","Fire"])
# table.align = "l"
# print(table)


