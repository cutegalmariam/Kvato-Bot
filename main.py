from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Final = '6479166117:AAEcBK7JNwiJXX8Z_2WI0Jo3kNJHFmrs3t8'
BOT_USERNAME: Final = '@kvato_botuka_bot'


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE ):
    await update.message.reply_text('Hi, thanks for choosing me to discuss the most ground-braking philosophical questions.')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE ):
    await update.message.reply_text('AY, I am a bot! Ask, me something or I will leave, got stuff to do!')


async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE ):
    await update.message.reply_text('Dis a custom command')


#response


def response_handler(text: str) -> str:
    text_changed: str = text.lower()
    if 'hello' in text_changed:
        return 'hi!'
    if 'gamarjoba' in text_changed:
        return 'gagimarjos, brat'
    if 'how are you?' in text_changed:
        return 'good, duh!'
    return 'sorry, broski I do not speak that language!'


async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text #this is an incoming message
    response: str = response_handler(text)

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = response_handler(new_text)
        else:
            return

    else:
        response_handler(text)

    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


if __name__ == '__main__':
    print('bot started')
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    app.add_handler(MessageHandler(filters.TEXT, message_handler))
    app.add_error_handler(error)
    print('polling')
    app.run_polling(poll_interval=2)




