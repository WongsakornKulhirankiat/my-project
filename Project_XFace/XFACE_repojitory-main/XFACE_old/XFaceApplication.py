import glob
import time
import cv2
import numpy as np
import pickle
import os
import shutil
import xlsxwriter
import xlwt
import base64
import io
import csv
import math
import traceback

from datetime import date, datetime
from functools import partial
from ctypes import c_char_p 
from multiprocessing import Manager, Process, Value
from time import sleep
from XFaceAntiSpoof import test

import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst
from gi.repository import GLib
import mediapipe as mp         #yamaji 12.5

# region >>=============== SoundLoader ===============<<
os.environ["KIVY_AUDIO"] = "sdl2"
from kivy.core.audio import SoundLoader
Sounds = {
    'success': SoundLoader.load('assets/sound/success.wav'),
    'input': SoundLoader.load('assets/sound/input.wav'),
    'short_beep': SoundLoader.load('assets/sound/short_beep.wav'),
    'digital_beep': SoundLoader.load('assets/sound/digital_beep.wav'),
    'click': SoundLoader.load('assets/sound/click.wav'),
}
# endregion >>=============== SoundLoader ===============<<

from kivy.app import App
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.core.window import Window   #2023/12/28 fujiwara tuika
from kivy.lang import Builder
from kivy.properties import NumericProperty, StringProperty, ListProperty, BooleanProperty, ObjectProperty
from kivy.metrics import dp
from kivy.uix.modalview import ModalView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition, CardTransition, NoTransition
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior

from kivymd.app import MDApp
from kivymd.toast import toast
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDIconButton,MDFlatButton, MDRaisedButton, MDTextButton, MDRectangleFlatButton
from kivymd.uix.bottomsheet import MDCustomBottomSheet
from kivymd.uix.list import ILeftBodyTouch, IRightBodyTouch, ILeftBody, TwoLineIconListItem, IconLeftWidget,OneLineAvatarListItem,TwoLineAvatarListItem# NandeDownloadTwoLineAvatarIconListItem, NandeUploadTwoLineAvatarIconListItem,
from kivymd.uix.selectioncontrol import MDCheckbox
#from kivymd.uix.card import NandeCardPost
from kivymd.uix.imagelist import MDSmartTile
from kivymd.uix.dialog import MDDialog
from kivymd.uix.pickers import MDDatePicker, MDTimePicker

from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelOneLine
#from kivy.properties import StringProperty,ListProperty,BooleanProperty,ObjectProperty
from kivymd.theming import ThemableBehavior
from kivymd.uix.card import MDCard
from kivymd.uix.textfield import MDTextField, MDTextFieldRect
from kivy.graphics import Ellipse, Color
from kivy.uix.popup import Popup

# region >>=============== Initialization ===============<<

sm = None
ps = None
sc = None
RASPBERRY = True
CAMERA_INIT = True
CAMERA = True
FINGERPRINT_INIT = True
FINGERPRINT = True
SHAREDVARS = {'SERVER':True}

import XFaceLogging
import XFaceDAO
import XFaceAPI
import XFaceEncodingData

try:
    import XFaceGPIOControllers
    #import XFaceLivenessServices
except Exception:
    RASPBERRY = False
    XFaceLogging.system("[NANDE  ]", "Failed to initialize XFaceGPIOControllers.")
    XFaceLogging.system("[NANDE  ]", traceback.format_exc())

try:
    import XFacePiCamera
    import face_recognition
    try:
        import XFaceSeekCompact
        sc = XFaceSeekCompact.SeekCompact()
    except Exception:
        sc = None
    ps = XFacePiCamera.PiVideoStream()
    ps.CAMERA_FLAG.clear()
    ps.start()
    # Create interprocess variables (process can't share normal variables even if they're global variables)
    m = Manager()
    camera_processing   = m.Value(c_char_p,'-')  # Camera communicating value.       -:idle, name:dooropen, '0'~'-10':registeration
    camera_temp_no      = Value('i',0)           # Circular pic list order.          0:idle, 1~4:circularlist
    camera_pool_valid   = Value('i',1)           # One camera process at a time.    0:invalid, 1:valid
except Exception:
    CAMERA_INIT = False
    CAMERA = False
    XFaceLogging.system("[NANDE  ]", "Failed to initialize XFacePiCamera.")
    XFaceLogging.system("[NANDE  ]", traceback.format_exc())

try: 
    import XFaceCapacitiveFP
    XFaceGPIOControllers.GPIO.output(XFaceGPIOControllers.Finger_RST_Pin, XFaceGPIOControllers.GPIO.HIGH) 
    time.sleep(0.25)
    r = XFaceCapacitiveFP.GetUserCount()
    if r == XFaceCapacitiveFP.ACK_TIMEOUT:
        raise Exception("Fingerprint Module not connected")
except Exception:
    FINGERPRINT_INIT = False
    FINGERPRINT = False
    XFaceLogging.system("[NANDE  ]", "Failed to initialize XFaceCapacitiveFP.")
    XFaceLogging.system("[NANDE  ]", traceback.format_exc())

XFaceLogging.SHAREDVARS = SHAREDVARS
XFaceDAO.SHAREDVARS = SHAREDVARS 
XFaceAPI.SHAREDVARS = SHAREDVARS
XFaceEncodingData.SHAREDVARS = SHAREDVARS
SHAREDVARS['XFaceLogging'] = XFaceLogging
SHAREDVARS['XFaceDAO'] = XFaceDAO
SHAREDVARS['XFaceEncodingData'] = XFaceEncodingData
if SHAREDVARS['SERVER']: SHAREDVARS['XFaceAPI'] = XFaceAPI
if FINGERPRINT: SHAREDVARS['XFaceCapacitiveFP'] = XFaceCapacitiveFP

# ========== post init ==========
XFaceDAO.initServerDAO()
if XFaceDAO.localDAO.getSystemValue('CAMERA') == '0': CAMERA = False
if XFaceDAO.localDAO.getSystemValue('FINGERPRINT') == '0': FINGERPRINT = False

# endregion >>=============== Initialization ===============<<



## region #####################################  SCREEN  ###################################

class ScreenManagement(ScreenManager):
    def show_loading(self, screen):
        screen.loading = ModalView(
            auto_dismiss = False,
            size_hint=(0.3, 0.3),
            background='assets/trans.png')
        screen.loading.add_widget(Loading())
        screen.loading.open(animation=False)
    
    def play(self, sound):
        try:
            # [input, digital_beep, beep, success]
            sound = Sounds[sound]
            sound.volume = self.volume/800
            sound.play()
            #print("Sound found at %s" % sound.source)
            #print("Sound is %.3f seconds" % sound.length)
        except Exception as e:
            print(e)

class Loading(FloatLayout):
    angle = NumericProperty(0)
    def __init__(self, **kwargs):
        super(Loading, self).__init__(**kwargs)
        anim = Animation(angle = 360, duration=2) 
        anim += Animation(angle = 360, duration=2)
        anim.repeat = True
        anim.start(self)

    def on_angle(self, item, angle):
        if angle == 360:
            item.angle = 0
