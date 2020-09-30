from controller import Supervisor
from controller import Node
from controller import Field


TIME_STEP = 32

referee = Supervisor()

ball = referee.getFromDef("BALL")
zerovel = [0,0,0,0,0,0]
trans_field = ball.getField("translation")



while referee.step(TIME_STEP) != -1:

    ball_pos = ball.getPosition()
    ball_vel = ball.getVelocity()
    
  
    

    print("ball position x:"+str(ball_pos[0]) +"  y:"+str(ball_pos[1])+"  z"+str(ball_pos[2]) )
    print(ball_vel)


    if ball_pos[0] >4.5 or ball_pos[0]<-4.5:

       
        ball.setVelocity(zerovel)
        trans_field.setSFVec3f([ball_pos[0],0.113,ball_pos[2]])
        
      
        
        if ball_pos[2]<0.75 and ball_pos[2]> -0.75 and ball_pos[1]<0.15:
            trans_field.setSFVec3f([0,0.113,0])


    if ball_pos[2] >3 or ball_pos[2]<-3:

        ball.setVelocity(zerovel)
        trans_field.setSFVec3f([ball_pos[0],0.113,ball_pos[2]])