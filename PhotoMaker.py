import time
from picamera2 import Picamera2


def make_photo(pcam2: Picamera2):
    pcam2.start()
    time.sleep(2)
    img = pcam2.capture_array()
    pcam2.stop()
    pcam2.close()
    return img

if __name__ == "__main__":
    picam2 = Picamera2()
    img = make_photo(picam2)