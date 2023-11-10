from aiogram import Bot, Dispatcher, executor, types
import time
from aiogram.types import BotCommand
import asyncio 
import aioschedule

API_TOKEN = '*****your token******'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

stickerblock = 0
maxstickerblock = 25
blockedstickerblock = 0
continuer = 0

photoblock = 0
maxphotoblock = 25
blockedphotoblock = 0

gifblock = 0
maxgifblock = 25
blockedgifblock = 0

videoblock = 0
maxvideoblock = 15
blockedvideoblock = 0

@dp.message_handler(commands=['about'], content_types=['any'])
async def startup_message(message: types.Message):
   info_msg = await message.answer('Малик Альф Саиф. Версия 0.3. Made by WebMast from WebAnLiMaks studio, hosted by Nikita44')
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
   print(f'\nДоступных стикеров осталось:  {maxstickerblock - stickerblock}. Заблокированных : {blockedstickerblock}')
   time.sleep(2)
   await static.delete()

@dp.message_handler(commands=['photo'], content_types=['any'])
async def startup_message(message: types.Message):
   global photoblock, maxphotoblock, blockedphotoblock
   static = await message.answer(f'Доступных картинок осталось:  {maxphotoblock - photoblock}. Заблокированных : {blockedphotoblock}')
   time_set = time.time()
   local_time = time.ctime(time_set)
   log = open('log.txt', 'a')
   user_sticker = message.from_user.first_name
   await message.delete()
   log.write(f'\n {local_time} : {user_sticker} вызвал статистику. Доступных картинок осталось:  {maxphotoblock - photoblock}. Заблокированных : {blockedphotoblock}')
   log.close()
   print(f'\n Доступных картинок осталось:  {maxphotoblock - photoblock}. Заблокированных : {blockedphotoblock}')
   time.sleep(2)
   await static.delete()

@dp.message_handler(commands=['video'], content_types=['any'])
async def startup_message(message: types.Message):
   global videoblock, maxvideoblock, blockedvideoblock
   static = await message.answer(f'Доступных видосов осталось:  {maxvideoblock - videoblock}. Заблокированных : {blockedvideoblock}')
   time_set = time.time()
   local_time = time.ctime(time_set)
   log = open('log.txt', 'a')
   user_sticker = message.from_user.first_name
   await message.delete()
   log.write(f'\n {local_time} : {user_sticker} вызвал статистику. Доступных видосов осталось:  {maxvideoblock - videoblock}. Заблокированных : {blockedvideoblock}')
   log.close()
   print(f'\n Доступных видосов осталось:  {maxvideoblock - videoblock}. Заблокированных : {blockedvideoblock}')
   time.sleep(2)
   await static.delete()

@dp.message_handler(commands=['gif'], content_types=['any'])
async def startup_message(message: types.Message):
   global gifblock, maxgifblock, blockedgifblock
   static = await message.answer(f'Доступных гифок осталось:  {maxgifblock - gifblock}. Заблокированных : {blockedgifblock}')
   time_set = time.time()
   local_time = time.ctime(time_set)
   log = open('log.txt', 'a')
   user_sticker = message.from_user.first_name
   await message.delete()
   log.write(f'\n {local_time} : {user_sticker} вызвал статистику. Доступных гифок осталось:  {maxgifblock - gifblock}. Заблокированных : {blockedgifblock}')
   log.close()
   print(f'\n Доступных гифок осталось:  {maxgifblock - gifblock}. Заблокированных : {blockedgifblock}')
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
   info_start_msg = await message.reply("Я Малик Альф-Саиф и если не будешь следовать правилам, то я наведу такую трёпку\nВ частности, если вы будете спаммить стикерами, то каждого буду банить в зависимости, сколько решат поставить времени.\n Пока WebMastом(Виктором Яланжи) реализовывается, так что вам не долго осталось радоваться. >:)  ")

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
   global stickerblock, videoblock, gifblock, photoblock

   stickerblock = 0
   videoblock = 0
   gifblock = 0
   photoblock = 0

   time_set = time.time()
   local_time = time.ctime(time_set)
   log = open('log.txt', 'a')
   log.write(f'\n {local_time}: Обнуление лимита стикеров, видео, гифок, фоток')
   log.close()

