import time
from picamera2 import Picamera2, Preview

#To take a photo#
picam = Picamera2()

config = picam.create_preview_configuration()
picam.configure(config)

picam.start_preview(Preview.QTGL)

picam.start()
time.sleep(2)
picam.capture_file("ArUco_4_6x6.jpg")

#picam.close()

#5sec video#
#picam2 = Picamera2()
#picam.start_and_record_video("test.mp4",duration=5)