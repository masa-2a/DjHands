import cv2
from adapters.camera import CV2CameraAdapter
from adapters.detector import MediaPipeDetector
from presenter.presenter import CV2Presenter
from use_case.process_frame import ProcessFrame

# Optionally configure global MP settings here

if __name__ == '__main__':
    camera = CV2CameraAdapter(0)
    detector = MediaPipeDetector()
    presenter = CV2Presenter()
    processor = ProcessFrame(camera, detector, presenter)
    try:
        processor.run()
    except KeyboardInterrupt:
        pass
    finally:
        cv2.destroyAllWindows()