class HomeScreen(Screen):
    def on_enter(self):
        if FINGERPRINT:
            self.fp_state = 0
            self.chk = Clock.schedule_interval(self.check_finger_press, 0.5)
        self.u = Clock.schedule_interval(self.update, 1)
        Clock.schedule_once(self.add_head, 1)
        if RASPBERRY:
            XFaceGPIOControllers.GPIO.output(XFaceGPIOControllers.Finger_RST_Pin, XFaceGPIOControllers.GPIO.LOW)
        if CAMERA:
            self.add_camera()

    def on_pre_leave(self):
        if FINGERPRINT:
            XFaceGPIOControllers.GPIO.output(XFaceGPIOControllers.Finger_RST_Pin, XFaceGPIOControllers.GPIO.LOW)
            Clock.unschedule(self.chk)
        if CAMERA:
            self.remove_camera()
        Clock.unschedule(self.u)

    def update(self, _):
        d = datetime.now()
        self.ids.home_date_label.text = d.strftime("%A") +" "+ d.strftime("%d") +" "+ d.strftime("%b") +" "+ d.strftime("%Y")
        self.ids.home_time_label.text = d.strftime("%X")
        # if RASPBERRY:  #yamaji comment out
        #     self.ids.home_cpu_label.text = str(XFaceGPIOControllers.CPUTemperature().temperature)[:2] + "°C"    

    def add_head(self, _):
        if RASPBERRY:
            self.ids.on_raspberry.opacity = 1
        if CAMERA:
            self.ids.on_camera.opacity = 1
        else:
            self.ids.on_camera.opacity = 0.4
        if FINGERPRINT:
            self.ids.on_fingerprint.opacity = 1
        else:
            self.ids.on_fingerprint.opacity = 0.4
        if SHAREDVARS['SERVER']:
            self.ids.on_database.opacity = 1
            self.ids.home_sync_button.opacity = 1
            self.ids.home_sync_button.size_hint = None, None

    def check_finger_press(self, _):
        if XFaceCapacitiveFP.rLock.acquire() == True:
            if self.fp_state == 0:  # wake up
                if XFaceGPIOControllers.GPIO.input(XFaceGPIOControllers.Finger_WAKE_Pin):   # If you press your finger
                    time.sleep(0.01)
                    if XFaceGPIOControllers.GPIO.input(XFaceGPIOControllers.Finger_WAKE_Pin):
                        XFaceGPIOControllers.GPIO.output(XFaceGPIOControllers.Finger_RST_Pin, XFaceGPIOControllers.GPIO.HIGH)   # Pull up the RST to start the module and start matching the fingers
                        self.fp_state = 1
            elif self.fp_state == 1:
                print ("Waiting Finger......Please try to place the center of the fingerprint flat to sensor !")
                time.sleep(0.5)   #2024/01/09 fujiwara tuika
                r = XFaceCapacitiveFP.VerifyUser()
                print(r,"fujiwara_r_check_XFaceApplication")   #2024/01/09 fujiwara tuika
                # sm.play('input')
                if r[0] == XFaceCapacitiveFP.ACK_SUCCESS:
                    print ("Matching successful with fingerprint index: " + str(r[1]))
                    XFaceDAO.localDAO.cursor.execute("select NAME from FINGERPRINT where FINGERPRINT_ID = '{}'".format(r[1]))
                    result = XFaceDAO.localDAO.cursor.fetchone()
                    if not result is None:
                        if sc is None:
                            self.doorOpen(result[0], mode = 'fingerprint')
                        else:
                            self.doorOpen(result[0], mode = 'fingerprint', temp = sc.snap())
                    else:
                        print("User not found!")
                        toast("User not found!")
                elif r[0] == XFaceCapacitiveFP.ACK_NO_USER:
                    print ("Failed: This fingerprint was not found in the library !")
                    toast("No match found!")
                # elif r[0] == XFaceCapacitiveFP.ACK_TIMEOUT:
                #     print ("Failed: Time out !")
                #     toast("Please press the finger properly!")
                elif r[0] == XFaceCapacitiveFP.ACK_GO_OUT:
                    print ("Failed: Please try to place the center of the fingerprint flat to sensor !")
                #After the matching action is completed, drag RST down to sleep
                #and continue to wait for your fingers to press
                XFaceGPIOControllers.GPIO.output(XFaceGPIOControllers.Finger_RST_Pin, XFaceGPIOControllers.GPIO.LOW)
                self.fp_state = 2
                print("fujiwara_fingercheck_miss")   #2024/01/09 fujiwara tuika
            elif self.fp_state > 4:
                XFaceGPIOControllers.GPIO.output(XFaceGPIOControllers.Finger_RST_Pin, XFaceGPIOControllers.GPIO.LOW)
                self.fp_state = 0
            else:
                self.fp_state += 1
            XFaceCapacitiveFP.rLock.release()

    def add_camera(self):
        self.backSub = cv2.createBackgroundSubtractorMOG2(history=1,varThreshold=168,detectShadows=False)
        self.backSub.setBackgroundRatio(0.3)
        self.motion_flag = False
        self.idle_count = 0

        frame = face_recognition.load_image_file('assets/testpic.png')                   #yamaji 11.6 add following 3 lines
        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)

        if not ps.CAMERA_FLAG.is_set():
            ps.CAMERA_FLAG.set()
            camera_processing.value = '-' ##d
            camera_temp_no.value = 0
            camera_pool_valid.value = 1
            #Gst.init(None)
            self.ref = Clock.schedule_interval(self.refresh, 0.085)
            self.upd = Clock.schedule_interval(self.process, 0.1)

    def remove_camera(self):
        if ps.CAMERA_FLAG.is_set():
            ps.CAMERA_FLAG.clear()
            try:
                Clock.unschedule(self.ref)
                Clock.unschedule(self.upd)
            except Exception: pass
            self.ids.home_camera.source = 'assets/trans.png'
            cv2.imwrite('assets/temp.png', face_recognition.load_image_file('assets/trans.png')) #yamaji 11.20  cv2.imread => face_recognition.load_image_file
            ps.clear()


    def refresh(self, _):
        frame = ps.read()
        if not frame is None and not sm.welcome_modal:
            canny = cv2.Canny(frame,50,150, apertureSize = 3, L2gradient = True)
            canny = self.backSub.apply(canny)
            canny = cv2.medianBlur(canny,5)
            threshold = sum(sum(canny>200))
            if threshold > 30:
                self.idle_count = 0
                self.motion_flag = True
            else:
                self.idle_count += 1
                if self.idle_count == 30:
                    self.motion_flag = False
                    self.ids.home_camera.source = 'assets/trans.png'
                    self.ids.home_camera.reload()

            if self.motion_flag or self.idle_count < 30:
                value = camera_temp_no.value
                if value < 2: value += 1
                else: value = 1
                camera_temp_no.value = value
                imgname = 'temp_' + str(value) + '.png'
                cv2.imwrite('assets/'+ imgname, frame)
                self.ids.home_camera.source = 'assets/'+ imgname
                self.ids.home_camera.reload()
                
    def process(self, _):
        if camera_temp_no.value == 0:
            return

        if camera_processing.value != '-':
            name = camera_processing.value
            camera_processing.value = '-'
            camera_temp_no.value = 0
            if sc is None:
                self.doorOpen(name, mode='camera')
            else:
                self.doorOpen(name, mode='camera', temp = sc.snap())

        elif camera_pool_valid.value == 1 and self.motion_flag:
            camera_pool_valid.value = 0
            for i in range(len(sm.process_pool)-5):
                sm.process_pool[0].join()
                sm.process_pool.pop(0)


            #p = Process(target=self.processCamera)
            #p.start()
            #sm.process_pool.append(p)
            self.processCamera()

    def processCamera(self):
        try:
            value = camera_temp_no.value
            imgname = 'temp_' + str(value) + '.png'
            #imgname = 'V.png'
            #frame = cv2.imread('assets/'+ imgname)
            frame = face_recognition.load_image_file('assets/'+ imgname) #yamaji
            if not frame is None:
                a = time.time()
                bgr_frame = frame[:, :, ::-1]
                # label = test(                                                                 #yamaji 10.20 anti spoof off
                #             image=frame,
                #             model_dir='/home/guest/nande/anti_spoof_models',
                #             device_id=0
                #             )
                # print(label)
                label=1
            ################### LIGHTING ###################
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                mean = np.mean(gray)
                if mean < 70 :
                    XFaceGPIOControllers.setInfrared(1)
                else:
                    XFaceGPIOControllers.setInfrared(0)
            ################################################
                if label==1:
                ################## DETECT `350ms ###############
                    #start = time.time()
                    face_locations = face_recognition.face_locations(bgr_frame)
                    #print('detect times : %.3f ms'%((end - start)*1000))
                    if len(face_locations) > 0:
                        biggest_face = face_locations[0]
                        for tuple in face_locations:
                            if tuple[2] - tuple[0] > biggest_face[2] - biggest_face[0]:
                                biggest_face = tuple
                        face_location = []
                        face_location.append(biggest_face)
                        print(face_location)
                ################################################
            
                ################## RECOGNITION #################
                        #a = time.time()
                        face_encodings = face_recognition.face_encodings(bgr_frame, face_location)
                        face_distances = face_recognition.face_distance(XFaceEncodingData.PickleData.data["encodings"], face_encodings[0])
                        name=""
                        #if True in face_distances:
                        if min(face_distances)*100 < 32:
                            matchedIdxs = [i for (i,b) in enumerate(face_distances) if b]
                            counts = {}
                            for i in matchedIdxs:
                                if face_distances[i]*100 < 32:
                                    name = XFaceEncodingData.PickleData.data["names"][i]
                                    counts[name] = counts.get(name,0) + 1
                            name = max(counts, key=counts.get)
                        print('recognition time : %.3f ms'%((time.time() - a)*1000))
                ################################################
                        a = time.time()
                        
                        if name != "": #and min(face_distances)*100 < 32:
                        #if label==1 and min(face_distances)*100 < 32:
                            #i = np.argmin(face_distances)
                            #name = XFaceEncodingData.PickleData.data["names"][i]
                            print('Hello, ' + name + '\nTotalTime: ' +str(time.time() - a))                                  #2023/11/2 fujiwara   TotalTome -> TotalTime
                            camera_processing.value = name
                            cv2.imwrite('log/OpenDoorPic/'+str(time.strftime("%Y-%m-%d-%H-%M-%S"))+'_'+ name +'.png', frame)
                        
        except Exception as e:
            print(e)
            XFaceLogging.system("555", traceback.format_exc())

        finally:
            camera_pool_valid.value = 1

    def doorOpen(self, name, mode='numpad', temp='-'):
        # set welcome
        sm.welcome_modal = True
        
        # save log image
        if CAMERA:
            frame=ps.read()
            #cv2.imwrite('log/OpenDoorPic/'+str(time.strftime("%Y-%m-%d-%H-%M-%S"))+'_'+ name +'.png', frame)  #yamaji 11.20
            self.idle_count = 0
            self.motion_flag = False
            self.ids.home_camera.source = 'assets/trans.png'
            self.ids.home_camera.reload()

        # delete from pickle if user not exists
        XFaceDAO.localDAO.cursor.execute("select NAME from EMPLOYEE where NAME = '{}'".format(name))
        employee = XFaceDAO.localDAO.cursor.fetchone()
        if employee is None and name != "Administrator":
            XFaceEncodingData.PickleData.deleteFace(name)
            return

        # collect data to show welcome
        im = None
        #folder = 'pic/' + name
        #g = glob.glob(folder+'/*png') + glob.glob(folder+'/*jpg')
        # for filename in g:
        #     im = filename
        #     break
        # if im is None:
        #     im = 'assets/temp_profile.png'
        folder='pic/' + name + '/' + name + '.png'
        if os.path.exists(folder):
            im=folder
        else:
            im = 'assets/temp_profile.png'
        img = Image(source = im,
                    allow_stretch = True,
                    keep_ratio = True,
                    size_hint=(1.5, 1.5),  #yamaji 10.26 add
                    )
        """content = MDLabel(font_style='Body1',
                        theme_text_color='Secondary',
                        # text='Hello, {}\n\
                        #       \nDepartment: {}\
                        #       \nRole: {}'
                        #       .format(name, employee[0], employee[1]),
                        text='Hello, {}\n\
                            {}°C'.format(name, temp),
                        )
                        #size_hint_x = .5)"""
        content = MDLabel(font_style='Body1',
                        theme_text_color='Custom',
                        text='Hello, {}\n\
                            {}°C'.format(name, temp),
                        text_color=(1,1,1,1),                  #korn 11.1
                        )
        content.bind(texture_size=content.setter('size'))
        bLayout = BoxLayout(size_hint_y=1, size_hint_x=.9, spacing=10)
        bLayout.add_widget(img)
        bLayout.add_widget(content)
        #yamaji from
        # show welcome modal
        # self.dialog = MDDialog(title="Login Success!",
        #                     text="",
        #                     size_hint=(.8, .5),
        #                     #text_button_ok='',
        #                     #text_button_cancel='',
        #                     auto_dismiss=False)
        dialog=BoxLayout(orientation='vertical',)
        #label=MDLabel(text="",font_size=18,pos_hint={"center_x":0.5, "center_y":0.5},)
        label=MDLabel(text="",font_size=18,pos_hint={"center_x":0.5, "center_y":0.5},theme_text_color="Custom",text_color=(1,1,1,1)) #korn 11.1
        space=BoxLayout(size_hint=(1,0.5))
        dialog.add_widget(label)
        dialog.add_widget(bLayout)
        dialog.add_widget(space)
        self.dialog = Popup(
            title="Login Success",
            title_size = '20sp',    #yamaji 10.26 add
            size_hint=(0.8, 0.5),
            content = dialog,
            )      #yamaji to
        self.dialog.open()

        XFaceGPIOControllers.doOpenDoor()
        Clock.schedule_once(lambda x: XFaceGPIOControllers.GPIO.output(XFaceGPIOControllers.OP_Door, XFaceGPIOControllers.GPIO.LOW), 5.0)

        # Auto dismiss to welcome modal
        def modalDismiss(self, root):
            sm.welcome_modal = False
            try:
                root.dialog.dismiss()
            except Exception:
                XFaceLogging.system('599', traceback.format_exc())
        Clock.schedule_once(partial(modalDismiss, root=self), 5.0)   #2024/01/10 fujiwara 3.5 -> 5.0

        # Speak Hello {}
        def speak(name):
            try:
                volume = int(2000 * (math.log10(sm.volume/300)))
                os.system("espeak -v en+f2 -s150 'Hello {}' --stdout > /home/pi/nande/assets/sound/greetings".format(name))
                os.system("omxplayer --vol "+str(volume)+" -o local /home/pi/nande/assets/sound/greetings >/dev/null 2>&1")
            except Exception:
                XFaceLogging.system("643", traceback.format_exc())
        
        if os.name != 'nt':
            #XFaceGPIOControllers.openningDoor()

            for i in range(len(sm.process_pool)-5):
                sm.process_pool[0].join()
                sm.process_pool.pop(0)

            p = Process(target=speak, args=(name,))
            sm.process_pool.append(p)
            p.start()

        # finally, save log
        XFaceLogging.door(mode.upper(), name)

import kivymd.material_resources as m_res#yamaji from
class NandeDownloadTwoLineAvatarIconListItem(TwoLineAvatarListItem):
    _txt_right_pad = NumericProperty("40dp")
    ndpassword = StringProperty("1111")
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._txt_right_pad = dp(40) + m_res.HORIZ_MARGINS

class NandeUploadTwoLineAvatarIconListItem(TwoLineAvatarListItem):#yamaji to
    _txt_right_pad = NumericProperty("40dp")
    ndpassword = StringProperty("1111")
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._txt_right_pad = dp(40) + m_res.HORIZ_MARGINS

