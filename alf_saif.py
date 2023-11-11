from aiogram import Bot, Dispatcher, executor, types
import time
from aiogram.types import BotCommand
import asyncio
import aioschedule
from datetime import datetime, timedelta, timezone

API_TOKEN = '***************YOUR_API***************'


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

stickerblock = 0
maxstickerblock = 25
blockedstickerblock = 0
continuer = 0


#your utc region
utc = 1

hoster = 'WebMast'

gifblock = 0
maxgifblock = 25
blockedgifblock = 0

user_track_spam = ''
new_message_time = 0.0
old_message_time = 0.0
stop_spam_sticker = 'CAACAgQAAxkBAAEB67RlT7UCv46lCb1QULxPKEZp6FxKDgAC2AwAApzYQFLmTLCt5d5_tDME'
spam_sticker_seconds = 0

@dp.message_handler(commands=['about'], content_types=['any'])
async def startup_message(message: types.Message):
   info_msg = await message.answer(f'Малик Альф Саиф. Версия 0.04. Made by WebMast from WebAnLiMaks studio, hosted by {hoster}')
   video_msg = await message.answer_photo(r'https://github.com/evembar/malik_bot/raw/main/startup.webp')
   time_set = time.time()
   local_time = time.ctime(time_set)
   log = open('log.txt', 'a')
   user_sticker = message.from_user.first_name
   log.write(f'\n {local_time}: Пользователь {user_sticker} Вызвал версию бота')
   log.close()
   print(f'\n {local_time}: Пользователь {user_sticker} Вызвал версию бота')
   time.sleep(15)
   await info_msg.delete()
   await video_msg.delete()
   await message.delete()

@dp.message_handler(commands=['sticker'], content_types=['any'])
async def startup_message(message: types.Message):
   global stickerblock, maxstickerblock, blockedstickerblock
   static = await message.answer(f'Доступных стикеров осталось:  {maxstickerblock - stickerblock}. Заблокированных : {blockedstickerblock}')
   time_set = time.time()
   local_time = time.ctime(time_set)
   log = open('log.txt', 'a')
   user_sticker = message.from_user.first_name
   await message.delete()
   log.write(f'\n {local_time} : {user_sticker} вызвал статистику. Доступных стикеров осталось:  {maxstickerblock - stickerblock}. Заблокированных : {blockedstickerblock}')
   log.close()
   print(f'\n {local_time} : Доступных стикеров осталось:  {maxstickerblock - stickerblock}. Заблокированных : {blockedstickerblock}')
   time.sleep(2)
   await static.delete()

@dp.message_handler(commands=['gif'], content_types=['any'])
async def startup_message(message: types.Message):
   global gifblock, maxgifblock, blockedgifblock
   static = await message.answer(f'{local_time} : Доступных гифок осталось:  {maxgifblock - gifblock}. Заблокированных : {blockedgifblock}')
   time_set = time.time()
   local_time = time.ctime(time_set)
   log = open('log.txt', 'a')
   user_sticker = message.from_user.first_name
   await message.delete()
   log.write(f'\n {local_time} : {user_sticker} вызвал статистику. Доступных гифок осталось:  {maxgifblock - gifblock}. Заблокированных : {blockedgifblock}')
   log.close()
   print(f'\n {local_time} : Доступных гифок осталось:  {maxgifblock - gifblock}. Заблокированных : {blockedgifblock}')
   time.sleep(2)
   await static.delete()
   
@dp.message_handler(commands=['clear_log'], content_types=['any'])
async def startup_message(message: types.Message):
   webmast_id = 1702139456
   nikita44_id=2023745296
   ivanban_id=5507903625

   if message.from_user.id == webmast_id or message.from_user.id == nikita44_id or message.from_user.id == ivanban_id:
      import os
      os.remove('log.txt')
      log = open('log.txt', 'w+')
      log.write('\nЛоги были очищены')
      log.close()

      time_set = time.time()
      local_time = time.ctime(time_set)
      log = open('log.txt', 'a')
      user_sticker = message.from_user.first_name
      log.write(f'\n {local_time}: Пользователь {user_sticker} Очистил логи')
      log.close()
      print(f'\n {local_time}: Пользователь {user_sticker} Очистил логи')

      clear_log_info = await message.answer('Лог файл был очищен')
      await message.delete()
      time.sleep(2)
      await clear_log_info.delete()
   else:

      time_set = time.time()
      local_time = time.ctime(time_set)
      log = open('log.txt', 'a')
      user_sticker = message.from_user.first_name
      log.write(f'\n {local_time}: Пользователь {user_sticker} Попытался очистить логи')
      log.close()
      print(f'\n {local_time}: Пользователь {user_sticker} Попытался очистить логи')

      clear_log_info = await message.answer('Доступ ограничен. Попросите об этом админов')
      await message.delete()
      time.sleep(5)
      await clear_log_info.delete()

