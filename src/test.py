from functions import getPhase, getFft, getWaveData, getMagnitude, getGenr
from functions import getDiscreteFrequency, getMaxMagnitude, getTimeVector
from functions import splitSoundIntoSegments, getRms
import json

data = {}

paths = ["sounds/david.wav", "sounds/cristian.wav", "sounds/christian.wav"]
for path in paths:
    data[path] = {}
    fs, sound = getWaveData(path)
    soundsArray = splitSoundIntoSegments(sound, fs)

    for i, currentsound in enumerate(soundsArray):
        transform = getFft(currentsound)
        magnitude = getMagnitude(transform)
        rms = getRms(magnitude)
        df = getDiscreteFrequency(fs, transform)
        hz = getMaxMagnitude(magnitude, df)
        data[path][i] = {'rms': rms, 'hz': hz}

print(data["sounds/david.wav"])
# with open("sounddata.json", 'w') as json_file:
#   json.dump(data, json_file, indent=4)