class ListDownloadItemWithCheckbox(NandeDownloadTwoLineAvatarIconListItem): pass
class ListUploadItemWithCheckbox(NandeUploadTwoLineAvatarIconListItem): pass
class MyCheckbox(IRightBodyTouch, MDCheckbox): pass
class MyAvatar(ILeftBody, Image): pass
class SyncScreen(Screen):
    def back(self):
        sm.transition = CardTransition(duration=0.3, mode='pop', direction='right')
        sm.current = 'home'

    def on_enter(self):
        self.ids.sync_button.disabled = True
        self.ids.sync_switch.disabled = True
        self.fetch()

    def on_leave(self):
        self.ids.sync_scroll.clear_widgets()
        self.ids.sync_img.opacity = 0
        self.ids.sync_label.opacity = 0

    def onSyncClick(self):

        def _confirm(self):#(text, _): yamaji from
            # if text == 'Cancel':
            #     return
            # elif text == 'Yes':
            self.dialog.dismiss()
            self.apply()

        download_row_count = 0
        upload_row_count = 0
        delete_local_count = 0
        delete_server_count = 0
        msg = ''
        for i in self.ids.sync_scroll.children:
            if i.ids.checkbox.state == "normal":
                # Delete
                if i.type == 'download':
                    delete_server_count += 1
                elif i.type == 'upload':
                    delete_local_count +=1
            elif i.ids.checkbox.state == "down":
                # Keep
                if i.type == 'download':
                    download_row_count += 1
                elif i.type == 'upload':
                    upload_row_count += 1

        if delete_server_count > 0: msg += '[color=ff3333]' + str(delete_server_count) + ' row(s) on server will be deleted.[/color]\n'
        if delete_local_count > 0: msg += '[color=ff3333]' + str(delete_local_count) + ' row(s) on locals will be deleted.[/color]\n'
        if download_row_count > 0: msg += '[color=11dd11]' + str(download_row_count) + ' row(s) on server will be downloaded to local.[/color]\n'
        if upload_row_count > 0: msg += '[color=11dd11]' + str(upload_row_count) + ' row(s) on local will be uploaded to server.[/color]\n'
        
        # self.dialog = MDDialog(
        #     title="Are you sure?",
        #     size_hint=(0.8, 0.3),
        #     #text_button_ok="Yes",
        #     text= msg,
        #     #text_button_cancel="Cancel",
        #     events_callback=_confirm,
        # )
        dialog=BoxLayout(orientation='vertical',)
        #label=MDLabel(text="msg",font_size=18,pos_hint={"center_x":0.5, "center_y":0.5},)
        label=MDLabel(text="msg",font_size=18,pos_hint={"center_x":0.5, "center_y":0.5},theme_text_color="Custom",text_color=(1,1,1,1)) #korn 11.1
        buttun=BoxLayout(orientation='horizontal',spacing=10)
        space=BoxLayout(size_hint=(0.4,0.01))
        yes_button=MDFlatButton(text='Yes',on_release=lambda _:  _confirm(self),md_bg_color=(0.7,0.7,0.7,1),)
        cancel_button=MDFlatButton(text='Cancel',on_release=lambda _: self.dialog.dismiss(),md_bg_color=(0.7,0.7,0.7,1))
        buttun.add_widget(space)
        buttun.add_widget(yes_button)
        buttun.add_widget(cancel_button)
        dialog.add_widget(label)
        dialog.add_widget(buttun)
        self.dialog = Popup(
            title="Are you sure",
            size_hint=(0.8, 0.3),
            content = dialog,
            )
        self.dialog.open()

    def fetch(self):
        sm.show_loading(self)
        # Compare local database with server database and fetch rows
        def _fetch(self, _):
            if SHAREDVARS['SERVER']:
                row_count = 0
                max_row_count = 30

                self.ids.sync_switch.active = True

                XFaceDAO.serverDAO.cursor.execute('select NAME from EMPLOYEE order by NAME')
                server_employees = XFaceDAO.serverDAO.cursor.fetchall()
                server_names = [employee[0] for employee in server_employees]

                XFaceDAO.localDAO.cursor.execute('select NAME from EMPLOYEE order by NAME')
                local_employees = XFaceDAO.localDAO.cursor.fetchall()
                local_names = [employee[0] for employee in local_employees]

                # rows to DOWNLOAD TO LOCAL
                for name in server_names:
                    if name not in local_names:
                        image = XFaceAPI.get(name)
                        if image != 'Success':
                            pic_path = 'assets/temp_profile.png'
                        else:
                            pic_path = 'pic/{}/{}.png'.format(name,name)
                        list_item = ListDownloadItemWithCheckbox(text=name,
                                                    secondary_text='found on server')
                        list_item.ids.avatar.source = pic_path
                        list_item.ids.checkbox.state = "down"
                        self.ids.sync_scroll.add_widget(list_item)
                    if row_count >= max_row_count: break
                    row_count += 1
                
                # rows to UPLOAD TO SERVER
                for name in local_names:
                    if name not in server_names:
                        folder = "pic/" + name
                        if not os.path.exists(folder):
                            pic_path = 'assets/temp_profile.png'
                        else:
                            g = glob.glob(folder+'/*png') + glob.glob(folder+'/*jpg')
                            for path in g:
                                pic_path = path
                                break
                        list_item = ListUploadItemWithCheckbox(text=name,
                                                    secondary_text='found on local')
                        list_item.ids.avatar.source = pic_path
                        list_item.ids.checkbox.state = "down"
                        self.ids.sync_scroll.add_widget(list_item)
                    if row_count >= max_row_count: break
                    row_count += 1

            if len(self.ids.sync_scroll.children) > 0:
                self.ids.sync_img.opacity = 0
                self.ids.sync_label.opacity = 0
                self.ids.sync_button.disabled = False
                self.ids.sync_switch.disabled = False

            else:
                XFaceLogging.system('INFO','data synchonization completed.')
                self.ids.sync_img.opacity = 1
                self.ids.sync_label.opacity = 1
                self.ids.sync_button.disabled = True
                self.ids.sync_switch.disabled = True

            self.loading.dismiss()
            print('Fetch changes finish')
        Clock.schedule_once(partial(_fetch,self))

    def apply(self):
        sm.show_loading(self)
        def _apply(self, _):
            # Apply Sync
            download_row_count = 0
            upload_row_count = 0
            delete_local_count = 0
            delete_server_count = 0
            for i in self.ids.sync_scroll.children:
                name = i.text

                if i.ids.checkbox.state == "normal":
                    # Delete on server
                    if i.type == 'download':
                        delete_server_count += 1
                        XFaceDAO.serverDAO.deleteEmployee(name)

                    # Delete on local
                    elif i.type == 'upload':
                        delete_local_count+=1
                        XFaceDAO.localDAO.deleteEmployee(name)

                elif i.ids.checkbox.state == "down":
                    # Apply Download to local
                    if i.type == 'download':
                        download_row_count += 1
                        XFaceDAO.copyFromServerToLocal(name)

                # Apply Upload to server
                    elif i.type == 'upload':
                        upload_row_count += 1
                        XFaceDAO.copyFromLocalToServer(name)

            s = ""
            if download_row_count > 0: s += str(download_row_count) + " row(s) has been downloaded.\n"
            if upload_row_count > 0: s += str(upload_row_count) + " row(s) has been uploaded.\n"
            if delete_local_count > 0: s += str(delete_local_count) + " row(s) has been delete on local.\n"
            if delete_server_count > 0: s += str(delete_server_count) + " row(s) has been delete on server.\n"
            if s != '': toast(s[:-1])
            self.ids.sync_scroll.clear_widgets()
            self.loading.dismiss()
            self.on_enter()
        Clock.schedule_once(partial(_apply,self))
        
    def pressSw(self, instance):
        if instance.active:
            for i in self.ids.sync_scroll.children:
                i.ids.checkbox.state = "down"
        else:
            for i in self.ids.sync_scroll.children:
                i.ids.checkbox.state = "normal"

class NumpadScreen(Screen):
    def on_enter(self):
        self.tick = 0
        self.timer = Clock.schedule_interval(self.count, 1)
        XFaceDAO.localDAO.cursor.execute('select NAME, PASSWORD from EMPLOYEE')
        result = XFaceDAO.localDAO.cursor.fetchall()
        self.dict = {record[1]:record[0] for record in result}
        self.submit("")                    #yamaji 11.8 add    against background not appearing
        self.display.text =""              #yamaji 11.8 add

    def on_pre_leave(self):
        Clock.unschedule(self.timer)
        self.display.text = ''
        KeyPass = self.keypress
        self.keypress = ""

    def count(self, _):
        if self.tick > 9:
            print('back to main screen due to no respond')
            sm.transition = SlideTransition(duration=0.1, direction='left')
            sm.current = 'home'
        else: self.tick += 1

    def submit(self, KeyPass):
        if KeyPass == '025600':
            sm.get_screen('home').doorOpen("Administrator")
        elif KeyPass == '0':
            sm.transition = NoTransition()
            sm.current = 'admin'
        elif len(KeyPass) > 4 and KeyPass[:5] == '99999':
            raise Exception("Exit")
        else:
            if KeyPass in self.dict:

                if sc is None:
                    sm.get_screen('home').doorOpen(self.dict[KeyPass])
                else:
                    sm.get_screen('home').doorOpen(self.dict[KeyPass] ,temp = sc.snap())        

            else:
                self.display.text = "User not found"

    def enter(self, text):
        sm.play('digital_beep')
        self.tick = 0
        if text == "submit":
            self.display.text = ''
            print('submit : ' + self.keypress)
            KeyPass = self.keypress
            self.keypress = ""
            self.submit(KeyPass)
        elif self.display.text == "User not found":
            self.display.text = "*"
            self.keypress = text
        else:
            self.display.text += "*"
            self.keypress += text

class IconLeftSampleWidget(ILeftBodyTouch, MDIconButton): pass
class NandeTile(ButtonBehavior, RelativeLayout): pass
class AdminScreen(Screen):
    def on_enter(self):
        if CAMERA:
            sm.get_screen('r3').remove_camera(reset=True)

    def on_pre_leave(self, *args):
        return super().on_pre_leave(*args)

    def clearRegister(self):
        sm.get_screen('r1').enterKey('Clear')
        sm.get_screen('r2').main_field = 'passcode_field2'
        sm.get_screen('r2').enter('back')

        if CAMERA:
            camera_processing.value = '0'
            sm.get_screen('r3').count = 0
            sm.get_screen('r3').ids.photo_switch.disabled = False
            sm.get_screen('r3').ids.photo_switch_label.text = "Enable Face-Recognition?"
        else:
            sm.get_screen('r3').ids.photo_switch.disabled = True
            sm.get_screen('r3').ids.photo_switch_label.text = "Camera module not found."
            
        if FINGERPRINT:
            #finger_state.value = -7
            sm.get_screen('r4').ids.fingerprint_switch.active = False
            sm.get_screen('r4').finger_count = 0
            sm.get_screen('r4').ids.fingerprint_switch.disabled = False
            sm.get_screen('r4').ids.fingerprint_switch_label.text = "Enable Fingerprint?"
            sm.get_screen('r4').ids.register_fingerprint_label.text = "Waiting for fingerprint..."
            sm.get_screen('r4').finger_eigens = []
            sm.get_screen('r4').chk = None
        else:
            sm.get_screen('r4').ids.fingerprint_switch.disabled = True
            sm.get_screen('r4').ids.fingerprint_switch_label.text = "Scanner not found."
        
        sm.get_screen('r3').photoSwitchOn(False)
        sm.get_screen('r3').ids.photo_switch.active = False

        sm.get_screen('r1').status = 'remove'
        sm.get_screen('r2').status = 'remove'
        sm.get_screen('r3').status = 'alert'
        sm.get_screen('r4').status = 'alert'

