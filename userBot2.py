#teamrocket
def run(bulletX,bulletY,playerX,playerY,enemyX,enemyY,
        playerState,enemyState, bulletCount):
  directions = ['left', 'right','none']
  shoot = 0
  if(playerX>enemyX) :
    i = 0
  elif(playerX<enemyX) :
    i = 1
  else :
    i = 2
  move = directions[i]
  if(playerX-enemyX<200 | playerX-enemyX>-200):
   shoot = 1
  while (bulletX==playerX & (bulletY-playerY)<200):
    if(playerX!=0):
      move = 'left'
    else:
      move = 'right'
  return move, shoot
 
  # TODO: logic to determine where to move and shoot
  # move = 'left' or 'right'
  # shoot = True or False