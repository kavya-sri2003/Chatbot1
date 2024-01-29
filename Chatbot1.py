import random

class SimpleChatbot:
    def __init__(self):
        self.context = {}

    def greet(self):
        return "Hello! I'm your simple chatbot. How can I help you today?"

    def farewell(self):
        return "Goodbye! Feel free to chat with me again."

    def handle_question(self, question):
        if "name" in question.lower():
            return "I'm just a simple chatbot, you can call me ChatGPT."
        elif "how are you" in question.lower():
            return "I'm a program, so I don't have feelings, but thanks for asking!"
        elif "what can you do" in question.lower():
            return "I can answer questions, have conversations, and more! Feel free to ask me anything."
        elif "your favorite color" in question.lower():
            return "I don't have a favorite color, but I'm here to assist you with any questions."
        elif "thank you" in question.lower():
            return "You're welcome! If you have more questions, feel free to ask."
        else:
            return "I'm sorry, I didn't quite understand that. Can you please rephrase or ask a different question?"

    def ask_user_questions(self):
        questions = ["What is your name?", "How can I assist you today?", "Tell me something interesting about yourself."]
        for i in range(3):
            user_response = input(random.choice(questions) + " ")
            self.context[f"response_{i+1}"] = user_response
            print("Great! Thanks for sharing.")

    def chat(self):
        print(self.greet())

        while True:
            user_input = input("You: ")

            if user_input.lower() == "exit":
                print(self.farewell())
                break

            response = self.handle_question(user_input)

            if "name" in user_input.lower() and "response_1" in self.context:
                response += f" By the way, nice to meet you, {self.context['response_1']}!"

            print("Chatbot:", response)

if __name__ == "__main__":
    chatbot = SimpleChatbot()
    chatbot.ask_user_questions()
    chatbot.chat()