@dp.message_handler(commands=['obnull_limit_all'], content_types=['any'])
async def startup_message(message: types.Message):
   webmast_id = 1702139456
   nikita44_id=2023745296
   ivanban_id=5507903625

   if message.from_user.id == webmast_id or message.from_user.id == nikita44_id or message.from_user.id == ivanban_id:
      global stickerblock, blockedstickerblock, photoblock, blockedphotoblock, gifblock, blockedgifblock

      stickerblock = 0
      blockedstickerblock = 0

      gifblock = 0
      blockedgifblock = 0
      
      photoblock = 0
      blockedphotoblock = 0

      time_set = time.time()
      local_time = time.ctime(time_set)
      log = open('log.txt', 'a')
      user_sticker = message.from_user.first_name
      log.write(f'\n {local_time}: Пользователь {user_sticker} Обнулил лимиты')
      log.close()
      print(f'\n {local_time}: Пользователь {user_sticker} Обнулил лимиты')

      clear_log_info = await message.answer('Обнуление лимита доступных к отправке медиа')
      await message.delete()
      time.sleep(2)
      await clear_log_info.delete()
   else:

      time_set = time.time()
      local_time = time.ctime(time_set)
      log = open('log.txt', 'a')
      user_sticker = message.from_user.first_name
      log.write(f'\n {local_time}: Пользователь {user_sticker} Попытался Обнулить лимиты')
      log.close()
      print(f'\n {local_time}: Пользователь {user_sticker} Попытался Обнулить лимиты')

      clear_log_info = await message.answer('Доступ ограничен. Попросите об этом админов')
      await message.delete()
      time.sleep(5)
      await clear_log_info.delete()


@dp.message_handler(commands=['cont_mod'], content_types=['any'])
async def startup_message(message: types.Message):
   webmast_id = 1702139456
   nikita44_id=2023745296
   ivanban_id=5507903625

   if message.from_user.id == webmast_id or message.from_user.id == nikita44_id or message.from_user.id == ivanban_id:
      global continuer

      if continuer == 0:
         continuer = 1
      elif continuer == 1:
         continuer = 0

      time_set = time.time()
      local_time = time.ctime(time_set)
      log = open('log.txt', 'a')
      user_sticker = message.from_user.first_name
      log.write(f'\n {local_time}: Пользователь {user_sticker} Изменил функцию "продолжать."')
      log.close()
      print(f'\n {local_time}: Пользователь {user_sticker} Изменил функцию "продолжать.')

      clear_log_info = await message.answer('Изменена функция "продолжать.')
      await message.delete()
      time.sleep(2)
      await clear_log_info.delete()
   else:

      time_set = time.time()
      local_time = time.ctime(time_set)
      log = open('log.txt', 'a')
      user_sticker = message.from_user.first_name
      log.write(f'\n {local_time}: Пользователь {user_sticker} Попытался Изменить функцию "продолжать.')
      log.close()
      print(f'\n {local_time}: Пользователь {user_sticker} Попытался Изменить функцию "продолжать.')

      clear_log_info = await message.answer('Доступ ограничен. Попросите об этом админов')
      await message.delete()
      time.sleep(5)
      await clear_log_info.delete()


@dp.message_handler(commands=['start']) #Явно указываем в декораторе, на какую команду реагируем. 
async def send_welcome(message: types.Message):
   info_start_msg = await message.reply("Я Малик Альф-Саиф и если не будешь следовать правилам, то я наведу такую трёпку\nВ частности, если вы будете спаммить стикерами, то каждого буду банить в зависимости, сколько решат поставить времени.\n WebMast уже реализовал это, приятного общения!!!. >:)  ")

   time_set = time.time()
   local_time = time.ctime(time_set)
   log = open('log.txt', 'a')
   user_sticker = message.from_user.first_name
   log.write(f'\n {local_time}: Пользователь {user_sticker} Cделал старт меня')
   log.close()
   print(f'\n {local_time}: Пользователь {user_sticker} Cделал старт меня')
   await message.delete()
   time.sleep(10)
   await info_start_msg.delete()

