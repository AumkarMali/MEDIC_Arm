import speech_recognition as sr
import os
import wave
import simpleaudio as sa
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# Initialize the recognizer and IBM Watson Text to Speech
recognizer = sr.Recognizer()

# IBM Watson API key
api_key = 'JCoD4sHVpURg-mRU2Z2M7AdpNhnc5rYJFSBeaK7qUk5H'

# Initialize IBM Watson TTS service
authenticator = IAMAuthenticator(api_key)
text_to_speech = TextToSpeechV1(
    authenticator=authenticator
)
text_to_speech.set_service_url(
    'https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/9eea1d81-0642-4cd7-8560-2782ee6d4ff1'
)

def text_to_speech_function(text):
    if text.strip():
        print("PROGRAM --> ", text)

        # Convert text to speech and save it as a WAV file
        with open('speech.wav', 'wb') as audio_file:
            audio_file.write(
                text_to_speech.synthesize(text, voice='en-GB_CharlotteV3Voice',
                                          accept='audio/wav').get_result().content
            )

        try:
            # Play using play_buffer() with file handling
            with wave.open('speech.wav', 'rb') as wave_file:
                # Read wave file
                wave_data = wave_file.readframes(wave_file.getnframes())

                # Play the buffer
                play_obj = sa.play_buffer(wave_data, num_channels=wave_file.getnchannels(),
                                          bytes_per_sample=wave_file.getsampwidth(), sample_rate=wave_file.getframerate())
                play_obj.wait_done()

            # Remove the file after playing
            os.remove('speech.wav')

        except KeyboardInterrupt:
            pass

def box1():
    print("box 1")
    # Add kinematics code for placing in box 1
    text_to_speech_function("Placing object in box 1")

def box2():
    print("box 2")
    # Add kinematics code for placing in box 2
    text_to_speech_function("Placing object in box 2")

def box3():
    print("box 3")
    # Add kinematics code for placing in box 3
    text_to_speech_function("Placing object in box 3")

def box4():
    print("box 4")
    # Add kinematics code for placing in box 4
    text_to_speech_function("Placing object in box 4")

continue_program = True

while continue_program:
    # Set up the microphone input
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("--- LISTENING TO COMMAND ---")

        try:
            # Listen for a command with a timeout and phrase time limit
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)  # Adjust these values
            print("Recognizing...")

            # Recognize speech using Google Web Speech API
            text = recognizer.recognize_google(audio)
            
            # Changeable Commands
            if "quit" in text:
                print("--- ENDING PROGRAM ---")
                text_to_speech_function("Ending program")
                continue_program = False
            elif "syringe" in text:
                box1()  # Places object in the first box
            elif "small" in text:
                box2()  # Places object in the second box
            elif "medium" in text:
                box3()  # Places object in the third box
            elif "large" in text:
                box4()  # Places object in the fourth box
        

        except sr.UnknownValueError:
            print("Error: voice misunderstood.")
      
        except sr.RequestError:
            print("Error: connecting to the speech service.")
            text_to_speech_function("Sorry, there was an issue connecting to the speech service.")
