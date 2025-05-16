import face_recognition
import EncodingData
import time

### This part is necessary to run face_recognition smoothly ##########
frame = face_recognition.load_image_file('testpic.png')                  
face_locations = face_recognition.face_locations(frame)
face_encodings = face_recognition.face_encodings(frame, face_locations)
if len(face_locations)>0:print("sucsess")
######################################################################

def recognition(cam_number, rec_time):
    try:
        name=""
        imgname = 'cam{}.jpg'.format(cam_number)
        frame = face_recognition.load_image_file('CameraLog/'+ imgname) 
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
                    matchedIdxs = [i for (i,b) in enumerate(face_distances) if b]
                    counts = {}
                    for i in matchedIdxs:
                        if face_distances[i]*100 < 32:
                            name = EncodingData.PickleData.data["names"][i]
                            counts[name] = counts.get(name,0) + 1
                    name = max(counts, key=counts.get)
            ################################################
                if rec_time == 0:
                    rec_time = time.time()

        return rec_time, name       
      
    except Exception as e:
        print("face recognition err",e)

