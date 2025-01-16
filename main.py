from telethon import TelegramClient, events
from dotenv import load_dotenv
import os

# config
chat_id = -1002367854241  # ID чата, куда пересылать сообщения # -4698701054
chat_id = -4698701054  # ID чата, куда пересылать сообщения # -4698701054
thread_id = 3450  # ID топика, куда пересылать сообщения
channel_link = 'https://t.me/tempiuasygbdiuasgdbua'
target_words = [
    'джаз', 'джазовый', 'джазовую', 'ищу', 'добрый день'
]

load_dotenv()
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
bot_token = os.getenv("BOT_TOKEN")

client = TelegramClient('session_name', api_id, api_hash)
bot_client = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)


@client.on(events.NewMessage(chats=channel_link))
async def handler(event):
    message = event.message

    found_words = []
    for target_word in target_words:
        if target_word.lower() in message.message.lower():
            found_words.append(target_word)

    if len(found_words) > 0:
        message_link = f"https://t.me/{event.chat.username}/{message.id}"
        found_words_str = ', '.join(found_words)
        text = f"Найденные слова: {found_words_str}\n\n{message.message}\n\nСсылка: {message_link}"
        try:
            sent_message = await bot_client.send_message(
                chat_id, text,
                reply_to=thread_id,
            )
            if sent_message:
                print(f"Сообщение успешно отправлено: {sent_message.id}")
            else:
                print("Не удалось отправить сообщение.")
        except Exception as e:
            print(f"Ошибка при отправке сообщения: {e}")


async def main():
    await client.start()
    print("Клиент запущен. Ожидаю новые сообщения.")
    await client.run_until_disconnected()


if __name__ == "__main__":
    client.loop.run_until_complete(main())
