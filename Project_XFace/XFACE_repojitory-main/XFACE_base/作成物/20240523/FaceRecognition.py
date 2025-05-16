import face_recognition
import EncodingData
import time
import numpy as np
import os

### This part is necessary to run face_recognition smoothly ##########
frame = face_recognition.load_image_file('testpic.png')                  
face_locations = face_recognition.face_locations(frame)
face_encodings = face_recognition.face_encodings(frame, face_locations)
if len(face_locations)>0:print("sucsess")
######################################################################
imgpath = 'CameraLog/cap.jpg'
current_directory = os.getcwd()  # 現在のディレクトリを取得
file_path = os.path.join(current_directory, imgpath)

def recognition():
    try:
        name=""
        id =""
        adminflag=""
        frame = face_recognition.load_image_file(file_path) 
        if not frame is None:
            a = time.time()
            #bgr_frame = frame[:, :, ::-1]
            ################## DETECT `350ms ###############
            face_locations = face_recognition.face_locations(frame)
            if len(face_locations) > 0:
                biggest_face = face_locations[0]
                for tuple in face_locations:
                    if tuple[2] - tuple[0] > biggest_face[2] - biggest_face[0]:
                        biggest_face = tuple
                face_location = []
                face_location.append(biggest_face)
            ################################################
    
            ################## RECOGNITION #################
                a = time.time()
                face_encodings = face_recognition.face_encodings(frame, face_location)
                face_distances = face_recognition.face_distance(EncodingData.PickleData.data["encodings"], face_encodings[0])
                
                if min(face_distances)*100 < 32:
                    i = np.argmin(face_distances)
                    name = EncodingData.PickleData.data["names"][i]
                    id = EncodingData.PickleData.data["user_id"][i]
                    adminflag = EncodingData.PickleData.data["adminflag"][i]
            ################################################

        return name, id, adminflag 
      
    except Exception as e:
        print("face recognition err",e)


def load_image_Facerecognition(path):
    imagefile = face_recognition.load_image_file(path)
    return imagefile

def addpickle_Facerecognition(userid,username,adminflag):
    EncodingData.PickleData.addFace(userid,username,adminflag)

def deletepickle_Facerecognition(userid):
    EncodingData.PickleData.deleteFace(userid)