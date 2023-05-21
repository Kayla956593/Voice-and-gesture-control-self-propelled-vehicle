#This is a support Module mainly for the speech from text and also to aid the
#System into knowing when a finger is up or when a finger is down based on the
#joints
import cv2
import mediapipe as freedomtech
from gtts import gTTS
import os

drawingModule = freedomtech.solutions.drawing_utils #draw joint
handsModule = freedomtech.solutions.hands #hand detection
mod=handsModule.Hands() #The object for which the hand detection model is built

h=480
w=640

 #Convert text to speech and play
def speak(a):
    tts = gTTS(text=a, lang='en')
    tts.save("audio.mp3")
    os.system("mpg321 audio.mp3")
    
# The position coordinates of key points of the hand are extracted from the result.
# Store these position coordinates in a list and return
def findpostion(frame1):
    list=[]
    results = mod.process(cv2.cvtColor(frame1, cv2.COLOR_BGR2RGB))
    #whether hand landmarks are detected. 
    #If the key points of the hand are detected, enter the loop.
    if results.multi_hand_landmarks != None:
       for handLandmarks in results.multi_hand_landmarks:
           #Draw connecting lines of hand keypoints on the image
           drawingModule.draw_landmarks(frame1, handLandmarks, handsModule.HAND_CONNECTIONS)
           list=[]
           #Traverse each key point in handLandmarks.landmark to get its position coordinates in the image
           for id, pt in enumerate (handLandmarks.landmark):
                x = int(pt.x * w)
                y = int(pt.y * h)
                list.append([id,x,y])

    return list            

# Traverse each point in handsModule.HandLandmark,
# which is the name of the key point of the hand.
def findnameoflandmark(frame1):
     list=[]
     results = mod.process(cv2.cvtColor(frame1, cv2.COLOR_BGR2RGB))
     if results.multi_hand_landmarks != None:
        for handLandmarks in results.multi_hand_landmarks:


            for point in handsModule.HandLandmark:
                 list.append(str(point).replace ("< ","").replace("HandLandmark.", "").replace("_"," ").replace("[]",""))
     return list
