### README for Telegram Bot with Python

This repository contains Python code for creating a Telegram Bot using the Telegram API. The bot is designed to respond to specific commands and can perform tasks like displaying a "Hello, World" message or providing COVID-19 global summary information.

#### Steps to Get the Telegram Bot API:

1. **Create a Telegram Account:**
   If you don't have a Telegram account, create one.

2. **Find BotFather:**
   Search for BotFather on Telegram, an official bot that helps create APIs for new bots.

3. **Start the Chat:**
   In the BotFather chat, type `/start` and then `Newbot`.

4. **Bot Configuration:**
   Follow the prompts to configure your new bot, including giving it a name and a unique username.

5. **Get API Key:**
   Copy the API key provided by BotFather.

#### How to Use the Code:

1. **Install Required Packages:**
   Ensure you have the necessary packages installed using:
   ```bash
   pip install python-telegram-bot
   ```

2. **Replace TOKEN:**
   Replace `'TOKEN'` in the code with the API key obtained from BotFather.

3. **Hello World Example:**
   A simple "Hello, World" example is provided in the code. Run the script and send `/hello` to your bot on Telegram.

4. **COVID-19 Summary Example:**
   An additional example fetches global COVID-19 summary information. Send `/summary` to your bot to receive the latest data.

#### Code Files:

- **`bot.py`:**
  Contains the main code for setting up and running the Telegram bot.

#### Additional Notes:

- Ensure you have a valid API key from BotFather before running the code.
- Customize the code to add more functionalities or commands to your bot.
- For further details on the Telegram API and bot development, refer to the official [Telegram Bot API documentation](https://core.telegram.org/bots/api).

Feel free to explore the code and adapt it according to your preferences. If you encounter any issues, refer to the official documentation or seek help from the Telegram Bot community.
