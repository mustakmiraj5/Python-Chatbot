import random
def chatbot():
    print("Hello! I'm a simple chatbot. How can I assist you today?")
    print("Type 'exit' to end the conversation.")

    greetings = ["Hello there!", "Yo!", "Hi!", "Hey!", "Greetings!", "What's up?", "Hi there, How's it going?"]
    well_being = ["I'm just a computer program, but thanks for asking!", "I'm doing well, thanks for asking!", "I'm just a chatbot, but I'm here to help!", "I'm good, thanks for asking!"]
    weather = ["I'm sorry, I don't have access to real-time weather information. I guess it's nice outside!", "I'm sorry, I don't have access to real-time weather information. I guess it's raining outside!", "I'm sorry, I don't have access to real-time weather information. I guess it's snowing outside!", "I'm sorry, I don't have access to real-time weather information. I guess it's cloudy outside!", "I'm sorry, I don't have access to real-time weather information. I guess it's windy outside!", "I'm sorry, I don't have access to real-time weather information. I guess it's sunny outside!"]
    name = ["I'm just a chatbot.", "I'm am Thanos!.", "I'm just a chatbot. You can call me ChatBot.", "I'm just a chill guy.", "I'm just a chatbot. You can call me Mini Bot.", "I'm just a chatbot. You can call me PyChat."]
    thanks = ["You're welcome!", "No problem!", "My pleasure!", "Don't mention it!", "Anytime!", "You're welcome!"]
    while True:
        user_input = input("You: ").lower().strip()

        if user_input in ["quit", "exit"]:
            print("Chatbot: Goodbye!")
            break
        if "hello" in user_input or "hi" in user_input:
            print("Chatbot:", random.choice(greetings))
        elif "how are you" in user_input:
            print("Chatbot:", random.choice(well_being))
        elif "what's your name" in user_input:
            print("Chatbot:", random.choice(name))
        elif "what can you do" in user_input:
            print("Chatbot: I can answer simple questions and have basic conversations.")
        elif "thanks" in user_input:
            print("Chatbot:", random.choice(thanks))
        elif "what is the weather today" in user_input:
            print("Chatbot:", random.choice(weather))
        else:
            print("Chatbot: I'm sorry, I don't understand. Can you please rephrase?")

if __name__ == "__main__":
    chatbot()