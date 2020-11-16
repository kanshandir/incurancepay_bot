import telebot

from telebot import types

bot = telebot.TeleBot('1480581627:AAHm08OQPEbwiLcIaG9-Dxq2LeN71ddDff0')


@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    item1 = types.KeyboardButton("НАЧНЕМ!")
    markup.add(item1)

    msg = bot.send_message(message.chat.id,
                           "ЗДРАВСТВУЙТЕ, Я - КАЛЬКУЛЯТОР \n"
                           "МОЯ ЗАДАЧА - ПОМОЧЬ ВАМ РАССЧИТАТЬ СТРАХОВЫЕ ВЗНОСЫ ДЛЯ ИП.".format(message.from_user,
                                                                                                bot.get_me()),
                           reply_markup=markup)
    bot.register_next_step_handler(msg, type_of_tax_sys)


def type_of_tax_sys(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    t1 = types.KeyboardButton("ДОХОДЫ")
    t2 = types.KeyboardButton("ДОХОДЫ МИНУС РАСХОДЫ")
    markup.add(t1, t2)
    msg = bot.send_message(message.chat.id, "ВЫБЕРИТЕ ВИД УСН", reply_markup=markup)
    bot.register_next_step_handler(msg, choose_sys)


def choose_sys(message):
    if message.text == "ДОХОДЫ":
        msg = bot.send_message(message.chat.id, 'ВВЕДИТЕ СУММУ ДОХОДОВ: ')
        bot.register_next_step_handler(msg, get_income_only)
    elif message.text == "ДОХОДЫ МИНУС РАСХОДЫ":
        msg1 = bot.send_message(message.chat.id, 'ВВЕДИТЕ СУММУ ДОХОДОВ: ')
        bot.register_next_step_handler(msg1, get_income)


def get_income_only(message):
    try:
        inc = int(message.text)
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        y1 = types.KeyboardButton("2017")
        y2 = types.KeyboardButton("2018")
        y3 = types.KeyboardButton("2019")
        y4 = types.KeyboardButton("2020")
        markup.add(y1, y2, y3, y4)

        msg = bot.send_message(message.chat.id, 'Выберите рассчетный период:', inc, reply_markup=markup)
        bot.register_next_step_handler(msg, get_only_inc_res, inc)
    except Exception as e:
        print(e)
        bot.reply_to(message, 'Что то пошло не так...проверьте правильность ввода')


def get_only_inc_res(message, inc):
    res = 23400
    res1 = 26545
    res2 = 29354
    res3 = 32448
    if message.text == '2017' and inc < 300000:
        bot.send_message(message.chat.id, f' Ваш доход меньше 300 000 руб. \n'
                                          f'Ваш налог за 2017 год составит: {res}')
    elif message.text == '2017' and inc > 300000:
        res4 = (inc - 300000) * 0.01 + res
        bot.send_message(message.chat.id, f' Ваш доход свыше 300 000 руб. \n'
                                          f'Ваш налог за 2017 год составит: {res4}')
    elif message.text == '2018' and inc < 300000:
        bot.send_message(message.chat.id, f' Ваш доход меньше 300 000 руб. \n'
                                          f'Ваш налог за 2018 год составит: {res1}')
    elif message.text == '2018' and inc > 300000:
        res5 = (inc - 300000) * 0.01 + res1
        bot.send_message(message.chat.id, f' Ваш доход свыше 300 000 руб. \n'
                                          f'Ваш налог за 2018 год составит: {res5}')
    elif message.text == '2019' and inc < 300000:
        bot.send_message(message.chat.id, f' Ваш доход меньше 300 000 руб. \n'
                                          f'Ваш налог за 2019 год составит: {res2}')
    elif message.text == '2019' and inc > 300000:
        res6 = (inc - 300000) * 0.01 + res2
        bot.send_message(message.chat.id, f' Ваш доход свыше 300 000 руб. \n'
                                          f'Ваш налог за 2019 год составит: {res6}')
    elif message.text == '2020' and inc < 300000:
        bot.send_message(message.chat.id, f' Ваш доход меньше 300 000 руб. \n'
                                          f'Ваш налог за 2020 год составит: {res3}')
    elif message.text == '2020' and inc > 300000:
        res7 = (inc - 300000) * 0.01 + res3
        bot.send_message(message.chat.id, f' Ваш доход свыше 300 000 руб. \n'
                                          f'Ваш налог за 2020 год составит: {res7}')


def get_income(message):
    try:
        inc = int(message.text)
        msg = bot.send_message(message.chat.id, 'ТЕПЕРЬ УКАЖИТЕ РАСХОДЫ:')
        bot.register_next_step_handler(msg, get_expenses, inc)
    except Exception as e:
        print(e)
        bot.reply_to(message, 'Это не число или что то пошло не так...')


def get_expenses(message, inc):
    try:
        exp = int(message.text)
        dif = inc - exp
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        y1 = types.KeyboardButton("2017")
        y2 = types.KeyboardButton("2018")
        y3 = types.KeyboardButton("2019")
        y4 = types.KeyboardButton("2020")
        markup.add(y1, y2, y3, y4)

        msg = bot.send_message(message.chat.id, 'Выберите рассчетный период:', inc, reply_markup=markup)
        bot.register_next_step_handler(msg, get_income_expenses_res, dif)
    except Exception as e:
        print(e)
        bot.reply_to(message, 'Что то пошло не так...проверьте правильность ввода')


def get_income_expenses_res(message, dif):
    res = 23400
    res1 = 26545
    res2 = 29354
    res3 = 32448
    if message.text == '2017' and dif < 300000:
        bot.send_message(message.chat.id, f' Ваш доход меньше 300 000 руб. \n'
                                          f'Ваш налог за 2017 год составит: {res}')
    elif message.text == '2017' and dif > 300000:
        res4 = (dif - 300000) * 0.01 + res
        bot.send_message(message.chat.id, f' Ваш доход свыше 300 000 руб. \n'
                                          f'Ваш налог за 2017 год составит: {res4}')
    elif message.text == '2018' and dif < 300000:
        bot.send_message(message.chat.id, f' Ваш доход меньше 300 000 руб. \n'
                                          f'Ваш налог за 2018 год составит: {res1}')
    elif message.text == '2018' and dif > 300000:
        res5 = (dif - 300000) * 0.01 + res1
        bot.send_message(message.chat.id, f' Ваш доход свыше 300 000 руб. \n'
                                          f'Ваш налог за 2018 год составит: {res5}')
    elif message.text == '2019' and dif < 300000:
        bot.send_message(message.chat.id, f' Ваш доход меньше 300 000 руб. \n'
                                          f'Ваш налог за 2019 год составит: {res2}')
    elif message.text == '2019' and dif > 300000:
        res6 = (dif - 300000) * 0.01 + res2
        bot.send_message(message.chat.id, f' Ваш доход свыше 300 000 руб. \n'
                                          f'Ваш налог за 2019 год составит: {res6}')
    elif message.text == '2020' and dif < 300000:
        bot.send_message(message.chat.id, f' Ваш доход меньше 300 000 руб. \n'
                                          f'Ваш налог за 2020 год составит: {res3}')
    elif message.text == '2020' and dif > 300000:
        res7 = (dif - 300000) * 0.01 + res3
        bot.send_message(message.chat.id, f' Ваш доход свыше 300 000 руб. \n'
                                          f'Ваш налог за 2020 год составит: {res7}')

if __name__ == '__main__':
    bot.polling(none_stop=True)
