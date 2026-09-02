import cv2
import os
import numpy as np

haar_file = "haarcascade_frontalface_default.xml"
datasets = "datasets"

print("Recognising face.")

(images, labels, names, id) = ([], [], {}, 0)

# Load stuff
for (subdirs, dirs, files) in os.walk(datasets):
    for subdir in dirs:
        names[id] = subdir
        subjectpath = os.path.join(datasets, subdir)

        for filename in os.listdir(subjectpath):
            path = os.path.join(subjectpath, filename)
            label = id

            image = cv2.imread(path, 0)

            if image is not None:
                images.append(image)
                labels.append(label)

        id += 1

# image size
(width, height) = (130, 100)
(images, labels) = [np.array(lis) for lis in [images, labels]]

# make the face model happen
model = cv2.face.LBPHFaceRecognizer_create()
model.train(images, labels)

# Load haarfacecascade
face_cascade = cv2.CascadeClassifier(haar_file)

# Start webcam
webcam = cv2.VideoCapture(0)

while True:
    (_, im) = webcam.read()

    if im is None:
        break

    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5
    )

    for (x, y, w, h) in faces:

        # resize detected face
        face = gray[y:y+h, x:x+w]
        face_resize = cv2.resize(face, (width, height))

        # who the face belongs to
        prediction = model.predict(face_resize)

        label, confidence = prediction

        # Decide whether the face is recognised
        if confidence < 100:
            # Recognised face -> GREEN
            colour = (0, 255, 0)
            text = '%s - %.0f' % (names[label], confidence)

        else:
            # Unknown face -> RED
            colour = (0, 0, 255)
            text = 'Unknown'

        # Draw the rectangle using the selected colour
        cv2.rectangle(
            im,
            (x, y),
            (x + w, y + h),
            colour,
            3
        )

        # Draw the name above the rectangle
        cv2.putText(
            im,
            text,
            (x, y - 10),
            cv2.FONT_HERSHEY_PLAIN,
            1.5,
            colour,
            2
        )

    # Display webcam
    cv2.imshow('OpenCV', im)

    # exit key
    key = cv2.waitKey(10)

    if key == 27:
        break

webcam.release()
cv2.destroyAllWindows()