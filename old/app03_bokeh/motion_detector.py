from datetime import datetime
import cv2
import pandas

first_frame = None
isChanged=False

df = pandas.DataFrame(columns=['Start', 'End'])

video=cv2.VideoCapture(0)

while True:
    check, frame = video.read()
    isChangedCurrent=False

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray,(21,21),0)

    if first_frame is None:
        first_frame=gray
    
    diff_frame=cv2.absdiff(first_frame,gray)

    thresh_frame=cv2.threshold(diff_frame,30,255,cv2.THRESH_BINARY)[1]
    thresh_frame=cv2.dilate(thresh_frame, None, iterations=2)

    (cnts,_)=cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv2.contourArea(contour)>1000:
            (x,y,w,h)=cv2.boundingRect(contour)
            cv2.rectangle(gray,(x,y),(x+w,y+h),(0,255,0),3)
            isChangedCurrent=True

    if isChanged!=isChangedCurrent:
        
        if isChangedCurrent:
            df=df.append({'Start':datetime.now(), 'End':None}, ignore_index=True)
        else:
            df["End"].iloc[-1]=datetime.now() 
        
        isChanged=isChangedCurrent   

    cv2.imshow('Gray',gray)
    cv2.imshow('Difference',diff_frame)
    cv2.imshow('Thres',thresh_frame)

    key = cv2.waitKey(100)
    if key==27:    # Esc key to stop
        break

video.release()
cv2.destroyAllWindows

if df["End"].iloc[-1]==None:
    df["End"].iloc[-1]=datetime.now()    

df.to_csv('Time.csv') 