import random
import time
import board
import numberCoordinate as nC



player1,player2=1,1 #Define initial value on starting square
p1 = nC.player1_initial_position#Getting the number to coordinate dictionary from numberCoordinate.py
p2 = nC.player2_initial_position #Getting the number to coordinate dictionary from numberCoordinate.py



#Function to roll and change the dice
def rollDice():
   n = random.randint(1,6)
   board.board.dice("dice1.gif",board.diceT)
   time.sleep(.11)
   board.board.dice("dice2.gif",board.diceT)
   time.sleep(.11)
   board.board.dice("dice3.gif",board.diceT)
   time.sleep(.11)
   board.board.dice("dice4.gif",board.diceT)
   time.sleep(.11)
   board.board.dice("dice5.gif",board.diceT)
   time.sleep(.11)
   board.board.dice("dice6.gif",board.diceT)
   time.sleep(.11)
   board.board.dice("dice"+str(n)+".gif",board.diceT)
   return n

#Function to move the bull (Snake and Ladder rules included)
def movePlayer1(n):
   global player1
   
    

   #Code block to move the player gradually from the start square to the terminating square
   for i in range(1,n+1):
      time.sleep(0.2)
      player1 = player1+1
      if (player1==25):
         print("Big Bad Bull Wins")
         x,y= (p1.get(player1))[0],(p1.get(player1))[1]
         board.board.player1(board.window,x,y,board.pmover1)
         board.board.winner(board.window)
         
         break
      elif (player1>25):
         print("Big Bad Bull Won")
         board.board.winner(board.window)
         
      else:
         x,y= (p1.get(player1))[0],(p1.get(player1))[1]
         board.board.player1(board.window,x,y,board.pmover1)
      
         
   #Code to define snake and ladder point and implement ascension and descension    

   #Ladder Rules
   if (player1==5):
      x,y= (p1.get(6))[0],(p1.get(6))[1]
      board.board.player1(board.window,x,y,board.pmover1)
      x,y= (p1.get(15))[0],(p1.get(15))[1]
      board.board.player1(board.window,x,y,board.pmover1)
      player1=15
      
   if (player1==9):
      x,y= (p1.get(12))[0],(p1.get(12))[1]
      board.board.player1(board.window,x,y,board.pmover1)
      player1=12
      
   if (player1==18):
      x,y= (p1.get(23))[0],(p1.get(23))[1]
      board.board.player1(board.window,x,y,board.pmover1)
      player1=23

   #Snake Rules
   if (player1==8):
      x,y= (p1.get(3))[0],(p1.get(3))[1]
      board.board.player1(board.window,x,y,board.pmover1)
      player1=3
      
   if (player1==20):
      x,y= (p1.get(11))[0],(p1.get(11))[1]
      board.board.player1(board.window,x,y,board.pmover1)

      x,y= (p1.get(10))[0],(p1.get(10))[1]
      board.board.player1(board.window,x,y,board.pmover1)

      x,y= (p1.get(1))[0],(p1.get(1))[1]
      board.board.player1(board.window,x,y,board.pmover1)
      player1=1
      
   if (player1==24):
      x,y= (p1.get(17))[0],(p1.get(17))[1]
      board.board.player1(board.window,x,y,board.pmover1)

      x,y= (p1.get(14))[0],(p1.get(14))[1]
      board.board.player1(board.window,x,y,board.pmover1)
      player1=14

#Function to move the cow (Snake and Ladder rules included)
def movePlayer2(n):
   global player2
      #Code block to move the player gradually from the start square to the terminating square
   for i in range(1,n+1):
      time.sleep(0.2)
      player2 = player2+1
      if (player2==25):
         print("Fluffy Cow Wins")
         x,y= (p2.get(player2))[0],(p2.get(player2))[1]
         board.board.player2(board.window,x,y,board.pmover2)
         board.board.winner(board.window)
         
         break
      elif (player2>25):
         print("Fluffy Cow Won")
         board.board.winner(board.window)
         
         
      else:
         x,y= (p2.get(player2))[0],(p2.get(player2))[1]
         board.board.player2(board.window,x,y,board.pmover2)
         
      x,y= (p2.get(player2))[0],(p2.get(player2))[1]
      board.board.player2(board.window,x,y,board.pmover2)

   #Code to define snake and ladder point and implement ascension and descension   

   #Ladder Rules
   if (player2==5):
      x,y= (p2.get(6))[0],(p2.get(6))[1]
      board.board.player2(board.window,x,y,board.pmover2)
      x,y= (p2.get(15))[0],(p2.get(15))[1]
      board.board.player2(board.window,x,y,board.pmover2)
      player2=15
      
   if (player2==9):
      x,y= (p2.get(12))[0],(p2.get(12))[1]
      board.board.player2(board.window,x,y,board.pmover2)
      player2=12
      
   if (player2==18):
      x,y= (p2.get(23))[0],(p2.get(23))[1]
      board.board.player2(board.window,x,y,board.pmover2)
      player2=23

   #Snake Rules
   if (player2==8):
      x,y= (p2.get(3))[0],(p2.get(3))[1]
      board.board.player2(board.window,x,y,board.pmover2)
      player2=3
      
   if (player2==20):
      x,y= (p2.get(11))[0],(p2.get(11))[1]
      board.board.player2(board.window,x,y,board.pmover2)

      x,y= (p2.get(10))[0],(p2.get(10))[1]
      board.board.player2(board.window,x,y,board.pmover2)

      x,y= (p2.get(1))[0],(p2.get(1))[1]
      board.board.player2(board.window,x,y,board.pmover2)
      player2=1
      
   if (player2==24):
      x,y= (p2.get(17))[0],(p2.get(17))[1]
      board.board.player2(board.window,x,y,board.pmover2)

      x,y= (p2.get(14))[0],(p2.get(14))[1]
      board.board.player2(board.window,x,y,board.pmover2)
      player2=14

   

def startplay():
   #Code to allow users to play
   global player1,player2
   player1,player2=1,1
   
   
   print("\nNew Game!!")
   play = True
   while (play):
      
      if (player1>24 or player2>24):
         
         print("\nGame Restarting...")
         x,y= (p1.get(1))[0],(p1.get(1))[1]
         board.board.player1(board.window,x,y,board.pmover1)
         x,y= (p2.get(1))[0],(p2.get(1))[1]
         board.board.player2(board.window,x,y,board.pmover2)
         startplay();
         break
      a = input("\nFluffy Cow: Press Enter To Roll Dice.. ")
      d = rollDice()
      movePlayer1(d)
      if (player1>24 or player2>24):
         
         print("\nGame Restarting...")
         x,y= (p1.get(1))[0],(p1.get(1))[1]
         board.board.player1(board.window,x,y,board.pmover1)
         x,y= (p2.get(1))[0],(p2.get(1))[1]
         board.board.player2(board.window,x,y,board.pmover2)
         startplay();
         break
      print("Your dice landed on "+str(d)+".You are on Square "+str(player1))
      b = input("\nBig Bad Bull: Press Enter To Roll Dice..  ")
      d = rollDice()
      movePlayer2(d)
      print("Your dice landed on "+str(d)+".You are on Square "+str(player2))
      if (player1>24 or player2>24):
         
         print("\nGame Restarting...")
         x,y= (p1.get(1))[0],(p1.get(1))[1]
         board.board.player1(board.window,x,y,board.pmover1)
         x,y= (p2.get(1))[0],(p2.get(1))[1]
         board.board.player2(board.window,x,y,board.pmover2)
         startplay();
         break
      
      
start = board.board()
startplay()
