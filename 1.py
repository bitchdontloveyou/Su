import random
import time 
from telethon.sync import TelegramClient, events
api_id = 1765001
api_hash = '31e44198df1635fa81c45fd8a23ba8e0'
with TelegramClient('name', api_id, api_hash) as client :
    nixya = 5
    while (nixya < 55) :
        pytin = random.randint(0, 1)
        if (pytin == 0) : 
            privets = ['Привет', 'Здравствуйте', 'Добрый день', 'Добрый вечер', 'Доброе утро', 'Хай', 'Хелло', 'Халло', 'Доброго времени суток', 'Здравствуй', 'Здрасти']
            nachalo = random.choice(privets) 
            client.send_message('@RuAnon_bot', '/stop')
            time.sleep(1)
            client.send_message('@RuAnon_bot', '/start') 
            time.sleep(3)
            client.send_message('@RuAnon_bot', nachalo)
            client.send_message('@RuAnon_bot', 'Работа интересует?')
            client.send_message('@RuAnon_bot', 'Без привязки к месту и возврасту.') 
            client.send_message('@RuAnon_bot', 'Подойдет даже школьникам.') 
            client.send_message('@RuAnon_bot', 'Не криминал (не работа закладчиком и т.д.)')
            client.send_message('@RuAnon_bot', 'Если интересует пиши сюда: @abbcddd . ')
            time.sleep(10)
        if (pytin == 1) :
            privets = ['Привет', 'Здравствуйте', 'Добрый день', 'Добрый вечер', 'Доброе утро', 'Хай', 'Хелло', 'Халло', 'Доброго времени суток', 'Здравствуй', 'Здрасти']
            nachalo = random.choice(privets) 
            client.send_message('@RuAnon_bot', '/stop')
            time.sleep(1)
            client.send_message('@RuAnon_bot', '/start') 
            time.sleep(3)
            client.send_message('@RuAnon_bot', nachalo)
            client.send_message('@RuAnon_bot', 'Работа интересует? Без привязки к месту и возврасту. Подойдет даже школьникам. Не криминал (не работа закладчиком и т.д.). Если интересует пиши сюда: @abbcddd .')
