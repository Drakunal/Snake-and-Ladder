import turtle as t


#Define the font style of the board numbers
FONT = ("Times New Roman", 15, "bold")
window = t.Screen()
pmover1 = t.Turtle()
pmover2 = t.Turtle()
diceT = t.Turtle()
#Class for designing the board of snake and ladder 
class board():
        

        def __init__(self):
                
                
                window.bgcolor("light yellow")
                window.setup(650, 650)

                #Define the turtle characteristics
                t.hideturtle()
                t.pencolor("blue")
                t.pensize(3)
                t.up()
                t.goto(-125,-125)
                t.down()
                t.speed(0)

                #Code for drawing the boxes of the board
                for k in range(-125,375,100):
                   for j in range(-125,375,100):
                      t.sety(j)
                      t.setx(k)
                      for i in range(4):
                         t.right(90)
                         t.forward(100)
                
                t.up()
                t.goto(-120,-120)
                t.pensize(2)
                
                #Define the color of the numbers on the board
                t.pencolor("red")

                #Code for writing the number 1 to 5 and 11 to 15 and 21 to 25
                x,y=1,6
                for k in range(-150,400,200):
                   for j in range(-210,290,100):
                      board.text_at_xy(j,k , x)
                      x+=1
                   x+=5

                #Code for writing the number 6 to 10 and 16 to 20
                for k in range(-60,200,200):
                   for j in range(190,-275,-100):
                      board.text_at_xy(j,k , y)
                      y+=1
                   y+=5
                t.speed(1)   
                #####----------Display Game Image Gif---------########
                   
                #display ladder
                window.addshape('ladder.gif')
                tr = t.Turtle()
                
                #tr.hideturtle()
                tr.up()
                tr.goto(230,-90)
                tr.shape('ladder.gif')

                #display ladder2
                window.addshape('ladder2.gif')
                tr2 = t.Turtle()
                tr2.up()
                tr2.goto(40,170)
                tr2.shape('ladder2.gif')
     
                
                tr3 = t.Turtle()
                tr3.up()
                tr3.goto(-70,-30)
                tr3.shape('ladder2.gif')
    
                #display orange snake
                window.addshape('snake.gif')
                tr = t.Turtle()
                tr.up()
                tr.goto(130,110)
                tr.shape('snake.gif')
                

                #display red snake
                window.addshape('snake2.gif')
                tr = t.Turtle()
                tr.up()
                
                tr.goto(30,-120)
                tr.shape('snake2.gif')

                #display purple snake
                window.addshape('snake3.gif')
                tr = t.Turtle()
                tr.up()
                
                tr.goto(-160,0)
                tr.shape('snake3.gif')

                #Display the initial dice
                
                board.dice('dice6.gif',diceT)
                board.player2(window,-180,-150,pmover2)
                board.player1(window,-190,-190,pmover1)

                t.goto(-270,0)
                

        def dice(dice,diceT):
                
                #Display initial dice
                window.addshape(dice)
                
                
                diceT.up()
                diceT.goto(-270,100)
                diceT.shape(dice)
                
        def player1(window,x,y,pmover1):
                
                #Display initial bull
                
                window.addshape('cow.gif')
                
                pmover1.up()
                pmover1.speed(3)
                pmover1.goto(x,y)
                pmover1.shape('cow.gif')
                pmover1.goto(x,y)
                
        def player2(window,x,y,pmover2):
                
                #Display initial cow
                
                window.addshape('bull.gif')
                pmover2.speed(3)
                pmover2.up()
                pmover2.goto(x,y)
                pmover2.shape('bull.gif')
                pmover2.goto(x,y)
        

        def text_at_xy(x, y, text):
                t.penup()
                t.goto(x, y)
                t.write(text, font=FONT)
                
        def winner(window):
                window.addshape('win.gif')
                tr = t.Turtle()

                #tr.hideturtle()
                tr.up()

                tr.shape('win.gif')
                q = input("Press Enter to Restart the Snake and Ladder Game: ")
                tr.hideturtle()
                
                
     
                
                
              

#start = board()

