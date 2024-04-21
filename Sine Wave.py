from pysinewave import SineWave
import time
from random import randint

#Account for octave registers

notesListSharps = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B","C#"]

sinewave = SineWave(pitch = 12)
sinewave.play()
time.sleep(5)
sinewave.stop()

tune = ["C","D","E","F","G","A","B","C%","C%","B","A","G","F","E","D","C"]
tune2 = ["C","E","G","C%","G","E","C"]

for i in range(0,len(tune)):
    sinewave = SineWave(pitch = notesListSharps.index(tune[i]))
    sinewave.play()
    time.sleep(1)
    sinewave.stop()
    
for i in range(0,len(tune2)):
    sinewave = SineWave(pitch = notesListSharps.index(tune2[i]))
    sinewave.play()
    time.sleep(1)
    sinewave.stop()
    