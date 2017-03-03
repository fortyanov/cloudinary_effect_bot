import sys
import time
import telepot
from pprint import pprint

from cloudinary_utils import upload_photo, add_filter

BOT_TOKEN = '276304489:AAGIn6JF1AtTBKhzNXSJ8rqcEg9VpLXjIwY'
# BOT_TOKEN = sys.argv[1] # передавать токен в качестве параметра


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)
    pprint(msg)

    if content_type == 'text':
        bot.sendMessage(chat_id, 'received %s' % msg['text'])

    if content_type == 'photo':
        telegram_file = bot.getFile(msg['photo'][-1]['file_id'])
        telegram_url = 'https://api.telegram.org/file/bot%s/%s' % (BOT_TOKEN, telegram_file['file_path'])
        cloudinary_file = upload_photo(telegram_url)
        cloudinary_url = add_filter(cloudinary_file['public_id'])
        bot.sendPhoto(chat_id, cloudinary_url)


if __name__ == '__main__':
    bot = telepot.Bot(BOT_TOKEN)
    print(bot.getMe())

    # pprint(bot.getUpdates(offset=567168723)) # значения брать из update_id
    # pprint(bot.getUpdates())

    bot.message_loop(handle)

    while True:
        time.sleep(10)
