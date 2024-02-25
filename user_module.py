import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier

class HandGestureClassifier:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.detector = HandDetector(maxHands=2)    
        self.classifier = Classifier("Model/keras_model.h5", "Model/labels.txt")
        self.offset = 20
        self.imgSize = 300
        self.labels = ["Hello", "I love you", "No", "Okay", "Please", "Thank you", "Yes"]
        self.release_flag = False

    def release(self):
        self.cap.release()
        cv2.destroyAllWindows()

    def process_frame(self):
        while not self.release_flag:
            success, img = self.cap.read()
            imgOutput = img.copy()
            hands, img = self.detector.findHands(img)

            if hands:
                for hand in hands:
                    x, y, w, h = hand['bbox']

                    imgCrop = img[y - self.offset:y + h + self.offset, x - self.offset:x + w + self.offset]
                    # Check if imgCrop is not empty before resizing
                    if imgCrop.shape[0] != 0 and imgCrop.shape[1] != 0:
                        imgResize = cv2.resize(imgCrop, (self.imgSize, self.imgSize))

                        prediction, index = self.classifier.getPrediction(imgResize, draw=False)
                        label = self.labels[index]

                        cv2.putText(imgOutput, label, (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 0), 2)
                        cv2.rectangle(imgOutput, (x - self.offset, y - self.offset),
                            (x + w + self.offset, y + h + self.offset), (0, 255, 0), 4)

            cv2.imshow('Image', imgOutput)
            key = cv2.waitKey(1)
            if key == ord('b'):
                self.release_flag = True

        # Release resources only if the flag is set
        if self.release_flag:
            self.release()

if __name__ == "__main__":
    gesture_classifier = HandGestureClassifier()
    gesture_classifier.process_frame()

