## Preparation for running
#### Put files FaceRecognition and EncodingData and testpic(a image of face) in the same directory
#### Also need CameraLog/cap.jpg
#### Connect a USBcamera

import os
import time
import cv2
import FaceRecognition

from threading import Thread, Event

### camera settings #################
WIDTH = 800
HEIGHT = 600
FPS = 5

current_directory = os.getcwd()  # 現在のディレクトリを取得

def cam_set(DEVICE_ID, WIDTH, HEIGHT, FPS):
    capture = cv2.VideoCapture(DEVICE_ID)
    capture.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
    capture.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)
    capture.set(cv2.CAP_PROP_FPS, FPS)

    return capture

#####################################################################

### Save images and perform facial recognition #######################
def save_and_recognition(cap):
    result = ""
    if cap is not None:
        ret, frame = cap.read()
        if ret:
            imgpath = 'CameraLog/cap.jpg'
            file_path = os.path.join(current_directory, imgpath)
            cv2.imwrite(file_path, frame)
            result = FaceRecognition.recognition()
        else:
            print("failed to capture frame")
    else:
        print("failed to open capture")

    return result
#####################################################################

### camera flag ##########
cameraflag = Event()
cameraflag.set()#True

### camera start ##########
def camera_start():
    global camerathread
    cameraflag.set()#True
    #camerathread = Thread(args=(mainapp,), target=main)
    camerathread.daemon = True
    camerathread.start()

### camera stop ##########
def camera_stop():
    cameraflag.clear()#False
    camerathread.join()

### main roop #######################################################
def main():
    try:
        cap = None
        imgfilepath = 'CameraLog'
        file_path = os.path.join(current_directory, imgfilepath)
        if not os.path.exists(file_path):
            os.makedirs(file_path)
        while True:#cameraflag.is_set():#bool check
            #namevalue = "FUJIWARASAN"
            #mainapp.print_mathod(namevalue)

    ### Activate the camera
            if cap is None:
                cap = cam_set(0, WIDTH, HEIGHT, FPS)

    ### Save images and perform facial recognition
            if cap is not None:
                result = save_and_recognition(cap)
                if result[0] != "":
                    print('Hello, ' + result[0])
                    userid = 100000
                    recognitiontime = str(time.strftime("%H:%M"))
                    #mainapp.FaceRecognition_match(userid, recognitiontime)
                time.sleep(1)

    except Exception as e:
        print(e)
        if cap is not None: cap.release()

def remove_camera(cap):
    if cap is not None: cap.release()
    cap = None


if __name__ == '__main__':
    main()
