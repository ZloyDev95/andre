import telebot
from telegram.ext import Updater, CommandHandler
import requests
import re

bot = telebot.TeleBot('1040197602:AAHyxkvUSSQl_PRoWehvrzLQMX8TpBfp7DI')

#Main
keymain = telebot.types.ReplyKeyboardMarkup(True)
keymain.row('Готовые клады 🎁')
keymain.row('Оператор 👤')
keymain.row('Канал 📢', 'Чат 💬')
keymain.row('Рулетки 🎁 Конкурсы')
keymain.row('Сотрудничество 💼')

#Города
keycity = telebot.types.ReplyKeyboardMarkup(True,True)

keycity.row('Винница')
keycity.row('В начало 🔙')

#Районы
keycitypart = telebot.types.ReplyKeyboardMarkup(True,True)

keycitypart.row('Урожай')
keycitypart.row('Центр')
keycitypart.row('Вишенка')
keycitypart.row('Замостье')
keycitypart.row('В начало 🔙')

#Товары
keystaff = telebot.types.ReplyKeyboardMarkup(True,True)

keystaff.row('❄️АМФ❄️')
keystaff.row('В начало 🔙')

#ОплатаПроверка
keypaycheck = telebot.types.ReplyKeyboardMarkup(True,True)

keypaycheck.row('✔️ Проверить оплату','✖️ Отмена')

#Оплата1
keypay1 = telebot.types.ReplyKeyboardMarkup(True,True)

keypay1.row('🔷 EasyPay (335 грн)')
keypay1.row('✖️ Отменить заказ')

#Оплата0.5
keypay = telebot.types.ReplyKeyboardMarkup(True,True)

keypay.row('🔷 EasyPay (225 грн)')
keypay.row('✖️ Отменить заказ')


#Количество
keyamount = telebot.types.ReplyKeyboardMarkup(True,True)

keyamount.row('❄️0.5г')
keyamount.row('❄️1г')
keyamount.row('В начало 🔙')

#Количество2
keyamount2 = telebot.types.ReplyKeyboardMarkup(True,True)

keyamount2.row('❄️1г')
keyamount2.row('В начало 🔙')


#Back
keybacking = telebot.types.ReplyKeyboardMarkup(True,True)
keybacking.row('В начало 🔙')


@bot.message_handler(commands=['start'])
### ПРИВЕТСТВИЕ ###
def start_message(message):
    bot.send_message(message.chat.id, 'Добро пожаловать в бот автопродаж 24/7\n\nВ данный момент все покупки только через бот @AndrevineBot', reply_markup=keymain)
    bot.send_message(message.chat.id, '🔔🔔🔔: ', reply_markup=keymain)
    bot.send_message(message.chat.id, '⚠️Aккаунт @andrevine заблокирован!\nНовый телеграм @andrevine_shop t.me/andrevine_shop ✔️', reply_markup=keymain)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'канал 📢':
        bot.send_message(message.chat.id, '📢 https://t.me/joinchat/AAAAAFC_fHQ8P26NqeKw3Q', reply_markup=keybacking)
    elif message.text.lower() == 'чат 💬':
        bot.send_message(message.chat.id, '💬 https://t.me/joinchat/PJ9WIhQbU8LX2WuI1yxLVQ', reply_markup=keybacking)
    elif message.text.lower() == 'сотрудничество 💼':
        bot.send_message(message.chat.id, 'По всем вопросам, предложениям и жалобам 👤 @andrevine_shop', reply_markup=keybacking)
        bot.send_message(message.chat.id, 'https://t.me/andrevine_shop', reply_markup=keybacking)
    elif message.text.lower() == 'рулетки 🎁 конкурсы':
        bot.send_message(message.chat.id, 'В данный момент конкурсов нет ⛔️', reply_markup=keybacking)
    elif message.text.lower() == 'в начало 🔙':
    	return start_message(message) 
    elif message.text.lower() == 'оператор 👤':
        bot.send_message(message.chat.id, '👤 https://t.me/andrevine_shop', reply_markup=keybacking)
        bot.send_message(message.chat.id, 'https://imgur.com/a/NvGiJn5', reply_markup=keybacking)
    elif message.text.lower() == 'готовые клады 🎁':
        bot.send_message(message.chat.id, '➖ Выберите город', reply_markup=keycity)
    elif message.text.lower() == 'винница':
        bot.send_message(message.chat.id, '➖ Выберите район', reply_markup=keycitypart)
    elif message.text.lower() == 'урожай':
        bot.send_message(message.chat.id, 'Товары отсутствуют (❌)', reply_markup=keybacking)
    elif message.text.lower() == 'центр':
        bot.send_message(message.chat.id, 'Товары отсутствуют (❌)', reply_markup=keybacking)
    elif message.text.lower() == 'замостье':
        bot.send_message(message.chat.id, '➖ Выберите товар', reply_markup=keystaff)
    elif message.text.lower() == 'вишенка':
        bot.send_message(message.chat.id, '➖ Выберите товар', reply_markup=keystaff)
    elif message.text.lower() == '❄️амф❄️':
        bot.send_message(message.chat.id, '➖ Выберите количество', reply_markup=keyamount)
    elif message.text.lower() == '❄️0.5г':
        bot.send_message(message.chat.id, '➖ Выберите способ оплаты товара', reply_markup=keypay)
    elif message.text.lower() == '❄️1г':
        bot.send_message(message.chat.id, '➖ Выберите способ оплаты товара', reply_markup=keypay1)
    elif message.text.lower() == '🔷 easypay (335 грн)':
        bot.send_message(message.chat.id, "◼️ Инструкция по оплате товара через EasyPay.\nПополните кошелек 32227109 одним платежом на сумму 335 грн или больше (без учета комиссии)\n\n➖После пополнения кошелька нажмите 'Проверить оплату'", reply_markup=keypaycheck)
    elif message.text.lower() == '✖️ отменить заказ':
        return start_message(message) 
    elif message.text.lower() == '🔷 easypay (225 грн)':
        bot.send_message(message.chat.id, "◼️ Инструкция по оплате товара через EasyPay.\nПополните кошелек 32227109 одним платежом на сумму 225 грн или больше (без учета комиссии)\n\n➖После пополнения кошелька нажмите 'Проверить оплату'", reply_markup=keypaycheck)
    elif message.text.lower() == '✖️ отмена':
        return start_message(message) 



bot.polling()
