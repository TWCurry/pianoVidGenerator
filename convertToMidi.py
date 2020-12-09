import sys, os
from pydub import AudioSegment

wavFileName = "temp.wav"

def convertToWav(initFileType, fileLoc, outputFileLoc):
    if initFileType == "m4a":
        convertM4aToWav(fileLoc)
    else:
        raise NotImplementedError
    convertWavToMidi(outputFileLoc)
    removeWavFile()
    

def convertM4aToWav(fileLoc):
    audio = AudioSegment.from_file(fileLoc, "m4a")
    audio.export(wavFileName, format="wav")

def convertWavToMidi(outputFileLoc):
    print 

def removeWavFile():
    os.remove(wavFileName)

if __name__ == "__main__":
    print("This script is designed to run as a module, please run main.py.")
    sys.exit(1)