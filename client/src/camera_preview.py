# client/src/camera_preview.py

import cv2
import tkinter as tk
import PIL.Image
import PIL.ImageTk

class CameraPreview :

    def __init__(self, window_name, cam_client):
        self.window_name = window_name
        self.cam_client = cam_client
        #cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
        self.window = tk.Tk()
        self.window.title(self.window_name)
        self.window.geometry("800x600")
        self.label_img = tk.Label(self.window, image=None)

    def sync_frame(self):
        self.frame = self.cam_client.frame

    def update_window(self, frame):
            #self.sync_frame()
            if frame is not None :
                #cv2.imshow(self.window_name, self.frame) # Afficher l'image
                #cv2.waitKey(1) # Attent une milisecond pour laisser OpenCV geré les evenement : redimensionement, touche préssé...
                frame = self.convert_img(frame)

                self.label_img.config(image=frame)
                self.label_img.image = frame
                self.label_img.pack()

    def convert_img(self, img):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = PIL.Image.fromarray(img)
        img = PIL.ImageTk.PhotoImage(img)
        return img

    def run(self):
        self.window.mainloop()