class RegisterScreen(Screen):
    def on_enter(self):
        self.names = []
        self.dataread = False
    def checkNameSql(self, text):
        #if SHAREDVARS['SERVER']:
        if len(text)>0:
            if self.dataread == False:
                XFaceDAO.localDAO.cursor.execute('select NAME from EMPLOYEE')
                result = XFaceDAO.localDAO.cursor.fetchall()
                self.names = [row[0].upper() for row in result]
                self.dataread = True
            if text in self.names or len(text)>20:                               #2023/11/8 fujiwara tuika
                self.status = 'remove'
                self.ids.f1_name_label.color = [1,0,0,1]
                if text in self.names:
                    self.ids.f1_name_label.text = 'This name already exist in database!'
                else:
                    self.ids.f1_name_label.text = 'Name exceeds 20 characters!'  #2023/11/8 fujiwara tuika en
            else:
                self.status = 'check'
                self.ids.f1_name_label.color = [0,1,0,1]
                self.ids.f1_name_label.text = 'The name is valid'
        else:
            self.status = 'remove'
            self.ids.f1_name_label.color = [1,0,0,1]
            self.ids.f1_name_label.text = 'Please enter a name.'
    def enterKey(self, text):
        if text == "BackSpc":
            if len(self.ids.f1_name.text) > 0:
                self.ids.f1_name.text = self.ids.f1_name.text[:-1]
        elif text == "Clear":
            self.ids.f1_name.text = ""
        else:
            self.ids.f1_name.text += text
class RegisterScreen2(Screen):
    def toState(self, state):
        if state == 2:
            Animation(_sizeX=.3,_sizeY=.15,_posX=.2,_posY=.75,md_bg_color=(1,1,1,0),text_color=(0,0,0,.2),font_size=12,duration=.4, t='out_cubic').start(self.ids.passcode_field1)
            Animation(_sizeX=.8,_sizeY=.4,_posX=.5,_posY=.40,md_bg_color=(1,1,1,.8),text_color=(.3,.3,1,1),font_size=30,duration=.4, t='out_cubic').start(self.ids.passcode_field2)
            self.main_field = 'passcode_field2'
            self.ids.mlabel.color = (.3,.3,1,1)
            self.ids.mlabel.text = 'Please enter confirm passcode'
            self.ids.back_button.text = "Back"
        else:
            Animation(_sizeX=.8,_sizeY=.4,_posX=.5,_posY=.40,md_bg_color=(1,1,1,.8),text_color=(.3,.3,1,1),font_size=30,duration=.4, t='out_cubic').start(self.ids.passcode_field1)
            Animation(_sizeX=.3,_sizeY=.15,_posX=.8,_posY=.05,md_bg_color=(1,1,1,0),text_color=(0,0,0,.2),font_size=12,duration=.4, t='out_cubic').start(self.ids.passcode_field2)
            self.main_field = 'passcode_field1'
            self.ids.mlabel.color = (.3,.3,1,1)
            self.ids.mlabel.text = 'Please enter 4-digit passcode'
            self.ids.back_button.text = "Clear"
    def enter(self, n):
        if n == '<-':
            exec("self.ids."+self.main_field+".num = "+"self.ids."+self.main_field+".num[:-1]")
            exec("self.ids."+self.main_field+".text = "+"self.ids."+self.main_field+".text[:-1]")
            if self.main_field == 'passcode_field1':
                self.ids.mlabel.color = (.3,.3,1,1)
                self.ids.mlabel.text = 'Please enter 4-digit passcode'
        elif n == 'back':
            if self.status == 'check':
                self.status = 'remove'
                self.ids.backspace_button.disabled = False
            if self.main_field == 'passcode_field2':
                self.enter('clear')
                self.toState(1)
                self.enter('clear')
            elif self.main_field == 'passcode_field1':
                self.toState(1)
                self.enter('clear')
        elif n == 'clear':
            exec("self.ids."+self.main_field+".num = ''")
            exec("self.ids."+self.main_field+".text = ''")
        else:
            if len(self.ids.passcode_field2.num) < 4:
                if self.main_field == 'passcode_field1' and len(self.ids.passcode_field1.num) >= 4: pass
                else:
                    exec("self.ids."+self.main_field+".num += n")
                    exec("self.ids."+self.main_field+".text += '*'")
                if self.main_field == 'passcode_field1':
                    if len(self.ids.passcode_field1.num) == 4:
                        XFaceDAO.localDAO.cursor.execute('select PASSWORD from EMPLOYEE')
                        result = XFaceDAO.localDAO.cursor.fetchall()
                        self.plist = [row[0] for row in result]
                        if self.ids.passcode_field1.num [:4] in self.plist:
                            self.ids.mlabel.color = (1,0,0,1)
                            self.ids.mlabel.text = 'Passcode already exists!'
                        else:
                            self.toState(2)

                    else:
                        self.ids.mlabel.color = (.3,.3,1,1)
                        self.ids.mlabel.text = 'Please enter 4-digit passcode'
                else:
                    if len(self.ids.passcode_field2.num) >= 4:
                        if self.ids.passcode_field1.num != self.ids.passcode_field2.num:
                            self.ids.mlabel.color = (1,0,0,1)
                            self.ids.mlabel.text = 'Passcode not matched!'
                        else:
                            self.status = 'check'
                            self.ids.backspace_button.disabled = True
                            self.ids.mlabel.color = (.1,.8,.2,1)
                            self.ids.mlabel.text = 'Passcode OK!'
                    else:
                        self.ids.mlabel.color = (.3,.3,1,1)
                        self.ids.mlabel.text = 'Please enter confirm passcode'
class RegisterScreen3(Screen):
    try:
        def on_pre_leave(self):
            if self.status != 'check':
                #self.ids.photo_switch.active = False
                self.children[0].children[0].children[4].active = False  #yamaji 11.1
    
    except Exception as e:
        print(e)

    def photoSwitchOn(self, is_active):
        self.take=0
        if is_active:
            Animation(opacity=1, t='in_cubic', duration=0.4).start(self.ids.register_camera)
            Animation(opacity=1, t='in_cubic', duration=0.4).start(self.ids.register_camera_label)
            Animation(_x=.5, _y=.1, t='in_out_cubic', duration=0.4).start(self.ids.photo_switch) #2023/11/7 fujiwara _x=.7, _y=.82 -> _x=.5, _y=.1
            Animation(_x=.81, _y=.15, t='in_out_cubic', duration=0.4).start(self.ids.photo_switch_label) #2023/11/7 fujiwara _x=.76, _y=.82 -> _x=.81, _y=.15
            self.add_camera()
            if int(camera_processing.value) <= -10:                                                         #2023/11/7 fujiwara hituyou?
               Animation(opacity=1, t='in_cubic', duration=0.2).start(self.ids.retake_button)               #2023/11/7 fujiwara hituyou?
        else:    
            if CAMERA:
                Animation(opacity=0, t='out_cubic', duration=0.4).start(self.ids.register_camera)
                Animation(opacity=0, t='out_cubic', duration=0.4).start(self.ids.register_camera_label)
                Animation(_x=.5, _y=.5, t='in_out_cubic', duration=0.4).start(self.ids.photo_switch)
                Animation(_x=.81, _y=.55, t='in_out_cubic', duration=0.4).start(self.ids.photo_switch_label)
                self.remove_camera(reset=False)
                if self.ids.retake_button.opacity == 1:
                   self.ids.retake_button.opacity = 0
                self.status = 'alert'
                print("fujiwara_facedirection44")
    
    def add_camera(self):
        if not ps.CAMERA_FLAG.is_set():
            ps.CAMERA_FLAG.set()
            camera_temp_no.value = 0
            camera_pool_valid.value = 1
            self.ref = Clock.schedule_interval(self.refresh, 0.11)
            self.upd = Clock.schedule_interval(self.process, 0.1)

    def remove_camera(self, reset=True):
        if ps.CAMERA_FLAG.is_set():
            ps.CAMERA_FLAG.clear()
            #self.ref = Clock.schedule_interval(self.refresh, 0.11)           #2023/11/2 fujiwara comment out
            #self.upd = Clock.schedule_interval(self.process, 0.1)            #2023/11/2 fujiwara comment out
            Clock.unschedule(self.ref)
            Clock.unschedule(self.upd)
            ps.clear()
            camera_pool_valid.value = 1
        if reset:
            camera_processing.value = '0'

    def refresh(self, _):
        frame = ps.read()
        if not frame is None:
            value = camera_temp_no.value
            if value < 2: value += 1
            else: value = 1
            camera_temp_no.value = value
            #value=self.take  #yamaji 10.20
            imgname = 'temp_' + str(value) + '.png'
            new_frame = cv2.resize(frame, (400, 250)) #(width,height)   Korn 11.30 add
            frip_image = cv2.flip(new_frame,1) #korn 12.7 add
            cv2.imwrite('assets/'+ imgname, frip_image) #korn 12.7 frame -> frip_image
            self.ids.register_camera.source = 'assets/'+ imgname
            self.ids.register_camera.reload()

    def process(self, _):
        if camera_temp_no.value == 0:
            return
        
        # directions_list=['Please face forward.','Please turn to the right.','Please look up.','Please turn the left.','Please look down.']
        # i=self.take
        # if camera_processing.value == '0':
        #     self.ids.register_camera_label.color = (.3,.3,1,1)
        #     #self.ids.register_camera_label.text = 'Finding a face...\n{}'.format(directions_list[0])refresh
        #     self.ids.register_camera_label.text = f'{directions_list[i]}\nFinding a face...'
        #     self.status = 'remove'
        # elif camera_processing.value == '-1':
        #     self.ids.register_camera_label.color = (.3,.3,1,1)
        #     self.ids.register_camera_label.text = f'{directions_list[i]}\nDo not move.. 3'
        # elif camera_processing.value == '-3':
        #     self.ids.register_camera_label.color = (.3,.3,1,1)
        #     self.ids.register_camera_label.text = f'{directions_list[i]}\nDo not move.. 2'
        # elif camera_processing.value == '-5':
        #     self.ids.register_camera_label.color = (.3,.3,1,1)
        #     self.ids.register_camera_label.text = f'{directions_list[i]}\nDo not move.. 1'
        # elif camera_processing.value == '-7':
        #     self.ids.register_camera_label.color = (.1,.8,.2,1)
        #     self.ids.register_camera_label.text = 'Photo captured successfully!'
        #     self.remove_camera(reset=False)
        #     self.status = 'check'
        #     shutil.copy('assets/temp_{}.png'.format(self.take), 'assets/temp.png')
        #     Animation(opacity=1, t='in_cubic', duration=0.2).start(self.ids.retake_button)
        #     if i<4: Animation(opacity=1, t='in_cubic', duration=0.2).start(self.ids.next_button)
        if camera_processing.value == '0':
            self.ids.register_camera_label.color = (.3,.3,1,1)
            self.ids.register_camera_label.text = 'Finding a face...'
            self.status = 'remove'
        elif camera_processing.value == '-1':
            self.ids.register_camera_label.color = (.3,.3,1,1)
            self.ids.register_camera_label.text = 'Do not move.. 3'
        elif camera_processing.value == '-3':
            self.ids.register_camera_label.color = (.3,.3,1,1)
            self.ids.register_camera_label.text = 'Do not move.. 2'
        elif camera_processing.value == '-5':
            self.ids.register_camera_label.color = (.3,.3,1,1)
            self.ids.register_camera_label.text = 'Do not move.. 1'
        elif camera_processing.value == '-7':
            self.ids.register_camera_label.color = (.1,.8,.2,1)
            self.ids.register_camera_label.text = 'Photo captured successfully!'
            self.remove_camera(reset=False)
            self.status = 'check'
            self.ids.photo_switch.disabled = True                                            #2023/11/7 fujiwara tuika
            self.ids.photo_switch_label.text = "Photo captured successfully!"                #2023/11/7 fujiwara tuika
            shutil.copy('assets/temp_{}.png'.format(camera_temp_no.value), 'assets/temp.png')
            Animation(opacity=1, t='in_cubic', duration=0.2).start(self.ids.retake_button)

        
        if camera_pool_valid.value == 1 and int(camera_processing.value) > -7:
            camera_pool_valid.value = 0
            for i in range(len(sm.process_pool)-5):
                sm.process_pool[0].join()
                sm.process_pool.pop(0)

            p = Process(target=self.processCamera)
            sm.process_pool.append(p)
            p.start()
            print("fujiwara_camera_activecheck")
    
    def processCamera(self):
        face_locations = ''
        mp_face_mesh = mp.solutions.face_mesh  #yamaji 12.5 add
        face_mesh = mp_face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5) #yamaji 12.5
        try:
            value = camera_temp_no.value
            #value=self.take
            imgname = 'temp_' + str(value) + '.png'
            frame = cv2.imread('assets/'+ imgname)
            if not frame is None:
                bgr_frame = frame[:, :, ::-1]
                face_locations = face_recognition.face_locations(bgr_frame)
        except Exception:
            XFaceLogging.system("1273", traceback.format_exc())
            camera_pool_valid.value = 1
            return
        if len(face_locations) > 0:
            try:
                #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)   #yamaji 12.6 comment out below 3 lines
                #gray_face = gray[int(face_locations[0][0]):int(face_locations[0][2]),int(face_locations[0][3]):int(face_locations[0][1])]
                #mean = np.mean(gray_face)
                # if mean < 120 :
                #     if mean < 80 :camera_set.value = 3
                #     else: camera_set.value = 2
                # elif mean > 135 : camera_set.value = -2

                ######################################## yamaji 12.5 from     use mediapipe
                # Flip the image horizontally for a later selfie-view display
                # Also convert the color space from BGR to RGB
                image = cv2.cvtColor(cv2.flip(frame, 1), cv2.COLOR_BGR2RGB)

                # To improve performance
                image.flags.writeable = False
                
                # Get the result
                results = face_mesh.process(image)
                
                # To improve performance
                image.flags.writeable = True
                
                # Convert the color space from RGB to BGR
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

                img_h, img_w, img_c = image.shape
                face_3d = []
                face_2d = []

                if results.multi_face_landmarks:
                    for face_landmarks in results.multi_face_landmarks:
                        for idx, lm in enumerate(face_landmarks.landmark):
                            if idx == 33 or idx == 263 or idx == 1 or idx == 61 or idx == 291 or idx == 199:
                                if idx == 1:
                                    nose_2d = (lm.x * img_w, lm.y * img_h)
                                    nose_3d = (lm.x * img_w, lm.y * img_h, lm.z * 3000)

                                x, y = int(lm.x * img_w), int(lm.y * img_h)

                                # Get the 2D Coordinates
                                face_2d.append([x, y])

                                # Get the 3D Coordinates
                                face_3d.append([x, y, lm.z])       
                        
                        # Convert it to the NumPy array
                        face_2d = np.array(face_2d, dtype=np.float64)
                        face_3d = np.array(face_3d, dtype=np.float64)

                        # The camera matrix
                        focal_length = 1 * img_w

                        cam_matrix = np.array([ [focal_length, 0, img_h / 2],
                                                [0, focal_length, img_w / 2],
                                                [0, 0, 1]])

                        # The distortion parameters
                        dist_matrix = np.zeros((4, 1), dtype=np.float64)

                        # Solve PnP
                        success, rot_vec, trans_vec = cv2.solvePnP(face_3d, face_2d, cam_matrix, dist_matrix)

                        # Get rotational matrix
                        rmat, jac = cv2.Rodrigues(rot_vec)

                        # Get angles
                        angles, mtxR, mtxQ, Qx, Qy, Qz = cv2.RQDecomp3x3(rmat)

                        # Get the y rotation degree
                        x = angles[0] * 360
                        y = angles[1] * 360
                        z = angles[2] * 360

                        # See where the user's head tilting
                        if y < -10:
                            self.face_direction = "Looking Right"
                        elif y > 10:
                            self.face_direction = "Looking Left"
                        elif x < -5:
                            self.face_direction = "Looking Down"
                        elif x > 15:
                            self.face_direction = "Looking Up"
                        else:
                            self.face_direction = "Forward"
                        print(self.face_direction)

                ######################################## yamaji 12.5 to
            except Exception: pass
            camera_processing.value = str(int(camera_processing.value)-1)
        else:
            camera_processing.value = '0'
            if np.all(frame==0):
                print("frame==0")#yamaji 10.19
                self.remove_camera()
            
            # self.add_camera()
        camera_pool_valid.value = 1    
    
    def retake(self):
        camera_processing.value = '0'
        self.ids.next_button.opacity = 0
        self.ids.photo_switch.disabled = False                                            #2023/11/7 fujiwara tuika
        self.ids.photo_switch_label.text = "Enable Face-Recognition?"                     #2023/11/7 fujiwara tuika
        self.remove_camera(reset=False)
        self.add_camera()
        print("retake")

    def next(self):
        camera_processing.value = '0'
        self.ids.retake_button.opacity = 0
        self.take+=1
        self.remove_camera(reset=False)
        self.add_camera()
        print("next")
