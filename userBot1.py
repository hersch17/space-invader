import random
def run(bulletX,bulletY,playerX,playerY,enemyX,enemyY,playerState,enemyState, bulletCount):
  directions = ['left', 'right']
  i = random.randrange(0, 2)
  move = directions[i]
  shoot = random.randrange(0, 2)
  if enemyState==0:
    if playerX==enemyX:
      return move,shoot==True
  if enemyState==1:
    if playerX==enemyX:
      return move,shoot
  return move,shoot