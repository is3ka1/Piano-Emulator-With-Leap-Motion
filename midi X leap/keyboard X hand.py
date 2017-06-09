import Leap
from keyboard import *
from hand_demo import *
controller=Leap.Controller()

#scene = display(title='leap motion',width=800,height=600,background=(0.5,0.6,0.5) ,autoscale = False)

hands=[hand_demo(), hand_demo()]
for i in range(1,6):
    octave(25, i).pos=(0,100,0)

scene.center.y+=100
while True:

            rate(100)

            frame=controller.frame()
            i=0
            for hand in frame.hands:
                hands[i].update(hand)
                i+=1
