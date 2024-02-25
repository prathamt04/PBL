# The `HandImageCapture` class captures hand images, processes them, and saves them to a specified
# folder.
import cv2
from cvzone2.HandTrackingModule import HandDetector
import numpy as np
import math
import time
import os


class HandImageCapture:
    def __init__(self, folder_name="hello"):
        self.cap = cv2.VideoCapture(0)
        self.detector = HandDetector(maxHands=2)
        self.offset = 20
        self.img_size = 300
        self.counter = 0
        self.parent_folder = "Signs"
        self.folder = os.path.join(self.parent_folder, folder_name)

        # Create the folder if it doesn't exist
        if not os.path.exists(self.folder):
            os.makedirs(self.folder)

    def capture_images(self):
        """ 
        Capture images using the key "S" and turn off the camera when pressing "B"
        """
        while True:
            success, img = self.cap.read()
            hands, img = self.detector.findHands(img)
            
            for hand in hands:
                img_white = self.process_hand_image(hand, img)
                cv2.imshow('ImageWhite', img_white)
            cv2.imshow('Image', img)
            key = cv2.waitKey(1)

            if key == ord("s"):
                self.save_image(img_white)

            elif key == ord("b"):
                break

    def process_hand_image(self, hand, img):
        """
        Image processing function 
        """
        x, y, w, h = hand['bbox']
        img_white = np.ones((self.img_size, self.img_size, 3), np.uint8) * 255

        img_crop = img[y - self.offset:y + h + self.offset, x - self.offset:x + w + self.offset]
    
        # Checking if the cropped image is not empty (matlab imwrite window jahape save img hai)
        if not img_crop.size:
            return img_white  # Return the white image without processing

        aspect_ratio = h / w

        if aspect_ratio > 1:
            k = self.img_size / h
            w_cal = math.ceil(k * w)
            img_resize = cv2.resize(img_crop, (w_cal, self.img_size))
            w_gap = math.ceil((self.img_size - w_cal) / 2)
            img_white[:, w_gap: w_cal + w_gap] = img_resize
        else:
            k = self.img_size / w
            h_cal = math.ceil(k * h)
            img_resize = cv2.resize(img_crop, (self.img_size, h_cal))
            h_gap = math.ceil((self.img_size - h_cal) / 2)
            img_white[h_gap: h_cal + h_gap, :] = img_resize

        return img_white

    def save_image(self, img_white):
        self.counter += 1
        timestamp = time.time()
        file_path = os.path.join(self.folder, f'Image_{self.counter}_{timestamp}.jpg')
        
        try:
            cv2.imwrite(file_path, img_white)
            print(f"Image saved: {file_path}")
        except Exception as e:
            print(f"Error saving image: {e}")
    
    def count_files(parent_folder, folder_name):
        folder_path = os.path.join(parent_folder, folder_name)
        try:
            # Get the list of files in the folder
            files = os.listdir(folder_path)
            # Count the number of files
            num_files = len(files)
            
            return num_files
        except FileNotFoundError:
            print(f"The folder {folder_path} does not exist.")
            return 0
        

    def print_file_names(parent_folder, folder_name):
        folder_path = os.path.join(parent_folder, folder_name)
        try:
            # Get the list of files in the folder
            files = os.listdir(folder_path)
            if files:
                print(f"Files in the folder '{folder_name}':")
            for idx, file in enumerate(files, 1):
                print(f"{idx}. {file}")
            else:
                print(f"No files found in the folder '{folder_name}'.")
        except FileNotFoundError:
            print(f"The folder {folder_path} does not exist.")

