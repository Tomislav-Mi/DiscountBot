import random
from constants import FRANCO_MANCA_CODE, FRANCO_MANCA_NAMES, FRANCO_HELP, GORILLAS_CODE, GORILLAS_NAME, GORILLA_HELP, \
    ZAPP_CODE, ZAPP_NAME, ZAPP_HELP, \
    BOLT_CODE, BOLT_NAME, BOLT_HELP, HELP_MESSAGE, SWEAR_WORDS, SAD_BOT, GETT_HELP, GETT_CODE, GETT_NAME


def error(update, context):
    print(f"Update {update} caused error {context.error}")


def return_instruction(text_input):
    if text_input in FRANCO_MANCA_NAMES:
        return FRANCO_HELP

    if text_input in GORILLAS_NAME:
        return GORILLA_HELP

    if text_input in ZAPP_NAME:
        return ZAPP_HELP

    if text_input in BOLT_NAME:
        return BOLT_HELP

    if text_input in GETT_NAME:
        return GETT_HELP


def return_list(text_input):
    if text_input in FRANCO_MANCA_NAMES:
        return FRANCO_MANCA_CODE

    if text_input in GORILLAS_NAME:
        return GORILLAS_CODE

    if text_input in ZAPP_NAME:
        return ZAPP_CODE

    if text_input in BOLT_NAME:
        return BOLT_CODE

    if text_input in GETT_NAME:
        return GETT_CODE

    if text_input in ("help", "hlp", "hep"):
        return HELP_MESSAGE

    if text_input in SWEAR_WORDS:
        return random.choice(SAD_BOT)

    return HELP_MESSAGE


def handle_message(update, context):
    text = str(update.message.text).lower()
    code_list = return_list(text)
    instruction = return_instruction(text)
    update.message.reply_text(code_list)
    update.message.reply_text(instruction)
