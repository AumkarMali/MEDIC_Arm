import os
import wave
import simpleaudio as sa
import speech_recognition as sr
import openai
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from pymongo import MongoClient
import time
import serial
import re

# IBM Watson API key for text-to-speech
api_key = 'JCoD4sHVpURg-mRU2Z2M7AdpNhnc5rYJFSBeaK7qUk5H'

# Set up OpenAI API Key
openai.api_key = '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'

# Initialize the recognizer and IBM Watson Text to Speech
recognizer = sr.Recognizer()

# Initialize IBM Watson TTS service
authenticator = IAMAuthenticator(api_key)
text_to_speech = TextToSpeechV1(
    authenticator=authenticator
)
text_to_speech.set_service_url(
    'https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/9eea1d81-0642-4cd7-8560-2782ee6d4ff1'
)

# Set up serial communication with Arduino
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
time.sleep(2)  # Allow time for serial connection to establish



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
            
def send_command_to_arduino(command, delay=16):
    ser.reset_input_buffer()
    ser.write(command.encode() + b"\n")
    print(f"Sent command to Arduino: {command}")
    time.sleep(delay)  # Increased delay to give enough time for robot movement

def box1():
    print("box 1")
    text_to_speech_function("Placing object in box 1")
    send_command_to_arduino("box1")

def box2():
    print("box 2")
    text_to_speech_function("Placing object in box 2")
    send_command_to_arduino("box2")

def box3():
    print("box 3")
    text_to_speech_function("Placing object in box 3")
    send_command_to_arduino("box3")

def box4():
    print("box 4")
    text_to_speech_function("Placing object in box 4")
    send_command_to_arduino("box4")
    
def box5():
    print("box ")
    text_to_speech_function("Placing object in box 5")
    send_command_to_arduino("box5")

def box6():
    print("box 6")
    text_to_speech_function("Placing object in box 6")
    send_command_to_arduino("box6")


def addCommand():
    # Initial prompt for adding a command
    text_to_speech_function("Please say the command in the format 'add [command name] to [box number]'")
    print("Listening for command...")

    # Listening for full sentence input
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=20)
            print("Recognizing...")
            user_input = recognizer.recognize_google(audio).strip().lower()
            print(f"User said: {user_input}")

            # Extracting the command name and box number from the sentence
            match = re.search(r"add (\w+) to (first|second|third|fourth|fifth) box", user_input)

            if match:
                command_name = match.group(1).strip()
                box_name = match.group(2).strip()

                # Map the box names to actual box numbers
                box_mapping = {
                    "first": "one",
                    "second": "two",
                    "third": "three",
                    "fourth": "four",
                    "fifth": "five",
                    "sixth": "six"
                }

                # Retrieve the box number from the mapping
                if box_name in box_mapping:
                    box_number = box_mapping[box_name]

                    # Prepare data to be inserted into MongoDB
                    data = {
                        "name": command_name,
                        "box": box_number
                    }

                    # Insert into MongoDB
                    print("Inserting command into MongoDB...")
                    collection.insert_one(data)
                    text_to_speech_function(f"Command {command_name} for box {box_name} added successfully.")

                else:
                    text_to_speech_function(f"Sorry, I couldn't recognize the box number {box_name}.")
                    print(f"Error: Box number '{box_name}' not recognized.")
            else:
                text_to_speech_function("Sorry, I couldn't understand the command format.")
                print("Error: Invalid command format. Expected format: 'add [command] to [box]'")

        except sr.UnknownValueError:
            print("Error: voice misunderstood.")
            text_to_speech_function("Sorry, I couldn't understand that. Could you please repeat?")
        
        except sr.RequestError:
            print("Error: connecting to the speech service.")
            text_to_speech_function("Sorry, there was an issue connecting to the speech service.")
        
        except Exception as e:
            print(f"Error: {str(e)}")
            text_to_speech_function("Sorry, there was an error processing your request. Please try again.")

    

