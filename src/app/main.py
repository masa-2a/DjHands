import cv2
from src.adapters.camera import CV2CameraAdapter
from src.adapters.detector import HandLandMarker
from src.presenter.presenter import CV2Presenter
from src.use_case.process_frame import ProcessFrame
from src.adapters.ableton_osc import AbletonOSCAdapter
from src.entities.Hands import Hand

# main application file for the program

if __name__ == '__main__':
    camera = CV2CameraAdapter(0)
    detector = HandLandMarker()
    presenter = CV2Presenter()
    ableton_osc = AbletonOSCAdapter()
    left_hand = Hand()
    right_hand = Hand()
    processor = ProcessFrame(camera, detector, presenter, ableton_osc, left_hand, right_hand)


    try:
        processor.run()
    except KeyboardInterrupt:
        pass
    finally:
        cv2.destroyAllWindows()
