# Discount Bot
- A cloud-based bot that hands out discount codes on Telegram.[^1]

## Key Features
- Sends a list with company names to the user from which to choose.
- Based on the user's choice, the bot returns a discount code with instructions on how to use the code.
- Any input by the user returns a list with company names. This is to make the user experience as simple as possible.
- Insults, however, will cause the bot to respond differently.

## How to Use
- Use Telegram's bot "BotFather" to create a new bot account.
- Once a new bot account is created, you'll receive an access token for your bot's API.
- Insert the token in [constants.py](https://github.com/Tomislav-Mi/DiscountBot/blob/main/constants.py) > ```API_KEY = "[Your api key goes here.]"```.
- Upload the code to a server, run [main.py](https://github.com/Tomislav-Mi/DiscountBot/blob/main/main.py) and keep it running at all time.[^2]

## Link to Live Version
- Link to Discount Bot: https://t.me/discount_beep_bot



[^1]: First project that is based on my own idea. The idea came whilst talking to my brother over the phone. After I had hung up I rushed to the computer to code it down. 
[^2]: The code is simple but I had great fun writing it, digging through the documentation of Python Telegram Bot’s library (https://python-telegram-bot.readthedocs.io/en/stable/), and finding a solution on how to run the code 24/7 (ended up with https://www.pythonanywhere.com/).
