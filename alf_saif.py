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
version = '1.2.1'
black_user_list=[]
timehour=0

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
   spam_sticker_seconds = 0

   admin1=int(input('Укажите ID первого админа для начального администрирования> '))
   print('Отлично. Теперь с помощью комманды /setup вы сможете детально настроить бота')

   user_track_spam_gif = ''
   new_message_time_gif = 0.0
   old_message_time_gif = 0.0
   spam_gif_seconds = 0

@dp.message_handler(commands=['about'], content_types=['any'])
async def startup_message(message: types.Message):
   info_msg = await message.answer(f'Malik Alf-Saif {version} Made by WebMast from WebAnLiMaks studio, hosted by {hoster}.')
   time_set = time.time()
   local_time = time.ctime(time_set)
   log = open('log.txt', 'a')
   user_sticker = message.from_user.first_name
   log.write(f'\n {local_time}: Пользователь {user_sticker} Вызвал версию бота')
   log.close()
   print(f'\n {local_time}: Пользователь {user_sticker} Вызвал версию бота')
   await asyncio.sleep(5)
   await info_msg.delete()
   await message.delete()

@dp.message_handler(commands=['sticker'], content_types=['any'])
async def startup_message(message: types.Message):
   global stickerblock, maxstickerblock, blockedstickerblock
   static = await message.answer(f'Доступных стикеров осталось: {maxstickerblock - stickerblock}. Заблокированных : {blockedstickerblock}')
   time_set = time.time()
   local_time = time.ctime(time_set)
   log = open('log.txt', 'a')
   user_sticker = message.from_user.first_name
   await message.delete()
   log.write(f'\n {local_time} : {user_sticker} вызвал статистику. Доступных стикеров осталось:  {maxstickerblock - stickerblock}. Заблокированных : {blockedstickerblock}')
   log.close()
   print(f'\n {local_time} : Доступных стикеров осталось: {maxstickerblock - stickerblock}. Заблокированных : {blockedstickerblock}')
   await asyncio.sleep(2)
   await static.delete()

@dp.message_handler(commands=['muted_ever_user'], content_types=['any'])
async def startup_message(message: types.Message):
   global black_user_list
   static = await message.answer(f'Список замученных пользователей: {black_user_list}')
   time_set = time.time()
   local_time = time.ctime(time_set)
   log = open('log.txt', 'a')
   user_sticker = message.from_user.first_name
   await message.delete()
   log.write(f'\n {local_time} : {user_sticker} вызвал список замученых пользователей. Список замученных пользователей: {black_user_list}')
   log.close()
   print(f'\n {local_time} : Список замученных пользователей: {black_user_list}')
   await asyncio.sleep(2)
   await static.delete()

@dp.message_handler(commands=['gif'], content_types=['any'])
async def startup_message(message: types.Message):
   global gifblock, maxgifblock, blockedgifblock

   time_set = time.time()
   local_time = time.ctime(time_set)

   static = await message.answer(f'Доступных гифок осталось:  {maxgifblock - gifblock}. Заблокированных : {blockedgifblock}')
   
   log = open('log.txt', 'a')
   user_sticker = message.from_user.first_name
   await message.delete()
   log.write(f'\n {local_time} : {user_sticker} вызвал статистику. Доступных гифок осталось:  {maxgifblock - gifblock}. Заблокированных : {blockedgifblock}')
   log.close()
   print(f'\n {local_time} : Доступных гифок осталось:  {maxgifblock - gifblock}. Заблокированных : {blockedgifblock}')
   await asyncio.sleep(2)
   await static.delete()

