import telebot
from calc import model_racional as mr
import log_generate as lg

bot = telebot.TeleBot('TOKEN')
chat_id = ''
dic = {}


@bot.message_handler(commands=['start'])
def start(message):
    lg.write_data(f'Бот получил команду "{message.text}"')
    bot.send_message(message.chat.id, f'Привет {message.from_user.first_name}!')
    bot.send_message(message.chat.id, 'Чтобы начать считать пример напиши:\n''\nпосчитаем\n')


@bot.message_handler(commands=['help'])
def help(message):
    lg.write_data(f'Бот получил команду "{message.text}"')
    bot.send_message(chat_id, '/start - команда запуска\n'
                              'посчитаем - могу считать примеры записанные в одну строку например: 35*(75/5);\n'
                              '/help - вывод известных мне команд;')


@bot.message_handler()
def get_user_text(message):  # Выбор функций бота
    lg.write_data(f'Бот получил команду "{message.text}"')
    mes = message
    global chat_id
    chat_id = mes.chat.id
    if mes.text.lower() == 'посчитаем':
        bot.send_message(chat_id, 'Считаю примеры в одну строку, например: 35*(75/5) \nВводи свой пример: ')
        lg.write_data(f'Получаем пример для решения')
        bot.register_next_step_handler(mes, count_example)
    else:
        lg.write_data(f'Зафиксирована неизвестная команда')
        bot.send_message(message.chat.id, 'Я тебя не понимаю! Воспользуйся командой "/help"!')


def count_example(message):  # Функция решения примера
    example, example_list = mr.get_nums(message.text)
    lg.write_data(f'Пользователь ввел пример: {example}')
    result = mr.get_result(example_list)
    lg.write_data(f'Получен ответ: {result}')
    bot.send_message(chat_id, f'{example} = {result}')


def start_bot():
    print('Сервер запущен')
    bot.polling(none_stop=True)
