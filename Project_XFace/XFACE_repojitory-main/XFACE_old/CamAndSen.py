## Preparation for running
#### Put files FaceRecognition and EncodingData and testpic(a image of face) in the same directory
#### Connect two sensors and two cameras

import Jetson.GPIO as GPIO
import cv2
import os
import time
import FaceRecognition

### GPIO settings for sensor #######
GPIO_PIN = 15
GPIO_PIN2 = 29
GPIO.setmode(GPIO.BOARD)
GPIO.setup(GPIO_PIN, GPIO.IN)
GPIO.setup(GPIO_PIN2, GPIO.IN)
####################################

### camera settings #################
WIDTH = 800
HEIGHT = 600
FPS = 5

def cam_set(DEVICE_ID, WIDTH, HEIGHT, FPS):
    cap = cv2.VideoCapture(DEVICE_ID)
    cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('Y','U','Y','V'))
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)
    cap.set(cv2.CAP_PROP_FPS, FPS)

    fourcc = decode_fourcc(cap.get(cv2.CAP_PROP_FOURCC))
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    fps = cap.get(cv2.CAP_PROP_FPS)
    print("ID:{} fourcc:{} fps:{} width:{} height:{}".format(DEVICE_ID, fourcc, fps, width, height))

    return cap

def decode_fourcc(v):
    v = int(v)
    return "".join([chr((v >> 8 * i) & 0xFF) for i in range(4)])
#####################################################################

### Save images and perform facial recognition #######################
def save_and_recognition(cap1, cap2, cap1_rec_start, cap2_rec_start):
    name1, name2 = "", ""
    if cap1 is not None:
        ret1, frame1 = cap1.read()
        if ret1:
            cv2.imwrite("CameraLog/cam1.jpg", frame1)
            result1 = FaceRecognition.recognition(1, cap1_rec_start)
            if result1[0] != 0 and result1[1] != "":
                if cap1_rec_start == 0: cap1_rec_start = result1[0]
                name1 = result1[1]
        else:
            print("failed to open cap1")
            cap1.release()
            
    if cap2 is not None:
        ret2, frame2 = cap2.read()
        if ret2:
            cv2.imwrite("CameraLog/cam2.jpg", frame2)
            result2 = FaceRecognition.recognition(2, cap2_rec_start)
            if result2[0] != 0 and result2[1] != "":
                if cap2_rec_start == 0: cap2_rec_start = result2[0]
                name2 = result2[1]
            else:
                print("failed to open cap2")
                cap2.release()

    return cap1_rec_start, cap2_rec_start, name1, name2
#####################################################################

### main roop #######################################################
def main():
    try:
        cap1, cap2= None, None
        cap1_start, cap2_start = None, None
        cap1_rec_start, cap2_rec_start = 0, 0
        name1 ,name2 = "", ""
        if not os.path.exists("CameraLog"):
            os.makedirs("CameraLog")

        while True:
            inputValue1 = GPIO.input(GPIO_PIN)
            inputValue2 = GPIO.input(GPIO_PIN2)

            ### Active the camera when the sensor responds
            if inputValue1 == 1 and cap1 is None: 
                cap1 = cam_set(0, WIDTH, HEIGHT, FPS)
                cap1_start = time.time()
            if inputValue2 == 1 and cap2 is None: 
                cap2 = cam_set(2, WIDTH, HEIGHT, FPS)
                cap2_start =time.time()

            ### Save images and perform facial recognition
            if cap1 is not None or cap2 is not None:
                result = save_and_recognition(cap1, cap2, cap1_rec_start, cap2_rec_start)
                print(result)
                if cap1_rec_start == 0: cap1_rec_start = result[0]
                if cap2_rec_start == 0: cap2_rec_start = result[1]
                if name1 =="": name1 = result[2]
                if name2 =="": name2 = result[3]
                end_time = time.time()

                ### Check if the same person has been authenticated for more than 1 second
                if name1 != "" and end_time - cap1_rec_start >= 1: 
                    if name1 == result[2]: 
                        print('Hello, ' + name1)
                        cap1_rec_start = 0
                        name1 = ""
                    else:
                        cap1_rec_start = result[0]
                        name1 = result[2]
                if name2 != "" and end_time - cap2_rec_start >= 1: 
                    if name2 == result[3]: 
                        print('Bye, ' + name2)
                        cap2_rec_start = 0
                        name2 = ""
                    else:
                        cap2_rec_start = result[1]
                        name2 = result[3]
                
                ### Turn off camera after specified time
                if cap1_start is not None and end_time - cap1_start >= 5:
                    cap1.release()
                    cap1, cap1_start = None, None
                if cap2_start is not None and end_time - cap2_start >= 5:#count2 == 5:
                    cap2.release()
                    cap2, cap2_start = None, None

    except Exception as e:
        print(e)
        if cap1 is not None: cap1.release()
        if cap2 is not None: cap2.release()
        GPIO.cleanup()

if __name__ == '__main__':
    main()




