import cv2
import mediapipe as mp
import time
import mediapipe.python.solutions.hands as mpHands

cap = cv2.VideoCapture(1)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
cTime = 0
pTime = 0
# palm detection module basically works on complete image and provide a cropped image of the hand
# hand landmark module: find 21 different landmarks on cropped image of the hand
while True:
    success, img = cap.read()
    # convert the BGR to RGB because the hands only use the RGB
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            # print(handLms)
            for id, lm in enumerate(handLms.landmark):
                #print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                print(id, cx, cy)
                if id == 0:
                    cv2.circle(img, (cx, cy), 25, (255, 0, 255), cv2.FILLED)

            # print(mpHands.HAND_CONNECTIONS)
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
    if results.multi_handedness:
        print(results.multi_handedness)
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (10, 70),
                cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
