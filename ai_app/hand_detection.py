import cv2

hand_cascade = cv2.CascadeClassifier("hand.xml") # face cascade

video = cv2.VideoCapture(0)
while True:
    x, frame = video.read()
    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # detecting faces and features by following lines
    hand = hand_cascade.detectMultiScale(gray_image, 1.1, 5)
    print(hand)
    # drawing bounding boxes around found faces from video frame by frame
    for x, y, w, h in hand:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)


    cv2.imshow('Video', frame) # displaying frames

    if cv2.waitKey(1) == ord('q'): # stop by pressing 'q' on the keyboard
        break

video.release() # video released, stop capturing
cv2.destroyAllWindows()