from transformers import AutoModelForCausalLM, AutoTokenizer
import pyttsx3
import speech_recognition as sr
import os
import json

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 0.9)

# Load pre-trained model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")

# Function to save training data
def train_data(new_data, file_path="custom_data.json"):
    if not os.path.exists(file_path):
        with open(file_path, "w") as file:
            json.dump([], file)
    with open(file_path, "r") as file:
        data = json.load(file)
    data.append(new_data)
    with open(file_path, "w") as file:
        json.dump(data, file)
    print("Data has been added and saved.")

# Function for chatbot response
def get_response(input_text):
    input_ids = tokenizer.encode(input_text + tokenizer.eos_token, return_tensors="pt")
    chat_history_ids = model.generate(input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)
    response = tokenizer.decode(chat_history_ids[:, input_ids.shape[-1]:][0], skip_special_tokens=True)
    return response

# Function for speech-to-text
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand that.")
            return ""
        except sr.RequestError:
            print("Request error. Please check your connection.")
            return ""

# Function for text-to-speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

def chatbot():
    print("Welcome to the AI Chatbot!")
    print("Type 'audio' to use voice input/output, or 'text' to type.")
    print("Type 'exit' to quit.")
    chat_mode = input("Choose your mode (audio/text): ").strip().lower()
    if chat_mode == "audio":
        while True:
            user_input = listen()
            if user_input.lower() == "exit":
                speak("Goodbye!")
                break
            response = get_response(user_input)
            print(f"AI: {response}")
            speak(response)
    elif chat_mode == "text":
        while True:
            user_input = input("You: ").strip()
            if user_input.lower() == "exit":
                print("Goodbye!")
                break
            response = get_response(user_input)
            print(f"AI: {response}")
    else:
        print("Invalid mode. Please restart and choose 'audio' or 'text'.")

if __name__ == "__main__":
    chatbot()

# to run python3 chatbot.py