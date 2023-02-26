from turtle import Turtle
import turtle
t = Turtle()

# import turtle
# t = turtle.Turtle()
def draw_line():
    t.pd()
    t.fd(200)
    t.pu()
    t.bk(200)
    t.pd()
    t.bk(200)
def half_line():
    t.pd()
    t.fd(200)

q = input("Which line you want to see? (Half/Full)")
if q in ["full", "Full"]:
   draw_line()
elif q in ["half", "Half"]:
    half_line()
else:
    print("Invalid Input")


t.hideturtle()
turtle.mainloop()


