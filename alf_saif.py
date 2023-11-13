from aiogram import Bot, Dispatcher, executor, types
import time
from aiogram.types import BotCommand
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.types import ParseMode
import aiogram.utils.markdown as md
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
import aioschedule
from datetime import datetime
import os
import random

if os.path.isfile('session.py'):
   try:
      import session as ses
      API_TOKEN = ses.API_TOKEN
   except:
      API_TOKEN = input('Укажите API токен бота> ')
else:
   API_TOKEN = input('Укажите API токен бота> ')

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)

try:
   stickerblock = 0
   maxstickerblock = ses.maxstickerblock
   blockedstickerblock = 0
   continuer = 0

   utc = ses.utc

   hoster = ses.hoster

   gifblock = 0
   maxgifblock = ses.maxgifblock
   blockedgifblock = 0

   user_track_spam = ''
   new_message_time = 0.0
   old_message_time = 0.0
   stop_spam_sticker = 'CAACAgQAAxkBAAEB67RlT7UCv46lCb1QULxPKEZp6FxKDgAC2AwAApzYQFLmTLCt5d5_tDME'
   spam_sticker_seconds = 0

   admin1=ses.admin1
   admin2=ses.admin2
   admin3=ses.admin3


   user_track_spam_gif = ''
   new_message_time_gif = 0.0
   old_message_time_gif = 0.0
   spam_gif_seconds = 0
except:
   stickerblock = 0
   maxstickerblock = 25
   blockedstickerblock = 0
   continuer = 0

   utc = 4

   hoster = 'noname-hoster'

   gifblock = 0
   maxgifblock = 25
   blockedgifblock = 0

   user_track_spam = ''
   new_message_time = 0.0
   old_message_time = 0.0
   stop_spam_sticker = 'CAACAgQAAxkBAAEB67RlT7UCv46lCb1QULxPKEZp6FxKDgAC2AwAApzYQFLmTLCt5d5_tDME'
   spam_sticker_seconds = 0

   admin1=int(input('Укажите ID первого для начального администрирования> '))
   admin2=int(input('Укажите ID второго админа для начального администрирования> '))
   admin3=int(input('Укажите ID третьего админа для начального администрирования> '))


   user_track_spam_gif = ''
   new_message_time_gif = 0.0
   old_message_time_gif = 0.0
   spam_gif_seconds = 0

@dp.message_handler(commands=['about'], content_types=['any'])
async def startup_message(message: types.Message):
   info_msg = await message.answer(f'Малик Альф Саиф. Версия 0.06. Made by WebMast from WebAnLiMaks studio, hosted by {hoster}.')
   video_msg = await message.answer_photo(r'https://github.com/evembar/malik_bot/raw/main/startup.webp')
   time_set = time.time()
   local_time = time.ctime(time_set)
   log = open('log.txt', 'a')
   user_sticker = message.from_user.first_name
   log.write(f'\n {local_time}: Пользователь {user_sticker} Вызвал версию бота')
   log.close()
   print(f'\n {local_time}: Пользователь {user_sticker} Вызвал версию бота')
   time.sleep(5)
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

   time_set = time.time()
   local_time = time.ctime(time_set)

   static = await message.answer(f'{local_time} : Доступных гифок осталось:  {maxgifblock - gifblock}. Заблокированных : {blockedgifblock}')
   
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
   #webmast_id = 1702139456 
   #nikita44_id=2023745296
   #ivanban_id=5507903625

   if message.from_user.id == admin1 or message.from_user.id == admin2 or message.from_user.id == admin3:
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

   if message.from_user.id == admin1 or message.from_user.id == admin2 or message.from_user.id == admin3:
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

class Form(StatesGroup):
   hoster_name = State()
   utc_number = State()
   max_sticker = State() 
   max_gif = State()
   id_admin1 = State()
   id_admin2 = State()
   id_admin3  = State()
   


