import cv2

class CV2CameraAdapter:
    def __init__(self, index: int = 1):
        self.cap = cv2.VideoCapture(index)

    def frames(self):
        if not self.cap.isOpened():
            raise RuntimeError("Cannot open webcam")
        while True:
            success, img = self.cap.read()
            if not success:
                break
            yield img
        self.cap.release()