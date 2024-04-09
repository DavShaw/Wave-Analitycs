from functions import getPhase, getFft, getWaveData, getMagnitude, getGenr
from functions import getDiscreteFrequency, getMaxMagnitude, getTimeVector
from functions import splitSoundIntoSegments, getRms, getMfcc, getFormant
import json

data = {}

paths = ["sounds/david.wav", "sounds/cristian.wav", "sounds/christian.wav"]
for path in paths:
    newKey = paths.index(path)
    data[newKey] = {}
    fs, sound = getWaveData(path)
    soundsArray = splitSoundIntoSegments(sound, fs)

    for i, currentsound in enumerate(soundsArray):
        transform = getFft(currentsound)
        magnitude = getMagnitude(transform)
        rms = getRms(magnitude)
        rms = round(rms, 4)
        df = getDiscreteFrequency(fs, transform)
        hz = getMaxMagnitude(magnitude, df)
        hz = round(hz, 4)
        formant = getFormant(transform, magnitude, df)
        formant = round(formant, 4)
        data[newKey][i] = {'frequency': hz,
                           'magnitude': rms, 'formant': formant}

print(data)
print(f"Data type: {(type(data))}")
with open("sounddata.json", 'w') as json_file:
    json.dump(data, json_file, indent=4)
