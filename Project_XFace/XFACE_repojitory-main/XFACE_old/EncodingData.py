import os
import pickle
import cv2
if os.name != 'nt': import face_recognition

SHAREDVARS = None

class PickleDataClass():
    def __init__(self):
        pickle_path = 'CameraLog/encodings.pickle'
        if not os.path.exists(pickle_path):
            blank = {"encodings": [], "names": []}
            with open(pickle_path, "wb") as f1:
                f1.write(pickle.dumps(blank))
        with open(pickle_path,'rb') as file:
            data=file.read()
        if len(data)==0:
            print("空")
        try:
            pickle_data=pickle.loads(data)
            print("データはpickle形式")
        except pickle.UnpicklingError:
            print("pickle形式ではない")
        self.data = pickle.loads(open(pickle_path, "rb").read())

    def addFace(self, name):
        encodings =[]
        names =[]
        imgDirectory = ""   #### on hold for now
        img = cv2.imread(imgDirectory)
        rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        boxes = face_recognition.face_locations(rgb, model='hog')
        encodings = face_recognition.face_encodings(rgb, boxes)
        
        for encoding in encodings:
            self.data["encodings"].append(encoding)
            self.data["names"].append(name)
            break
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

        with open('encodings.pickle', "wb") as f:
            f.write(pickle.dumps(self.data))

        print("Delete 1 encoded data successfully!")
        #SHAREDVARS['XFaceLogging'].system('SUCCESS:FACE', "Delete {}'s face successfully".format(name))
        self.reInitializeData()
    
    def reInitializeData(self):
        self.data = pickle.loads(open('encodings.pickle', "rb").read())
        #SHAREDVARS['XFaceLogging'].system('SUCCESS:FACE', "re initialize faces data successfully")

PickleData = PickleDataClass()

if __name__ == '__main__':
    PickleData.addFace("yamaji")
