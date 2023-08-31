BODY_PARTS_COLOR_MAP_IDS = set(tuple(range(100,127)))
COLOR_MAP = {
    -1: (255., 255., 255.),
    0: (0., 0., 0.),
    1: (174., 199., 232.),
    2: (152., 223., 138.),
    3: (31., 119., 180.),
    4: (255., 187., 120.),
    5: (188., 189., 34.),
    6: (140., 86., 75.),
    7: (255., 152., 150.),
    8: (214., 39., 40.),
    9: (197., 176., 213.),
    10: (148., 103., 189.),
    11: (196., 156., 148.),
    12: (23., 190., 207.),
    14: (247., 182., 210.),
    15: (66., 188., 102.),
    16: (219., 219., 141.),
    17: (140., 57., 197.),
    18: (202., 185., 52.),
    19: (51., 176., 203.),
    20: (200., 54., 131.),
    21: (92., 193., 61.),
    22: (78., 71., 183.),
    23: (172., 114., 82.),
    24: (255., 127., 14.),
    25: (91., 163., 138.),
    26: (153., 98., 156.),
    27: (140., 153., 101.),
    28: (158., 218., 229.),
    29: (100., 125., 154.),
    30: (178., 127., 135.),
    31: (120., 185., 128.),
    32: (146., 111., 194.),
    33: (44., 160., 44.),
    34: (112., 128., 144.),
    35: (96., 207., 209.),
    36: (227., 119., 194.),
    37: (213., 92., 176.),
    38: (94., 106., 211.),
    39: (82., 84., 163.),
    40: (100., 85., 144.),
    41: (0., 0., 255.), #artificial human
    # body parts
    100: (35., 69., 100.), # rightHand
    101: (73., 196., 37.), # rightUpLeg
    102: (121., 25., 252.), # leftArm
    103: (96., 237., 31.), # head
    104: (55., 40., 93.), # leftEye
    105: (75., 180., 125.), # rightEye
    106: (165., 38., 65.), # leftLeg
    107: (63., 75., 77.), # leftToeBase
    108: (27., 255., 80.), # leftFoot
    109: (82., 110., 90.), # spine1
    110: (87., 54., 10.), # spine2
    111: (210., 200., 110.), # leftShoulder
    112: (217., 212., 76.), # rightShoulder
    113: (254., 176., 234.), # rightFoot 
    114: (111., 140., 56.), # rightArm
    115: (83., 15., 157.), # leftHandIndex1
    116: (98., 255., 160.), # rightLeg
    117: (153., 170., 17.), # rightHandIndex1
    118: (54., 82., 122.), # leftForeArm
    119: (10., 19., 94.), # rightForeArm
    120: (1., 147., 72.), # neck
    121: (47., 210., 21.), # rightToeBase
    122: (174., 22., 133.), # spine
    123: (98., 58., 83.), # leftUpLeg
    124: (222., 25., 45.), # leftHand
    125: (75., 233., 65.), # hips
}

INST_COLOR_MAP = {
    0: (0., 0., 0.),
    1: (255., 0., 0.),
    2: (0., 255., 0.),
    3: (0., 0., 255.),
    4: (255., 255., 0.),
    5: (255., 0., 255.),
    6: (0., 255., 255.),
    7: (255., 204., 153.),
    8: (255., 102., 0.),
    9: (0., 128., 128.),
    10: (153., 153., 255.),
}
