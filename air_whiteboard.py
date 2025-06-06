import cv2
import numpy as np
import os
import platform
from datetime import datetime
from cvzone.HandTrackingModule import HandDetector

# Webcam setup
cap = cv2.VideoCapture(1)
cap.set(3, 1280)
cap.set(4, 720)

# Hand detector
detector = HandDetector(detectionCon=0.8, maxHands=1)

# Drawing canvas
canvas = np.zeros((720, 1280, 3), dtype=np.uint8)
prev_x, prev_y = 0, 0

# Whiteboard mode toggle
whiteboard_mode = False
five_finger_prev = False
lock_triggered = False

while True:
    success, frame = cap.read()
    frame = cv2.flip(frame, 1)

    hands, _ = detector.findHands(frame, draw=True)

    if hands:
        lmList = hands[0]['lmList']
        fingers = detector.fingersUp(hands[0])
        x, y = lmList[8][:2]

        # Toggle whiteboard mode on 5 fingers
        if fingers == [1, 1, 1, 1, 1]:
            if not five_finger_prev:
                whiteboard_mode = not whiteboard_mode
                print(f"{'✅ Entered' if whiteboard_mode else '↩️ Exited'} whiteboard mode")
            five_finger_prev = True
        else:
            five_finger_prev = False

        # Lock screen on 4 fingers
        if fingers == [0, 1, 1, 1, 1]:
            if not lock_triggered:
                lock_triggered = True
                print("🔒 Locking Windows screen...")
                if platform.system() == "Windows":
                    os.system("rundll32.exe user32.dll,LockWorkStation")
                else:
                    print("⚠️ Lock feature only supported on Windows.")
        else:
            lock_triggered = False

        # Drawing logic (1 finger)
        if fingers == [0, 1, 0, 0, 0]:
            if prev_x == 0 and prev_y == 0:
                prev_x, prev_y = x, y
            cv2.line(canvas, (prev_x, prev_y), (x, y), (0, 0, 255), 8)
            prev_x, prev_y = x, y

        # Clear screen (2 fingers)
        elif fingers == [0, 1, 1, 0, 0]:
            canvas = np.zeros((720, 1280, 3), dtype=np.uint8)
            prev_x, prev_y = 0, 0

        # Save drawing (3 fingers)
        elif fingers == [0, 1, 1, 1, 0]:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"drawing_{timestamp}.jpg"
            bg = np.ones_like(frame, dtype=np.uint8) * 255 if whiteboard_mode else frame.copy()
            imgGray = cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY)
            _, imgInv = cv2.threshold(imgGray, 50, 255, cv2.THRESH_BINARY_INV)
            imgInv = cv2.cvtColor(imgInv, cv2.COLOR_GRAY2BGR)
            final = cv2.bitwise_and(bg, imgInv)
            final = cv2.bitwise_or(final, canvas)
            cv2.imwrite(filename, final)
            print(f"🖼️ Drawing saved as: {filename}")

        else:
            prev_x, prev_y = 0, 0

    else:
        prev_x, prev_y = 0, 0
        five_finger_prev = False
        lock_triggered = False

    # Create background based on mode
    bg = np.ones_like(frame, dtype=np.uint8) * 255 if whiteboard_mode else frame.copy()

    # Combine canvas and background
    imgGray = cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY)
    _, imgInv = cv2.threshold(imgGray, 50, 255, cv2.THRESH_BINARY_INV)
    imgInv = cv2.cvtColor(imgInv, cv2.COLOR_GRAY2BGR)

    output = cv2.bitwise_and(bg, imgInv)
    output = cv2.bitwise_or(output, canvas)

    cv2.imshow("Smart Air Whiteboard", output)

    if cv2.waitKey(1) == 13:  # Enter key
        print("🛑 Exiting...")
        break

cap.release()
cv2.destroyAllWindows()
