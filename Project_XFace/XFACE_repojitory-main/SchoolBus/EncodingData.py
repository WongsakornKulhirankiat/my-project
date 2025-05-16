import os
import pickle
import cv2
if os.name != 'nt': import face_recognition

SHAREDVARS = None

class PickleDataClass():
    def __init__(self):
        pickle_path = 'CameraLog/encodings.pickle'
        if not os.path.exists(pickle_path):
            blank = {"encodings": [], "names": [],"student_id": []}
            with open(pickle_path, "wb") as f1:
                f1.write(pickle.dumps(blank))
        with open(pickle_path,'rb') as file:
            data=file.read()
        if len(data)==0:
            print("there is no data")
        try:
            pickle_data=pickle.loads(data)
        except pickle.UnpicklingError:
            print("Data is not in pickle format")
        self.data = pickle.loads(open(pickle_path, "rb").read())

    def addFace(self, name, id):
        imgDirectory = ""   #### on hold for now
        img = cv2.imread(imgDirectory)
        rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        boxes = face_recognition.face_locations(rgb, model='hog')
        encodings = face_recognition.face_encodings(rgb, boxes)
        
        if encodings:
            encoding = encodings[0]
            self.data["encodings"].append(encoding)
            self.data["names"].append(name)
            self.data["student_id"].append(id)
        f = open('CameraLog/encodings.pickle', "wb")
        f.write(pickle.dumps(self.data))
        f.close()
        print("Add 1 encoded data successfully!")
        #SHAREDVARS['XFaceLogging'].system('SUCCESS:FACE', "Append {}'s face successfully".format(name))
        self.reInitializeData()
        
    def deleteFace(self, name):
        indices = [i for i, n in enumerate(self.data["names"]) if n ==name]
        if not indices:
            return
        
        for i in reversed(indices):
            self.data["names"].pop(i)
            self.data["encodings"].pop(i)
            self.data["student_id"].pop(i)

        with open('encodings.pickle', "wb") as f:
            f.write(pickle.dumps(self.data))

        print("Delete 1 encoded data successfully!")
        #SHAREDVARS['XFaceLogging'].system('SUCCESS:FACE', "Delete {}'s face successfully".format(name))
        self.reInitializeData()
    
    def reInitializeData(self):
        self.data = pickle.loads(open('CameraLog/encodings.pickle', "rb").read())
        #SHAREDVARS['XFaceLogging'].system('SUCCESS:FACE', "re initialize faces data successfully")

    def faid_data(self, tag_to_find):#for my check and not needed for app
        with open('CameraLog/encodings.pickle', "rb") as f:
            data = pickle.load(f)
            names = data.get("names", [])
            student_ids = data.get("student_id",[])

            for i, name in enumerate(names):
                if name == tag_to_find:
                    if i < len(student_ids):
                        return student_ids[i]
                    else:
                        print("not found")
                        return None
            return("tag not found")
        

PickleData = PickleDataClass()

if __name__ == '__main__':#for my check and not needed for app
    #PickleData.addFace("yamaji",5)

    student_id = PickleData.faid_data("obama")
    if student_id is not None: print(student_id)
