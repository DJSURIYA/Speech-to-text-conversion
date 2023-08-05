import pyaudio
from pocketsphinx import LiveSpeech

# Initialize the PyAudio object
pa = pyaudio.PyAudio()

# Define the microphone settings
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
CHUNK = 1024

# Open the microphone stream
stream = pa.open(format=FORMAT,
                 channels=CHANNELS,
                 rate=RATE,
                 input=True,
                 frames_per_buffer=CHUNK)

print("Listening...")

# Start listening and decoding
stream.start_stream()

# Initialize the LiveSpeech object
speech = LiveSpeech(
    verbose=False,
    sampling_rate=RATE,
    buffer_size=CHUNK
)

# Process the audio stream
for phrase in speech:
    print("Recognized:", phrase)

# Clean up
stream.stop_stream()
stream.close()
pa.terminate()
