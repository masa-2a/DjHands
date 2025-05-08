import cv2
import mediapipe as mp
import numpy as np


class CV2Presenter:
    def __init__(self):
        self.drawing = mp.solutions.drawing_utils
        self.connections = mp.solutions.hands.HAND_CONNECTIONS

    def show(self, frame: np.ndarray, landmarks: list):
        for lm in landmarks:
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            self.drawing.draw_landmarks(
                frame, lm, self.connections
            )
        cv2.imshow("HandLandmarker", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            raise KeyboardInterrupt()