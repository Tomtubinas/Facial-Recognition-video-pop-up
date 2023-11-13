import numpy as np
import cv2
import tkinter as tk
# pylint: disable=E1101
# runs on python 3.10.11

scanFace = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

cap = cv2.VideoCapture(0)

root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.destroy()

def detect_bounding_box(vid):
    image = cv2.cvtColor(vid, cv2.COLOR_BGR2GRAY)
    faces = scanFace.detectMultiScale(image, 1.1, 6, minSize=(40, 40))
    for (x, y, w, h) in faces:
        cv2.rectangle(vid, (x, y), (x + w, y + h), (255, 0, 255), 4)
    return faces

while True:
    ret, frame = cap.read()

    frame = cv2.resize(frame, (screen_width, screen_height))
    faces = detect_bounding_box(frame)

    cv2.imshow('BEANS', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
