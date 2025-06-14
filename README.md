
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
- Control 10 seperate clips/audios/midis with your fingers
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
2. Install [AbletonOSC](https://github.com/ideoforms/AbletonOSC) and follow the instructions given on their github repo.
3. Make sure you are in Session view on ableton. (looks like ||| on the top right)
5. Organise 10 tracks each with 1 clip on the first clip slot (Should look something like this) Tracks 1-5 will belong to your right hand starting with your pinky for 1 and moving towards your thumb for 5. Similarly, tracks 6-10 belong to your left hand and move in the same way.
<img width="954" alt="Screenshot 2025-06-13 at 9 34 18 PM" src="https://github.com/user-attachments/assets/0f4e589d-b156-41c1-bea2-d09c75a15d91" />
(If you want a track to loop while youre finger is held up make sure to enable that. You can find it after you click on the item in the clop slot and then finding the loop button in the clip properties bar at the bottom of the screen.)
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

3. Install dependencies. Might be prompted to install a moer recent version, which should work unless otherwise stated.
```
pip install -r requirements.txt
```

## Usage 🧚🏽‍♀️

 Run the app/main.py file and a seperate camera window should open up. Move your fingers and create some music. To end your session hit q.
 
## License

## Feedback 📈

## Share your mixes!
