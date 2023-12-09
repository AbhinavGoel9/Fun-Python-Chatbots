
# Import necessary modules
import telegram
from telegram.ext import Updater, CommandHandler
import requests
import json

# Replace 'TOKEN' with your Telegram Bot API key obtained from BotFather
updater = Updater(token='TOKEN', use_context=True)
dispatcher = updater.dispatcher

# Define command handlers

def hello(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Hello, World')

hello_handler = CommandHandler('hello', hello)
dispatcher.add_handler(hello_handler)

def summary(update, context):
    response = requests.get('https://api.covid19api.com/summary')
    if(response.status_code == 200):
        data = response.json()
        global_summary = json.dumps(data['Global'], indent=2)
        context.bot.send_message(chat_id=update.effective_chat.id, text=global_summary)
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Error, something went wrong.")

corona_summary_handler = CommandHandler('summary', summary)
dispatcher.add_handler(corona_summary_handler)

# Start polling to receive messages
updater.start_polling()
```

### Additional Notes:

- Replace `'TOKEN'` with the actual Telegram Bot API key obtained from BotFather.
- The code sets up handlers for two commands: `/hello` and `/summary`.
- The `/hello` command responds with "Hello, World."
- The `/summary` command fetches global COVID-19 summary information using an API and responds with the data.
- Ensure that you have the `python-telegram-bot` package installed (`pip install python-telegram-bot`) before running the code.
- Customize the code to add more functionalities or commands to your Telegram bot.

This `bot.py` file contains the essential code for setting up a basic Telegram bot with the specified functionalities.
