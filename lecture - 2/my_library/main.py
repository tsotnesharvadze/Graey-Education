import turtle


me = turtle.Turtle()

me.penup()
me.setpos(0, 100)
me.pendown()
me.circle(10)
me.penup()


screen = me.screen

screen.title("Welcome to the turtle zoo!")

def forward_and_left(distnace: int, angle: float):
    me.forward(distnace)
    me.left(angle)


def go_forward():
    me.forward(1)
    screen.ontimer(go_forward, 20)

def left():
    me.left(20)

def right():
    me.right(20)

colors = ['red', 'green', 'blue']
from random import choice

# for i in range(360):
#     if i % 4 == 0:
#         clr = choice(colors)
#         me.color(clr)
#     me.left(1)
#     for i in range(4):
#         forward_and_left(100, 90)


screen.listen()

screen.onkey(go_forward, 'w')
screen.onkey(left, 'a')
screen.onkey(right, 'd')

screen.exitonclick()
screen.mainloop()