async def obnull_limit_rasp():
   global stickerblock,  gifblock

   stickerblock = 0
   gifblock = 0

   time_set = time.time()
   local_time = time.ctime(time_set)
   log = open('log.txt', 'a')
   log.write(f'\n {local_time}: Обнуление лимита стикеров,гифок')
   log.close()
   print(f'\n {local_time}: Обнуление лимита стикеров,гифок')

async def scheduler():
    while True:
         await aioschedule.run_pending()

         timezone = datetime(datetime.now().year, datetime.now().month, datetime.now().day, datetime.now().hour, datetime.now().minute, datetime.now().second)

         if (timezone.hour == 0 and timezone.minute == 0 and timezone.second == 0) or (timezone.hour == 1 and timezone.minute == 0 and timezone.second == 0) or (timezone.hour == 2 and timezone.minute == 0 and timezone.second == 0) or (timezone.hour == 3 and timezone.minute == 0 and timezone.second == 0):
           await obnull_limit_rasp()
         elif (timezone.hour == 4 and timezone.minute == 0 and timezone.second == 0) or (timezone.hour == 5 and timezone.minute == 0 and timezone.second == 0) or (timezone.hour == 6 and timezone.minute == 0 and timezone.second == 0) or (timezone.hour == 7 and timezone.minute == 0 and timezone.second == 0):
           await obnull_limit_rasp()
         elif (timezone.hour == 8 and timezone.minute == 0 and timezone.second == 0) or (timezone.hour == 9 and timezone.minute == 0 and timezone.second == 0) or (timezone.hour == 10 and timezone.minute == 0 and timezone.second == 0) or (timezone.hour == 11 and timezone.minute == 0 and timezone.second == 0):
           await obnull_limit_rasp()
         elif (timezone.hour == 12 and timezone.minute == 0 and timezone.second == 0) or (timezone.hour == 13 and timezone.minute == 0 and timezone.second == 0) or (timezone.hour == 14 and timezone.minute == 0 and timezone.second == 0) or (timezone.hour == 15 and timezone.minute == 0 and timezone.second == 0):
           await obnull_limit_rasp()
         elif (timezone.hour == 16 and timezone.minute == 0 and timezone.second == 0) or (timezone.hour == 17 and timezone.minute == 0 and timezone.second == 0) or (timezone.hour == 18 and timezone.minute == 0 and timezone.second == 0) or (timezone.hour == 19 and timezone.minute == 0 and timezone.second == 0):
           await obnull_limit_rasp()
         elif (timezone.hour == 20 and timezone.minute == 0 and timezone.second == 0) or (timezone.hour == 21 and timezone.minute == 0 and timezone.second == 0) or (timezone.hour == 22 and timezone.minute == 0 and timezone.second == 0) or (timezone.hour == 23 and timezone.minute == 0 and timezone.second == 0):
           await obnull_limit_rasp()
         else:
            pass

         await asyncio.sleep(1)
        


async def setup_default_commands(dp):
    

    await dp.bot.set_my_commands([
        BotCommand(command="about", description="О Малике"),
        BotCommand(command="cont_mod", description="Включение функции продолжайкина"),
        BotCommand(command="start", description="Приветствие от Малика"),
        BotCommand(command="obnull_limit_all", description="Обнуление лимита отправляемых медиа"),
        BotCommand(command="clear_log", description="Очистка логов"),
        BotCommand(command="sticker", description="Проверка доступных к отправке стикеров"),
        BotCommand(command="gif", description="Проверка доступных к отправке гифок"),
    ])
    asyncio.create_task(scheduler())
      

