#pip install pynput
import autopy as ap
import time

ap.mouse.move(250,650)
ap.mouse.click(ap.mouse.Button.LEFT)
time.sleep(0.5)    
ap.mouse.click(ap.mouse.Button.LEFT)

time.sleep(0.5)
ap.mouse.move(300,405)

ap.key.tap(ap.key.Code.RIGHT_ARROW, [ap.key.Modifier.META])        
time.sleep(.1)
ap.key.tap(ap.key.Code.RIGHT_ARROW, [ap.key.Modifier.META])        
time.sleep(.1)

for i in range(1, 1000):    
    rgbL1 = ap.color.hex_to_rgb(ap.screen.get_color(200,405))
    rgbR1 = ap.color.hex_to_rgb(ap.screen.get_color(300,405))

    rgbL2 = ap.color.hex_to_rgb(ap.screen.get_color(200,460))
    rgbR2 = ap.color.hex_to_rgb(ap.screen.get_color(300,460))    
    
    rgbM = ap.color.hex_to_rgb(ap.screen.get_color(250,405))

    print('L1 color is {0}'.format(rgbL1[0]))    
    print('R1 color is {0}'.format(rgbR1[0]))
    print('L2 color is {0}'.format(rgbL2[0]))    
    print('R2 color is {0}'.format(rgbR2[0]))
    # print('M color is {0}'.format(rgbM[0]))

    if rgbM[0]!=155:
        break
    
    delay = 0.14
    
    if rgbR2[0]>130 and rgbR2[0]<178 : #Brown
        print('L Key')
        ap.key.tap(ap.key.Code.LEFT_ARROW, [ap.key.Modifier.META])        
        time.sleep(delay)
    elif rgbL2[0]>130 and rgbL2[0]<178: #Brown
        print('R Key')
        ap.key.tap(ap.key.Code.RIGHT_ARROW, [ap.key.Modifier.META])        
        time.sleep(delay)    
    elif rgbL1[0]>130 and rgbL1[0]<178 : #Brown
        print('R Key')
        ap.key.tap(ap.key.Code.RIGHT_ARROW, [ap.key.Modifier.META])        
        time.sleep(delay)
    elif rgbR1[0]>130 and rgbR1[0]<178: #Brown
        print('L Key')
        ap.key.tap(ap.key.Code.LEFT_ARROW, [ap.key.Modifier.META])        
        time.sleep(delay)
    
    
    
    
    # if rgb[0]==218:
    #     ap.key.tap(ap.key.Code.LEFT_ARROW, [ap.key.Modifier.META])
    # else:
    #     ap.key.tap(ap.key.Code.RIGHT_ARROW, [ap.key.Modifier.META])

    # print('color is {0}'.format(rgb))
    #print('color is {0}'.format(rgb[0]))
    #155 brown
     
