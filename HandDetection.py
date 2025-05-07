import os.path

import mediapipe as mp
import numpy as np
from mediapipe.tasks import python

def convertToMpImage(image: np.ndarray) -> mp.Image:
    return mp.Image(image_format=mp.ImageFormat.SRGB, data=image)

def getModelPath():
    return os.path.abspath("hand_landmarker.task")

def InitaliseHandLandmarker():
BaseOptions = mp.tasks.BaseOptions #creates the handlandmarker object
HandLandmarker = mp.tasks.vision.HandLandmarker #
HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
HandLandmarkerResult = mp.tasks.vision.HandLandmarkerResult
VisionRunningMode = mp.tasks.vision.RunningMode

# Create a hand landmarker instance with the live stream mode:
def print_result(result: HandLandmarkerResult, output_image: mp.Image, timestamp_ms: int):
    print('hand landmarker result: {}'.format(result))

options = HandLandmarkerOptions(
    base_options=BaseOptions(model_asset_path=model_path),
    num_hands=2,
    running_mode=VisionRunningMode.LIVE_STREAM,
    result_callback=print_result)
with HandLandmarker.create_from_options(options) as landmarker:

