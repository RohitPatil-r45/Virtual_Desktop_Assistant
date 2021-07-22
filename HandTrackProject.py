import os
import cv2
import random
import subprocess
import webbrowser
import datetime
import numpy as np
import pyautogui
import HandTrackingModule as htm     #importing HandTrackingModule.py
from pynput.keyboard import Key, Controller
n = 0
keyboard = Controller()

cap = cv2.VideoCapture(0)

detector = htm.handDetector(detectionCon=0.75)

tipIds = [4, 8, 12, 16, 20]

listpred = []
count = 0

L0 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
L1 = [[0, 1, 0, 0, 0], [0, 1, 0, 0, 0], [0, 1, 0, 0, 0], [0, 1, 0, 0, 0], [0, 1, 0, 0, 0], [0, 1, 0, 0, 0], [0, 1, 0, 0, 0], [0, 1, 0, 0, 0], [0, 1, 0, 0, 0], [0, 1, 0, 0, 0], [0, 1, 0, 0, 0], [0, 1, 0, 0, 0], [0, 1, 0, 0, 0], [0, 1, 0, 0, 0], [0, 1, 0, 0, 0]]
L2 = [[0, 1, 1, 0, 0], [0, 1, 1, 0, 0], [0, 1, 1, 0, 0], [0, 1, 1, 0, 0], [0, 1, 1, 0, 0], [0, 1, 1, 0, 0], [0, 1, 1, 0, 0], [0, 1, 1, 0, 0], [0, 1, 1, 0, 0], [0, 1, 1, 0, 0], [0, 1, 1, 0, 0], [0, 1, 1, 0, 0], [0, 1, 1, 0, 0], [0, 1, 1, 0, 0], [0, 1, 1, 0, 0]]
L3 = [[0, 1, 1, 1, 0], [0, 1, 1, 1, 0], [0, 1, 1, 1, 0], [0, 1, 1, 1, 0], [0, 1, 1, 1, 0], [0, 1, 1, 1, 0], [0, 1, 1, 1, 0], [0, 1, 1, 1, 0], [0, 1, 1, 1, 0], [0, 1, 1, 1, 0], [0, 1, 1, 1, 0], [0, 1, 1, 1, 0], [0, 1, 1, 1, 0], [0, 1, 1, 1, 0], [0, 1, 1, 1, 0]]
L4 = [[0, 1, 1, 1, 1], [0, 1, 1, 1, 1], [0, 1, 1, 1, 1], [0, 1, 1, 1, 1], [0, 1, 1, 1, 1], [0, 1, 1, 1, 1], [0, 1, 1, 1, 1], [0, 1, 1, 1, 1], [0, 1, 1, 1, 1], [0, 1, 1, 1, 1], [0, 1, 1, 1, 1], [0, 1, 1, 1, 1], [0, 1, 1, 1, 1], [0, 1, 1, 1, 1], [0, 1, 1, 1, 1]]
L5 = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]
L6 = [[0, 1, 0, 0, 1], [0, 1, 0, 0, 1], [0, 1, 0, 0, 1], [0, 1, 0, 0, 1], [0, 1, 0, 0, 1], [0, 1, 0, 0, 1], [0, 1, 0, 0, 1], [0, 1, 0, 0, 1], [0, 1, 0, 0, 1], [0, 1, 0, 0, 1], [0, 1, 0, 0, 1], [0, 1, 0, 0, 1], [0, 1, 0, 0, 1], [0, 1, 0, 0, 1], [0, 1, 0, 0, 1]]
L7 = [[0, 1, 1, 0, 1], [0, 1, 1, 0, 1], [0, 1, 1, 0, 1], [0, 1, 1, 0, 1], [0, 1, 1, 0, 1], [0, 1, 1, 0, 1], [0, 1, 1, 0, 1], [0, 1, 1, 0, 1], [0, 1, 1, 0, 1], [0, 1, 1, 0, 1], [0, 1, 1, 0, 1], [0, 1, 1, 0, 1], [0, 1, 1, 0, 1], [0, 1, 1, 0, 1], [0, 1, 1, 0, 1]]
L8 = [[1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1]]
L9 = [[1, 1, 0, 0, 1], [1, 1, 0, 0, 1], [1, 1, 0, 0, 1], [1, 1, 0, 0, 1], [1, 1, 0, 0, 1], [1, 1, 0, 0, 1], [1, 1, 0, 0, 1], [1, 1, 0, 0, 1], [1, 1, 0, 0, 1], [1, 1, 0, 0, 1], [1, 1, 0, 0, 1], [1, 1, 0, 0, 1], [1, 1, 0, 0, 1], [1, 1, 0, 0, 1], [1, 1, 0, 0, 1]]
L10 = [[0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1], [0, 0, 1, 1, 1]]

