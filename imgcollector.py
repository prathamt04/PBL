import os
import cv2
from main import HandImageCapture

parent_folder = "Signs"
flag = True
while flag:   
    
    print("1) Train a existing Sign \n2) Train a new Sign \n3) Get count on samples \n4) Print samples of signs \n5) Exit ")
    choice = int(input("Enter your choice :"))
    if choice == 1:   
        folder_name = input("Enter the name of the folder: ")
        flag = False
    elif choice == 2:
        print("Creating new folder")
        folder_name = input("Enter the name of the folder: ")
        
        folder_path = os.path.join(parent_folder, folder_name)
        os.makedirs(folder_path, exist_ok=True)
        flag = False
        
    elif choice == 3:
        samples = input("Enter the sign to get a count : ")
        num_files = HandImageCapture.count_files(parent_folder, samples)
        print(f"Number of files in the folder '{samples}': {num_files}")
        
    elif choice == 4:
        folder_in_question = input("Enter folder to get files : ")
        print("files in folder{folder_in_question} are : ")
        HandImageCapture.print_file_names(parent_folder, folder_in_question)
    elif choice== 5:
        print("Exiting the program.........")
        exit(0)
        
    else:
        print("Wrong input")
        flag= True
    
if __name__ == "__main__":
    image_capture = HandImageCapture(folder_name)
    image_capture.capture_images()
    image_capture.cap.release()
    cv2.destroyAllWindows()
