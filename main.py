import keyboard
import mss
import cv2
import numpy
from time import time, sleep
import pyautogui

pyautogui.PAUSE = 0

print("Для старта: 's'")
print("Для выхода: 'q'")
keyboard.wait('s')
left = True
x = 320
y = 812
sct = mss.mss()
dimensions_left = {
        'left':  320,
        'top': 812,
        'width': 200,
        'height': 500
    }

dimensions_right = {
        'left':  500,
        'top': 812,
        'width': 200,
        'height': 500
    }

wood_left = cv2.imread('img/left.jpg')
wood_right = cv2.imread('img/right.jpg')

w = wood_left.shape[1]
h = wood_left.shape[0]

#fps_time = time()
while True:
        if left:
            scr = numpy.array(sct.grab(dimensions_left))
            wood = wood_left
        else:
            scr = numpy.array(sct.grab(dimensions_right))
            wood = wood_right

        scr_remove = scr[:,:,:3]

        result = cv2.matchTemplate(scr_remove, wood, cv2.TM_CCOEFF_NORMED)
        
        _, max_val, _, max_loc = cv2.minMaxLoc(result)
        #print(f"Max Val: {max_val} Max Loc: {max_loc}")
        src = scr.copy()
        if max_val >= .34:
            left = not left
            if left:
                x=240
            else:
                x=840
        
        
        cv2.rectangle(scr, max_loc, (max_loc[0] + w, max_loc[1] + h), (0,255,255), 2)
        
        cv2.imshow('Screen Shot',   src)
        cv2.waitKey(1)
        pyautogui.click(x=x, y=y)
        sleep(.12)
        if keyboard.is_pressed('q'):
            break    

    #print('FPS: {}'.format(1 / (time() - fps_time)))
    #fps_time = time()