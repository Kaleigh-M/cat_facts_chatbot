# cat_facts_chatbot

# Cat Facts Bot

This project is a simple chatbot built using Python's `Tkinter` library for the GUI, which provides random cat facts on request. It listens to user input, responds with a cat fact when requested, and displays the conversation in a user-friendly chat window.

## Features
- **Get Random Cat Facts**: Ask for a cat fact, and the bot fetches one from an API.
- **Multiple Requests**: You can ask for more cat facts after the initial response.
- **Simple and Clean UI**: A user-friendly chat interface with styled messages for both the user and the bot.
- **Real-time Responses**: The bot shows a short delay with a "thinking" message before responding.

## How It Works
1. The bot responds to user inputs containing phrases like "cat fact" or "give me a cat fact".
2. It fetches a random cat fact from the [Meow Facts API](https://meowfacts.herokuapp.com/).
3. The user can continue to ask for more facts after the first one.
4. The chatbot is case-insensitive and uses basic pattern matching to identify cat fact requests.

## Dependencies
- **Python 3.x**
- **Tkinter**: For creating the GUI. It comes pre-installed with Python.
- **Requests**: To make API calls. Install it using:
  ```
  pip install requests
  ```

## How to Run the Project
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/cat-facts-bot.git
   ```
2. Navigate to the project directory:
   ```bash
   cd cat-facts-bot
   ```
3. Run the script:
   ```bash
   python cat_facts_bot.py
   ```

## Project Structure
- `cat_facts_bot.py`: The main script that contains the code for the chatbot and the GUI.
  
## Example Usage
1. Open the bot and type "Give me a cat fact".
2. The bot will respond with a random cat fact.
3. To get another fact, type "another" or a similar request.
4. If the bot doesn't recognize the input, it will ask you to request a cat fact.

## Screenshots
![cat-fact-bot-picture](https://github.com/user-attachments/assets/1259607c-f4c8-446b-bc27-1bf6c9f8d19d)



## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contributions
Feel free to fork the repository and submit pull requests to add new features, fix bugs, or improve the project.
