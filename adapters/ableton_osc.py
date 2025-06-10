from pythonosc.udp_client import SimpleUDPClient
#for the current set of functions, ableton should be open with 10 seperate tracks.
# 5 or less for each hand
# 1-> thumb
# 2-> index
# 3-> middle
# 4 -> ring
# 5 ->

class AbletonOSCAdapter:
    def __init__(self):
        self.ip = "127.0.0.1"
        self.to_ableton = 11000
        self.from_ableton = 11001
        self.client = SimpleUDPClient(self.ip, self.to_ableton)


    def pinky_function(self, handedness, ) : #drum kit
        if handedness == "right":

        else:

    def ring_function(self): #harmonizers

    def middle_function(self): #synth

    def index_functoin(self): #bass

    def thumb_function(self): #vocals



    