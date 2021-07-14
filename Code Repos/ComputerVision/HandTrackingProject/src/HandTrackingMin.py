import cv2
import mediapipe as mp
import time
import mediapipe.python.solutions.hands as mpHands

cap = cv2.VideoCapture(1)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
# palm detection module basically works on complete image and provide a cropped image of the hand
# hand landmark module: find 21 different landmarks on cropped image of the hand
while True:
    success, img = cap.read()
    # convert the BGR to RGB because the hands only use the RGB
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            #print(handLms)
            print(mpHands.HAND_CONNECTIONS)
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
    if results.multi_handedness:
        print(results.multi_handedness)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
