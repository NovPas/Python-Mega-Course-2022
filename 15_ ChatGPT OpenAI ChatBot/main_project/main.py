import tkinter as tk
from tkinter import Tk


class ChatForm(Tk):
    def __init__(self):
        super().__init__()

        # Set the window title and size
        self.title("Chat GPT")
        self.geometry("400x390")
        self.resizable(False, False)  # Disable window resizing

        self.send_button1 = None
        self.entry1 = None
        self.chat_listing1 = None

        self.create_widgets()

    def create_widgets(self):
        self.chat_listing1 = tk.Text(self, height=20, width=47)
        self.chat_listing1.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        self.chat_listing1.configure(state='disabled')  # Set the text widget as read-only

        self.entry1 = tk.Entry(self, width=54)
        self.entry1.grid(row=1, column=0, padx=10, pady=5)
        self.entry1.focus()  # Set the initial focus to the entry widget
        self.entry1.bind("<Return>", self.send_message_enter)  # Bind Enter key press to callback function

        self.send_button1 = tk.Button(self, text="Send", command=self.send_message)
        self.send_button1.grid(row=1, column=1, padx=5, pady=5)

    def send_message(self):
        message = self.entry1.get()
        # Process the message (e.g., send it to a chat server)
        # Update the chat listing field with the sent message
        print(message)
        self.entry1.delete(0, tk.END)  # Clear the input field

    def send_message_enter(self, event):
        self.send_message()


# Create the main window
window_main = ChatForm()

# Start the Tkinter event loop
window_main.mainloop()
