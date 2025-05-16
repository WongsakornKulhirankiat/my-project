## Preparation for running
#### Put files FaceRecognition and EncodingData and testpic(a image of face) in the same directory
#### Connect a camera

import cv2
import os
import time
import FaceRecognition

from threading import Thread, Event
from multiprocessing import Process, Value

### camera settings #################
WIDTH = 800
HEIGHT = 600
FPS = 5
current_directory = os.getcwd()  # 現在のディレクトリを取得
userRegPhoto_path = 'photoget/testpic.png' 
userRegPhoto_directory = os.path.join(current_directory, userRegPhoto_path)# ユーザー登録で画像を一時保存するディレクトリ

def cam_set(DEVICE_ID, WIDTH, HEIGHT, FPS):
    capture = cv2.VideoCapture(DEVICE_ID)
    capture.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('Y','U','Y','V'))
    capture.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
    capture.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)
    capture.set(cv2.CAP_PROP_FPS, FPS)

    fourcc = decode_fourcc(capture.get(cv2.CAP_PROP_FOURCC))
    width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
    fps = capture.get(cv2.CAP_PROP_FPS)
    print("ID:{} fourcc:{} fps:{} width:{} height:{}".format(DEVICE_ID, fourcc, fps, width, height))

    return capture

def decode_fourcc(v):
    v = int(v)
    return "".join([chr((v >> 8 * i) & 0xFF) for i in range(4)])
#####################################################################

### Save images and perform facial recognition #######################
def save_and_recognition(cap):
    result = ""
    if cap is not None:
        imgpath = 'CameraLog/bus.jpg'
        file_path = os.path.join(current_directory, imgpath)
        ret, frame = cap.read()
        if ret:
            cv2.imwrite(file_path, frame)
            result = FaceRecognition.recognition()
        else:
            print("failed to open capture")
            cap.release()

    return result #データは　name, id
#####################################################################

### camera flag ##########
cameraflag = Event()
cameraflag.set()   #True

### camera start ##########
def camera_start(mainapp):
    global camerathread
    cameraflag.set()   #True
    camerathread = Thread(args=(mainapp,), target=main)
    camerathread.daemon = True
    camerathread.start()

### camera stop ##########
def camera_stop():
    cameraflag.clear()   #False
    camerathread.join()

### main roop #######################################################
def main(mainapp):
    try:
        cap = None
        imgfilepath = 'CameraLog'
        file_path = os.path.join(current_directory, imgfilepath)
        if not os.path.exists(file_path):
            os.makedirs(file_path)

        while cameraflag.is_set():      #bool check
            ### Active the camera
            if cap is None: 
                cap = cam_set(0, WIDTH, HEIGHT, FPS)

            ### Save images and perform facial recognition
            if cap is not None:
                result = save_and_recognition(cap)
                if result[0] != "":
                    print('Hello, ' + result[0])
                    userid = 100000
                    recognitiontime = str(time.strftime("%H:%M"))
                    mainapp.FaceRecognition_match(userid,recognitiontime)
                time.sleep(1)

    except Exception as e:
        print(e)
        if cap is not None: cap.release()

### for user registation #######################################################
def camera_Registation():#ユーザー登録用　カメラ起動
    cap = None
    while True:
        ### Active the camera
        if cap is None: 
            cap = cam_set(0, WIDTH, HEIGHT, FPS)

def photograph(cap):#ユーザー登録写真撮影用　カメラキャプチャーから1フレームの画像読み込み
    if cap is not None:
        ret, frame = cap.read()
        if ret:
            cv2.imwrite(userRegPhoto_directory, frame)
        else:
            print("failed to open capture")
            cap.release()
#################################################################################

def remove_camera(cap):
    if cap is not None: cap.release()
    cap = None

if __name__ == '__main__':
    main()
