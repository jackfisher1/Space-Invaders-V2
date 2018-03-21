#Made with Python 3.6.4.
#Made 21/03/2018 by Jack Fisher.
#This code also has titles to point out which parts of the code do what.

import turtle
import os
import math
import random

#---LOGIN CODE---

uname = input("Enter the correct username to access the next step.")
if uname == "py7hon2":
    pcode = input("Enter the correct pin to access the project.")
    if pcode == "76538":

#---END OF LOGIN CODE---

#---BEGINING OF GAME CODE---

        #set up the screen
        wn = turtle.Screen()
        wn.bgcolor("black")
        wn.title("Space Invaders V2")

        #draw border
        border_pen = turtle.Turtle()
        border_pen.speed(0)
        border_pen.color("white")
        border_pen.penup()
        border_pen.setposition(-300,-300)
        border_pen.pendown()
        border_pen.pensize(3)
        for side in range(4):
            border_pen.fd(600)
            border_pen.lt(90)
        border_pen.hideturtle()

        #Set score 0
        score = 0

        #Draw score
        score_pen = turtle.Turtle()
        score_pen.speed(0)
        score_pen.color("white")
        score_pen.penup()
        score_pen.setposition(-290, 275)
        scorestring = "Score: %s" %score
        score_pen.write(scorestring, False, align="left", font=("Arial", 16, "bold"))
        score_pen.hideturtle()

        #Draw copyright message (Optional)
        copy_pen = turtle.Turtle()
        copy_pen.speed(0)
        copy_pen.color("white")
        copy_pen.penup()
        copy_pen.setposition(0, -350)
        copy_pen.write("Copyright © Jack Fisher", True, align="center", font=("Arial", 16, "bold"))
        copy_pen.hideturtle()

        #Draw instructions message (Optional)
        copy_pen = turtle.Turtle()
        copy_pen.speed(0)
        copy_pen.color("white")
        copy_pen.penup()
        copy_pen.setposition(0, -370)
        copy_pen.write("Left: Move Left, Right: Move Right, Space: Fire Bullet, Up: Grow, Down: Shrink", True, align="center", font=("Arial", 12, "bold"))
        copy_pen.hideturtle()

        #Title the game
        title_pen = turtle.Turtle()
        title_pen.speed(0)
        title_pen.color("white")
        title_pen.penup()
        title_pen.setposition(0, 330)
        title_pen.write("Space Invaders V2", True, align="center", font=("Arial", 20, "bold"))
        title_pen.hideturtle()

        #Create the player's bullet
        bullet = turtle.Turtle()
        bullet.color("cyan")
        bullet.shape("triangle")
        bullet.penup()
        bullet.speed(-50)
        bullet.setheading(90)
        bullet.shapesize(0.5, 0.5)
        bullet.hideturtle()

        bulletspeed = 20

        #Define bullet state
        bulletstate = "ready"

        #Create the player
        player = turtle.Turtle()
        player.color("white")
        player.shape("triangle")
        player.penup()
        player.speed(0)
        player.setposition(0, -250)
        player.setheading(90)
        player.shapesize(1, 1)

        playerspeed = 15

        #Choose a number of enemies
        number_of_enemies = 10
        #Create an empty list of enemies
        enemies = []

        #Add enemies to the list
        for i in range(number_of_enemies):
            #Create the enemy
            enemies.append(turtle.Turtle())

        for enemy in enemies:
            enemy.color("red")
            enemy.shape("circle")
            enemy.penup()
            enemy.speed(0)
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)
            enemy.setheading(-90)

        enemyspeed = 2

        #move the player left and right
        def move_left():
            x = player.xcor()
            x -= playerspeed
            if x < -280:
                x = - 280
            player.setx(x)

        def move_right():
            x = player.xcor()
            x +=playerspeed
            if x > 280:
                x = 280
            player.setx(x)

        def grow():
            player.shapesize(2, 2)
            bullet.shapesize(1, 1)

        def shrink():
            player.shapesize(1, 1)
            bullet.shapesize(0.5, 0.5)

        def fire_bullet():
            #Declare bulletstate as a global if it needs changed
            global bulletstate
            if bulletstate == "ready":
                bulletstate = "fire"
                #move the bullet to just above the player
                x = player.xcor()
                y = player.ycor() + 10
                bullet.setposition(x, y)
                bullet.showturtle()

        def isCollision(t1, t2):
            distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
            if distance <15:
                return True
            else:
                return False
        #Create keyboard bindings
        turtle.listen()
        turtle.onkey(move_left, "Left")
        turtle.onkey(move_right, "Right")
        turtle.onkey(fire_bullet, "space")
        turtle.onkey(grow, "Up")
        turtle.onkey(shrink, "Down")

        #Main game loop
        while True:

            for enemy in enemies:       
                #Move the enemy
                x = enemy.xcor()
                x += enemyspeed
                enemy.setx(x)

                #Make the enemies shoot
                

                #Move the enemy back and down
                if enemy.xcor() > 280:
                    #Move all enemies down
                    for e in enemies:
                        y = e.ycor()
                        y -= 40
                        e.sety(y)
                    enemyspeed *= -1
                    
                if enemy.xcor() <-280:
                    for e in enemies:
                        y = e.ycor()
                        y -= 40
                        e.sety(y)
                    enemyspeed *= -1

                #Check for a collision between bullet and enemy
                if isCollision(bullet, enemy):
                    #Reset the bullet
                    bullet.hideturtle()
                    bulletstate = "ready"
                    bullet.setposition(0, -400)
                    #Reset the enemy
                    x = random.randint(-200, 200)
                    y = random.randint(100, 250)
                    enemy.setposition(x, y)
                    #Update the score
                    score += 10
                    scorestring = "Score: %s" %score
                    score_pen.clear()
                    score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))


                if isCollision(player, enemy):
                    player.hideturtle()
                    enemy.hideturtle()
                    print ("Game Over")
                    wait (5)
                    exit()

            #Move the bullet
            if bulletstate == "fire":
                y = bullet.ycor()
                y += bulletspeed
                bullet.sety(y)

            #Check bullet boundry
            if bullet.ycor() > 275:
                bullet.hideturtle()
                bulletstate = "ready"

#---END OF GAME CODE---




