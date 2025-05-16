## Preparation for running
#### Put files FaceRecognition and EncodingData and testpic(a image of face) in the same directory
#### Connect a camera

import cv2
import os
import time
#import FaceRecognition   PCで作業を行う場合はコメントアウト

from threading import Thread, Event
from multiprocessing import Process, Value

import XFaceDAO
dbaccess = XFaceDAO.XFaceDAO()

### camera settings #################
WIDTH = 800
HEIGHT = 600
FPS = 5

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
    if cap is not None:
        ret, frame = cap.read()
        if ret:
            cv2.imwrite("CameraLog/bus.jpg", frame)
            #name = FaceRecognition.recognition()   PCで作業を行う場合はコメントアウト
            name = "fujiwara"
        else:
            print("failed to open capture")
            cap.release()

    return name
#####################################################################

### camera flag ##########
cameraflag = Event()
cameraflag.set()   #True

### camera start ##########
def camera_start():
    global camerathread
    cameraflag.set()   #True
    camerathread = Thread(target=main)
    camerathread.daemon = True
    camerathread.start()

### camera stop ##########
def camera_stop():
    cameraflag.clear()   #False
    camerathread.join()

### main roop #######################################################
def main():   #PCで作業を行う場合はmainの中身を変更
    try:
        #cap = None
        #if not os.path.exists("CameraLog"):
        #    os.makedirs("CameraLog")

        while cameraflag.is_set():      #bool check
            #testlist = dbaccess.getUserInfo()
            #print("OK",testlist)
            userid = "100000"
            username = "fujiwara"
            #FaceRecognition_match(userid,username)
            print("Data insert")
            time.sleep(2)
            

            ### Active the camera
            #if cap is None: 
            #    cap = cam_set(0, WIDTH, HEIGHT, FPS)

            ### Save images and perform facial recognition
            #if cap is not None:
            #    result = save_and_recognition(cap)
            #    if result != "":
            #        print('Hello, ' + result)
            #    time.sleep(1)

    except Exception as e:
        print(e)
        #if cap is not None: cap.release()

def remove_camera(cap):
    if cap is not None: cap.release()
    cap = None

def FaceRecognition_match(userid,username):
        insertFLAG = dbaccess.getAccessRecord_count(userid,username)
        if insertFLAG % 2 ==0:   #guusuu
            dbaccess.insertAccessRecord_Enter(userid,username)
        else:
            dbaccess.insertAccessRecord_Exit(userid,username)


if __name__ == '__main__':
    main()