@dp.message_handler(content_types=['any']) #Создаём новое событие, которое запускается в ответ на любой текст, введённый пользователем.
async def echo(message: types.Message): #Создаём функцию с простой задачей — отправить обратно тот же текст, что ввёл пользователь.
   global stickerblock, maxstickerblock, blockedstickerblock,gifblock, maxgifblock, blockedgifblock, user_track_spam, new_message_time, old_message_time, spam_sticker_seconds
   if message.sticker:
      if message.chat.type == 'private':
         await message.answer('Не думай, что ты можешь меня обхитрить, ибо я только в группах навожу порядок. Спамь сколько хочешь тут!')
      else: 
         
         if stickerblock == maxstickerblock:
            await message.delete()
            blockedstickerblock +=1
            status = 'Отказано'
         else:
            stickerblock +=1
            status = 'НЕОтказано'

         timemsg = datetime(datetime.now().year, datetime.now().month, datetime.now().day, datetime.now().hour, datetime.now().minute, datetime.now().second, datetime.now().microsecond)

         if user_track_spam == '':
            user_track_spam = message.from_user.first_name
            print(user_track_spam)
            new_message_time == timemsg.microsecond
            old_message_time = ''
         else:
            if user_track_spam == message.from_user.first_name:
               if new_message_time == '':
                  new_message_time == timemsg.microsecond
                  print(f'Принято стикерко за {new_message_time}')
               else:
                  old_message_time = new_message_time
                  new_message_time = timemsg.microsecond
                  print(f'Принято стикерко за {new_message_time}')
                  if new_message_time < 400000 and old_message_time < 400000 :
                     spam_sticker_seconds += 1
                     print(f'Быстрый стикер: {spam_sticker_seconds} из 3')
                  else:
                     new_message_time == timemsg.microsecond
                     old_message_time = ''
                     spam_sticker_seconds = 0
                     print("Медленный стикер")

                  if spam_sticker_seconds == 3:
                     #antispam_message_sticker = await message.answer_sticker(stop_spam_sticker)
                     antispam_message_text = await message.answer(f'Критичная спам атака, происходит блокировка спаммера {user_track_spam}. Блокировка будет длиться в течении 15 минут')
                     ban_time= (int(time.time()) + 900*utc+900)
                     print(ban_time)

                     await bot.restrict_chat_member(chat_id=message.chat.id, user_id=message.from_user.id,until_date=ban_time, can_send_messages=False)
                     
                     print(ban_time)
                     
                     asyncio.sleep(1)
                     #antispam_message_sticker.delete()
                     await antispam_message_text.delete()
            else:
               user_track_spam = message.from_user.first_name
               print(user_track_spam)
               print(2)
               new_message_time == timemsg.microsecond
               old_message_time = ''

         time_set = time.time()
         local_time = time.ctime(time_set)
         log = open('log.txt', 'a')
         user_sticker = message.from_user.first_name
         log.write(f'\n {local_time}: Пользователь {user_sticker} Отправил стикер. Статус - {status}')
         log.close()
         print(f'\n {local_time}: Пользователь {user_sticker} Отправил стикер. Статус - {status}')


   elif message.animation:
      if message.chat.type == 'private':
         await message.answer('Гифки и прочее дерьмо, как этим вы пользуетесь, малыши?')
      else: 
         
         if gifblock == maxgifblock:
            await message.delete()
            blockedgifblock +=1
            status = 'Отказано'
         else:
            gifblock +=1
            status = 'НЕОтказано'

         time_set = time.time()
         local_time = time.ctime(time_set)
         log = open('log.txt', 'a')
         user_sticker = message.from_user.first_name
         log.write(f'\n {local_time}: Пользователь {user_sticker} Отправил гифку. Статус - {status}')
         log.close()
         print(f'\n {local_time}: Пользователь {user_sticker} Отправил гифку. Статус - {status}')
   else:
      global continuer
      if continuer == 1:
         cont_msg = await message.answer('Продолжай.')
         time_set = time.time()
         local_time = time.ctime(time_set)
         log = open('log.txt', 'a')
         user_sticker = message.from_user.first_name
         log.write(f'\n {local_time}: Пользователь {user_sticker} Предложил мне.')
         log.close()
         print(f'\n {local_time}: Пользователь {user_sticker} Предложил мне.')
         asyncio.sleep(1)
         cont_msg.delete()
      else:
         pass

if __name__ == '__main__':
   
   print('Запуск Malik Alf-Salif 0.04')
   executor.start_polling(dp, skip_updates=True, on_startup=setup_default_commands)
