from typing import NamedTuple

from mediapipe.tasks.python.components.containers.landmark import NormalizedLandmark

from adapters.camera import CV2CameraAdapter
from adapters.detector import HandLandMarker
from adapters.fingerlift import is_finger_lifted
from presenter.presenter import CV2Presenter
from adapters.ableton_osc import AbletonOSCAdapter
from entities.Hands import Hand
import time

class ProcessFrame:
    def __init__(self, camera: CV2CameraAdapter, detector: HandLandMarker, presenter: CV2Presenter, abletonosc: AbletonOSCAdapter, left_hand: Hand, right_hand: Hand):
        self.camera = camera
        self.detector = detector
        self.presenter = presenter
        self.threshold = 0.05
        self.ableton = abletonosc
        self.last_sent = 0
        self.SEND_INTERVAL = 1 #500 ms
        self.left_hand = left_hand
        self.right_hand = right_hand


    """Runs all the required function each time a frame detects a hand"""
    def run(self):
        #self.ableton.setup_playback()
        for frame in self.camera.frames():
            results = self.detector.detect(frame) #is a [handlandmarks[], handedness].. list
            current_time = time.time()
            if results and (current_time - self.last_sent) > self.SEND_INTERVAL : #check that a real list was returned
                for info_set in results:
                    if info_set[0]:
                        handedness = info_set[1].classification[0].label # "Left" or "Right"
                        if handedness == "Left":
                            self.process_hand(info_set[0],handedness, self.left_hand)
                        else:
                            self.process_hand(info_set[0], handedness, self.right_hand)
                        self.last_sent = current_time
                        print("hand processed at"+str(self.last_sent)) #debug
                all_hands = [item[0] for item in results]
                self.presenter.show(frame, all_hands)
            else:
                self.turnOffAll() #no landmarks or hands detected at all




    """ Checks if each finger is raised, if yes it calls the appropriate function for that finger
        Preconditions, hand must be of type normalised hand landmarker
    """
    def process_hand(self, handlandmark_list: list[NormalizedLandmark], handedness: str, hand: Hand):
            pink_tip_y = handlandmark_list.landmark[20].y
            #print("pinky tip "+str(pink_tip_y))
            pink_mcp_y = handlandmark_list.landmark[19].y
            #print("pinky mcp " +str(pink_mcp_y))
            if is_finger_lifted(pink_tip_y, pink_mcp_y, self.threshold):
                if not hand.pinky: #if finger isn't currently lifted
                    self.ableton.pinky_function(handedness, True)
            else:
                if hand.pinky: #finger is already lifted
                    self.ableton.pinky_function(handedness, False)

            ring_tip_y = handlandmark_list.landmark[16].y
            ring_mcp_y = handlandmark_list.landmark[15].y
            if is_finger_lifted(ring_tip_y, ring_mcp_y, self.threshold):
                if not hand.ring:  # if finger isn't currently lifted
                    self.ableton.ring_function(handedness, True)
            else:
                if hand.ring:
                    self.ableton.ring_function(handedness, False)

            middle_tip_y = handlandmark_list.landmark[12].y
            middle_mcp_y = handlandmark_list.landmark[10].y
            if is_finger_lifted(middle_tip_y, middle_mcp_y, self.threshold):
                if not hand.middle:
                    self.ableton.middle_function(handedness, True)
            else:
                if hand.middle:
                    self.ableton.middle_function(handedness, False)

            index_tip_y = handlandmark_list.landmark[8].y
            index_mcp_y = handlandmark_list.landmark[6].y
            if is_finger_lifted(index_tip_y, index_mcp_y, self.threshold):
                if not hand.index:
                    self.ableton.index_function(handedness, True)
            else:
                if hand.index:
                    self.ableton.index_function(handedness, False)

            thumb_tip_y = handlandmark_list.landmark[4].y
            index_threshold_y = handlandmark_list.landmark[5].y
            if is_finger_lifted(thumb_tip_y, index_threshold_y, self.threshold):
                if not hand.thumb:
                    self.ableton.thumb_function(handedness, True)
            else:
                if hand.thumb:
                    self.ableton.thumb_function(handedness, False)

    """turns off all operations"""
    def turnOffAll(self):
        self.turnOffHand(self.left_hand, "Left")
        self.turnOffHand(self.right_hand, "Right")

    def turnOffHand(self, hand: Hand, handedness: str):
        if hand.pinky:
            self.ableton.pinky_function(handedness, False)
        if hand.ring:
            self.ableton.ring_function(handedness, False)
        if hand.index:
            self.ableton.index_function(handedness, False)
        if hand.middle:
            self.ableton.middle_function(handedness, False)
        if hand.thumb:
            self.ableton.thumb_function(handedness, False)