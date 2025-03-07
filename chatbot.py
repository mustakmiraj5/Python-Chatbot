def chatbot():
    print("Hello! I'm a simple chatbot. How can I assist you today?")
    print("Type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ").lower().strip()

        if user_input in ["quit", "exit"]:
            print("Chatbot: Goodbye!")
            break

        if "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hello there!")
        elif "how are you" in user_input:
            print("Chatbot: I'm just a computer program, but thanks for asking!")
        elif "what's your name" in user_input:
            print("Chatbot: I'm just a chatbot. You can call me Chatbot.")
        elif "what can you do" in user_input:
            print("Chatbot: I can answer simple questions and have basic conversations.")
        elif "thanks" in user_input:
            print("Chatbot: You're welcome!")
        elif "what is the weather today" in user_input:
            print("Chatbot: I'm sorry, I don't have access to real-time weather information. I guess it's nice outside!")
        else:
            print("Chatbot: I'm sorry, I don't understand. Can you please rephrase?")

if __name__ == "__main__":
    chatbot()