async def scheduler():
    aioschedule.every().day.at("0:00").do(obnull_limit_rasp)
    aioschedule.every().day.at("1:00").do(obnull_limit_rasp)
    aioschedule.every().day.at("2:00").do(obnull_limit_rasp)
    aioschedule.every().day.at("3:00").do(obnull_limit_rasp)
    aioschedule.every().day.at("4:00").do(obnull_limit_rasp)
    aioschedule.every().day.at("5:00").do(obnull_limit_rasp)
    aioschedule.every().day.at("6:00").do(obnull_limit_rasp)
    aioschedule.every().day.at("7:00").do(obnull_limit_rasp)
    aioschedule.every().day.at("8:00").do(obnull_limit_rasp)
    aioschedule.every().day.at("9:00").do(obnull_limit_rasp)
    aioschedule.every().day.at("10:00").do(obnull_limit_rasp)
    aioschedule.every().day.at("11:00").do(obnull_limit_rasp)
    aioschedule.every().day.at("12:00").do(obnull_limit_rasp)
    aioschedule.every().day.at("13:00").do(obnull_limit_rasp)
    aioschedule.every().day.at("14:00").do(obnull_limit_rasp)
    aioschedule.every().day.at("15:00").do(obnull_limit_rasp)
    aioschedule.every().day.at("16:00").do(obnull_limit_rasp)
    aioschedule.every().day.at("17:00").do(obnull_limit_rasp)
    aioschedule.every().day.at("18:00").do(obnull_limit_rasp)
    aioschedule.every().day.at("19:00").do(obnull_limit_rasp)
    aioschedule.every().day.at("20:00").do(obnull_limit_rasp)
    aioschedule.every().day.at("21:00").do(obnull_limit_rasp)
    aioschedule.every().day.at("22:00").do(obnull_limit_rasp)
    aioschedule.every().day.at("23:00").do(obnull_limit_rasp)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


async def setup_default_commands(dp):
    

    await dp.bot.set_my_commands([
        BotCommand(command="about", description="О Малике"),
        BotCommand(command="cont_mod", description="Включение функции продолжайкина"),
        BotCommand(command="start", description="Приветствие от Малика"),
        BotCommand(command="obnull_limit_all", description="Обнуление лимита отправляемых медиа"),
        BotCommand(command="clear_log", description="Очистка логов"),
        BotCommand(command="sticker", description="Проверка доступных к отправке стикеров"),
        BotCommand(command="photo", description="Проверка доступных к отправке картинок"),
        BotCommand(command="gif", description="Проверка доступных к отправке гифок"),
        BotCommand(command="video", description="Проверка доступных к отправке видео"),
    ])
    asyncio.create_task(scheduler())
      

@dp.message_handler(content_types=['any']) #Создаём новое событие, которое запускается в ответ на любой текст, введённый пользователем.
async def echo(message: types.Message): #Создаём функцию с простой задачей — отправить обратно тот же текст, что ввёл пользователь.
   global stickerblock, maxstickerblock, blockedstickerblock, photoblock, maxphotoblock, blockedphotoblock, gifblock, maxgifblock, blockedgifblock
   global videoblock, maxvideoblock, blockedvideoblock
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

         time_set = time.time()
         local_time = time.ctime(time_set)
         log = open('log.txt', 'a')
         user_sticker = message.from_user.first_name
         log.write(f'\n {local_time}: Пользователь {user_sticker} Отправил стикер. Статус - {status}')
         log.close()
         print(f'\n {local_time}: Пользователь {user_sticker} Отправил стикер. Статус - {status}')
   elif message.photo:
      if message.chat.type == 'private':
         await message.answer('Как буд-то мне сдались твои порнокартинки')
      else: 
         
         if photoblock == maxphotoblock:
            await message.delete()
            blockedphotoblock +=1
            status = 'Отказано'
         else:
            photoblock +=1
            status = 'НЕОтказано'

         time_set = time.time()
         local_time = time.ctime(time_set)
         log = open('log.txt', 'a')
         user_sticker = message.from_user.first_name
         log.write(f'\n {local_time}: Пользователь {user_sticker} Отправил картинку. Статус - {status}')
         log.close()
         print(f'\n {local_time}: Пользователь {user_sticker} Отправил картинку. Статус - {status}')
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
   elif message.video:
      if message.chat.type == 'private':
         await message.answer('Не бось, это видео с участием мамки?')
      else: 
         
         if videoblock == maxvideoblock:
            await message.delete()
            blockedvideoblock +=1
            status = 'Отказано'
         else:
            videoblock +=1
            status = 'НЕОтказано'

         time_set = time.time()
         local_time = time.ctime(time_set)
         log = open('log.txt', 'a')
         user_sticker = message.from_user.first_name
         log.write(f'\n {local_time}: Пользователь {user_sticker} Отправил видос. Статус - {status}')
         log.close()
         print(f'\n {local_time}: Пользователь {user_sticker} Отправил видос. Статус - {status}')
   else:
      global continuer
      if continuer == 1:
         await message.answer('Продолжай.')
         time_set = time.time()
         local_time = time.ctime(time_set)
         log = open('log.txt', 'a')
         user_sticker = message.from_user.first_name
         log.write(f'\n {local_time}: Пользователь {user_sticker} Предложил мне.')
         log.close()
         print(f'\n {local_time}: Пользователь {user_sticker} Предложил мне.')
      else:
         pass

if __name__ == '__main__':
   
   print('Запуск Malik Alf-Salif 0.3')
   executor.start_polling(dp, skip_updates=True, on_startup=setup_default_commands)
