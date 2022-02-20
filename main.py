from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
tim.pensize(4)


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def turn_right():
    tim.right(15)


def turn_left():

    tim.left(15)


def clear_drawing():
    tim.reset()


def toggle_pen():
    if tim.isdown():
        tim.penup()
    else:
        tim.pendown()


def circle_right():
    tim.circle(-50, 30)


def circle_left():
    tim.circle(50, 30)


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="space", fun=toggle_pen)
screen.onkey(key="c", fun=clear_drawing)
screen.onkey(key="q", fun=circle_left)
screen.onkey(key="e", fun=circle_right)


screen.exitonclick()