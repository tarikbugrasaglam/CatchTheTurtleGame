import turtle
import time
from random import randint
from idlelib.configdialog import font_sample_text

game_screen=turtle.Screen()
game_screen.bgcolor("white")
game_screen.title("Catch The Turtle!")

game_screen.tracer(0)

ken=turtle.Turtle()
ken.shape("turtle")
ken.color("dark green")

timer_text=turtle.Turtle()
timer_text.hideturtle()  # Hide the turtle icon
timer_text.penup()       # Stop drawing the turtle trail

score=0
score_text=turtle.Turtle()
score_text.hideturtle()
score_text.penup()
score_text.goto(0,300)

def increase_score(x,y):
    global score
    score+=1
    score_text.clear()
    score_text.write(f"Score: {score}",align="center",font=("Courier", 30, "normal"))

game_screen.onscreenclick(increase_score)


start=time.time()
previous_time=-1 #önceki zamanı tutan değişken

while (time.time()-start)<16:
    current_time=int(time.time()-start)

    if current_time!=previous_time:
        timer_text.clear()
        timer_text.goto(-70,350)
        ken.penup()
        ken.goto((randint(-200,200), randint(-200,200)))  # pozisyonu ayarlama
        ken.pendown()
        timer_text.write(f"Time={current_time}", font=("Courier", 30, "normal"))
        previous_time = current_time

    game_screen.update()
    #time.sleep(0.100)  # Kaplumbağanın hızını yavaşlatmak için bekleme süresi

score_text.goto(0, 0)  # Sonucu ortala
score_text.write(f"Times is done\n Score: {score}", align="center", font=("Courier", 30, "normal"))



turtle.mainloop()