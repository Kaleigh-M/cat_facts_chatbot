import tkinter as tk
import requests
from tkinter import font
import re

# Variable to track if the last response was a cat fact
last_response_was_cat_fact = False

def get_cat_fact():
    response = requests.get("https://meowfacts.herokuapp.com/")
    if response.status_code == 200:
        fact = response.json().get("data")[0]
        return fact
    else:
        return "Sorry, I couldn't fetch a cat fact right now."

# Function to send a message and get a response
def send_message(event=None):
    user_input = entry.get().strip().lower() 
    if user_input:
        chat_log.config(state=tk.NORMAL)
        
        # Insert user message with a newline
        chat_log.insert(tk.END, f"You: {user_input}\n\n", "user")  
        
        chat_log.insert(tk.END, "Bot: ...\n\n", "bot")  
      
        chat_log.config(state=tk.DISABLED)
        entry.delete(0, tk.END)
        
        root.after(1000, process_response, user_input)

# Function to check if user input contains a request for a cat fact
def is_cat_fact_request(user_input):
    # Common ways people may ask for a fact
    cat_fact_phrases = [
        "cat fact", "give me a cat fact", "tell me a cat fact", "cat facts",
        "i want a cat fact", "can you tell me a cat fact", "share a cat fact", 
        "what's a cat fact", "show me a cat fact", "fact about cats"
    ]
    return any(phrase in user_input for phrase in cat_fact_phrases)

# Function to check if user input is asking for more facts
def is_more_fact_request(user_input):
    # Common phrases for requesting more facts
    more_phrases = ["another", "more", "one more", "give me more", "again", "more cat facts", "what else"]
    return any(phrase in user_input for phrase in more_phrases)
  
def process_response(user_input):
    global last_response_was_cat_fact
    chat_log.config(state=tk.NORMAL)
    
    chat_log.delete("end-3lines", tk.END)

    if is_cat_fact_request(user_input):
        response = get_cat_fact()
        last_response_was_cat_fact = True
 
    elif is_more_fact_request(user_input) and last_response_was_cat_fact:
        response = get_cat_fact()
    else:
        response = "Sorry, I don't understand that. Please ask for a cat fact."
        last_response_was_cat_fact = False

    # Insert bot response
    chat_log.insert(tk.END, f"Bot: {response}\n\n", "bot")
    
    # Disable chat log for editing
    chat_log.config(state=tk.DISABLED)

# Create the main window
root = tk.Tk()
root.title("Cat Facts Bot")
root.geometry("700x800")

# fonts and colors
font_style = font.Font(family="Sans", size=12)
bg_color = "darkseagreen4"
text_color = "#333333"
user_message_color = "#007bff"
bot_message_color = "#28a745"
button_color = "darkseagreen3"
button_text_color = "#ffffff"
entry_bg_color = "#f0f0f0"

root.configure(bg=bg_color)

# Create the chat log
chat_log = tk.Text(root, state=tk.DISABLED, bg="white", fg=text_color, font=font_style, wrap=tk.WORD)
chat_log.tag_configure("user", foreground=user_message_color)
chat_log.tag_configure("bot", foreground=bot_message_color)
chat_log.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Create a frame for entry and button with bg color
input_frame = tk.Frame(root, bg=bg_color)
input_frame.pack(padx=10, pady=10, fill=tk.X)

# Create the entry box for user input with styling
entry = tk.Entry(input_frame, width=60, font=font_style, borderwidth=2, relief="sunken", bg=entry_bg_color)
entry.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X, expand=True)

send_button = tk.Button(input_frame, text="Send", command=send_message, bg=button_color, fg=button_text_color, font=font_style, relief="raised")
send_button.pack(side=tk.RIGHT, padx=5, pady=5)

entry.bind("<Return>", send_message)

root.mainloop()
