def chatbot():
    print("Welcome to the AI Chatbot!")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        print(f"AI: You said '{user_input}'.")
        
if __name__ == "__main__":
    chatbot()
    # to run this type python3 chatbot.py
