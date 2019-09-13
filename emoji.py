import turtle


jim = turtle.Turtle()
bob = turtle.Turtle()
alex = turtle.Turtle()
clix = turtle.Turtle()


jim.shape("turtle")
bob.shape("turtle")
alex.shape("turtle")
clix.shape("turtle")


jim.up()
jim.goto(0, -100)
jim.down()

jim.begin_fill()
jim.fillcolor("yellow")
jim.circle(125)
jim.end_fill()

alex.up()
alex.goto(-67, -40)
alex.setheading(-60)
alex.width(5)
alex.down()
alex.circle(80, 120)
alex.fillcolor("black")

for i in range(-35, 105, 70):
    clix.up()
    clix.goto(i, 35)
    clix.setheading(0)
    clix.down()
    clix.begin_fill()
    clix.circle(10)
    clix.end_fill()














turtle.exitonclick()