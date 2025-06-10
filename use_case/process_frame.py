from typing import NamedTuple

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

    # runs all the required function each time a frame detects a hand
    def run(self):
        for frame in self.camera.frames():
            hands = self.detector.detect(frame)
            if hands: #check that a real list was returned
                for hand in hands: # hands = [left, right]
                    self.process_hand(hand)
                self.presenter.show(frame, hands)

    # checks if each finger is raised, if yes it calls the appropriate function for that finger
    # preconditioons, hand must be of type normalised hand landmarker
    def process_hand(self, hand):
            pink_tip_y = hand.landmark[20].y
            pink_mcp_y = hand.landmark[19].y
            if is_finger_lifted(pink_tip_y, pink_mcp_y, self.threshold):
                self.ableton.pinky_function()
            ring_tip_y = hand.landmark[16].y
            ring_mcp_y = hand.landmark[15].y
            if is_finger_lifted(ring_tip_y, ring_mcp_y, self.threshold):
                self.ableton.ring_function()
            middle_tip_y = hand.landmark[12].y
            middle_mcp_y = hand.landmark[10].y
            if is_finger_lifted(middle_tip_y, middle_mcp_y, self.threshold):
                self.ableton.middle_function()
            index_tip_y = hand.landmark[8].y
            index_mcp_y = hand.landmark[6].y
            if is_finger_lifted(index_tip_y, index_mcp_y, self.threshold):
                self.ableton.index_function()
            thumb_tip_y = hand.landmark[4].y
            index_threshold_y = hand.landmark[5].y
            if is_finger_lifted(thumb_tip_y, index_threshold_y, self.threshold):
                self.ableton.thumb_function()



