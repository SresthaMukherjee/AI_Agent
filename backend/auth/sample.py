import cv2
import os
import platform

# Use CAP_DSHOW only on Windows
if platform.system() == "Windows":
    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
else:
    cam = cv2.VideoCapture(0)

cam.set(3, 640)  # set video FrameWidth
cam.set(4, 480)  # set video FrameHeight

# Cross-platform path handling
cascade_path = os.path.join("backend", "auth", "haarcascade_frontalface_default.xml")
detector = cv2.CascadeClassifier(cascade_path)

face_id = input("Enter a Numeric user ID  here:  ")
print("Taking samples, look at camera ....... ")
count = 0

while True:
    ret, img = cam.read()
    if not ret:
        print("Failed to grab frame. Exiting...")
        break

    converted_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(converted_image, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        count += 1

        # Save captured face image
        img_path = os.path.join("backend", "auth", "samples", f"face.{face_id}.{count}.jpg")
        cv2.imwrite(img_path, converted_image[y:y+h, x:x+w])
        cv2.imshow('image', img)

    k = cv2.waitKey(100) & 0xff
    if k == 27:
        break
    elif count >= 100:
        break

print("Samples taken. Closing the program...")
cam.release()
cv2.destroyAllWindows()
