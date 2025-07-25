
# DjHands 👋🎧

DjHands is a program that lets you mix on Ableton Live 12 using your two hands!

This program works by implementing [Google Mediapipe Hand Landmarker](https://ai.google.dev/edge/mediapipe/solutions/vision/hand_landmarker) and [AbletonOSC](https://github.com/ideoforms/AbletonOSC) with Python!

## Table of Contents
1. [Features](#features)
2. [Set Up](#set-up)
3. [Usage](#usage)
4. [License](#license)
5. [Feedback](#feedback)
6. [Share your mixes!](#share-your-mixes)
   
---

## Features 🎼
- Control 10 separate clips/audios/midis with your fingers
- Use OSC to toggle clips
- Live beat building with hand movements

---

## Set Up 🏗

### Required Software 🎯
- Python 3.10+
- `mediapipe`
- `opencv-python`
- `python-osc`
- `rtmidi`
- [Ableton Live](https://www.ableton.com/en/) 11 or 12 (You can get a 30 day [free trial](https://www.ableton.com/en/trial/) version with full capabilities)

### On Ableton
1. Make sure you have **Ableton Live 11 or 12**.
2. Install [AbletonOSC](https://github.com/ideoforms/AbletonOSC) and follow the instructions given on their GitHub repo.
3. Make sure you are in Session view on ableton. (looks like ||| on the top right)
5. Organise 10 tracks each with 1 clip on the first clip slot (Should look something like this) Tracks 1-4 will belong to your right hand starting with your index for 1 and moving towards your pinky for 4. Similarly, tracks 5-9 belong to your left hand and move in the same way.
<img width="954" alt="Screenshot 2025-06-13 at 9 34 18 PM" src="https://github.com/user-attachments/assets/0f4e589d-b156-41c1-bea2-d09c75a15d91" />
(If you want a track to loop while you're finger is held up make sure to enable that. You can find it after you click on the item in the clop slot and then finding the loop button in the clip properties bar at the bottom of the screen.)
6. Once you've played around with all your sounds and everything is set up you can move to the next step.

### Program Setup

1. Clone the repo:
```bash
git clone https://github.com/masa-2a/DjHands.git
cd DjHands
```

2. Create a virtual environment
```
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
```

3. Install dependencies. Might be prompted to install a more recent version, which should work unless otherwise stated.
```
pip install -r requirements.txt
```

## Usage 🧚🏽‍♀️

 Run the app/main.py file and a seperate camera window should open up. Move your fingers and create some music. To end your session hit q.

 Here are a few tips:  
 1. If you prefer that everytime you lift your finger the clip starts instantly (rather to waiting for the next quantised bar) then set quantisation to 0 from the menu. Alternatively, you can set custom quantisaion for each track for more creativity.
 2. Instead of using it to mix beats you can also use it to assemble songs (vocals on one hand and instruments on another).
 3. play around with how it detects a closed fist/ unraised fingers to find the sweet spot.
Check out this video for a quick demo!
 
## License


## Feedback 📈

## Share your mixes!