@dp.message_handler(commands=['mut'], content_types=['any'])
async def startup_message(message: types.Message):
   global black_user_list

   if message.from_user.id == admin1 or message.from_user.id == admin2 or message.from_user.id == admin3:
      
      muted_user = message.text

      muted_user = muted_user.split()[1:]
      
      try:
         unmut_user = await bot.get_chat_member(chat_id=message.chat.id, user_id=muted_user[0])

         if unmut_user.is_chat_admin() == True:
            admin_info = await message.answer('Пользователь является админом')
            await asyncio.sleep(5)
            await admin_info.delete()
            await message.delete()
         else:
            try:
               await bot.restrict_chat_member(chat_id=message.chat.id, user_id=muted_user[0], can_send_messages=False)
               await bot.restrict_chat_member(chat_id=message.chat.id, user_id=muted_user[0], can_send_media_messages=False)
               await bot.restrict_chat_member(chat_id=message.chat.id, user_id=muted_user[0], can_send_other_messages=False)
               await message.answer(f'Замучен пользователь {unmut_user.user.first_name}.')
               black_user_list.append(unmut_user.user.first_name)
            except:
               admin_info = await message.answer(f'Не удается размутить пользователя {unmut_user.user.first_name}.')
               await asyncio.sleep(5)
               await admin_info.delete()
               await message.delete()
      except:
         admin_info = await message.answer(f'Проверьте ID пользователя')
         await asyncio.sleep(5)
         await admin_info.delete()
         await message.delete()
      

      time_set = time.time()
      local_time = time.ctime(time_set)
      log = open('log.txt', 'a')
      user_sticker = message.from_user.first_name
      log.write(f'\n {local_time}: Пользователь {user_sticker} замутил пользователя')
      log.close()
      print(f'\n {local_time}: Пользователь {user_sticker} замутил пользователя')
   else:

      time_set = time.time()
      local_time = time.ctime(time_set)
      log = open('log.txt', 'a')
      user_sticker = message.from_user.first_name
      log.write(f'\n {local_time}: Пользователь {user_sticker} Попытался замутить пользователя')
      log.close()
      print(f'\n {local_time}: Пользователь {user_sticker} Попытался замутить пользователя')

      clear_log_info = await message.answer('Доступ ограничен. Попросите об этом админов')
      await message.delete()
      await asyncio.sleep(5)
      await clear_log_info.delete()

@dp.message_handler(commands=['unmut'], content_types=['any'])
async def startup_message(message: types.Message):
   if message.from_user.id == admin1 or message.from_user.id == admin2 or message.from_user.id == admin3:
      
      muted_user = message.text

      muted_user = muted_user.split()[1:]

      try:
         unmut_user = await bot.get_chat_member(chat_id=message.chat.id, user_id=muted_user[0])

         if unmut_user.is_chat_admin() == True:
            admin_info = await message.answer('Пользователь является админом')
            await asyncio.sleep(5)
            await admin_info.delete()
            await message.delete()
         else:
            try:
               await bot.restrict_chat_member(chat_id=message.chat.id, user_id=muted_user[0], can_send_messages=True)
               await bot.restrict_chat_member(chat_id=message.chat.id, user_id=muted_user[0], can_send_media_messages=True)
               await bot.restrict_chat_member(chat_id=message.chat.id, user_id=muted_user[0], can_send_other_messages=True)
               await message.answer(f'Размучен пользователь {unmut_user.user.first_name}.')
               black_user_list.remove(unmut_user.user.first_name)
            except:
               admin_info = await message.answer(f'Не удается размутить пользователя {unmut_user.user.first_name}.')
               await asyncio.sleep(5)
               await admin_info.delete()
               await message.delete()
      except:
         admin_info = await message.answer(f'Проверьте ID пользователя')
         await asyncio.sleep(5)
         await admin_info.delete()
         await message.delete()
         
      time_set = time.time()
      local_time = time.ctime(time_set)
      log = open('log.txt', 'a')
      user_sticker = message.from_user.first_name
      log.write(f'\n {local_time}: Пользователь {user_sticker} размутил пользователя')
      log.close()
      print(f'\n {local_time}: Пользователь {user_sticker} размутил пользователя')
   else:
      time_set = time.time()
      local_time = time.ctime(time_set)
      log = open('log.txt', 'a')
      user_sticker = message.from_user.first_name
      log.write(f'\n {local_time}: Пользователь {user_sticker} Попытался размутить пользователя')
      log.close()
      print(f'\n {local_time}: Пользователь {user_sticker} Попытался размутить пользователя')

      clear_log_info = await message.answer('Доступ ограничен. Попросите об этом админов')
      await message.delete()
      await asyncio.sleep(5)
      await clear_log_info.delete()
   
