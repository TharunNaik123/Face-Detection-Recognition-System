import cv2
import face_recognition

image = face_recognition.load_image_file("test.jpg")
face_locations = face_recognition.face_locations(image)

for top, right, bottom, left in face_locations:
    cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)

cv2.imshow("Detected Faces", cv2.cvtColor(image, cv2.COLOR_RGB2BGR))
cv2.waitKey(0)
cv2.destroyAllWindows()
