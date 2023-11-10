#This is one way that I found to play a video but we would need to find out how to play this while a person is not paying attention
#to the screen. 

import cv2

def playVideo():
    file = r'Path to video file' 
    cap = cv2.VideoCapture(file)

    cv2.namedWindow("Video Player", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Video Player", 1920, 1080)
    
    while(cap.isOpened()):
        success, frame = cap.read()
        if success:
            cv2.imshow('Video Player', frame)
            quitButton = cv2.waitKey(25) & 0xFF == ord('q')
            closeButton = cv2.getWindowProperty('Video Player', cv2.WND_PROP_VISIBLE) < 1
            if quitButton or closeButton: 
                break
        else:
            break

    cap.release()
    cv2.destroyAllWindows()

playVideo()