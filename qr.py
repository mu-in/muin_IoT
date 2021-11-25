import cv2
import pyzbar.pyzbar as zbar
import time
import requests
import numpy as np

cap = cv2.VideoCapture(0)
block = np.zeros((384,384,3),np.uint8)

qr = ''
while True:
    success, frame = cap.read()

    if success:
        for code in zbar.decode(frame):
            if qr != code.data.decode("utf-8"):
                qr = code.data.decode("utf-8")
                res = requests.get(f'https://mu-in.herokuapp.com/user/qrcode?seed={qr}')
                print(res.json())
                if(res.json()['validation']==True):
                    cv2.putText(block,'입장하세요',150,150,cv2.FONT_HERSHEY_SIMPLEX,1,(33, 147, 58),2)
                    cv2.imshow('success',block)
                    time.sleep(5)
                    cv2.destroyWindow('success')
                
        cv2.imshow('cam',frame)

        key = cv2.waitKey(1)
        
        if key == 27: # esc
            break

cap.release()
cv2.destroyAllWindows()