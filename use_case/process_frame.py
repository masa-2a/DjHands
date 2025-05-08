from adapters.camera import CV2CameraAdapter
from adapters.detector import MediaPipeDetector
from presenter import CV2Presenter

class ProcessFrame:
    def __init__(self, camera: CV2CameraAdapter, detector: MediaPipeDetector, presenter: CV2Presenter):
        self.camera = camera
        self.detector = detector
        self.presenter = presenter

    def run(self):
        for frame in self.camera.frames():
            hands = self.detector.detect(frame)
            self.presenter.show(frame, hands)