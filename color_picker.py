import cv2
import numpy as np

def colorCallback(x):
    print(x)

img = np.zeros((512,512,3),np.uint8)

cv2.namedWindow('color')

cv2.createTrackbar('Blue','color',0,255,colorCallback)
cv2.createTrackbar('Green','color',0,255,colorCallback)
cv2.createTrackbar('Red','color',0,255,colorCallback)


while(1):
    cv2.imshow('color',img)

    if cv2.waitKey(1) == ord('q'):
        break

    b = cv2.getTrackbarPos('Blue','color')
    g = cv2.getTrackbarPos('Green','color')
    r = cv2.getTrackbarPos('Red','color')

    text = "("+str(b)+","+str(g)+","+str(r)+")"

    img[:] = [b,g,r]

    img = cv2.putText(
        img,
        text,
        (100, 100),
        fontScale=1,
        fontFace=cv2.FONT_HERSHEY_COMPLEX,
        color=(255, 255, 255),
        thickness=2
    )

cv2.destroyAllWindows()