@dp.message_handler(commands=['setup'], content_types=['any'])
async def startup_message(message: types.Message):

   if message.from_user.id == admin1 or message.from_user.id == admin2 or message.from_user.id == admin3:
      
      if message.chat.type == 'private':
         await message.answer('Конфигурация лаунчера. Сейчас будут задаваться вопросы, а вы должны ответить. Это нужно для того, чтобы создать файл для автоконфигурации лаунчера. Если не захотите отвечать, то вы можете активировать комманду /cancel')
         
         await Form.hoster_name.set()
         await message.reply("Скажите имя или псевдоним того, кто хостит этого бота?")


      else:
         setup_admin_msg = await message.answer('Данная команда выполняется в личном чате с ботом.')
         await asyncio.sleep(3)
         await setup_admin_msg.delete()


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

@dp.message_handler(state='*', commands='cancel')
@dp.message_handler(Text(equals='отмена', ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return

    await state.finish()
    await message.reply('Отмена настройки конфигурации')

@dp.message_handler(state=Form.hoster_name)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as ses_config:
        ses_config['hoster_name'] = message.text

    await Form.next()
    await message.reply("Напишите часовой пояс(UTC)?")

@dp.message_handler(lambda message: not message.text.isdigit(), state=Form.utc_number)
async def process_age_invalid(message: types.Message):
    return await message.reply("Напишите пожалуйста часовой пояс?!")

@dp.message_handler(state=Form.utc_number)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as ses_config:
        ses_config['utc_number'] = message.text

    await Form.next()
    await message.reply("Напишите максимальное количество отправляемых стикеров?")

@dp.message_handler(lambda message: not message.text.isdigit(), state=Form.max_sticker)
async def process_age_invalid(message: types.Message):
    return await message.reply("Напишите пожалуйста количество отправляемых стикеров?!")

@dp.message_handler(state=Form.max_sticker)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as ses_config:
        ses_config['max_sticker'] = message.text

    await Form.next()
    await message.reply("Напишите максимальное количество отправляемых гифок?")

@dp.message_handler(lambda message: not message.text.isdigit(), state=Form.max_gif)
async def process_age_invalid(message: types.Message):
    return await message.reply("Напишите количество отправляемых гифок?!")

@dp.message_handler(state=Form.max_gif)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as ses_config:
        ses_config['max_gif'] = message.text

    await Form.next()
    await message.reply("Укажите ID первого админа для администрирования?")

@dp.message_handler(lambda message: not message.text.isdigit(), state=Form.id_admin1)
async def process_age_invalid(message: types.Message):
    return await message.reply("Укажите ID первого админа для администрирования?!")

@dp.message_handler(state=Form.id_admin1)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as ses_config:
        ses_config['id_admin1'] = message.text

    await Form.next()
    await message.reply("Укажите ID второго админа для администрирования?")

@dp.message_handler(lambda message: not message.text.isdigit(), state=Form.id_admin2)
async def process_age_invalid(message: types.Message):
    return await message.reply("Укажите ID второго админа для администрирования?!")

@dp.message_handler(state=Form.id_admin2)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as ses_config:
        ses_config['id_admin2'] = message.text

    await Form.next()
    await message.reply("Укажите ID третьего админа для администрирования?")

@dp.message_handler(lambda message: not message.text.isdigit(), state=Form.id_admin3)
async def process_age_invalid(message: types.Message):
    return await message.reply("Укажите ID третьего админа для администрирования?!")

@dp.message_handler(state=Form.id_admin3)
async def process_name(message: types.Message, state: FSMContext):
    global hoster, utc, maxstickerblock, maxgifblock, stickerblock, gifblock
    async with state.proxy() as ses_config:
      ses_config['id_admin3'] = message.text
      markup = types.ReplyKeyboardRemove()


      await bot.send_message(message.chat.id, 'в конфигурации будет:')

      await bot.send_message(
               message.chat.id,
               md.text(
                  md.text('API токен бота: ', md.code(API_TOKEN)),
                  md.text('Имя хостера: ', md.bold(ses_config['hoster_name'])),
                  md.text('Часовой пояс: ', ses_config['utc_number']),
                  md.text('Максимальное количество стикеров: ', ses_config['max_sticker']),
                  md.text('Максимальное количество гифок: ', ses_config['max_gif']),
                  md.text('ID превого администратора: ', ses_config['id_admin1']),
                  md.text('ID второго администратора: ', ses_config['id_admin2']),
                  md.text('ID третьего администратора: ', ses_config['id_admin3']),
                  sep='\n',
               ),
               parse_mode=ParseMode.MARKDOWN,
         )
    await state.finish()
    
    if os.path.isfile('session.py'):
      os.remove('session.py')
      with open ('session.py', 'w') as f:
         f.write('\n')
         f.write(f'API_TOKEN="{API_TOKEN}"')
         f.write('\n')
         f.write(f'hoster="{ses_config["hoster_name"]}"')
         f.write('\n')
         f.write(f'utc={ses_config["utc_number"]}')
         f.write('\n')
         f.write(f'maxstickerblock=int({ses_config["max_sticker"]})')
         f.write('\n')
         f.write(f'maxgifblock=int({ses_config["max_gif"]})')
         f.write('\n')
         f.write(f'admin1=int({ses_config["id_admin1"]})')
         f.write('\n')
         f.write(f'admin2=int({ses_config["id_admin2"]})')
         f.write('\n')
         f.write(f'admin3=int({ses_config["id_admin3"]})')
         f.write('\n')
    else:
      with open ('session.py', 'w') as f:
         f.write('\n')
         f.write(f'API_TOKEN="{API_TOKEN}"')
         f.write('\n')
         f.write(f'hoster="{ses_config["hoster_name"]}"')
         f.write('\n')
         f.write(f'utc=int({ses_config["utc_number"]})')
         f.write('\n')
         f.write(f'maxstickerblock=int({ses_config["max_sticker"]})')
         f.write('\n')
         f.write(f'maxgifblock=int({ses_config["max_gif"]})')
         f.write('\n')
         f.write(f'admin1=int({ses_config["id_admin1"]})')
         f.write('\n')
         f.write(f'admin2=int({ses_config["id_admin2"]})')
         f.write('\n')
         f.write(f'admin3=int({ses_config["id_admin3"]})')
         f.write('\n')

    stickerblock=0
    gifblock=0
    maxstickerblock=ses_config['max_sticker']
    maxgifblock=ses_config['max_gif']
    utc=ses_config['utc_number']
    hoster=ses_config['hoster_name']

@dp.message_handler(commands=['view_config']) #Явно указываем в декораторе, на какую команду реагируем. 
async def send_welcome(message: types.Message):

   conf1 = await bot.send_message(message.chat.id, 'в конфигурации:')

   conf2 = await bot.send_message(
            message.chat.id,
            md.text(
               md.text('API токен бота: ', md.code(API_TOKEN)),
               md.text('Имя хостера: ', hoster),
               md.text('Часовой пояс: ', utc),
               md.text('Максимальное количество стикеров: ', maxstickerblock),
               md.text('Максимальное количество гифок: ', maxgifblock),
               md.text('ID превого администратора: ', admin1),
               md.text('ID второго администратора: ', admin2),
               md.text('ID третьего администратора: ', admin3),
               sep='\n',
            ),
            parse_mode=ParseMode.MARKDOWN,
      )

   time_set = time.time()
   local_time = time.ctime(time_set)
   log = open('log.txt', 'a')
   user_sticker = message.from_user.first_name
   log.write(f'\n {local_time}: Пользователь {user_sticker} Посмотрел конфигурацию бота')
   log.close()
   print(f'\n {local_time}: Пользователь {user_sticker} Посмотрел конфигурацию бота')
   await message.delete()
   time.sleep(4)
   await conf1.delete()
   await conf2.delete()




@dp.message_handler(commands=['cont_mod'], content_types=['any'])
async def startup_message(message: types.Message):

   if message.from_user.id == admin1 or message.from_user.id == admin2 or message.from_user.id == admin3:
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
   info_start_msg = await message.reply("Я Малик Альф-Саиф и если не будешь следовать правилам, то я наведу такую трёпку\nВ частности, если вы будете спаммить стикерами, то каждого буду банить в зависимости, сколько решат поставить времени.\n WebMast уже реализовал это, приятного общения!!!. >:) Правила таковы, слушайте админов и спамьте стикерами и гифками ")

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
        BotCommand(command="setup", description="Настроить Малика делать то, от чего вам нужно"),
        BotCommand(command="view_config", description="Посмотреть конфигурацию у конфигуратора"),
    ])
    asyncio.create_task(scheduler())
      

