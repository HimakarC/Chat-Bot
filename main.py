import tkinter as tk
from tkinter import scrolledtext

class SimpleChatbotGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Simple ChatBot")

        self.text_area = scrolledtext.ScrolledText(self.window, wrap=tk.WORD, width=50, height=15)
        self.text_area.pack(padx=10, pady=10)

        self.input_entry = tk.Entry(self.window, width=40)
        self.input_entry.pack(padx=10, pady=5)

        self.send_button = tk.Button(self.window, text="Send", command=self.send_message)
        self.send_button.pack(pady=5)

        self.conversation = []

        self.responses = {
            "hi": "Hello!",
            "hello": "Hi there!",
            "how are you": "I'm just a program, so I don't have feelings, but I'm here to help!",
            "what's your name": "I am a ChatBot.",
            'what are you doing': 'Nothing',
            "bye": "Goodbye! Have a great day!"
        }

    def send_message(self):
        user_input = self.input_entry.get().lower()
        self.conversation.append(f"You: {user_input}")
        self.text_area.insert(tk.END, f"You: {user_input}\n")
        self.input_entry.delete(0, tk.END)

        response = self.responses.get(user_input, "I'm sorry, I don't have a response for that.")
        self.conversation.append(f"ChatBot: {response}")
        self.text_area.insert(tk.END, f"ChatBot: {response}\n")

    def start(self):
        self.window.mainloop()

if __name__ == "__main__":
    chatbot_gui = SimpleChatbotGUI()
    chatbot_gui.start()
