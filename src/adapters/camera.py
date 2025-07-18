import cv2

class CV2CameraAdapter:
    def __init__(self, index: int = 1):
        self.cap = cv2.VideoCapture(index)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    def frames(self):
        if not self.cap.isOpened():
            raise RuntimeError("Cannot open webcam")
        while True:
            success, img = self.cap.read()
            if not success:
                break
            yield img
        self.cap.release()