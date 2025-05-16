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

imgpath = 'CameraLog/cap.jpg'
current_directory2 = os.getcwd()  # 現在のディレクトリを取得
file_path = os.path.join(current_directory2, imgpath)

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
        imgpath2 = file_path
        file_path2 = os.path.join(current_directory, imgpath2)
        ret, frame = cap.read()
        if ret:
            cv2.imwrite(file_path2, frame)
            result = FaceRecognition.recognition()
        else:
            print("failed to open capture")
            cap.release()

    return result #データは　name, id, adminflag
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
                    print('Hello, ')
                    login_username,login_userid,login_adminflag = result
                    print(login_userid, login_username, login_adminflag, "OKOKOKOK")
                    mainapp.facerecognition_success(login_userid,login_username, login_adminflag)
                    break
                time.sleep(1)

    except Exception as e:
        print(e)
        if cap is not None: cap.release()

### for user registation #######################################################

"""### camera flag ##########
registercameraflag = Event()
registercameraflag.set()   #True

### camera start ##########
def registercamera_start(mainapp):
    global registercamerathread
    registercameraflag.set()   #True
    registercamerathread = Thread(args=(mainapp,), target=camera_Registation)
    registercamerathread.daemon = True
    registercamerathread.start()

### camera stop ##########
def registercamera_stop():
    registercameraflag.clear()   #False
    registercamerathread.join()

def camera_Registation():#ユーザー登録用　カメラ起動
    cap = None
    while registercameraflag.is_set():
        ### Active the camera
        if cap is None: 
            cap = cam_set(0, WIDTH, HEIGHT, FPS)"""

def photograph():#ユーザー登録写真撮影用　カメラキャプチャーから1フレームの画像読み込み
    cap = cam_set(0, WIDTH, HEIGHT, FPS)
    if cap is not None:
        ret, frame = cap.read()
        if ret:
            cv2.imwrite(userRegPhoto_directory, frame)
            cap.release()
        else:
            print("failed to open capture")
            cap.release()
#################################################################################

def remove_camera(cap):
    if cap is not None: cap.release()
    cap = None

def load_image_BusCamera(path):
    imagefile = FaceRecognition.load_image_Facerecognition(path)
    return imagefile

def addpickle_BusCamera(userid,username,adminflag):
    FaceRecognition.addpickle_Facerecognition(userid,username,adminflag)

def editpickle_BusCamera(userid,username,adminflag):
    FaceRecognition.deletepickle_Facerecognition(userid)
    FaceRecognition.addpickle_Facerecognition(userid,username,adminflag)

def deletepickle_BusCamera(userid):
    FaceRecognition.deletepickle_Facerecognition(userid)


if __name__ == '__main__':
    #main()
    photograph()
