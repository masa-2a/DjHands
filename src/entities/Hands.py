from scipy.stats import false_discovery_control

""" The Hand class is used to kep track of each finger on each and (whether they are lifted or not)"""
class Hand:
    def __init__(self):
        self.pinky = False
        self.ring  = False
        self.index = False
        self.middle = False
        self.thumb = False


