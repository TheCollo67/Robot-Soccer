from controller import Supervisor

TIME_STEP = 32

supervisor = Supervisor()

ball_node = supervisor.getFromDef("BALL")
trans_field = ball_node.getField("translation")
radius_field = ball_node.getField("radius")
r = radius_field.getSFFloat()
INITIAL_POS = [0,r,0]

while supervisor.step(TIME_STEP) != -1:
    # this is done repeatedly
    values = trans_field.getSFVec3f()
    print("MY_ROBOT is at position: %g %g %g" % (values[0], values[1], values[2]))
    # GOAL TEST
    if((values[0] < -4.5 or values[0] > 4.5) and values[2] > -0.75 and values[2] < 0.75 and values[1] < r):
        trans_field.setSFVec3f(INITIAL_POS)
        ball_node.resetPhysics()
        print("goal log")      
    if(values[0] < -4.5 or values[0] > 4.5 or values[2] > 3 or values[2] < -3):
        ball_node.resetPhysics()
        print("out of bounds log")