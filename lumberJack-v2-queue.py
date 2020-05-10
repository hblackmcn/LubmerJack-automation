#Deveopled by Hossein Siamaknejad

#pip install pynput
import autopy as ap
from collections import deque 
import time

ap.mouse.move(250,650)
ap.mouse.click(ap.mouse.Button.LEFT)
time.sleep(0.5)    
ap.mouse.click(ap.mouse.Button.LEFT)
time.sleep(0.5)

q = deque() 
q.append('R')
q.append('R') 
isLeftDetected = False
isRightDetected = False

ap.mouse.move(200,305)

#Check if you are still in the game
while ap.color.hex_to_rgb(ap.screen.get_color(250,405))[0]==155:
    
    #RGB color of the left branch
    rgbL = ap.color.hex_to_rgb(ap.screen.get_color(200,305))
    
    #RGB color of the right branch
    rgbR = ap.color.hex_to_rgb(ap.screen.get_color(300,305))
    
    if rgbL[0]==155 and isLeftDetected==False: 
        q.append('L')
        q.append('L')
        isLeftDetected=True
    else:
        isLeftDetected=False

    if rgbR[0]==155 and isRightDetected==False:                
        q.append('R')
        q.append('R')
        isRightDetected=True
    else:
        isRightDetected=False

    if q:
        print('Queue= {0}'.format(q))
        popped = q.popleft()
        if popped=='R':
            ap.key.tap(ap.key.Code.LEFT_ARROW, [ap.key.Modifier.META])                  
        elif popped=='L':
            ap.key.tap(ap.key.Code.RIGHT_ARROW, [ap.key.Modifier.META])                
        time.sleep(0.15)