def act(listpred1):
    LCV = listpred1
    if L0 == LCV:
        # Volume down by 10%
        keyboard.press(Key.media_volume_down)
        keyboard.release(Key.media_volume_down)
        keyboard.press(Key.media_volume_down)
        keyboard.release(Key.media_volume_down)
        keyboard.press(Key.media_volume_down)
        keyboard.release(Key.media_volume_down)
        keyboard.press(Key.media_volume_down)
        keyboard.release(Key.media_volume_down)
        keyboard.press(Key.media_volume_down)
        keyboard.release(Key.media_volume_down)

    elif L1 == LCV:
        # Volume up by 10%
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)
    elif L2 == LCV:
        # Space Bar Press
        keyboard.press(Key.space)
        keyboard.release(Key.space)
    elif L3 == LCV:
        # Right Arrow Key Press
        keyboard.press(Key.right)
        keyboard.release(Key.right)
    elif L4 == LCV:
        # Left Arrow Key Press
        keyboard.press(Key.left)
        keyboard.release(Key.left)
    elif L5 == LCV:
        # Play and Pause Music and Video
        keyboard.press(Key.media_play_pause)
        keyboard.release(Key.media_play_pause)


    elif L6 == LCV:
        # Open Google Webpage
        def process_exists(process_name):
            call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name
            # use buildin check_output right away
            output = subprocess.check_output(call).decode()
            # check in last line for process name
            last_line = output.strip().split('\r\n')[-1]
            # because Fail message could be translated
            return last_line.lower().startswith(process_name.lower())

        if process_exists('chrome.exe') == True:
            print("Task is already running")
        else:
            webbrowser.open("http://www.google.com")
    elif L7 == LCV:

        webbrowser.open('https://www.youtube.com')

    elif L8 == LCV:
        # Minimize Current Program Screen
        keyboard.press(Key.cmd)
        keyboard.press(Key.down)
        keyboard.release(Key.cmd)
        keyboard.release(Key.down)
    elif L9 == LCV:
        music_dir = 'C:\Songs'    #Import your Songs folder URL
        songs = os.listdir(music_dir)
        while True:
            no = random.randint(0, len(songs) - 1)
            if os.path.join(music_dir, songs[no]).endswith('.mp3') == True:
                os.startfile(os.path.join(music_dir, songs[no]))
                break

    elif L10 == LCV:

        x = datetime.datetime.now()
        image = pyautogui.screenshot()
        image = cv2.cvtColor(np.array(image),
                             cv2.COLOR_RGB2BGR)
        a = (f"({x.year}_{x.month}_{x.day}_{x.hour}_{x.minute}_{x.second})")
        # writing it to the disk using opencv
        #cv2.imwrite(f"image_{x.year}/{x.month}/{x.day}_{x.hour}:{x.minute}:{x.second}.png", image)
        cv2.imwrite(f"Image_{a}.png", image)
        print("Image Saved.")




while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    #print(lmList)
    if len(lmList) != 0:
        fingers = []
        # Thumb
        if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)
        # 4 Fingers
        for id in range(1, 5):
            if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        #print(fingers)
        listpred.append(fingers)
        count = count + 1
    #print(count)
    #print(listpred)
    if count == 15:
        act(listpred)
        count = 0
        listpred.clear()

    cv2.imshow("Image", img)
    cv2.waitKey(1)