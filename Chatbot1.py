import random

class SimpleChatbot:
    def __init__(self):
        self.context = {}

    def greet(self):
        return "Hello! I'm your friendly chatbot. How can I assist you today?"

    def farewell(self):
        return "Goodbye! If you have more questions, feel free to ask anytime."

    def handle_basic_questions(self, question):
        responses = {
            "How are you?": ["I'm doing well, thank you!", "I'm just a program, but I'm here to help."],
            "What's your name?": ["I don't have a name, you can call me Chatbot.", "I'm just a virtual assistant."],
            "What can you do?": ["I can answer questions, provide information, and assist you.", "I'm here to help with anything you need."],
            "Who created you?": ["I was created by a developer using Python.", "My creator is a human programmer."],
            "Can you tell a joke?": ["Why don't scientists trust atoms? Because they make up everything!", "Sure, here's a joke for you."],
        }

        return random.choice(responses.get(question, ["I'm not sure how to answer that."]))

    def ask_user_questions(self):
        questions = ["How can I help you today?", "Is there anything specific you'd like to know?", "Do you have any questions for me?"]
        user_responses = []

        for question in questions:
            user_answer = input(question + "\nUser: ")
            user_responses.append(user_answer)

        return user_responses

    def chat(self):
        print(self.greet())

        while True:
            user_input = input("User: ")

            if user_input.lower() in ["bye", "exit", "quit"]:
                print(self.farewell())
                break

            if not user_input.strip():
                print("I'm sorry, but I didn't understand your input. Could you please try again?")
                continue

            if "previous_question" in self.context:
                response = self.handle_basic_questions(self.context["previous_question"])
                print(f"Chatbot: {response}")
                del self.context["previous_question"]
            else:
                print("I'm not sure how to respond. Can you please ask me a question?")
            
            self.context["previous_question"] = user_input

        print("Chat session ended.")

if __name__ == "__main__":
    chatbot = SimpleChatbot()
    chatbot.chat()
