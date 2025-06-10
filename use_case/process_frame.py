from typing import NamedTuple

from mediapipe.tasks.python.components.containers.landmark import NormalizedLandmark

from adapters.camera import CV2CameraAdapter
from adapters.detector import HandLandMarker
from adapters.fingerlift import is_finger_lifted
from presenter.presenter import CV2Presenter

class ProcessFrame:
    def __init__(self, camera: CV2CameraAdapter, detector: HandLandMarker, presenter: CV2Presenter, abletonosc):
        self.camera = camera
        self.detector = detector
        self.presenter = presenter
        self.threshold = 0.05
        self.ableton = abletonosc

    """runs all the required function each time a frame detects a hand"""
    def run(self):
        #self.ableton.setup_playback()
        for frame in self.camera.frames():
            results = self.detector.detect(frame) #is a [handlandmarks[], handedness].. list
            if results: #check that a real list was returned
                for info_set in results:
                    if info_set[0]:
                        self.process_hand(info_set[0], info_set[1])
                        self.presenter.show(frame, info_set[0])
            else:
                self.turnOffAll()



    """ checks if each finger is raised, if yes it calls the appropriate function for that finger
        preconditions, hand must be of type normalised hand landmarker
    """
    def process_hand(self, handlandmark_list: list[NormalizedLandmark], handedness: str):
            pink_tip_y = handlandmark_list.landmark[20].y
            pink_mcp_y = handlandmark_list.landmark[19].y
            if is_finger_lifted(pink_tip_y, pink_mcp_y, self.threshold):
                self.ableton.pinky_function(handedness, True)
            else:
                self.ableton.pinky_function(handedness, False)

            ring_tip_y = handlandmark_list.landmark[16].y
            ring_mcp_y = handlandmark_list.landmark[15].y
            if is_finger_lifted(ring_tip_y, ring_mcp_y, self.threshold):
                self.ableton.ring_function(handedness, True)
            else:
                self.ableton.ring_function(handedness, False)

            middle_tip_y = handlandmark_list.landmark[12].y
            middle_mcp_y = handlandmark_list.landmark[10].y
            if is_finger_lifted(middle_tip_y, middle_mcp_y, self.threshold):
                self.ableton.middle_function(handedness, True)
            else:
                self.ableton.middle_function(handedness, False)

            index_tip_y = handlandmark_list.landmark[8].y
            index_mcp_y = handlandmark_list.landmark[6].y
            if is_finger_lifted(index_tip_y, index_mcp_y, self.threshold):
                self.ableton.index_function(handedness, True)
            else:
                self.ableton.index_function(handedness, False)

            thumb_tip_y = handlandmark_list.landmark[4].y
            index_threshold_y = handlandmark_list.landmark[5].y
            if is_finger_lifted(thumb_tip_y, index_threshold_y, self.threshold):
                self.ableton.thumb_function(handedness, True)
            else:
                self.ableton.thumb_function(handedness, False)

    """turns off all operations"""
    def turnOffAll(self):
        for hand in ["Left", "Right"]:
            self.ableton.pinky_function(hand, False)
            self.ableton.ring_function(hand, False)
            self.ableton.index_function(hand, False)
            self.ableton.middle_function(hand, False)
            self.ableton.thumb_function(hand, False)