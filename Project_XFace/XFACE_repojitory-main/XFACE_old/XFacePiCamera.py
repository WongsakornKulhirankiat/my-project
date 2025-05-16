import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst
from time import sleep
from datetime import datetime
from threading import Thread, Event
import numpy as np
import cv2

class PiVideoStream(Thread):
    def __init__(self, resolution=(320,240), framerate=30):      #2023/11/2 resolution=(256, 256) -> resolution=(320,240)
        print("Jetson Stream", datetime.now())
        Gst.init(None)
        self.pipeline = None
        self.resolution = resolution
        self.framerate = framerate
        self.frame = None
        self._stop_event = Event()
        self.CAMERA_FLAG = Event()  # Camera frame is being read while CAMERA_FLAG is set(true)
        Thread.__init__(self, daemon=True)

    def create_pipeline(self):
        pipeline_str = (
            "nvarguscamerasrc sensor-id=0 ! video/x-raw(memory:NVMM), "
            f"width={self.resolution[0]}, height={self.resolution[1]}, format=NV12, framerate={self.framerate}/1 ! "
            "nvvidconv flip-method=2 ! video/x-raw, format=BGRx ! videoconvert ! video/x-raw, format=BGR ! "
            "appsink name=sink emit-signals=True sync=False max-buffers=1 drop=True"
        )
        self.pipeline = Gst.parse_launch(pipeline_str)
        appsink = self.pipeline.get_by_name("sink")
        appsink.set_property("caps", Gst.Caps.from_string("video/x-raw, format=BGR"))
        appsink.set_property("max-buffers", 1)
        appsink.set_property("drop", True)
        appsink.set_property("sync", False)
        appsink.connect("new-sample", self.on_new_sample)

    def on_new_sample(self, appsink):
        sample = appsink.emit("pull-sample")
        buf = sample.get_buffer()
        caps = sample.get_caps()
        height = caps.get_structure(0).get_value("height")
        width = caps.get_structure(0).get_value("width")
        self.frame = np.ndarray(
            (height, width, 3), buffer=buf.extract_dup(0, buf.get_size()), dtype=np.uint8
        )
        return Gst.FlowReturn.OK

    def start_pipeline(self):
        self.pipeline.set_state(Gst.State.PLAYING)

    def stop_pipeline(self):
        self.pipeline.set_state(Gst.State.NULL)

    def run(self):
        self.create_pipeline()
        self.start_pipeline()

        while True:
            """if self.CAMERA_FLAG.is_set():
                sleep(0.01)
                if not self.CAMERA_FLAG.is_set():     #2023/11/7 fujiwara comment out
                    break"""
            sleep(0.01)
            if self._stop_event.is_set():
                break
            sleep(0.1)

        self.stop_pipeline()

    def flip_vertically(image):
        """Flips an image vertically."""
        height, width, _ = image.shape
        flipped_image = np.zeros((height, width, 3), dtype=np.uint8)
        for y in range(height):
            flipped_image[y] = image[height - y - 1]
        return flipped_image

    def read(self):
        return self.frame

    def clear(self):
        self.frame = cv2.imread('assets/trans.png')

    def stop(self):
        self.CAMERA_FLAG.clear()
        self._stop_event.set()
        self.stop_pipeline()

if __name__ == '__main__':
    jvs = PiVideoStream()
    jvs.start()
    sleep(2)
    while True:
        print(jvs.read())