@dp.message_handler(commands=['clear_log'], content_types=['any'])
async def startup_message(message: types.Message):
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
      await asyncio.sleep(2)
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
      await asyncio.sleep(5)
      await clear_log_info.delete()

@dp.message_handler(commands=['admin_command'], content_types=['any'])
async def startup_message(message: types.Message):
   if message.from_user.id == admin1 or message.from_user.id == admin2 or message.from_user.id == admin3 :
      if message.chat.type == 'private':
         import os

         await message.answer('Вот список комманд:\n /setup - Настроить Малика делать то, от чего вам нужно\n /mut - Замутить пользователя. Команда работает так: /mut [ID пользователя]\n /unmut - Размутить пользователя. Команда работает так: /unmut [ID пользователя]\n /clear_log - Очистка логов\n /obnull_limit_all - Обнуление лимита отправляемых гифок и стикеров')


         time_set = time.time()
         local_time = time.ctime(time_set)
         log = open('log.txt', 'a')
         user_sticker = message.from_user.first_name
         log.write(f'\n {local_time}: Пользователь {user_sticker} просмотрел команды для админов')
         log.close()
         print(f'\n {local_time}: Пользователь {user_sticker} просмотрел команды для админов')
      else:
         clear_log_info = await message.answer('Данная комманда выполняется в личном чате')
         await message.delete()
         await asyncio.sleep(5)
         await clear_log_info.delete()
   else:
      time_set = time.time()
      local_time = time.ctime(time_set)
      log = open('log.txt', 'a')
      user_sticker = message.from_user.first_name
      log.write(f'\n {local_time}: Пользователь {user_sticker} Хотел посмотреть комманды админов')
      log.close()
      print(f'\n {local_time}: Пользователь {user_sticker} Хотел посмотреть комманды админов')

      clear_log_info = await message.answer('Данная комманда выполняется админами')
      await message.delete()
      await asyncio.sleep(5)
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

      clear_log_info = await message.answer('Обнуление лимита доступных к отправке стикеров и гифок')
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
      await asyncio.sleep(5)
      await clear_log_info.delete()

class Form(StatesGroup):
   hoster_name = State()
   utc_number = State()
   max_sticker = State() 
   max_gif = State()
   id_admin1 = State()
   id_admin2 = State()
   id_admin3  = State()
   
@dp.message_handler(commands=['view_log'], content_types=['any'])
async def startup_message(message: types.Message):
   if message.chat.type == 'private':
      view_log = open('log.txt', 'r')
      log_msg=view_log.read()
      view_log.close()
      if len(log_msg) > 4096:
         for x in range(0, len(log_msg), 4096):
            await bot.send_message(message.chat.id, log_msg[x:x+4096])

      time_set = time.time()
      local_time = time.ctime(time_set)
      log = open('log.txt', 'a')
      user_sticker = message.from_user.first_name
      log.write(f'\n {local_time}: Пользователь {user_sticker} Посмотрел логи')
      log.close()
      print(f'\n {local_time}: Пользователь {user_sticker} Посмотрел логи')
   else:
      setup_admin_msg = await message.answer('Данная команда выполняется в личном чате с ботом.')
      await asyncio.sleep(3)
      await setup_admin_msg.delete()
      await message.delete()

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
         await message.delete()
   else:
      time_set = time.time()
      local_time = time.ctime(time_set)
      log = open('log.txt', 'a')
      user_sticker = message.from_user.first_name
      log.write(f'\n {local_time}: Пользователь {user_sticker} попытался вызвать конфигуратор')
      log.close()
      print(f'\n {local_time}: Пользователь {user_sticker} попытался вызвать конфигуратор')

      clear_log_info = await message.answer('Доступ ограничен. Попросите об этом админов')
      await message.delete()
      await asyncio.sleep(5)
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
    global hoster, utc, maxstickerblock, maxgifblock, stickerblock, gifblock, admin2, admin3
    async with state.proxy() as ses_config:
      ses_config['id_admin3'] = message.text

      await bot.send_message(message.chat.id, 'в конфигурации будет:')

      admin2=int(ses_config['id_admin2'])
      admin3=int(ses_config['id_admin3'])

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
    maxstickerblock=int(ses_config['max_sticker'])
    maxgifblock=int(ses_config['max_gif'])
    utc=int(ses_config['utc_number'])
    hoster=ses_config['hoster_name']

