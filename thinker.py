import tkinter as tk
import os
from main import HandImageCapture

class HandImageCaptureGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Hand Image Capture")
        
        self.parent_folder = "Signs"
        self.flag = True

        self.menu_frame = tk.Frame(self.master)
        self.menu_frame.pack(pady=10)

        self.train_existing_button = tk.Button(self.menu_frame, text="Train existing sign", command=self.train_existing_sign)
        self.train_existing_button.grid(row=0, column=0, padx=10)

        self.train_new_button = tk.Button(self.menu_frame, text="Train new sign", command=self.train_new_sign)
        self.train_new_button.grid(row=0, column=1, padx=10)

        self.get_sample_count_button = tk.Button(self.menu_frame, text="Get sample count", command=self.get_sample_count)
        self.get_sample_count_button.grid(row=0, column=2, padx=10)

        self.print_samples_button = tk.Button(self.menu_frame, text="Print samples", command=self.print_samples)
        self.print_samples_button.grid(row=0, column=3, padx=10)

        self.exit_button = tk.Button(self.menu_frame, text="Exit", command=self.master.destroy)
        self.exit_button.grid(row=0, column=4, padx=10)

    def train_existing_sign(self):
        folder_name = input("Enter the name of the folder: ")
        self.flag = False

    def train_new_sign(self):
        print("Creating new folder")
        folder_name = input("Enter the name of the folder: ")
        folder_path = os.path.join(self.parent_folder, folder_name)
        os.makedirs(folder_path, exist_ok=True)
        self.flag = False

    def get_sample_count(self):
        samples = input("Enter the sign to get a count: ")
        num_files = HandImageCapture.count_files(self.parent_folder, samples)
        print(f"Number of files in the folder '{samples}': {num_files}")

    def print_samples(self):
        folder_in_question = input("Enter folder to get files: ")
        print(f"Files in folder '{folder_in_question}': ")
        HandImageCapture.print_file_names(self.parent_folder, folder_in_question)


def main():
    root = tk.Tk()
    app = HandImageCaptureGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