class RegisterScreen4(Screen): 
                # if mean < 120 :
                #     if mean < 80 :camera_set.value = 3
                #     else: camera_set.value = 2
                # elif mean > 135 : camera_set.value = -2
    def on_enter(self):
        if self.status == 'check':
            self.fp_state = 0
            self.chk = Clock.schedule_interval(self.check_finger_press, 0.25)    #2023/11/14 fujiwara comment out -> 2023/11/24 comment out kaijo

    def on_pre_leave(self):
        if self.status != 'check':
            #self.ids.fingerprint_switch.active = False
            self.finger_eigens = []  #2023/11/24 fujiwara tuika
            self.fp_state = 0  #2023/11/24 fujiwara tuika
            self.ids.register_fingerprint_label.text = "Waiting for fingerprint..."  #2023/11/24 fujiwara tuika
            self.children[0].children[0].children[4].active = False  #yamaji 11.1
        if FINGERPRINT:
            XFaceGPIOControllers.GPIO.output(XFaceGPIOControllers.Finger_RST_Pin, XFaceGPIOControllers.GPIO.LOW)
            try:
                Clock.unschedule(self.chk)
            except Exception: pass

    def fingerprintSwitchOn(self, is_active):
        if is_active:
            Animation(opacity=1, t='in_cubic', duration=0.4).start(self.ids.fingerprint_img)
            Animation(opacity=1, t='in_cubic', duration=0.4).start(self.ids.register_fingerprint_label)
            Animation(opacity=1, t='in_cubic', duration=0.4).start(self.ids.register_fingerprint_label2)
            Animation(_x=.65, _y=.82, t='in_out_cubic', duration=0.4).start(self.ids.fingerprint_switch)
            Animation(_x=.76, _y=.82, t='in_out_cubic', duration=0.4).start(self.ids.fingerprint_switch_label)
            self.fp_state = 0
            self.chk = Clock.schedule_interval(self.check_finger_press, 0.25)
            
            if len(self.finger_eigens) == 0:
                self.status = 'alert'  #2023/11/24 fujiwara remove -> alert
            else:
                Animation(opacity=1, t='in_cubic', duration=0.4).start(self.ids.fingerprint_reset_button)
                self.status = 'check'
        else:
            if FINGERPRINT:
                Animation(opacity=0, t='out_cubic', duration=0.4).start(self.ids.fingerprint_img)
                Animation(opacity=0, t='out_cubic', duration=0.4).start(self.ids.fingerprint_reset_button)
                Animation(opacity=0, t='out_cubic', duration=0.4).start(self.ids.register_fingerprint_label)
                Animation(opacity=0, t='out_cubic', duration=0.4).start(self.ids.register_fingerprint_label2)
                Animation(_x=.5, _y=.5, t='in_out_cubic', duration=0.4).start(self.ids.fingerprint_switch)
                Animation(_x=.86, _y=.55, t='in_out_cubic', duration=0.4).start(self.ids.fingerprint_switch_label)
                self.status = 'alert'
                Clock.unschedule(self.chk)
                XFaceGPIOControllers.GPIO.output(XFaceGPIOControllers.Finger_RST_Pin, XFaceGPIOControllers.GPIO.LOW)

    def check_finger_press(self, _):
        if XFaceCapacitiveFP.rLock.acquire() == True:
            if self.fp_state == 0:  # wake up
                if XFaceGPIOControllers.GPIO.input(XFaceGPIOControllers.Finger_WAKE_Pin):   # If you press your finger
                    time.sleep(0.01)
                    if XFaceGPIOControllers.GPIO.input(XFaceGPIOControllers.Finger_WAKE_Pin):
                        XFaceGPIOControllers.GPIO.output(XFaceGPIOControllers.Finger_RST_Pin, XFaceGPIOControllers.GPIO.HIGH)   # Pull up the RST to start the module and start matching the fingers
                        self.fp_state = 1
                        
            elif self.fp_state == 1:
                if len(self.finger_eigens) >= 3: #2023/11/24 fujiwara 10->3
                    self.status = 'check'  #2023/11/24 fujiwara tuika
                    self.ids.register_fingerprint_label.text = "Three successful fingerprint acquisitions"  #2023/11/24 fujiwara tuika
                    self.ids.fingerprint_switch.disabled = True  #2023/11/24 fujiwara tuika
                    return
                print ("Waiting Finger......Please try to place the center of the fingerprint flat to sensor !")
                r = XFaceCapacitiveFP.ComputeEigenvalues()
                if r[0] == XFaceCapacitiveFP.ACK_SUCCESS:
                    sm.play('input')
                    print ("ComputeEigenvalues successfully")
                    self.finger_eigens.append(r[1])
                    self.ids.register_fingerprint_label.text = "Fingerprint on hold: " + str(len(self.finger_eigens))
                    if len(self.finger_eigens) == 1:
                        Animation(opacity=1, t='in_cubic', duration=0.4).start(self.ids.fingerprint_reset_button)
                    #self.status = 'check'  #2023/11/24 fujiwara comment out
                elif r[0] == XFaceCapacitiveFP.ACK_TIMEOUT:
                    print ("Failed: Time out !")
                    toast("Press the finger properly")
                XFaceGPIOControllers.GPIO.output(XFaceGPIOControllers.Finger_RST_Pin, XFaceGPIOControllers.GPIO.LOW)
                self.fp_state = 2

            elif self.fp_state > 5:
                XFaceGPIOControllers.GPIO.output(XFaceGPIOControllers.Finger_RST_Pin, XFaceGPIOControllers.GPIO.LOW)
                self.fp_state = 0
            else:
                self.fp_state += 1
            XFaceCapacitiveFP.rLock.release()

    def clear_press(self):
        self.finger_eigens = []
        self.fp_state = 0
        XFaceGPIOControllers.GPIO.output(XFaceGPIOControllers.Finger_RST_Pin, XFaceGPIOControllers.GPIO.LOW)
        self.ids.register_fingerprint_label.text = "Waiting for fingerprint..."
        self.status = 'alert'  #2023/11/24 fujiwara remove -> alert
        self.ids.fingerprint_switch.disabled = False  #2023/11/24 fujiwara tuika
        Animation(opacity=0, t='out_cubic', duration=0.4).start(self.ids.fingerprint_reset_button)