@dp.message_handler(content_types=['any']) #Создаём новое событие, которое запускается в ответ на любой текст, введённый пользователем.
async def echo(message: types.Message): #Создаём функцию с простой задачей — отправить обратно тот же текст, что ввёл пользователь.
   global stickerblock, maxstickerblock, blockedstickerblock,gifblock, maxgifblock, blockedgifblock, user_track_spam, new_message_time, old_message_time, spam_sticker_seconds
   global user_track_spam_gif, old_message_time_gif, new_message_time_gif, spam_gif_seconds
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
                  if old_message_time < 400000 and new_message_time < 400000:
                     spam_sticker_seconds += 1
                     print(f'Быстрый стикер: {spam_sticker_seconds} из 1')
                  else:
                     new_message_time == timemsg.microsecond
                     old_message_time = ''
                     spam_sticker_seconds = 0
                     print("Медленный стикер")

                  if spam_sticker_seconds == 1:
                     #antispam_message_sticker = await message.answer_sticker(stop_spam_sticker)\

                     random_ban_time = int(random.randint(900,3600))

                     antispam_message_text = await message.answer(f'Критичная спам атака, происходит блокировка спаммера {user_track_spam}. Блокировка будет длиться в течении {int(random_ban_time/60)} минут')
                     ban_time= (int(time.time()) + random_ban_time*random_ban_time+900)
                     print(ban_time)

                     await bot.restrict_chat_member(chat_id=message.chat.id, user_id=message.from_user.id,until_date=ban_time, can_send_messages=False)
                     
                     print(ban_time)
                     
                     time.sleep(1)
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

         time_gif_msg = datetime(datetime.now().year, datetime.now().month, datetime.now().day, datetime.now().hour, datetime.now().minute, datetime.now().second, datetime.now().microsecond)

         if user_track_spam_gif == '':
            user_track_spam_gif = message.from_user.first_name
            print(user_track_spam_gif)
            new_message_time_gif == time_gif_msg.microsecond
            old_message_time_gif = ''
         else:
            if user_track_spam_gif == message.from_user.first_name:
               if new_message_time_gif == '':
                  new_message_time_gif == time_gif_msg.microsecond
                  print(f'Принято гиферко за {new_message_time}')
               else:
                  old_message_time_gif = new_message_time_gif
                  new_message_time_gif = time_gif_msg.microsecond
                  print(f'Принято гиферко за {new_message_time}')
                  if old_message_time_gif < 1500000 and new_message_time_gif < 1500000:
                     spam_gif_seconds += 1
                     print(f'Быстрый гифе: {spam_sticker_seconds} из 1')
                  else:
                     new_message_time == time_gif_msg.microsecond
                     old_message_time = ''
                     spam_sticker_seconds = 0
                     print("Медленный гиф")

                  if spam_gif_seconds == 1:
                     #antispam_message_sticker = await message.answer_sticker(stop_spam_sticker)

                     random_ban_time = int(random.randint(900,3600))

                     antispam_message_text = await message.answer(f'Критичная спам атака, происходит блокировка спаммера {user_track_spam}. Блокировка будет длиться в течении {random_ban_time} минут')
                     ban_time= (int(time.time()) + random_ban_time*utc+random_ban_time)
                     print(ban_time)

                     await bot.restrict_chat_member(chat_id=message.chat.id, user_id=message.from_user.id,until_date=ban_time, can_send_messages=False)
                     
                     print(ban_time)
                     
                     time.sleep(1)
                     #antispam_message_sticker.delete()
                     await antispam_message_text.delete()
            else:
               user_track_spam_gif = message.from_user.first_name
               print(user_track_spam_gif)
               print(2)
               new_message_time_gif == time_gif_msg.microsecond
               old_message_time_gif = ''

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
         asyncio.sleep(2)
         await cont_msg.delete()
      else:
         pass

if __name__ == '__main__':
   
   print('Запуск Malik Alf-Salif 0.06')
   try:
      executor.start_polling(dp, skip_updates=True, on_startup=setup_default_commands)
   except:
      API_TOKEN = input('Укажите API токен еще раз. После второго раза, скрипт закроется \n API TOKEN> ')
      executor.start_polling(dp, skip_updates=True, on_startup=setup_default_commands)
