import cv2
import mediapipe as mp
import numpy as np


class HandLandMarker:
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands()

    def detect(self, frame: np.ndarray):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(rgb)
        if results.multi_hand_landmarks and results.multi_handedness:
            # creates a new list where first index contains list of landmarks normalised and second index is Left or Right
            return list(zip(results.multi_hand_landmarks, results.multi_handedness))
        else:
            return [] #if either one of them doesn't exist then send empty list that will be flagged later