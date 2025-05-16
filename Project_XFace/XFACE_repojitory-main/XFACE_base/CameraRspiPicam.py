## Preparation for running
#### Put files FaceRecognition and EncodingData and testpic(a image of face) in the same directory
#### Also need CameraLog/cap.jpg
#### Connect a picamera3

import os
import time
import subprocess
import FaceRecognition

from threading import Thread, Event

### camera settings #################
WIDTH = 800
HEIGHT = 600
FPS = 5
CAMERA_ID = 0

current_directory = os.getcwd()  # 現在のディレクトリを取得
#####################################################################

### Save images and perform facial recognition #######################
def save_and_recognition():
    imgpath = 'CameraLog/cap.jpg'
    file_path = os.path.join(current_directory, imgpath)
    capture_image(file_path)
    result = FaceRecognition.recognition()
    return result

def capture_image(file_path):#Save image
# Use libcamera-still to capture an image
    cmd = [
        "libcamera-still",
        "--width", str(WIDTH),
        "--height", str(HEIGHT),
        "--timeout", "1000",
        "--output", file_path,
        "--nopreview"
        ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

#####################################################################

### camera flag ##########
cameraflag = Event()
cameraflag.set()# True

### camera start ##########
def camera_start(mainapp):
    global camerathread
    cameraflag.set()# True
    camerathread = Thread(args=(mainapp,), target=main)
    camerathread.daemon = True
    camerathread.start()

### camera stop ##########
def camera_stop():
    cameraflag.clear()# False
    camerathread.join()

### main loop #######################################################
def main(mainapp):
    try:
        imgfilepath = 'CameraLog'
        file_path = os.path.join(current_directory, imgfilepath)
        if not os.path.exists(file_path):
            os.makedirs(file_path)
        while cameraflag.is_set():# bool check
### Save images and perform facial recognition
            result = save_and_recognition()
            if result[0] != "":
                print('Hello, ' + result[0])
                userid = 100000
                recognitiontime = str(time.strftime("%H:%M"))
                mainapp.FaceRecognition_match(userid, recognitiontime)
                time.sleep(1)

    except Exception as e:print(e)

if __name__ == '__main__':
    class MainApp:
        def FaceRecognition_match(self, userid, recognitiontime):
            print(f"User {userid} recognized at {recognitiontime}")
    mainapp = MainApp()
    main(mainapp)