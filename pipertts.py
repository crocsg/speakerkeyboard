from piper import PiperVoice
import time
import wave
import pyaudio

#p = pyaudio.PyAudio()

# Open stream (2)


CHANNELS = 1
RATE = 22050
CHUNK = 16384


class GoodTTS ():
    def __init__(self):
        self.streamOut = None
        self.voice = None
        self.audio = None
    
    def open (self, enginepath):
        self.voice = PiperVoice.load(enginepath)
        self.voice.config.sample_rate = int (22050 *0.95)
        self.voice.config.num_symbols = 4096
        self.voice.config.num_speakers = 1

        self.audio = pyaudio.PyAudio()

        chunks = self.voice.synthesize("hello")
        
        for chunk in chunks:
            self.streamOut = self.audio.open(format=pyaudio.paInt16, channels=chunk.sample_channels,
                    rate=chunk.sample_rate, output=True, input_device_index=0, frames_per_buffer = 1)       
            print (chunk.sample_rate)
            break

    def say(self, message):
        for chunk in self.voice.synthesize(message):
            self.streamOut.write (chunk.audio_int16_bytes)
    

def playtts (message, stream):
    for chunk in voice.synthesize("Station Charles de Gaulles - Ligne A " + str(i)):
        stream.write (chunk.audio_int16_bytes)

def opentts ():
    for chunk in voice.synthesize("hello"):
        streamOut = audio.open(format=pyaudio.paInt16, channels=chunk.sample_channels,
                    rate=chunk.sample_rate, output=True, input_device_index=0, frames_per_buffer = 1)
        #streamOut.write (chunk.audio_int16_bytes)
        return streamOut


def closetts (stream):
    stream.close()

def oldtest ():
    audio = pyaudio.PyAudio()

    # start Recording


    voice = PiperVoice.load("C:/Users/sgngo/home/tmp/pipertest/fr_FR-siwis-medium.onnx")
    voice.config.sample_rate == 22050
    voice.config.num_symbols == 256
    voice.config.num_speakers == 1


    def playtts (message, stream):
        for chunk in voice.synthesize("Station Charles de Gaulles - Ligne A " + str(i)):
            stream.write (chunk.audio_int16_bytes)

    for i in range (0,25):
        print ("essai", i)
        for chunk in voice.synthesize("Station Charles de Gaulles - Ligne A " + str(i)):
            #set_audio_format(chunk.sample_rate, chunk.sample_width, chunk.sample_channels)
            #write_raw_data(chunk.audio_int16_bytes)
            print (len(chunk.audio_int16_bytes))
            streamOut = audio.open(format=pyaudio.paInt16, channels=chunk.sample_channels,
                        rate=chunk.sample_rate, output=True, input_device_index=0, frames_per_buffer = 1)
            streamOut.write (chunk.audio_int16_bytes)
            streamOut.close ()

        #voice.synthesize("Bonjour Piper, "+ str(i)) 

        time.sleep (1)
        #"voice.synthesize_wav("Bonjour Piper, "+ str(i), streamOut) 
        #time.sleep(2)

def main ():
    
    tts = GoodTTS ()
    tts.open ("fr_FR-siwis-medium.onnx")
    for i in range (0,2):
        tts.say(str(i))
        time.sleep (0.05)
    
    stations= [
     "La Poterie",
     "Le blaune",
     "Triangle",
     "Italie",
     "Henri Fréville",
     "Clémenceau",
     "Jacques Cartier",
     "Station Gare",
     "Charles de Gaulle",
     "République",
     "Sainte-Anne",
     "Anatole France",
     "Ponchaillou",
     "Villejean  Université",
     "J F Kennedy"

    ]
   
    for station in stations:
        tts.say (station)


if __name__ == "__main__":
    main ()