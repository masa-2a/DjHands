import cv2

class CV2CameraAdapter:
    def __init__(self, index: int = 0):
        self.cap = cv2.VideoCapture(index)

    def frames(self):
        if not self.cap.isOpened():
            raise RuntimeError("Cannot open webcam")
        while True:
            ok, img = self.cap.read()
            if not ok:
                break
            yield img
        self.cap.release()