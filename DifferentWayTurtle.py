import turtle
import random
from itertools import count

screen = turtle.Screen()
screen.bgcolor("light blue")
screen.title("CTT")
FONT=("Arial",25,"normal")
score=0
game_over=False

#turtle list
turtle_list=[]

#score turtle
score_turtle=turtle.Turtle()

#countdown turtle
countdown_turtle=turtle.Turtle()

def setup_score_turtle():
    score_turtle.hideturtle()
    score_turtle.color("dark blue")
    score_turtle.penup()

    top_height = screen.window_height() / 2
    y = top_height * 0.88

    score_turtle.setposition(0, y)
    score_turtle.write(arg="Score: 0", move=False, align="center", font=FONT)

grid_size=12

def make_turtle(x,y):
    t=turtle.Turtle()

    def handle_click(x,y):
        global score
        if not game_over:
            score += 1
            score_turtle.clear()
            score_turtle.write(arg=f"Score: {score}", move=False, align="center", font=FONT)

    t.onclick(handle_click)
    t.penup()
    t.shape("turtle")
    t.shapesize(2,2)
    t.color("dark green")
    t.goto(x*grid_size,y*grid_size)
    turtle_list.append(t)

x_coordinates=[-20,-10,0,10,20]
y_coordinates=[20,10,0,-10]

def setup_turtles():
    for i in x_coordinates:
        for j in y_coordinates:
            make_turtle(i,j)

    '''
    for i in range(-20,21,10):
        for j in range(20,-11,-10):
            turtle_instance=make_turtle(i,j)
            turtleList.append(turtle_instance)
    '''


def hide_turtles():
    for t in turtle_list:
        t.hideturtle()

#recursive function
def show_turtles_randomly():
    if not game_over:
        hide_turtles()
        random.choice(turtle_list).showturtle()
        screen.ontimer(show_turtles_randomly,500)

def count_down(time):
    global game_over
    countdown_turtle.hideturtle()
    top_height = screen.window_height() / 2
    y = top_height * 0.88
    countdown_turtle.setposition(0, y-30)
    countdown_turtle.clear()
    if time>0:
        countdown_turtle.penup()
        countdown_turtle.clear()
        screen.update()  # Ekrandaki sayacı optimize tutmak amacıyla yaptık ve tracer(1)'i kaldırdık.Bundan dolayı da else'e de bir update ekledik.
        countdown_turtle.write(arg=f"Time: {time}", move=False, align="center", font=FONT)
        screen.ontimer(lambda: count_down(time-1),1000)

    else:
        game_over=True
        countdown_turtle.clear()
        hide_turtles()
        countdown_turtle.write(arg="Game Over!", move=False, align="center", font=FONT)
        screen.update() #ekranı güncel tutmak amacı ile update fonksiyonunu çağırdık.

turtle.tracer(0)
setup_score_turtle()
setup_turtles()
hide_turtles()
show_turtles_randomly()
count_down(10)




turtle.mainloop()
