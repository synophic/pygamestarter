import turtle
import os
import math
import random
import sys

#creat a game screen
win = turtle.Screen()
win.bgcolor("black")
win.title("Invaders")

#register shape
turtle.register_shape("player.gif")
turtle.register_shape("inv01.gif")
turtle.register_shape("bullet.gif")

#make a yellow game border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("yellow")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(4)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

#set the score
score = 0
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align = "left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

#player setting                
player = turtle.Turtle()
player.color("blue")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)
playerspeed = 15

#random spawn enemy
numenemies = 5
enemies = []

for i in range(numenemies):
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.color("red")
    enemy.shape("inv01.gif")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)

enemyspeed = 2
    
def movelf():
    """gain lift key"""
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)

def movergh():
    """gain right key"""
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

def fire():
    """fire a bullet"""
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()

def close():
    """close game screen"""
    turtle.bye()
    sys.exit()
        
def collision(t1, t2):
    """calculate a collision between player&enemy"""
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False

#keyboard input    
turtle.listen()
turtle.onkey(movelf, "Left")
turtle.onkey(movergh, "Right")
turtle.onkey(fire, "space")
turtle.onkey(close, "Escape")

#create a bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("bullet.gif")
bullet.penup()
bullet.speed(0)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 20

bulletstate = "ready"

#maingame loop
while True:

    for enemy in enemies:
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)
        if enemy.xcor() > 280:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemyspeed *= -1
        if enemy.xcor() < -280:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemyspeed *= -1
        if collision(bullet, enemy):
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)
            score += 10
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align = "left", font=("Arial", 14, "normal"))

        if collision(player, enemy):
            player.hideturtle()
            enemy.hideturtle()
            print("GAME OVER")
            break

    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"

