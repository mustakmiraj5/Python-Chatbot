def chatbot():
    print("Hello! I'm a simple chatbot. How can I assist you today?")
    print("Type 'exit' to end the conversation.")

    responses = {
            "hello": "Hello there!",
            "hi": "Yo!",
            "how are you": "I'm just a computer program, but thanks for asking!",
            "what's your name": "I'm just a chatbot. You can call me Chatbot.",
            "what can you do": "I can answer simple questions and have basic conversations.",
            "thanks": "You're welcome!",
            "what is the weather today": "I'm sorry, I don't have access to real-time weather information. I guess it's nice outside!"

        }
    while True:
        user_input = input("You: ").lower().strip()

        if user_input in ["quit", "exit"]:
            print("Chatbot: Goodbye!")
            break
        
        response = "Hmm, I’m not sure what to say to that. Try something else!"
        for key in responses:
            if key in user_input:
                response = responses[key]
                break
        print("Chatbot:", response)

if __name__ == "__main__":
    chatbot()