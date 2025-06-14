from mediapipe.tasks.python.components.containers.landmark import NormalizedLandmark

from src.adapters.camera import CV2CameraAdapter
from src.adapters.detector import HandLandMarker
from src.adapters.fingerlift import is_finger_lifted
from src.presenter.presenter import CV2Presenter
from src.adapters.ableton_osc import AbletonOSCAdapter
from src.entities.Hands import Hand
import time

class ProcessFrame:
    def __init__(self, camera: CV2CameraAdapter, detector: HandLandMarker, presenter: CV2Presenter, abletonosc: AbletonOSCAdapter, left_hand: Hand, right_hand: Hand):
        self.camera = camera
        self.detector = detector
        self.presenter = presenter
        self.threshold = 0.05
        self.ableton = abletonosc
        self.last_sent = 0
        self.SEND_INTERVAL = 0.01 #500 ms
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
                self.presenter.show(frame, [])

    def process_finger(self, handlandmarks, hand_obj: Hand, finger_name: str, tip_id: int, mcp_id: int, handedness: str,
                       ableton_func):
        tip_y = handlandmarks.landmark[tip_id].y
        mcp_y = handlandmarks.landmark[mcp_id].y
        is_up = is_finger_lifted(tip_y, mcp_y, self.threshold)
        state = getattr(hand_obj, finger_name)

        if is_up and not state:
            ableton_func(handedness, True)
            setattr(hand_obj, finger_name, True)

        elif not is_up and state:
            ableton_func(handedness, False)
            setattr(hand_obj, finger_name, False)

    def process_hand(self, handlandmarks: list[NormalizedLandmark], handedness: str, hand_obj: Hand):
        fingers = [
            ("pinky", 20, 19, self.ableton.pinky_function),
            ("ring", 16, 15, self.ableton.ring_function),
            ("middle", 12, 10, self.ableton.middle_function),
            ("index", 8, 6, self.ableton.index_function),
            #("thumb", 4, 5, self.ableton.thumb_function),  # comparing tip to index base
        ]

        for name, tip_id, mcp_id, func in fingers:
            self.process_finger(handlandmarks, hand_obj, name, tip_id, mcp_id, handedness, func)

    """turns off all operations"""
    def turnOffAll(self):
        self.turnOffHand(self.left_hand, "Left")
        self.turnOffHand(self.right_hand, "Right")

    def turnOffHand(self, hand: Hand, handedness: str):
        if hand.pinky:
            self.ableton.pinky_function(handedness, False)
            hand.pinky = False
        if hand.ring:
            self.ableton.ring_function(handedness, False)
            hand.ring = False
        if hand.index:
            self.ableton.index_function(handedness, False)
            hand.index = False
        if hand.middle:
            self.ableton.middle_function(handedness, False)
            hand.middle = False
        #if hand.thumb:
        #    self.ableton.thumb_function(handedness, False)
        #    hand.thumb = F alse