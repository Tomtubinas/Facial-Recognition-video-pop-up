import numpy as np
import cv2
import tkinter as tk
# pylint: disable=E1101
# runs on python 3.10.11

cap = cv2.VideoCapture(0)

root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.destroy()

print(f"Monitor size: {screen_width}x{screen_height} pixels")

while True:
    ret, frame = cap.read()

    frame = cv2.resize(frame, (screen_width, screen_height))

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
