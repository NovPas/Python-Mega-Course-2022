import cv2
import time
from emailing import send_email
from datetime import datetime
from threading import Thread

first_frame = None
video = cv2.VideoCapture(0)
time.sleep(1)
refresh_first_fresh_time = time.time()
email_sent_time = time.time()
email_sent_frequency = 5

while True:

    activated = False

    check, frame = video.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame_gau = cv2.GaussianBlur(gray_frame, (5, 5), 0)

    if first_frame is None or time.time() - refresh_first_fresh_time > 10:
        first_frame = gray_frame_gau
        refresh_first_fresh_time = time.time()

    delta_frame = cv2.absdiff(gray_frame_gau, first_frame)
    thresh_frame = cv2.threshold(delta_frame, 60, 255, cv2.THRESH_BINARY)[1]
    dil_frame = cv2.dilate(thresh_frame, None, iterations=2)

    contours, check = cv2.findContours(dil_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) > 5000:
            x, y, w, h = cv2.boundingRect(contour)
            rectangle = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
            if rectangle.any():
                activated = True

    cur_time = time.time()
    if activated and cur_time - email_sent_time > email_sent_frequency:
        email_sent_time = cur_time
        file_path = 'images/'+datetime.now().strftime("%M-%S")+'.png'
        cv2.imwrite(file_path, frame)

        # Threading
        email_thread = Thread(target=send_email, args=(file_path,))
        email_thread.daemon = True
        email_thread.start()


    cv2.imshow('My video', frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

video.release()