class RegisterScreen5(Screen):
    def on_pre_enter(self):
        self.ids.c1.source = 'assets/' + sm.get_screen('r1').status + '.png'
        self.ids.c2.source = 'assets/' + sm.get_screen('r2').status + '.png'
        self.ids.c3.source = 'assets/' + sm.get_screen('r3').status + '.png'
        self.ids.c4.source = 'assets/' + sm.get_screen('r4').status + '.png'

        self.ids.c1_label.text = 'Name: ' + sm.get_screen('r1').ids.f1_name.text + '\n' + sm.get_screen('r1').ids.f1_name_label.text if \
                            self.ids.c1.source == 'assets/check.png' \
                            else 'Name is required!'

    def save(self):
        name = sm.get_screen('r1').ids.f1_name.text
        password = sm.get_screen('r2').ids.passcode_field2.num
        print(password)
        def _confirm(self):#yamaji(text, _)
            # if text == 'Cancel':
            #     return
            #if text == 'Yes':
            self.dialog.dismiss()
            sm.show_loading(self)
            def _apply(self, _):
                sm.current = 'admin'
                XFaceGPIOControllers.GPIO.output(XFaceGPIOControllers.Finger_RST_Pin, XFaceGPIOControllers.GPIO.HIGH)
                time.sleep(0.25)
                if self.ids.c3.source == 'assets/check.png':
                    pic_path = 'pic/'+name
                    if not os.path.exists(pic_path):
                        os.makedirs(pic_path)
                        shutil.copy('assets/temp.png', '{}/{}.png'.format(pic_path, name))
                        # for i in range(5):
                        #     filename ='assets/temp_{}.png'.format(i)
                        #     picname = name
                        #     if i>0: picname=name+'_{}'.format(i)
                        #     shutil.copy(filename, '{}/{}.png'.format(pic_path, picname))
                if FINGERPRINT:
                    XFaceDAO.localDAO.insertFingerprint(name, sm.get_screen('r4').finger_eigens)
                XFaceDAO.localDAO.insertEmployee(name, password, 'department', 'role')
                if SHAREDVARS['SERVER']:
                    XFaceDAO.serverDAO.insertEmployee(name, password, 'department', 'role')

                toast("Insert employee successfully!")
                self.loading.dismiss()
            Clock.schedule_once(partial(_apply,self))

        exists = None
        try:
            XFaceDAO.localDAO.cursor.execute("select * from EMPLOYEE where NAME = '{}'".format(name))   #2023/11/1 fujiwara ,format -> .format
            exists = XFaceDAO.localDAO.cursor.fetchone()
        except Exception: pass
        if exists is None:#yamaji from
            # self.dialog = MDDialog(
            #         title="Confirmation",
            #         size_hint=(0.8, 0.3),
            #         text_button_ok="Yes",
            #         text="Do you want to insert\nName: " + name + " \nto the system?",
            #         text_button_cancel="Cancel",
            #         events_callback=_confirm,
            #     )
            # self.dialog.open()
            dialog=BoxLayout(orientation='vertical',)
            #label=MDLabel(text="Do you want to insert\nName: " + name + " \nto the system?",font_size=18,pos_hint={"center_x":0.5, "center_y":0.5},)
            label=MDLabel(text="Do you want to insert\nName: " + name + " \nto the system?",font_size=18,pos_hint={"center_x":0.5, "center_y":0.5},theme_text_color="Custom",text_color=(1,1,1,1)) #korn 11.1
            buttun=BoxLayout(orientation='horizontal',spacing=10)
            space=BoxLayout(size_hint=(0.4,0.01))
            yes_button=MDFlatButton(text='Yes',on_release=lambda _:  _confirm(self),md_bg_color=(0.7,0.7,0.7,1),)
            cancel_button=MDFlatButton(text='Cancel',on_release=lambda _: self.dialog.dismiss(),md_bg_color=(0.7,0.7,0.7,1))
            buttun.add_widget(space)
            buttun.add_widget(yes_button)
            buttun.add_widget(cancel_button)
            dialog.add_widget(label)
            dialog.add_widget(buttun)
            self.dialog = Popup(
                title="Confirmation",
                size_hint=(0.8, 0.3),
                content = dialog,
                )
            self.dialog.open()#yamaji to
        

        else:
            toast("This name already exist in database, please contact adminstrator.")

class SaveMenu(MDBoxLayout):
    pass

from kivy.core.window import Window
from kivy.uix.anchorlayout import AnchorLayout
from kivymd.uix.menu import MDDropdownMenu
from kivy.uix.widget import Widget
class CardPostImage(BoxLayout):
    source = StringProperty()
    text_post = StringProperty()
    tile_text = StringProperty("Title")
    tile_font_style = StringProperty("H5")
    tile_text_color = ListProperty([1, 1, 1, 1])
    callback = ObjectProperty(lambda *x: None)
    card_size = ListProperty((0, 0))
class NandeCardPost(BoxLayout):
    name_data = StringProperty("Name Author\nDate and time")
    ndpassword = StringProperty("-1")
    text_post = StringProperty("Your text post...")
    path_to_avatar = StringProperty("data/logo/kivy-icon-512.png")
    card_size = [Window.width - 10, dp(90)]
    size_hint = None,None
    source = StringProperty()
    tile_text = StringProperty("Title")
    tile_font_style = StringProperty("H5")
    tile_text_color = ListProperty([1, 1, 1, 1])
    buttons = ListProperty()#"""A list of icons for buttons that will be used under the text of the post when "with_image" is True"""
    right_menu = ListProperty()#"""If the list is not empty a button will be added to display the menu list"""
    likes_stars = BooleanProperty(False)#"""If True, stars will be added to the card for evaluation"""
    callback = ObjectProperty(lambda *x: None)#"""User function"""
    swipe = BooleanProperty(False)#"""Whether to apply to the card the function of a swap"""
    with_image = BooleanProperty(False)#"""If True, we use a post with an image"""
    _list_instance_likes_stars = ListProperty()
    _card_shifted = False
    _shift_x = 10

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.card_shifted = None

    def on_touch_move(self, touch):
        pass

    def on_touch_down(self, touch):
        if self.swipe and not self.card_shifted and self.collide_point(*touch.pos):
            Clock.schedule_once(self.shift_post_left, 0.1)
        
        if self.swipe and self.card_shifted:
            Clock.schedule_once(self.shift_post_right, 0.1)
        return super().on_touch_down(touch)

    def shift_post_left(self, interval=0.1):
        def on_anim_complete(*args):
            self._card_shifted = True
            self.card_shifted = self
            self.ids.delet_post_button.disabled = False
        Animation(x=-dp(90), d=0.1, t="in_out_cubic").start(self.ids.root_box)
        if self.likes_stars:
            Animation(x=-dp(90), d=0.1, t="in_out_cubic").start(
                self.children[0]
            )
        anim = Animation(opacity=1, d=0.5, t="in_out_cubic")
        anim.bind(on_complete=on_anim_complete)
        anim.start(self.ids.box_delete_post_button)

    def shift_post_right(self, interval=0.1):
        def on_anim_complete(*args):
            self._card_shifted = False
            self.card_shifted = None
            self.ids.delet_post_button.disabled = True

        Animation(x=self._shift_x, d=0.1, t="in_out_cubic").start(
            self.ids.root_box
        )
        if self.likes_stars:
            Animation(x=self._shift_x, d=0.3, t="in_out_cubic").start(
                self.children[0]
            )
        anim = Animation(opacity=0, d=0.05, t="in_out_cubic")
        anim.bind(on_complete=on_anim_complete)
        anim.start(self.ids.box_delete_post_button)

class DeleteEmployeeScreen(Screen):
    cards_created = False
    card_post_list = []

    def searchChangeColor(self):
        if self.ids.search_box.current_color[0]==0:
            Animation(current_color=(.2,.4,.9,1),duration=.25, t='in_cubic').start(self.ids.search_box)
        else:
            Animation(current_color=(0,0,0,.1),duration=.25, t='out_cubic').start(self.ids.search_box)

    def queryName(self, text):
        for i in self.ids.grid_card.children:
            if text != i.name_data[:len(text)].upper():
                i.size[1] =0
                i.ids.sep.height = 0
                i.opacity = 0
            else:
                i.size[1] = dp(90)
                i.ids.sep.height = dp(1)
                i.opacity = 1
    
    def on_leave(self):
        self.ids.grid_card.clear_widgets()
        self.ids.search_field.text = ""
            
    def on_enter(self):
        def callback(instance, value):
            def animation_complete(self, self2):
                toast(f"Delete Employee {instance.name_data}\nSuccessfully")
                instance.parent.remove_widget(instance)

            def cDelete(self):#(text, widget): yamaji from
                # if text == 'Cancel':
                #     return
                # elif text == 'Yes':
                self.dialog.dismiss()#yamaji to
                animation1 = Animation(opacity=0, height=0, left_font_size=dp(0), right_font_size=dp(0), d=0.1)
                animation1.start(instance)
                animation1.bind(on_complete=animation_complete)

                name = instance.name_data

                XFaceDAO.localDAO.deleteEmployee(name)
                if SHAREDVARS['SERVER']:
                    XFaceDAO.serverDAO.deleteEmployee(name)

                XFaceEncodingData.PickleData.deleteFace(name)
                return

            if value and isinstance(value, int):
                toast(f"Set like in {value} stars")
            elif value and isinstance(value, str):
                toast(f"Repost with {value}")
            elif value and isinstance(value, list):
                toast(value[1])
            else:#yamaji from
                # self.dialog = MDDialog(
                #     title="Confirmation",
                #     size_hint=(0.8, 0.4),
                #     text_button_ok="Yes",
                #     text="Do you want to delete " + instance.name_data + " from system?",
                #     text_button_cancel="Cancel",
                #     events_callback=cDelete,
                #     #radius= "",
                # )
                dialog=BoxLayout(orientation='vertical',)
                #label=MDLabel(text="Do you want to delete " + instance.name_data + " from system?",font_size=18,pos_hint={"center_x":0.5, "center_y":0.5},)
                label=MDLabel(text="Do you want to delete " + instance.name_data + " from system?",font_size=18,pos_hint={"center_x":0.5, "center_y":0.5},theme_text_color="Custom",text_color=(1,1,1,1)) #korn 11.1
                buttun=BoxLayout(orientation='horizontal',spacing=10)
                space=BoxLayout(size_hint=(0.4,0.01))
                yes_button=MDFlatButton(text='Yes',on_release=lambda _:  cDelete(self),md_bg_color=(0.7,0.7,0.7,1),)
                cancel_button=MDFlatButton(text='Cancel',on_release=lambda _: self.dialog.dismiss(),md_bg_color=(0.7,0.7,0.7,1))
                buttun.add_widget(space)
                buttun.add_widget(yes_button)
                buttun.add_widget(cancel_button)
                dialog.add_widget(label)
                dialog.add_widget(buttun)
                self.dialog = Popup(
                    title="Confirmation",
                    size_hint=(0.8, 0.3),
                    content = dialog,
                    )#yamaji to
                self.dialog.open()
        instance_grid_card = self.ids.grid_card

        XFaceDAO.localDAO.cursor.execute('select NAME from EMPLOYEE order by NAME')
        result = XFaceDAO.localDAO.cursor.fetchall()

        if not result:
            toast("No employee found")
        else:
            for record in result:
                im = 'pic/{}/{}.png'.format(record[0],record[0])
                if not os.path.exists(im):
                    im = 'assets/temp_profile.png'
                card_post = NandeCardPost(   
                                    path_to_avatar=im, 
                                    name_data=record[0],
                                    text_post="Tap to delete",
                                    swipe=True,
                                    callback=callback)
                #icon=IconLeftWidget(icon=im, size_hint_x=None, width=self.height)
                #card_post.add_widget(icon)
                card_post.size=self.ids.scroll.width,70
                self.card_post_list.append(card_post)
                instance_grid_card.add_widget(card_post)

