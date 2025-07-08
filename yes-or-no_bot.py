import os
import random
from telegram import Update 
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

# Список ключевых слов для категории вопросов про отношения:
RELATIONSHIP_KEYWORDS = [
    "отношения", "продолжать отношения", "расставаться", "быть вместе", "жениться", "выйти замуж", 
    "любовь", "свидание", "встречаться", "брак", "развод",  "помириться"
]

# Ответы для обычных вопросов
YES = "Да"
NO = "Нет"

# Функция-обработчик входящих сообщений
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    if any(keyword in text for keyword in RELATIONSHIP_KEYWORDS):
        response = YES
    else:
        response = random.choice([YES, NO])
    await update.message.reply_text(response)

def main():
    token = os.getenv("TELEGRAM_TOKEN")
    if not token:
        print("Error: TELEGRAM_TOKEN is not set")
        return

    app = ApplicationBuilder().token(token).build()
    # ловим все текстовые сообщения, не являющиеся командами
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot is running...")
    app.run_polling()

if __name__ == '__main__':
    main()
