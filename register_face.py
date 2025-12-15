import cv2
import os

name = input("Enter person name: ")
folder = f"dataset/{name}"
os.makedirs(folder, exist_ok=True)

cap = cv2.VideoCapture(0)
count = 0

print("Press 'c' to capture image | 'q' to quit")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Register Face", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('c'):
        cv2.imwrite(f"{folder}/{count}.jpg", frame)
        print(f"Saved image {count}")
        count += 1

    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
