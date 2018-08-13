import turtle
import time

boom=10

timer = turtle.Turtle()
timer.penup()
timer.hideturtle()
timer.goto(0, 300)


while boom >0:
    timer.write(str(boom), move = True, align = "center", font = ("Arial", 20, "normal"))
    
    time.sleep(1)
    boom -= 1
    timer.clear()
    timer.goto(0, 300)
    if boom == 0:
        print("Your time is up kid, go back to bed")
        quit()

        
 
        
  
