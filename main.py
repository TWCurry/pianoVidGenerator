import sys
from convertToMidi import convertWavToMidi

def main():
    # Args
    try:
        inputFile = sys.argv[1]
        fileType = sys.argv[2]
    except Exception as e:
        print(f"Invalid parameters: {e}")
        sys.exit(1)
    
    convertWavToMidi(fileType, inputFile, "temp.mid")

if __name__ == "__main__":
    main()