@dp.message_handler(commands=['view_config'])
async def send_welcome(message: types.Message):
   if message.chat.type == 'private':
      conf1 = await bot.send_message(message.chat.id, 'в конфигурации:')
      conf2 = await bot.send_message(
               message.chat.id,
               md.text(
                  md.text('API токен бота: ', md.code(API_TOKEN)),
                  md.text('Имя хостера: ', hoster),
                  md.text('Часовой пояс: ', utc),
                  md.text('Максимальное количество стикеров: ', maxstickerblock),
                  md.text('Максимальное количество гифок: ', maxgifblock),
                  md.text('Первый администратор: ', admin1),
                  md.text('Второй администратор: ', admin2),
                  md.text('Третий администратор: ', admin3),
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
   else:
      conf1 = await bot.send_message(message.chat.id, 'в конфигурации:')
      name_admin1 = await bot.get_chat_member(message.chat.id, admin1)
      name_admin2 = await bot.get_chat_member(message.chat.id, admin2)
      name_admin3 = await bot.get_chat_member(message.chat.id, admin3)
      conf2 = await bot.send_message(
               message.chat.id,
               md.text(
                  md.text('API токен бота: ', md.code(API_TOKEN)),
                  md.text('Имя хостера: ', hoster),
                  md.text('Часовой пояс: ', utc),
                  md.text('Максимальное количество стикеров: ', maxstickerblock),
                  md.text('Максимальное количество гифок: ', maxgifblock),
                  md.text('Первый администратор: ', name_admin1.user.first_name),
                  md.text('Второй администратор: ', name_admin2.user.first_name),
                  md.text('Третий администратор: ', name_admin3.user.first_name),
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
      await asyncio.sleep(4)
      await conf1.delete()
      await conf2.delete()

@dp.message_handler(commands=['start']) 
async def send_welcome(message: types.Message):
   info_start_msg = await message.reply("Я бот, который блокирует нарушителей правил. Правила таковы, не спамьте стикерами и гифками ")

   time_set = time.time()
   local_time = time.ctime(time_set)
   log = open('log.txt', 'a')
   user_sticker = message.from_user.first_name
   log.write(f'\n {local_time}: Пользователь {user_sticker} Cделал старт меня')
   log.close()
   print(f'\n {local_time}: Пользователь {user_sticker} Cделал старт меня')
   await asyncio.sleep(10)
   await info_start_msg.delete()
   await message.delete()

async def obnull_limit_rasp():
   global stickerblock, gifblock

   stickerblock = 0
   gifblock = 0

   time_set = time.time()
   local_time = time.ctime(time_set)
   log = open('log.txt', 'a')
   log.write(f'\n {local_time}: Обнуление лимита стикеров,гифок')
   log.close()
   print(f'\n {local_time}: Обнуление лимита стикеров,гифок')

async def scheduler():
   global timehour
   while True:
         await aioschedule.run_pending()
         await asyncio.sleep(1)

         timehour +=1
         if timehour == 3600:
            await obnull_limit_rasp()
            timehour = 0
        
async def setup_default_commands(dp):
   await dp.bot.set_my_commands([
      BotCommand(command="start", description="Приветствие от Малика"),
      BotCommand(command="about", description="О Малике"),
      BotCommand(command="sticker", description="Проверка доступных к отправке стикеров"),
      BotCommand(command="gif", description="Проверка доступных к отправке гифок"),
      BotCommand(command="muted_ever_user", description="Список полностью замученных пользователей"),
      BotCommand(command="view_log", description="Посмотреть все логи"),
      BotCommand(command="admin_command", description="Команды для администрирования"),
      BotCommand(command="view_config", description="Посмотреть конфигурацию бота"),
    ])
   asyncio.create_task(scheduler())
      
@dp.message_handler(content_types=['any']) 
async def echo(message: types.Message):
   global stickerblock, maxstickerblock, blockedstickerblock,gifblock, maxgifblock, blockedgifblock, user_track_spam, new_message_time, old_message_time, spam_sticker_seconds
   global user_track_spam_gif, old_message_time_gif, new_message_time_gif, spam_gif_seconds, black_user_list
   if message.sticker:
      if message.chat.type == 'private':
         await message.answer('В личном чате сообщения не фильтруются.')
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
            new_message_time = timemsg.microsecond
            old_message_time = ''
         else:
            if user_track_spam == message.from_user.first_name:
               if new_message_time == '':
                  new_message_time = timemsg.microsecond
                  old_message_time = ''
                  print(f'Принят стикер за {new_message_time}')
               else:
                  old_message_time = new_message_time
                  new_message_time = timemsg.microsecond
                  print(f'Принят стикер за {new_message_time}')
                  if old_message_time < 35000 and new_message_time < 35000:
                     spam_sticker_seconds += 1
                     print(f'Быстрый стикер: {spam_sticker_seconds} из 1')
                  else:
                     new_message_time = timemsg.microsecond
                     old_message_time = ''
                     spam_sticker_seconds = 0
                     print("Медленный стикер")

                  if spam_sticker_seconds == 1:

                     time_utc = time.gmtime()
                     info_utc = time.strftime('%Y-%m-%d %H:%M:%S', time_utc)
                     utc_sec = datetime.strptime(info_utc,'%Y-%m-%d %H:%M:%S').timestamp()

                     ban_cel = 1800

                     ban_time = (int(utc_sec) + utc*3600 + 1800)
                     print(time.ctime(ban_time))

                     user_status = await bot.get_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)
                     
                     if user_status.is_chat_admin() == True:
                        await message.answer(f'Пользователь {user_track_spam} не блокируется, так как прав бота не достаточно, чтобы блокировать администраторов. Увы(')
                     else:
                        await bot.restrict_chat_member(chat_id=message.chat.id, user_id=message.from_user.id,until_date=ban_time, can_send_messages=False)
                        await bot.restrict_chat_member(chat_id=message.chat.id, user_id=message.from_user.id,until_date=ban_time, can_send_media_messages=False)
                        await bot.restrict_chat_member(chat_id=message.chat.id, user_id=message.from_user.id,until_date=ban_time, can_send_other_messages=False)
                        await message.answer(f'Пользователь {user_track_spam} быстро отправлял стикеры. Блокировка будет длиться в течении {int(ban_cel/60)} минут. Окончание блокировки: {time.ctime(ban_time)}')

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
         await message.answer('Гифки не фильтруются в личном чате')
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
            new_message_time_gif = time_gif_msg.microsecond
            old_message_time_gif = ''
         else:
            if user_track_spam_gif == message.from_user.first_name:
               if new_message_time_gif == '':
                  old_message_time_gif = ''
                  new_message_time_gif = time_gif_msg.microsecond
                  print(f'Принята гифка за {new_message_time}')
               else:
                  old_message_time_gif = new_message_time_gif
                  new_message_time_gif = time_gif_msg.microsecond
                  print(f'Принята гифка за {new_message_time}')
                  if old_message_time_gif < 5000000 and new_message_time_gif < 5000000:
                     spam_gif_seconds += 1
                     print(f'Быстрая отправленная гифка: {spam_sticker_seconds} из 1')
                  else:
                     new_message_time = time_gif_msg.microsecond
                     old_message_time = ''
                     spam_sticker_seconds = 0
                     print("Медленная отправленная гифка")

                  if spam_gif_seconds == 1:

                     time_utc = time.gmtime()
                     info_utc = time.strftime('%Y-%m-%d %H:%M:%S', time_utc)
                     utc_sec = datetime.strptime(info_utc,'%Y-%m-%d %H:%M:%S').timestamp()

                     ban_cel = 1800
                     
                     ban_time = (int(utc_sec) + utc*3600 + 1800)
                     print(time.ctime(ban_time))
                     
                     user_status = await bot.get_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)

                     if user_status.is_chat_admin() == True:
                        await message.answer(f'Пользователь {user_track_spam} не блокируется, так как прав бота не достаточно, чтобы блокировать администраторов. Увы(')
                     else:
                        await bot.restrict_chat_member(chat_id=message.chat.id, user_id=message.from_user.id,until_date=ban_time, can_send_messages=False)
                        await bot.restrict_chat_member(chat_id=message.chat.id, user_id=message.from_user.id,until_date=ban_time, can_send_media_messages=False)
                        await bot.restrict_chat_member(chat_id=message.chat.id, user_id=message.from_user.id,until_date=ban_time, can_send_other_messages=False)
                        await message.answer(f'Пользователь {user_track_spam} очень быстро отправлял гифки. Блокировка будет длиться в течении {int(ban_cel/60)} минут. Окончание блокировки: {time.ctime(ban_time)}')
            else:
               user_track_spam_gif = message.from_user.first_name
               print(user_track_spam_gif)
               print(2)
               new_message_time_gif = time_gif_msg.microsecond
               old_message_time_gif = ''

         time_set = time.time()
         local_time = time.ctime(time_set)
         log = open('log.txt', 'a')
         user_sticker = message.from_user.first_name
         log.write(f'\n {local_time}: Пользователь {user_sticker} Отправил гифку. Статус - {status}')
         log.close()
         print(f'\n {local_time}: Пользователь {user_sticker} Отправил гифку. Статус - {status}')
   elif message.text:
      old_message_time = ''
      old_message_time_gif = ''
      new_message_time = ''
      new_message_time = ''
      time_set = time.time()
      local_time = time.ctime(time_set)
      log = open('log.txt', 'a')
      user_sticker = message.from_user.first_name
      log.write(f'\n {local_time}: Пользователь {user_sticker} отправил сообщение текстом: {message.text}')
      log.close()
      print(f'\n {local_time}: Пользователь {user_sticker} отправил сообщение текстом: {message.text}')

if __name__ == '__main__':
   print(f'Malik Alf-Saif {version}')
   try:
      executor.start_polling(dp, skip_updates=True, on_startup=setup_default_commands)
   except:
      wifi_detect = input('Бот не запустился. Проверьте, у вас рабочая сеть и без ограничений. Если все впорядке, то пишите Y или y\nЕсли у вас какие-то проблемы, то пока не пишите до тех пор, пока не устраните проблемы) > ')
      if wifi_detect == 'Y' or wifi_detect == 'y':
         repeat_setup = input('Попробовать запустить сценарий еще раз?(Y,y(Да),N,n(Нет)) > ')
         if repeat_setup == 'Y' or repeat_setup == 'y':
            try:
               executor.start_polling(dp, skip_updates=True, on_startup=setup_default_commands)
            except:
               print('Попытка запустить бота с сценарием не удалась, но вы можете попытаться запустить его, введя вручную API бота')
               API_TOKEN = input('Укажите API токен \n API TOKEN> ')
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
               spam_sticker_seconds = 0

               admin1=int(input('Укажите ID первого админа для начального администрирования> '))
               print('Отлично. Теперь с помощью комманды /setup вы сможете детально настроить бота')

               user_track_spam_gif = ''
               new_message_time_gif = 0.0
               old_message_time_gif = 0.0
               spam_gif_seconds = 0
               executor.start_polling(dp, skip_updates=True, on_startup=setup_default_commands)
         elif repeat_setup == 'N' or repeat_setup == 'n':
            API_TOKEN = input('Укажите API токен \n API TOKEN> ')
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
            spam_sticker_seconds = 0

            admin1=int(input('Укажите ID первого админа для начального администрирования> '))
            print('Отлично. Теперь с помощью комманды /setup вы сможете детально настроить бота')

            user_track_spam_gif = ''
            new_message_time_gif = 0.0
            old_message_time_gif = 0.0
            spam_gif_seconds = 0
            executor.start_polling(dp, skip_updates=True, on_startup=setup_default_commands)
      else:
         print('Вас не просили что-то постороннее писать, поэтому скрипт отключится')
         quit()