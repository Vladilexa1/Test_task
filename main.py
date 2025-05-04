import time
import cv2
from datetime import datetime
from picamera2 import Picamera2


def make_photo(pcam2: Picamera2):
    pcam2.start()
    time.sleep(2) # wait load camera
    img = pcam2.capture_array()
    pcam2.stop()
    pcam2.close()
    return img

def save_photo(img, name=""):
    if name == "":
        name = datetime.now().strftime("%H%M%S%d%m%Y")
    success = cv2.imwrite(f"./img/{name}.jpg", img)
    if success:
        print("The photo is saved")
    else:
        print("Something went wrong")

def main():
    picam2 = Picamera2()
    img = make_photo(picam2)
    save_photo(img)


if __name__ == "__main__":
    main()