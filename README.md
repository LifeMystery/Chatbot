AI Chatbot with Text and Audio Interaction
This project is a Python-based AI chatbot that supports both text and audio interaction. It uses OpenAI's DialoGPT for conversational responses, Google Speech Recognition for speech-to-text, and pyttsx3 for text-to-speech functionality. The chatbot is also extensible, allowing you to train it with custom data.

---------------------------------------------------------------------------------------------------------------

Features
Dual Interaction Modes:
Text input/output via the console.
Audio input/output using a microphone and speaker.
Pre-trained Model: Powered by DialoGPT for human-like conversational responses.
Speech-to-Text: Converts user speech to text using Google's Speech Recognition API.
Text-to-Speech: Reads chatbot responses aloud using pyttsx3.
Custom Training: Allows adding new data for training and saving it locally.

---------------------------------------------------------------------------------------------------------------

Installation

1. Clone the Repository:
git clone <repository_url>
cd <repository_folder>

2. Install Dependencies: Use pip to install the required Python packages:
pip install transformers pyttsx3 SpeechRecognition

NB! If you encounter issues with pyaudio, install it using:
* On linux: 
sudo apt-get install portaudio19-dev
pip install pyaudio
* On maOS:
brew install portaudio
pip install pyaudio
* On Windows: Download and install the appropriate .whl file from PyPI, then run:
pip install <downloaded_whl_file>

---------------------------------------------------------------------------------------------------------------

Usage

1. Run the Program:
python3 chatbot.py
2. Choose an Interaction Mode:
    * audio: Interact with the chatbot using your microphone and hear its responses.
    * text: Interact by typing your inputs in the console.
3. Exit the Chatbot: Type exit to end the session.

---------------------------------------------------------------------------------------------------------------
File Structure
* chatbot.py: Main script for running the chatbot.
* custom_data.json: File for saving custom training data (automatically created if it doesn't exist).

--------------------------------------------------------------------------------------------------------------

How It Works

1. Initialization:
    * Loads the pre-trained DialoGPT model and tokenizer.
    * Configures the text-to-speech engine with a default rate and volume.
2. Modes:
    * Text Mode: Users type inputs, and the chatbot responds in text.
    * Audio Mode: Users speak inputs into a microphone, and the chatbot responds verbally.
3. Response Generation:
    * Converts user input into tokens using the tokenizer.
    * Uses DialoGPT to generate a conversational response.
    * Outputs the response in text and/or speech based on the selected mode.
4. Training Data:
    * New data can be saved to custom_data.json using the train_data function.

--------------------------------------------------------------------------------------------------------------

Future Enhancements
* Add support for loading and incorporating custom training data during model fine-tuning.
* Improve conversation continuity by maintaining chat history across exchanges.
* Add a graphical user interface (GUI) for easier interaction.

--------------------------------------------------------------------------------------------------------------

Troubleshooting

Common Issues:
* Microphone Not Detected: Ensure your microphone is connected and configured correctly. Test it with other applications.
* Speech Recognition Errors: Check your internet connection as Google's Speech Recognition API requires it.
* Missing Dependencies: Ensure all required Python packages are installed.