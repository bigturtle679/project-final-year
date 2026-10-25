import re
import random

intents = {
    "greeting": {
        "patterns": ["hello", "hi", "hey", "good morning",
                     "good evening", "good afternoon"],
        "responses": ["Hello!", "Hi there!", "Greetings!",
                      "Hey! How can I help you?"]
    },

    "farewell": {
        "patterns": ["bye", "goodbye", "see you later",
                     "farewell", "take care"],
        "responses": ["Goodbye!", "Take care!",
                      "See you later!", "Have a great day!"]
    },

    "thanks": {
        "patterns": ["thank you", "thanks", "thank you so much",
                     "much appreciated", "thanks a lot"],
        "responses": ["You're welcome!", "Glad I could help!",
                      "Anytime!", "No problem!"]
    },

    "bot_name": {
        "patterns": ["what is your name", "who are you",
                     "tell me your name"],
        "responses": ["I am your friendly chatbot!",
                      "You can call me Chatbot!",
                      "I am a chatbot created to help you."]
    },

    "bot_purpose": {
        "patterns": ["what can you do", "how can you help me",
                     "what do you do"],
        "responses": ["I can answer basic questions and chat with you!",
                      "I am here to help you.",
                      "I can respond to simple queries."]
    },

    "feeling": {
        "patterns": ["how are you", "how are you doing",
                     "are you okay"],
        "responses": ["I am doing great!",
                      "I am feeling helpful today!",
                      "I am ready to help you."]
    },

    "age": {
        "patterns": ["how old are you", "what is your age",
                     "when were you created"],
        "responses": ["I do not have an age like humans.",
                      "Age is just a number for a chatbot!"]
    },

    "weather": {
        "patterns": ["what is the weather",
                     "how is the weather today",
                     "tell me the weather"],
        "responses": ["I cannot check live weather right now.",
                      "Please check your weather app for updates."]
    },

    "joke": {
        "patterns": ["tell me a joke", "make me laugh",
                     "tell a joke"],
        "responses": [
            "Why did the computer go to the doctor? It had a virus!",
            "I would tell you a UDP joke, but you might not get it!"
        ]
    },

    "help": {
        "patterns": ["help me", "i need help",
                     "can you help me"],
        "responses": ["Sure! What do you need help with?",
                      "Of course! How can I assist you?"]
    }
}


def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    tokens = text.split()
    return tokens


def match_intent(processed_input):
    for intent, data in intents.items():
        for pattern in data["patterns"]:
            processed_pattern = preprocess(pattern)

            if all(word in processed_input
                   for word in processed_pattern):
                return intent

    return None


def get_response(intent):
    return random.choice(intents[intent]["responses"])


def chatbot():
    print("Chatbot: Hello! I am your chatbot.")
    print("Type 'bye' or 'exit' to end the conversation.")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() in ["bye", "exit"]:
            print("Chatbot: Goodbye!")
            break

        processed_input = preprocess(user_input)
        matched_intent = match_intent(processed_input)

        if matched_intent:
            response = get_response(matched_intent)
        else:
            response = "Sorry, I could not understand that."

        print("Chatbot:", response)


if __name__ == "__main__":
    chatbot()
