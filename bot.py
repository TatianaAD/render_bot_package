
import logging
from telegram import Update, InputFile
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

# Включаем логгирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Токен из переменной окружения
TOKEN = os.getenv("BOT_TOKEN")

# Канал, на который проверяется подписка
CHANNEL_USERNAME = "@tm_ad_gsr"

# Текст при старте
WELCOME_TEXT = """Привет 👋
Я — Татьяна, архитектор и GSR-специалист.

Ты здесь, потому что чувствуешь, что с пространством — что-то не то.
Если ловишь себя на раздражении дома — возможно, дело не в тебе, а в среде.

Я подготовила для тебя чек-лист:
5 главных ошибок, которые влияют на твоё состояние через интерьер.

🔗 Подпишись на канал @tm_ad_gsr — и бот сразу отправит тебе его 🎁

Здесь — проектирование внешнего и внутреннего. Загляни 🌿
"""

# Обработчик команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    chat_member = await context.bot.get_chat_member(chat_id=CHANNEL_USERNAME, user_id=user_id)

    if chat_member.status in ("member", "administrator", "creator"):
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Вот твой файл 📎")
        await context.bot.send_document(chat_id=update.effective_chat.id, document=InputFile("5_errors_interior_state_detailed.pdf"))
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=WELCOME_TEXT)

# Запуск приложения
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
