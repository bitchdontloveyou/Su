import time 
import telethon 
api_id = 1765001
api_hash = '31e44198df1635fa81c45fd8a23ba8e0'

client = TelegramClient('session_name', api_id, api_hash)
client.start()
while True :
    client.send_message(""RuAnon_bot"", '/stop')
    time.sleep(5)
    client.send_message(""RuAnon_bot"", '/start' )
    time.sleep(10)
    client.send_message(""RuAnon_bot"", 'Работа интересует? Без 
привязки к месту и возврасту. 
Подойдет даже школьникам. Не 
криминал (не работа закладчиком
и т.д.) Если интересует пиши 
сюда: @abbcddd . ')
    time.sleep(10)
