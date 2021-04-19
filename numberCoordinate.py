"""This file defines and creates a relationship between the number
   of on the sqaures and the coordinate of the players.
   It is easier because it is better to move the players by relating to the
   number on the board that their raw absolute positions"""

'''This is  function to create a dictionary for storing the relationship
   between the number on the board and coordinate from the initial
   position of the players.
   number on the board are the keys.'''
def player_coordinate(player_initial_position):
   
   position=1
   x,y= (player_initial_position.get(1))[0],(player_initial_position.get(1))[1]
      
   for position in range(1,25):
      if (position == 5 or position == 10 or position ==15 or position == 20):
         y+=100
         player_initial_position.update({position+1:[x,y]})
      if (position<5):
         x+=100
         player_initial_position.update({position+1:[x,y]})
      if (position>5 and position<10):
         x-=100
         player_initial_position.update({position+1:[x,y]})
      if (position>10 and position<15):
         x+=100
         player_initial_position.update({position+1:[x,y]})
      if (position>15 and position<20):
         x-=100
         player_initial_position.update({position+1:[x,y]})
      if (position>20):
         x+=100
         player_initial_position.update({position+1:[x,y]})
   player_coordinates = player_initial_position
   return player_coordinates


#Initial position of the cow on the board on square 1
player1_initial_position = {1:[-190,-190]} 
#number Coordinate Dictionary for player one
player1_coordinate = player_coordinate(player1_initial_position)

#Initial position of the bull on the board on square 1
player2_initial_position = {1:[-180,-150]}
#Number Coordinate Dictionary for player two
player2_coordinate = player_coordinate(player2_initial_position)
