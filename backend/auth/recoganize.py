# import time
# import cv2
# import pyautogui as p
# import os  # For handling cross-platform paths
# import numpy as np



# def AuthenticateFace():

#     flag = ""
#     # Local Binary Patterns Histograms
#     recognizer = cv2.face_LBPHFaceRecognizer.create()

#     # Use os.path.join to create platform-independent paths
#     trainer_path = os.path.join('backend', 'auth', 'trainer', 'trainer.yml')
#     cascade_path = os.path.join('backend', 'auth', 'haarcascade_frontalface_default.xml')

#     # Load the trained model
#     recognizer.read(trainer_path)

#     # Initialize haar cascade for object detection approach
#     faceCascade = cv2.CascadeClassifier(cascade_path)

#     font = cv2.FONT_HERSHEY_SIMPLEX  # Denotes the font type

#     id = 4  # Number of persons you want to recognize
#     names = ['', '', '', '', 'Srestha']  # Names, leave first empty because counter starts from 0

#     # Use the default webcam for macOS/Windows
#     cam = cv2.VideoCapture(1)  
#     cam.set(3, 640)  # Set video FrameWidth
#     cam.set(4, 480)  # Set video FrameHeight

#     # Define min window size to be recognized as a face
#     minW = 0.1 * cam.get(3)
#     minH = 0.1 * cam.get(4)

#     while True:
#         ret, img = cam.read()  # Read the frames using the above-created object

#         # Convert the image to grayscale
#         converted_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#         faces = faceCascade.detectMultiScale(
#             converted_image,
#             scaleFactor=1.2,
#             minNeighbors=5,
#             minSize=(int(minW), int(minH)),
#         )
        
#         for (x, y, w, h) in faces:
#             # Draw a rectangle around the detected face
#             cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

#             # Predict on the face region
#             id, accuracy = recognizer.predict(converted_image[y:y + h, x:x + w])

#             # if accuracy < 100:
#             #     id = names[id]
#             #     accuracy = "  {0}%".format(round(100 - accuracy))
#             #     flag = 1
#             # else:
#             #     id = "unknown"
#             #     accuracy = "  {0}%".format(round(100 - accuracy))
#             #     flag = 0
#         confidence = 100 - accuracy  # Calculate confidence percentage
        

#         if confidence >= 30:  # Only accept if confidence is 70% or more
#             id = names[id]
#             accuracy = "  {0}%".format(round(confidence))
#             flag = 1
#         else:
#             id = "unknown"
#             accuracy = "  {0}%".format(round(confidence))
#             flag = 0

#             cv2.putText(img, str(id), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
#             cv2.putText(img, str(accuracy), (x + 5, y + h - 5),
#                         font, 1, (255, 255, 0), 1)

#         cv2.imshow('camera', img)

#         # Break loop if 'ESC' is pressed or face recognized
#         k = cv2.waitKey(10) & 0xff
#         if k == 27:  # Press 'ESC' to exit
#             break
#         if flag == 1:
#             break
  
#     # Cleanup after exit
#     cam.release()
#     cv2.destroyAllWindows()

#     return flag

# #AuthenticateFace()

import time
import cv2
import pyautogui as p
import os
import numpy as np

def AuthenticateFace():
    flag = 0

    # Ensure you're using OpenCV with contrib modules
    recognizer = cv2.face.LBPHFaceRecognizer_create()

    trainer_path = os.path.join('backend', 'auth', 'trainer', 'trainer.yml')
    cascade_path = os.path.join('backend', 'auth', 'haarcascade_frontalface_default.xml')

    recognizer.read(trainer_path)
    faceCascade = cv2.CascadeClassifier(cascade_path)
    font = cv2.FONT_HERSHEY_SIMPLEX

    names = ['', '', '', 'Srestha']

    cam = cv2.VideoCapture(0)
    cam.set(3, 640)
    cam.set(4, 480)

    minW = 0.1 * cam.get(3)
    minH = 0.1 * cam.get(4)

    while True:
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(int(minW), int(minH)))

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

            id, accuracy = recognizer.predict(gray[y:y + h, x:x + w])
            confidence = 100 - accuracy

            if confidence >= 20:
                predicted_name = names[id] if id < len(names) else "Unknown"
                flag = 1
            else:
                predicted_name = "Unknown"

            conf_text = "  {0}%".format(round(confidence))
            cv2.putText(img, str(predicted_name), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
            cv2.putText(img, conf_text, (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)

        cv2.imshow('camera', img)

        k = cv2.waitKey(10) & 0xff
        if k == 27 or flag == 1:
            break

    cam.release()
    cv2.destroyAllWindows()

    return flag
#AuthenticateFace()