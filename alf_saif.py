from aiogram import Bot, Dispatcher, executor, types
import time
from aiogram.types import BotCommand

API_TOKEN = 'API you'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

stickerblock = 0
maxstickerblock = 50
blockedstickerblock = 0
continuer = 0

@dp.message_handler(commands=['about'], content_types=['any'])
async def startup_message(message: types.Message):
   info_msg = await message.answer('Малик Альф Саиф. Версия 0.02')
   video_msg = await message.answer_video(r'https://github.com/evembar/malik_bot/raw/main/startup.mp4')
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
   
@dp.message_handler(commands=['clear_log'], content_types=['any'])
async def startup_message(message: types.Message):
   webmast_id = 1702139456
   nikita44_id=2023745296
   ivanban_id=5507903625
   steveerage_id=1020333377

   if message.from_user.id == webmast_id or message.from_user.id == nikita44_id or message.from_user.id == ivanban_id or message.from_user.id == steveerage_id:
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

@dp.message_handler(commands=['obnull_limit_sticker'], content_types=['any'])
async def startup_message(message: types.Message):
   webmast_id = 1702139456
   nikita44_id=2023745296
   ivanban_id=5507903625
   steveerage_id=1020333377

   if message.from_user.id == webmast_id or message.from_user.id == nikita44_id or message.from_user.id == ivanban_id or message.from_user.id == steveerage_id:
      global stickerblock, blockedstickerblock

      stickerblock = 0
      blockedstickerblock = 0

      time_set = time.time()
      local_time = time.ctime(time_set)
      log = open('log.txt', 'a')
      user_sticker = message.from_user.first_name
      log.write(f'\n {local_time}: Пользователь {user_sticker} Обнулил лимит стикеров')
      log.close()
      print(f'\n {local_time}: Пользователь {user_sticker} Обнулил лимит стикеров')

      clear_log_info = await message.answer('Обнуление лимита доступных к отправке стикеров')
      await message.delete()
      time.sleep(2)
      await clear_log_info.delete()
   else:

      time_set = time.time()
      local_time = time.ctime(time_set)
      log = open('log.txt', 'a')
      user_sticker = message.from_user.first_name
      log.write(f'\n {local_time}: Пользователь {user_sticker} Попытался Обнулить лимит стикеров')
      log.close()
      print(f'\n {local_time}: Пользователь {user_sticker} Попытался оОбнулить лимит стикеров')

      clear_log_info = await message.answer('Доступ ограничен. Попросите об этом админов')
      await message.delete()
      time.sleep(5)
      await clear_log_info.delete()


@dp.message_handler(commands=['cont_mod'], content_types=['any'])
async def startup_message(message: types.Message):
   webmast_id = 1702139456
   nikita44_id=2023745296
   ivanban_id=5507903625
   steveerage_id=1020333377

   if message.from_user.id == webmast_id or message.from_user.id == nikita44_id or message.from_user.id == ivanban_id or message.from_user.id == steveerage_id:
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


async def setup_default_commands(dp):

    await dp.bot.set_my_commands([
        BotCommand(command="about", description="О Малике"),
        BotCommand(command="cont_mod", description="Включение функции продолжайкина"),
        BotCommand(command="start", description="Приветствие от Малика"),
        BotCommand(command="obnull_limit_sticker", description="Обнуление лимита отправляемых стикеров"),
        BotCommand(command="clear_log", description="Очистка логов"),
        BotCommand(command="sticker", description="Проверка доступных к отправке стикеров")
    ])

@dp.message_handler(content_types=['any']) #Создаём новое событие, которое запускается в ответ на любой текст, введённый пользователем.
async def echo(message: types.Message): #Создаём функцию с простой задачей — отправить обратно тот же текст, что ввёл пользователь.
   global stickerblock, maxstickerblock, blockedstickerblock
   if message.sticker:
      if message.chat.type == 'private':
         await message.answer('Не думай, что ты можешь меня обхитрить, ибо я только в группах навожу порядок. Спамь сколько хочешь тут!')
      else: 
         sticker_msg = await message.answer_sticker(r'CAACAgIAAxkBAAEB359lS_yEjmo0q83gS-AUVBSu7ky0SgACQCUAAmXs8UvorPRByOyh_zME')
         
         if stickerblock == maxstickerblock:
            await message.delete()
            blockedstickerblock +=1
            status = 'Отказано'
         else:
            stickerblock +=1
            status = 'НЕОтказано'

         sigmanotsticker = await message.answer(f' Доступных стикеров осталось:  {maxstickerblock - stickerblock}. Заблокированных : {blockedstickerblock}')
         time_set = time.time()
         local_time = time.ctime(time_set)
         log = open('log.txt', 'a')
         user_sticker = message.from_user.first_name
         log.write(f'\n {local_time}: Пользователь {user_sticker} Отправил стикер. Статус - {status}')
         log.close()
         print(f'\n {local_time}: Пользователь {user_sticker} Отправил стикер. Статус - {status}')
         time.sleep(2)
         await sticker_msg.delete()
         await sigmanotsticker.delete()
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
   
   print('Запуск Malik Alf-Salif 0.2')
   executor.start_polling(dp, skip_updates=True, on_startup=setup_default_commands)