class BoxContentForBottomSheetCustomScreenList(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        time_zone_dict = {"-12:00":("International Date Line West", "Etc/GMT+12"),
                        "-11:00":("Midway Island, Samoa", "Etc/GMT+11"),
                        "-10:00":("Hawaii", "Etc/GMT+10"),
                        "-9:30":("Marquesas", "Pacific/Marquesas"),
                        "-9:00":("Alaska", "Etc/GMT+9"),
                        "-8:00":("Pacific Time (US and Canada); Tijuana", "Etc/GMT+8"),
                        "-7:00":("Mountain Time (US and Canada), Chihuahua, La Paz, Mazatlan, Arizona", "Etc/GMT+7"),
                        "-6:00":("Central Time (US and Canada), Saskatchewan, Guadalajara, Mexico City, Monterrey", "Etc/GMT+6"),
                        "-5:00":("Eastern Time (US and Canada), Indiana (East), Bogota, Lima, Quito", "Etc/GMT+5"),
                        "-4:00":("Atlantic Time (Canada),  Georgetown, La Paz, San Juan, Santiago", "Etc/GMT+4"),
                        "-3:30":("Newfoundland, St_Johns", "Canada/Newfoundland"),
                        "-3:00":("Brasilia, Georgetown", "Etc/GMT+3"),
                        "-2:00":("Mid-Atlantic", "Etc/GMT+2"),
                        "-1:00":("Azores, Cape Verde Islands", "Etc/GMT+1"),
                        "0:00":("Dublin, Edinburgh, Lisbon, London, Monrovia, Reykjavik", "GMT"),
                        "+1:00":("Belgrade, Bratislava, Budapest, Ljubljana, Prague, Sarajevo, Skopje, Warsaw, Zagreb, Brussels, Copenhagen, Madrid, Paris, Amsterdam, Berlin, Bern, Rome, Stockholm, Vienna", "Etc/GMT-1"),
                        "+2:00":("Minsk, Cairo, Helsinki, Kiev, Riga, Sofia, Tallinn, Vilnius", "Etc/GMT-2"),
                        "+3:00":("Moscow, St. Petersburg, Volgograd", "Etc/GMT-3"),
                        "+3:30":("Tehran", "Asia/Tehran"),
                        "+4:00":("Abu Dhabi, Muscat, Baku, Tbilisi, Yerevan", "Etc/GMT-4"),
                        "+4:30":("Kabul", "Asia/Kabul"),
                        "+5:00":("Ekaterinburg, Tashkent", "Etc/GMT-5"),
                        "+5:30":("Chennai, Kolkata, Mumbai, New Delhi", "Asia/Colombo"),
                        "+5:45":("Kathmandu", "Asia/Kathmandu"),
                        "+6:00":("Astana, Dhaka, Sri Jayawardenepura, Almaty, Novosibirsk", "Etc/GMT-6"),
                        "+6:30":("Yangon (Rangoon)", "Asia/Yangon"),
                        "+7:00":("Bangkok, Hanoi, Jakarta, Krasnoyarsk", "Etc/GMT-7"),
                        "+8:00":("Beijing, Chongqing, Hong Kong, Kuala Lumpur, Singapore, Taipei", "Etc/GMT-8"),
                        "+8:45":("Eucla", "Australia/Eucla"),
                        "+9:00":("Seoul, Osaka, Sapporo, Tokyo, Yakutsk", "Etc/GMT-9"),
                        "+9:30":("Darwin, Adelaide", "Australia/Darwin"),
                        "+10:00":("Canberra, Melbourne, Sydney, Brisbane, Hobart, Guam", "Etc/GMT-10"),
                        "+10:30":("Lord Howe Island", "Australia/LHI"),
                        "+11:00":("Magadan, Solomon Islands, New Caledonia", "Etc/GMT-11"),
                        "+12:00":("Fiji, Kamchatka, Marshall Is.", "Etc/GMT-12"),
                        "+12:45":("Chatham",  "Pacific/Chatham"),
                        "+13:00":("Nuku'alofa", "Etc/GMT-13"),
                        "+14:00":("Kiritimati", "Etc/GMT-14")
                        }
        for i in time_zone_dict.keys():
            a = ContentForBottomSheetCustomScreenList()
            a.text = "GMT"+i
            a.secondary_text = time_zone_dict[i][0]
            a.gmt_offset = i
            a.gmt_code = time_zone_dict[i][1]
            self.ids.box.add_widget(a)
class ContentForBottomSheetCustomScreenList(TwoLineIconListItem):
    def callback_for_menu_items(self,content):   #2023/10/24 fujiwara tuika (self) -> (self,content)
        try:
            sm.get_screen("settings").bottom_sheet.dismiss()
            #sm.get_screen("settings").ids.dtex.content.setTimeZone(self.gmt_offset, self.gmt_code, self.secondary_text)   #2023/10/23 fujiwara comment out
            datetimecontent = DateTimeContent()                                                                            #2023/10/23 fujiwara tuika
            datetimecontent.setTimeZone(content.gmt_offset, content.gmt_code, content.secondary_text)                      #2023/10/23 fujiwara tuika
        except Exception:
            XFaceLogging.system("1454", traceback.format_exc())
class DateTimeContent(MDBoxLayout):
    try:
        def __init__(self, **kwargs):                              #2023/10/19 fujiwara tuika
            super().__init__(**kwargs)
            Clock.schedule_once(self.initailizeDatetime)

        def initailizeDatetime(self, dt):
            d = datetime.now()
            self.ids.set_date.text = d.strftime("%b") + " " + d.strftime("%d") + " " + d.strftime("%Y")
            self.ids.set_clock.text = d.strftime("%H") + ":" + d.strftime("%M") + ":" + d.strftime("%S")

            s = XFaceDAO.localDAO.getSystemValue('TIME_ZONE')
            self.ids.set_time_zone.text = s

        def pressSw(self, sid, state):
            if sid == 'global' and state or sid == 'local' and not state:
                toast("Using global time")
                if not self.ids.global_time_switch.active:
                    self.ids.global_time_switch.active = True
                if self.ids.local_time_switch.active:
                    self.ids.local_time_switch.active = False
            elif sid == 'global' and not state or sid == 'local' and state:
                toast("Using local time")
                if self.ids.global_time_switch.active:
                    self.ids.global_time_switch.active = False
                if not self.ids.local_time_switch.active:
                    self.ids.local_time_switch.active = True

        def show_global_time_picker(self):
            custom_screen_for_bottom_sheet = BoxContentForBottomSheetCustomScreenList()
            sm.get_screen("settings").bottom_sheet = MDCustomBottomSheet(
                screen=custom_screen_for_bottom_sheet,
                bg_color=[.95, .95, .95, 1],
                animation=True,
                #radius_from='top',
            )
            sm.get_screen("settings").bottom_sheet.open()

        def setTimeZone(self, gmt_offset, gmt_code, secondary_text):
            s = "GMT"+gmt_offset+" "+secondary_text
            self.ids.set_time_zone.text = s
            
            XFaceDAO.localDAO.setSystemValue('TIME_ZONE', s)

            toast("Please restart XFace to take effect")
            try:
                os.system("sudo timedatectl set-timezone " + gmt_code)
            except Exception:
                XFaceLogging.system("1505", traceback.format_exc())

        def show_example_date_picker(self, *args):
            #MDDatePicker(self.set_previous_date).open()           #2023/10/24 fujiwara comment out
            date_dialog = MDDatePicker()                           #2023/10/24 fujiwara tuika start
            #date_dialog.bind(input_field_cls=self.set_previous_date)
            date_dialog.open()                                     #2023/10/24 fujiwara tuika end

        def show_example_time_picker(self):

            time_dialog = MDTimePicker()
            time_dialog.bind(time=self.get_time_picker_date)
            self.previous_time = datetime.now()
            time_dialog.set_time(self.previous_time)
            time_dialog.open()
            
        def set_previous_date(self, date_obj):
            s = date_obj.strftime("%b") + " " + date_obj.strftime("%d")+ " " + date_obj.strftime("%Y")
            self.ids.set_date.text = s
            self.previous_date = date_obj

            st = date_obj.strftime("%b") + " " + date_obj.strftime("%d") + " " + self.ids.set_clock.text[:-3]
            toast("Time set.\nPlease restart ExFace to take effect")
            try:
                os.system("sudo date -s " + st)
            except Exception:
                XFaceLogging.system("1520", traceback.format_exc())

        def get_time_picker_date(self, instance, time_string):
            self.ids.set_clock.text = str(time_string)
            self.previous_time = time_string
            s = self.ids.set_date.text.split(" ")
            st = s[0] + " " + s[1] + " " + str(time_string)[:5]             #2023/10/25 fujiwara syuusei [:5] -> [:8] -> [:5]
            toast("Time set.\nPlease restart ExFace to take effect")
            """try:                                                         #2023/10/25 fujiwara comment out start
                os.system("sudo date -s " + st)
            except Exception:
                XFaceLogging.system("1531", traceback.format_exc())"""      #2023/10/25 fujiwara comment out end
    except Exception as e:
        print(e)
class DisableEnableContent(MDBoxLayout):
    try:
        """def __init__(self, **kwargs):                                                                 #2023/10/19 fujiwara tuika start
            super().__init__(**kwargs)
            Clock.schedule_once(self.get_camera)
        
        def get_camera(self,dt):
            self.ids.setting_camera_switch.active = bool(XFaceDAO.localDAO.getSystemValue('CAMERA'))    #2023/10/19 fujiwara tuika end"""
        def initailizeDisableEnable(self):
            if CAMERA:
                self.ids.settings_grid.children[1].content.children[1].children[0].children[0].active = True #yamaji 10.30
            else:
                self.ids.settings_grid.children[1].content.children[1].children[0].children[0].active = False #yamaji 10.30
                if not CAMERA_INIT:
                    self.ids.settings_grid.children[1].content.children[1].children[0].children[0].active = True #yamaji 10.30
            if FINGERPRINT:
                self.ids.settings_grid.children[1].content.children[0].children[0].children[0].active = True #yamaji 10.30
            else:
                self.ids.settings_grid.children[1].content.children[0].children[0].children[0].active = False #yamaji 10.30
                if not FINGERPRINT_INIT:
                    self.ids.settings_grid.children[1].content.children[0].children[0].children[0].active = True #yamaji 10.30
        
        def pressSw(self, sid, state):
            global CAMERA
            global FINGERPRINT
            if sid == 'camera':
                if state:
                    if not CAMERA:
                        if CAMERA_INIT:
                            toast("Enable Camera")
                            CAMERA = True
                            XFaceDAO.localDAO.setSystemValue('CAMERA', '1')
                        else:
                            toast("Camera module cannot be enabled.")
                else:
                    if CAMERA:
                        toast("Disable Camera")
                        CAMERA = False
                        XFaceDAO.localDAO.setSystemValue('CAMERA', '0')
            elif sid == 'fingerprint':
                if state:
                    if not FINGERPRINT:
                        if FINGERPRINT_INIT:
                            toast("Enable Fingerprint Scanner")
                            FINGERPRINT = True
                            XFaceDAO.localDAO.setSystemValue('FINGERPRINT', '1')
                        else:
                            toast("Fingerprint module cannot be enabled.")
                else:
                    if FINGERPRINT:
                        toast("Disable Fingerprint Scanner")
                        FINGERPRINT = False
                        XFaceDAO.localDAO.setSystemValue('FINGERPRINT', '0')
    except Exception as e:
        print(e)
#class VolumeContent(BoxLayout): pass
class VolumeContent(BoxLayout):       #2023/10/19 fujiwara tuika start
    try:
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            Clock.schedule_once(self.get_volume)
        
        def get_volume(self,dt):
            self.ids.volume_slider.value = XFaceDAO.localDAO.getSystemValue('SYSTEM_VOLUME')
         
        def set_volume(self):
            volume = int(self.ids.settings_grid.children[0].content.ids.volume_slider.value)  #yamaji 10.30 add
            XFaceDAO.localDAO.setSystemValue('SYSTEM_VOLUME', str(volume))
            sm.volume = volume
    except Exception as e:
        print(e)                      #2023/10/19 fujiwara tuika end

class SettingsScreen(Screen):
    try:
        def on_enter(self):

            #self.ids.dtex.content.initailizeDatetime()
            #self.initailizeDatetime()
            self.ids.settings_grid.add_widget(
                MDExpansionPanel(
                    icon=f"assets/mono_clock.png",
                    content=DateTimeContent(),
                    panel_cls=MDExpansionPanelOneLine(text="Time",id="dtex"),
                )
            )
            self.ids.settings_grid.add_widget(
                MDExpansionPanel(
                    icon=f"assets/disabled.png",
                    content=DisableEnableContent(),
                    panel_cls=MDExpansionPanelOneLine(text="Disable/Enable module"),
                )
            )
            self.ids.settings_grid.add_widget(
                MDExpansionPanel(
                    icon=f"assets/speaker.png",
                    content=VolumeContent(),
                    panel_cls=MDExpansionPanelOneLine(text="Speaker Volume"),
                )
            )
            DisableEnableContent.initailizeDisableEnable(self)  #yamaji 10.30
                    
        def on_leave(self):
            #volume = int(self.ids.voex.content.ids.volume_slider.value)
            #XFaceDAO.localDAO.setSystemValue('SYSTEM_VOLUME', str(volume))
            #sm.volume = volume
            VolumeContent.set_volume(self)  #yamaji 10.30
            self.ids.settings_grid.clear_widgets() 

    except Exception as e:
        print(e)

class ExportScreen(Screen):
    def on_enter(self):
        self.usb_dir = ""
        self.check = Clock.schedule_interval(self.checkUSB, 0.5)
        toast("Finding USB")
    def on_leave(self):
        Clock.unschedule(self.check)
        self.ids.export_l1.color = (0,0,1,1)
        self.ids.export_l2.color = (0,0,0,.3)
        self.ids.export_l3.color = (0,0,0,.3)
        self.ids.export_img.source = 'assets/export_usb.png'
    def checkUSB(self, _):
        if os.name != 'nt':
            self.usb_dir = os.listdir('/media/guest/')#yamaji
        if(len(self.usb_dir) > 0):
            self.ids.export_l1.color = (0,0,0,.3)
            self.ids.export_l2.color = (0,0,1,1)
            self.ids.export_img.source = 'assets/export_download.png'
            toast("USB Found, transfering..")
            self.createXlsxFile()
            self.writeUSB()

    def createXlsxFile(self):
        XFaceDAO.localDAO.cursor.execute('select NAME, PASSWORD from EMPLOYEE')        
        ItemList = XFaceDAO.localDAO.cursor.fetchall()
        filename = "log/employee_list_" + str(time.strftime("%Y-%m-%d")) + ".xlsx"
        # Create one if not exists.
        if not os.path.isfile(filename):
            w = xlwt.Workbook(filename)
            w.add_sheet('Sheet1')
            w.save(filename)
        workbook = xlsxwriter.Workbook(filename)
        worksheet = workbook.add_worksheet()
        cell_format = workbook.add_format({'bold': True, 'italic': True,'align':'center'})
        cell_format2 = workbook.add_format({'align':'vcenter'})
        worksheet.set_column('A:A',20)
        worksheet.set_column('B:B',10)
        worksheet.set_column('C:C',20)
        worksheet.write('A1','Name',cell_format)
        worksheet.write('B1','Password',cell_format)
        worksheet.write('C1','Profile',cell_format)
        row = 1
        col = 0
        for name, Password in (ItemList):
            worksheet.write(row, col,     name,cell_format2)
            worksheet.write(row, col + 1, Password,cell_format2)
            worksheet.set_row(row,114)
            Image = cv2.imread('pic/{}/{}.png'.format(name, name))
            if Image is None:
                worksheet.write(row, col + 2, Image)
            else:
                # imgdata = base64.b64decode(Image)         #yamaji 11.10
                # image = io.BytesIO(imgdata)               #yamaji 11.10
                worksheet.insert_image(row,col+2, 'pic/{}/{}.png'.format(name, name), {'x_scale': 0.5, 'y_scale': 0.5})#yamaji 11.10 change    #'1.png', {'image_data': image,'x_scale': 0.1, 'y_scale': 0.1})
            row += 1
        workbook.close()

    def writeUSB(self):
        Clock.unschedule(self.check)
        d = datetime.now()
        source_dir = "log"
        destination_dir = "/media/guest/" +self.usb_dir[0]+ "/log_" + d.strftime("%Y") + d.strftime("%b") + d.strftime("%d") + "_" + d.strftime("%H") + d.strftime("%M") + d.strftime("%S")#yamaji
        # source_dir2 = "database"                                                                          #yamaji 11.10
        # destination_dir2 = "/media/guest/" +self.usb_dir[0]+ "/local_database" + d.strftime("%Y") + d.strftime("%b") + d.strftime("%d") + "_" + d.strftime("%H") + d.strftime("%M") + d.strftime("%S")#yamaji 11.10
        try:
            shutil.copytree(source_dir, destination_dir)
            #shutil.copytree(source_dir2, destination_dir2) #yamaji 11.10
            self.ids.export_l2.color = (0,0,0,.3)
            self.ids.export_l3.color = (0,0,1,1)
            self.ids.export_img.source = 'assets/export_tick.png'
        except Exception:
            toast("Error occurs during transfering data.")
            XFaceLogging.system("1658", traceback.format_exc())

class BgTile(MDSmartTile): pass
class BackgroundScreen(Screen):
    def on_pre_enter(self):
        for i in range(12):
            x = BgTile(source="assets/background/{}.png".format(i))
            x.bind(on_press=self.changeBackground)
            self.ids.background_grid.add_widget(x)
    def changeBackground(self, tile):
        def change():#(text, widget):#yamaji 10.18 from
            #if text == 'Yes':
            tile_source = tile.source
            sm.main_background = tile_source
            XFaceDAO.localDAO.setSystemValue('BACKGROUND', tile_source)
            self.dialog.dismiss()
            toast("Background Image is changed successfully!") #yamaji 10.18 to
        # self.dialog = MDDialog( #yamaji from
        #     title="Confirmation",
        #     size_hint=(0.8, 0.25),
        #     text_button_ok="Yes",
        #     text="Do you want to change the Background Image?",
        #     text_button_cancel="Cancel",
        #     events_callback=change,
        # )
        
        dialog=BoxLayout(orientation='vertical',)
        #label=MDLabel(text="Do you want to change the Background Image?",font_size=18,pos_hint={"center_x":0.5, "center_y":0.5},)
        label=MDLabel(text="Do you want to change the Background Image?",font_size=18,pos_hint={"center_x":0.5, "center_y":0.5},theme_text_color="Custom",text_color=(1,1,1,1)) #korn 11.1)
        buttun=BoxLayout(orientation='horizontal',spacing=10)
        space=BoxLayout(size_hint=(0.4,0.01))
        yes_button=MDFlatButton(text='Yes',on_release=lambda _:  change(),md_bg_color=(0.7,0.7,0.7,1),) #yamaji 10.18 change(self) => change()
        cancel_button=MDFlatButton(text='Cancel',on_release=lambda _: self.dialog.dismiss(),md_bg_color=(0.7,0.7,0.7,1))
        buttun.add_widget(space)
        buttun.add_widget(yes_button)
        buttun.add_widget(cancel_button)
        dialog.add_widget(label)
        dialog.add_widget(buttun)
        self.dialog = Popup(
            title="Confirmation",
            size_hint=(0.8, 0.25),
            content = dialog,
            )#yamaji to
        self.dialog.open()

    def on_leave(self):                            #2023/10/18 fujiwara tuika
        self.ids.background_grid.clear_widgets()   #2023/10/18 fujiwara tuika

class TwoLineAvatarListItem(OneLineAvatarListItem):
    _txt_top_pad = NumericProperty("20dp")
    _txt_bot_pad = NumericProperty("15dp")  # dp(20) - dp(5)
    _height = NumericProperty()
    _num_lines = 2

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.height = dp(72) if not self._height else self._height

# # endregion




# # region #####################################  MAIN  ###################################

"""tick_count = 0
shutdown_count = 0
def tick(self):
    global tick_count
    global shutdown_count
    tick_count += 0.09
    if tick_count > 300: # after 300 seconds
        tick_count = 0"""                                                          #2023/11/8 fujiwara comment out
        #XFaceLogging.system('INFO', XFaceGPIOControllers.getTemperature())
    # if not XFaceGPIOControllers.isShutdownBtn():
    #     shutdown_count += 0.09
    #     print('shutdown pressing')
    #     if shutdown_count > 3: # after 3 seconds
    #         raise Exception("Shutdown")
    # else: shutdown_count = 0

class XFACE(MDApp):
    Builder.load_file('XFaceApplication.kv')
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def build(self):
        global sm
        sm = ScreenManagement()
        sm.welcome_modal = False
        sm.process_pool = [] # pool of process to be join when exit app. Not joining will cause a zombie process problem
        #Window.rotation = 90   #2023/12/28 fujiwara tuika
        background = XFaceDAO.localDAO.getSystemValue('BACKGROUND')
        if background is None: sm.main_background = 'assets/background/0.png'
        else: sm.main_background = background
        sm.volume = int(XFaceDAO.localDAO.getSystemValue('SYSTEM_VOLUME'))
        #if RASPBERRY: sm.ticker = Clock.schedule_interval(tick, 0.09)                     #2023/11/8 fujiwara comment out
        self.createRequiredFile()
        XFaceLogging.system('INFO',"SYSTEM START UP")
        return sm
    def createRequiredFile(self):
        if not os.path.exists("log"):
            os.makedirs("log")
        if not os.path.exists("pic"):
            os.makedirs("pic")
        if not os.path.exists("log/OpenDoorPic"):
            os.makedirs("log/OpenDoorPic")
    def stop(self):
        raise Exception("Exit")

try:
    X = None
    X = XFACE()
    X.run()
except Exception as e:
    print(e)
    if str(e) not in ["Exit", "Shutdown"]:
        print(e)
        XFaceLogging.system("1521", traceback.format_exc())
    
    try:
        ps.stop()
        XFaceGPIOControllers.cleanup() #yamaji
        XFaceLogging.system("1700", 'ps.stop')
    except Exception: pass
    if sm != None:
        for process in sm.process_pool:
            try:
                process.join()
            except Exception: pass
    else: XFaceLogging.system('INFO','NO process_pool')
    """if RASPBERRY:
        try:
            Clock.unschedule(sm.ticker)
        except Exception: pass"""                             #2023/11/8 fujiwara comment out

    if str(e) == "Exit":
        XFaceLogging.system('INFO',"SYSTEM EXIT")
        App.stop(X)
    elif str(e) == "Shutdown":
        XFaceLogging.system('INFO',"SHUTDOWN")
        os.system("./ShutdownDelay.sh")
        App.stop(X)
    else:
        App.stop(X)

# # endregion
