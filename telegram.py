from telethon import TelegramClient, events, sync
import os
import shutil

api_id = 5616424
api_hash = '51830e5b2a0aa1492d72deb5b8844b80'
client = TelegramClient('api_session', api_id, api_hash)
phonenum = '+923205420522'


@client.on(events.NewMessage(chats="Test"))
async def handler(event):
    # import pdb;pdb.set_trace()
    sender = await event.get_sender()
    message = event.to_dict().get('message').to_dict().get('message')
    DIR = sender.to_dict().get('phone') + '/'
    if not message:
        image = await client.download_media(event.to_dict().get('message'))
        if not os.path.exists(sender.to_dict().get('phone')):
            os.makedirs(sender.to_dict().get('phone'))
            os.rename(image, 'OLD-------' + image)
            image = 'OLD-------' + image
        shutil.move(image, sender.to_dict().get('phone') + '/')

    elif os.path.exists(DIR) and \
            len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))]) == 3:
        try:
            messages = message.rstrip("\n").split('\n')
            meter_numbers = []
            meter_readings = []
            if len(messages) == 4:
                for index, numbers in enumerate(messages):
                    if index + 1 % 2 != 0 and numbers.rfind('JANH') == 0:
                        meter_numbers.append(numbers)
                    elif int(numbers):
                        meter_readings.append(numbers)
                if len(meter_readings) == 2 and len(meter_numbers) == 2 \
                        and len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))]) == 3:
                    shutil.rmtree(sender.to_dict().get('phone'))
        except:
            pass
    await event.respond('Testing chal rhe h dont reply')


with client:
    client.run_until_disconnected()