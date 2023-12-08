import cv2
import time
import tkinter as tk
import threading

scanFace = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

cap = cv2.VideoCapture(0)

root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.destroy()

video_path = r'Rick.mp4'

def play_video():
    video = cv2.VideoCapture(video_path)
    while True:
        ret, frame = video.read()
        if not ret:
            print("End of video")
            break
        cv2.imshow("Video", frame)
        if cv2.waitKey(28) & 0xFF == ord("q"):
            break
    video.release()
    cv2.destroyAllWindows()

def detect_bounding_box(vid):
    image = cv2.cvtColor(vid, cv2.COLOR_BGR2GRAY)
    faces = scanFace.detectMultiScale(image, 1.1, 6, minSize=(40, 40))
    for (x, y, w, h) in faces:
        cv2.rectangle(vid, (x, y), (x + w, y + h), (255, 0, 255), 4)
    return faces

video_playing = False

while True:
    ret, frame = cap.read()

    frame = cv2.resize(frame, (screen_width, screen_height))
    faces = detect_bounding_box(frame)

    cv2.imshow('BEANS', frame)

    if len(faces) == 0 and not video_playing:
        time.sleep(4)
        
        faces = detect_bounding_box(frame)
        if len(faces) == 0:
            video_playing = True
            video_thread = threading.Thread(target=play_video)
            video_thread.start()
            cap.release()
            cv2.destroyWindow('BEANS')

    elif len(faces) > 0:
        video_playing = False

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
