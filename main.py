import turtle
import time
import random
from random import randint

game_screen=turtle.Screen()
game_screen.bgcolor("white")
game_screen.title("Catch The Turtle!")

game_screen.tracer(0)  #Oyun akıcılığını optimize etmek adına yapılan kod.

#ekrandaki turtle'ın kodları
ken=turtle.Turtle()
ken.shape("turtle")
ken.color("dark green")
ken.shapesize(2,2)

#Turtle timer kodları
timer_text=turtle.Turtle()
timer_text.hideturtle()
timer_text.penup()

#Turtle score kodları
score=0
score_text=turtle.Turtle()
score_text.hideturtle()
score_text.penup()
score_text.goto(0,300)

game_over=False #oyun bittiğinde daha fazla tıkladığımızda puan almamak için.

#score'u kontrol eden fonksiyon
def increase_score(x,y):
    global score  #Fonksiyon içinde yerel değişken olmasın diye global terimini kullandık.
    if not game_over and ken.distance(x, y) < 20:
        score+=1
        score_text.clear()
        score_text.write(f"Score: {score}",align="center",font=("Courier", 30, "normal"))

start=time.time()
previous_time=-1 #önceki zamanı tutan değişken

while int(time.time()-start)<16:

    #Zamanı hesaplama
    current_time = int(time.time() - start)

    if current_time!=previous_time:
        timer_text.clear()
        timer_text.goto(-70,350)
        ken.penup()
        ken.goto((randint(-200,200), randint(-200,200)))  # pozisyonu ayarlama
        timer_text.write(f"Time={15-current_time}", font=("Courier", 30, "normal")) #Zaman kontrolü yapan kod.
        previous_time = current_time
        game_screen.onscreenclick(increase_score) #Ekrana tıkladıkça score'umuzu arttıran kod bloğu.

    game_screen.update() #ekranı sürekli güncel tutmamızı sağlayan kod bloğu.

game_over = True
score_text.goto(0, 0)
score_text.write(f"Times is finished\n Score: {score}", align="center", font=("Courier", 30, "normal"))
turtle.mainloop()