# Telegram Bot: AI Assistant

This project demonstrates the creation of a simple Telegram bot that answers users' questions using Gemini AI.

## Features

- Sends a welcome message in response to the /start command.
- Forwards the text sent by users to the Gemini AI model to receive an answer.

## Requirements

- Python 3.7 or higher
- The following Python packages:
  - python-telegram-bot
  - openai

To install the packages, run the following command in your terminal:

pip install python-telegram-bot openai

## Setup

### Telegram Bot Token

1. Open Telegram and contact **BotFather**.
2. Use the `/newbot` command to create a new bot.
3. BotFather will provide you with a token. Add this token to your code (for example, in the `TOKEN` variable).

### Gemini AI Token

1. Create a Google Cloud account or sign in with your existing account.
2. Create a new project and enable the **Gemini AI API**.
3. Create an **API Key** and add the token to your code.

## Project Structure

- **aibot.py**: Handles the connection with Gemini AI and response functions.
- **telebot.py**: Sets up the Telegram bot, commands, and message handlers.

## Running the Bot

1. Add your tokens to the appropriate variables in `aibot.py` and `telebot.py`.
2. Run the following command in your terminal:

python telebot.py

Your bot will start and wait for messages. Test your bot by sending the `/start` command.

## License

This project is licensed under the MIT License.
