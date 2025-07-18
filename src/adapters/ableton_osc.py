from pythonosc.udp_client import SimpleUDPClient
#for the current set of functions, ableton should be open with 10 seperate tracks.
# 5 or less for each hand
# 1 / 5-> index
# 2 / 6-> middle
# 3 / 7-> ring
# 4 / 8-> pinky

class AbletonOSCAdapter:
    def __init__(self):
        self.ip = "127.0.0.1"
        self.to_ableton = 11000
        self.from_ableton = 11001
        self.client = SimpleUDPClient(self.ip, self.to_ableton)

    def setup_playback(self):
        self.client.send_message("/live/song/start_playing", []) #fix this

    def pinky_function(self, handedness: str,  on: bool) : #drum kit
        if handedness == "Right":
            if on:
                self.client.send_message("/live/clip_slot/fire",[3, 0])
            else:
                self.client.send_message("/live/clip_slot/stop", [3, 0])
        else:
            if on:
                self.client.send_message("/live/clip_slot/fire", [8, 0])
            else:
                self.client.send_message("/live/clip_slot/stop", [8,0])

    def ring_function(self, handedness: str, on: bool):
        if handedness == "Right":
            if on:
                self.client.send_message("/live/clip_slot/fire",[3, 0])
            else:
                self.client.send_message("/live/clip_slot/stop", [3, 0])
        else:
            if on:
                self.client.send_message("/live/clip_slot/fire", [7, 0])
            else:
                self.client.send_message("/live/clip_slot/stop", [7,0])

    def middle_function(self, handedness: str, on: bool): #synth
        if handedness == "Right":
            if on:
                self.client.send_message("/live/clip_slot/fire",[2, 0])
            else:
                self.client.send_message("/live/clip_slot/stop", [2, 0])
        else:
            if on:
                self.client.send_message("/live/clip_slot/fire", [6, 0])
            else:
                self.client.send_message("/live/clip_slot/stop", [6,0])

    def index_function(self, handedness: str, on: bool): #bass
        if handedness == "Right":
            if on:
                self.client.send_message("/live/clip_slot/fire",[1, 0])
            else:
                self.client.send_message("/live/clip/stop", [1, 0])
        else:
            if on:
                self.client.send_message("/live/clip_slot/fire", [5, 0])
            else:
                self.client.send_message("/live/clip_slot/stop", [5,0])

    def thumb_function(self, handedness: str, on: bool): #vocals
        if handedness == "Right":
            if on:
                self.client.send_message("/live/clip_slot/fire",[9, 0])
            else:
                self.client.send_message("/live/clip_slot/stop", [9, 0])
        else:
            if on:
                self.client.send_message("/live/clip_slot/fire", [10, 0])
            else:
                self.client.send_message("/live/clip_slot/stop", [10,0])