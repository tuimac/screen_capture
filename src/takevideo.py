import cv2
import pyautogui
import numpy
import time

if __name__ == '__main__':
    codec = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter("Recorded.mp4", codec , 20, (1920, 1080))
    cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Live", 480, 270)
    while True:
        img = pyautogui.screenshot()
        frame = numpy.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        out.write(frame)
        cv2.imshow('Recording', frame)
        if cv2.waitKey(1) == ord('q'):
            break

    out.release()
    cv2.destroyAllWindows()
