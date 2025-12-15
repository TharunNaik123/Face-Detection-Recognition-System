A real-time Face Detection and Face Recognition system built using OpenCV and the face_recognition library. The system can detect multiple faces from images or live video and identify known individuals by comparing face embeddings.

This project is suitable for academic mini-projects, final year projects, internships, and viva examinations.

### Features

Face detection from images and webcam video

Face recognition using face embeddings

Supports multiple faces in a single frame

Draws bounding boxes and name labels

Easy registration of new people

Clean, modular, GitHub-ready code

 Project Structure
face-detection-recognition/
│
├── dataset/
│   ├── Person1/
│   │   ├── 0.jpg
│   │   └── 1.jpg
│   └── Person2/
│       └── 0.jpg
│
├── encodings.pickle
├── register_face.py
├── encode_faces.py
├── face_detector.py
├── face_recognizer.py
├── requirements.txt
└── README.md
 System Architecture

Face Registration – Capture face images and store them in dataset folders

Encoding Generation – Convert faces into 128-D embeddings

Face Detection – Detect faces using HOG-based model

Face Recognition – Match detected faces with known embeddings

### Technologies Used

Python

OpenCV

face_recognition (dlib)

NumPy

Imutils

### Installation
1️ Clone Repository
git clone <your-repo-link>
cd face-detection-recognition
2️ Install Dependencies
pip install -r requirements.txt


### How to Run
Step 1: Register a New Person
python register_face.py

Enter person name

Press c to capture images

Press q to quit

Step 2: Generate Face Encodings
python encode_faces.py

This creates encodings.pickle file.

Step 3: Run Face Recognition (Webcam)
python face_recognizer.py

Press q to exit.

Optional: Face Detection on Image
python face_detector.py
 Sample Output

Green bounding boxes around faces

Name label for known faces

"Unknown" label for unregistered faces

 Evaluation (Qualitative)

Correctly detects multiple faces

Recognizes known people under normal lighting

Accuracy improves with more training images

 Limitations

Performance affected by poor lighting

Accuracy depends on dataset size

Requires CPU with decent performance

 Future Enhancements

Use DNN-based face detector

Improve accuracy using more images per person

Build Flask / Streamlit web interface

Store encodings in database