def deleteCommand():
    # Connect to MongoDB
    client = MongoClient("mongodb+srv://aumkarmali539:AM20060305!_ilovesushi@clusterdata.gmzht.mongodb.net/?retryWrites=true&w=majority&appName=ClusterData")
    db = client["RobotMotion"]  # Database name
    collection = db["motion"]  # Collection name
    
    # Prompt for command name to delete
    text_to_speech_function("Enter the command name to delete")
    print("Listening for command name to delete...")

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)  # Adjust ambient noise before listening
        try:
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=10)
            print("Recognizing...")
            command_name = recognizer.recognize_google(audio)
            print(f"Command to delete: {command_name}")

            # Search for the command by name
            result = collection.delete_one({"name": command_name.lower()})

            if result.deleted_count > 0:
                text_to_speech_function(f"Command {command_name} deleted successfully.")
                print(f"Command {command_name} deleted successfully.")
            else:
                text_to_speech_function(f"No command found with the name {command_name}.")
                print(f"No command found with the name {command_name}.")
        
        except sr.UnknownValueError:
            print("Error: voice misunderstood.")
            text_to_speech_function("Sorry, I couldn't understand the command name.")
        except sr.RequestError:
            print("Error: connecting to the speech service.")
            text_to_speech_function("Sorry, there was an issue connecting to the speech service.")
        except Exception as e:
            print(f"Error: {str(e)}")
            text_to_speech_function("An error occurred while deleting the command.")




def start_medical_conversation():
    """ Starts a medical conversation using OpenAI API until 'quit' is said """
    conversation_history = [{"role": "system", "content": "You are a helpful medical assistant."}]
    text_to_speech_function("How can I assist you with your medical questions today?")

    while True:
        
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            print("Listening for medical conversation...")

            try:
                audio = recognizer.listen(source, timeout=10, phrase_time_limit=30)
                print("Recognizing...")
                user_input = recognizer.recognize_google(audio)
                print(f"User said: {user_input}")
                conversation_history.append({"role": "user", "content": user_input})
                
                if "quit" in user_input.lower():
                    text_to_speech_function("Ending medical conversation")
                    break

                # Use the new Chat Completion API
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",  # Ensure you're using the correct model
                    messages=conversation_history,
                    max_tokens=50
                )

                gpt_response = response['choices'][0]['message']['content'].strip()  # Get the GPT-3 response
                text_to_speech_function(gpt_response)
                
                # Append GPT response to conversation history
                conversation_history.append({"role": "assistant", "content": gpt_response})
            
            except sr.UnknownValueError:
                print("Error: voice misunderstood.")
            except sr.RequestError:
                print("Error: connecting to the speech service.")
                text_to_speech_function("Sorry, there was an issue connecting to the speech service.")
            except Exception as e:
                print(f"Error: {str(e)}")


text_to_speech_function("Medic arm started")
time.sleep(0.2)


# MongoDB Connection
client = MongoClient("mongodb+srv://aumkarmali539:AM20060305!_ilovesushi@clusterdata.gmzht.mongodb.net/?retryWrites=true&w=majority&appName=ClusterData")
db = client["RobotMotion"]
collection = db["motion"]

while True:
    with sr.Microphone() as source:
        print("--- LISTENING TO COMMAND ---")
        recognizer.adjust_for_ambient_noise(source) 

        try:
            audio = recognizer.listen(source, timeout=None, phrase_time_limit=None)
            print("Recognizing...")
            text = recognizer.recognize_google(audio).strip().lower()

            # Retrieve all commands from MongoDB
            commands = collection.find({}, {"name": 1, "box": 1, "_id": 0})

            # Check if any stored command exists in the recognized speech
            matched_command = None
            for command_data in commands:
                # Check if 'name' field exists in the document
                if "name" in command_data:
                    command_name = command_data["name"].lower()
                    if command_name in text:  # Checking if stored command exists in speech
                        matched_command = command_data
                        break
                else:
                    print("Warning: 'name' field missing in one of the documents.")

            if matched_command:
                box_number = matched_command["box"]
                print(f"Executing command: {matched_command['name']}, sending to box {box_number}")

                if box_number == "one":
                    box1()
                elif box_number == "two":
                    box2()
                elif box_number == "three":
                    box3()
                elif box_number == "four":
                    box4()
                elif box_number == "five":
                    box5()
                elif box_number == "six":
                    box6()
                else:
                    print(f"Invalid box number: {box_number}")

            elif "quit" in text:
                print("--- ENDING PROGRAM ---")
                text_to_speech_function("Ending program")
                break
            elif "add command" in text:
                addCommand()
            elif "delete command" in text:
                deleteCommand()
            elif "assistance" in text:
                start_medical_conversation()
            else:
                print(f"Unrecognized command: {text}")

        except sr.UnknownValueError:
            print("Error: voice misunderstood.")
        except sr.RequestError:
            print("Error: connecting to the speech service.")
            text_to_speech_function("Sorry, there was an issue connecting to the speech service.")
