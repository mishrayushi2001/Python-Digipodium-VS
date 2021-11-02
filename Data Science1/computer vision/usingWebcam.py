import cv2

#img = cv2.imread('../coin.jpg')

#cv2.imshow('using opencv', img)

#cv2.waitKey(500)

cap = cv2.VideoCapture(0)

while True:

    ret, frame= cap.read()

    #print(ret)
    
    cv2.imshow('using webcam', frame) 
    
    if cv2.waitKey(10) & 0xFF ==ord('q'):
        break
cv2.destroyAllWindows()
cap.release()
