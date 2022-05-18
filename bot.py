import telebot
from telebot import types
import config
import text

bot = telebot.TeleBot(config.TOKEN)

name = ''
nomer = 0
country = ''
formats = ''
subject = ''
clas = 0
individ = ''
day = ''

yea = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
graduate = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
keyboard1 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
keyboard2 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
start_keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
fm = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
pytoshka = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
individd = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
pytoshka.row('Оставить отзыв!')
fm.row('Онлайн', 'Офлайн')
graduate.row('1', '2', '3', '4', '5', '6')
graduate.row('7', '8', '9', '10', '11')
start_keyboard.row('Нур-Султан', 'Алматы')
start_keyboard.row('Шымкент', 'Атырау')
start_keyboard.row('Кызылорда','Другое...')
keyboard1.row('Математика', 'Физика', 'Химия')
keyboard1.row('Биология', 'Английский язык')
keyboard1.row('ЕНТ', 'IELTS')
keyboard1.row('НИШ, БИЛ, РФМШ', 'Программирование')
keyboard2.row('Позвонить', 'Написать', 'Адрес')
yea.row('Да', 'Нет')
individd.row('Индивидуально','Групповое обучение')
dday = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
dday.row('Суббота','Воскресенье')





@bot.message_handler(commands=['start'])
def start_message(message):
	markup_inline = types.InlineKeyboardMarkup()
	item_one = types.InlineKeyboardButton(text='Наши курсы', callback_data='1')
	item_two = types.InlineKeyboardButton(text='О наc', callback_data='2')
	item_three = types.InlineKeyboardButton(text='Контакты', callback_data='3')
	item_for = types.InlineKeyboardButton(text='Записаться на пробный урок!', callback_data='4')

	markup_inline.add(item_one, item_two, item_three, item_for)
	sti = open('anime.tgs', 'rb')
	bot.send_sticker(message.chat.id, sti)
	bot.send_message(message.chat.id, f'Привет👋🏻  *{message.from_user.first_name}* *{message.from_user.last_name}*!\n - К вашим услугам бот 👉🏻*Чарли* 🤖 Я стану вашим помощником в мире знаний.📚 Меня создала команда перспективных учителей образовательного центра *LeveL* .🏫Присоединяйся к нам!😉 \n\n- Чем я могу вам помочь?🙂 Выбери одно из ниже приведенных!)😌 ', reply_markup = markup_inline,parse_mode="Markdown")


@bot.callback_query_handler(func=lambda call: True)
def answer(call):
	if call.data == '1':
		bot.send_message(call.message.chat.id, "- Математика\n- Физика\n- Английский язык\n- Программирование\n- Подготвка к ЕНТ\n- Подготовка к IELTS\n- Подготовка к НИШ, БИЛ, РФМШ\n---------------------------------------\nЕсли вас заинтересовал каталог цен на предметы 👇🏻 \n https://wa.me/c/77058037757", reply_markup=keyboard1)
		bot.send_message(call.message.chat.id, 'Какой предмет вас заинтересовал?')
	elif call.data == '2':
		bot.send_message(call.message.chat.id, text.text)
	elif call.data == '3':
		bot.send_message(call.message.chat.id, 'Ты выбрал(-а) пункт 👉🏻  Контакты 📞', reply_markup=keyboard2)
	if call.data == '4':
		bot.send_message(call.message.chat.id, 'Ты выбрал(-а) пункт 👉🏻  Записаться на пробный урок ✅')
		bot.send_message(call.message.chat.id, 'Нажми на 👉🏻 /registration ✅')




@bot.message_handler(commands=['help'])
def send_settings(message):
	bot.send_message(message.chat.id, "Если у вас возникли вопросы вы можете связаться с нашим менеджером :\n\nWhatsApp - https://wa.link/bjrgou\n\nИли вы можете связаться на прямую по этому номеру : +77058037757")


@bot.message_handler(commands=["registration"])
def geo_phone(message):
	bot.send_message(message.from_user.id, 'Здраствуйте! Как вас зовут?')
	bot.register_next_step_handler(message, reg_name)


def reg_name(message):
	global name
	name = message.text
	bot.send_message(message.from_user.id, 'Ваш номер телефона WhatsApp:')
	bot.register_next_step_handler(message, reg_number)


def reg_number(message):
	global nomer
	nomer = message.text
	bot.send_message(message.from_user.id, 'С какого вы города?', reply_markup=start_keyboard)
	bot.register_next_step_handler(message, reg_country)


def reg_country(message):
	global country
	country = message.text
	bot.send_message(message.from_user.id, 'Предпочитаемый формат обучения: ', reply_markup=fm)
	bot.register_next_step_handler(message, reg_format)


def reg_format(message):
	global formats
	formats = message.text
	bot.send_message(message.from_user.id, 'Какой предмет вы выбрали?', reply_markup=keyboard1)
	bot.register_next_step_handler(message, reg_subject)


def reg_subject(message):
	global subject
	subject = message.text
	bot.send_message(message.from_user.id, 'Как вы бы хотели проходить обучение в нашем центре?', reply_markup= individd)
	bot.register_next_step_handler(message, reg_individ)


def reg_individ(message):
	global individ
	individ = message.text
	bot.send_message(message.from_user.id, 'Ваш класс обучения?', reply_markup=graduate)
	bot.register_next_step_handler(message, reg_clas)


def reg_clas(message):
	global clas
	if clas == 0:
		try:
			clas = int(message.text)
		except Exception:
			bot.send_message(message.from_user.id, 'Мне хватит одной цифры!)')
	bot.send_message(message.from_user.id, 'Когда вы бы хотели посетить пробный урок?', reply_markup=dday)
	bot.register_next_step_handler(message, reg_days)


def reg_days(message):
	global day
	day = message.text
	question = '*Перепроверьте вашу информацию!*\n' + '--------------------------------------\n' + 'Ваше имя : ' + name + '\n' + 'Город : ' + country + '\n' + 'Предмет : ' + subject +'\n'+'Формат обучения: ' + formats +'\n' + 'Обучение: '+ individ + '\n' + 'Класс : ' + str(clas) + '\n' + 'Номер телефона : ' + str(nomer) + '\n' + 'День записи: ' + day +'\n' + '--------------------------------------\n' +'*Все правильно?*'
	bot.send_message(message.from_user.id, question, reply_markup= yea, parse_mode="Markdown")


@bot.message_handler()
def worker(message):
	aswers = 'Имя: ' + name + '\n' + 'Номер: ' + str(nomer) + '\n' + 'Город: ' + country + '\n' + 'Предмет: ' + subject + '\n' + 'Класс: ' + str(clas) + '\n '+ 'Формат обучения: ' + formats +'\n'+ 'Обучение: ' + individ + '\n' + 'День записи: ' + day
	if message.text == 'Да':
		channel_id = -1001506079400  # Здесь укажите ID Вашего канала
		bot.send_message(channel_id, str(aswers))
		stik = open('goodbye.tgs', 'rb')
		bot.send_sticker(message.chat.id, stik, reply_markup=pytoshka)
	elif message.text == 'Нет':
		bot.message_handler(message.from_user.id, 'Окей, давай попробуем еще раз!)')
		bot.send_message(message.from_user.id, 'Как вас зовут?')
		bot.register_next_step_handler(message, reg_name)

	if message.text == 'Математика':
		bot.send_message(message.chat.id, "- Слово «математика» произошло от др.-греч. μάθημα, что означает изучение, знание, наука, и др.-греч. μαθηματικός, первоначально означающего восприимчивый, успевающий, позднее относящийся к изучению, впоследствии относящийся к математике.\n- *В нашей школе курс математики для любого класса стоит - 15.000 тенге*", parse_mode="Markdown")
	elif message.text == 'Физика':
		bot.send_message(message.chat.id, "- Фи́зика (от др.-греч. φυσική — «природный» от φύσις — «природа») — область естествознания: наука о наиболее общих законах природы, о материи, её структуре, движении и правилах трансформации. Понятия физики и её законы лежат в основе всего естествознания[1][2]. Является точной наукой.\n*В нашей школе курс физики для любого класса стоит - 15.000 тенге*", parse_mode="Markdown")
	elif message.text == 'Английский язык':
		bot.send_message(message.chat.id, "- Английский язык — важнейший международный язык, что является следствием колониальной политики Британской империи в XIX веке и мирового влияния Соединённых Штатов Америки в XX—XXI веках.\n- *В нашей школе курс английского языка для любого уровня стоит - 15.000 тенге*", parse_mode="Markdown")
	elif message.text == 'Химия':
		bot.send_message(message.chat.id, "- Химия - это одна из важнейших и обширных областей естествознания, наука, изучающая вещества, также их состав и строение, их свойства, зависящие от состава и строения, их превращения, ведущие к изменению состава — химические реакции, а также законы и закономерности, которым эти превращения подчиняются.\n- *В нашей школе курс химии для любого класса стоит - 15.000 тенге*", parse_mode="Markdown")
	elif message.text == 'Биология':
		bot.send_message(message.chat.id, "- Биоло́гия — наука о живых существах и их взаимодействии со средой обитания. Изучает все аспекты жизни, в частности: структуру, функционирование, рост, происхождение, эволюцию и распределение живых организмов на Земле.\n- *В нашей школе курс биологии для любого класса стоит - 15.000 тенге*", parse_mode="Markdown")
	elif message.text == 'Программирование':
		bot.send_message(message.chat.id, "- Программи́рование — процесс создания компьютерных программ. По выражению одного из основателей языков программирования Никлауса Вирта, «Программы = алгоритмы + структуры данных».\n- *В нашей школе курс программирования стоит - 15.000 тенге*", parse_mode="Markdown")
	elif message.text == 'ЕНТ':
		bot.send_message(message.chat.id, "- Результаты ЕНТ признаются вузами в качестве результатов вступительных экзаменов. Баллы ЕНТ также имеют значение при присуждении Президентской стипендии «Болашак». Впервые ЕНТ было введено в 2004 году.\n- *В нашей школе курс по подготовке к ЕНТ стоит - 45.000 тенге*", parse_mode="Markdown")
	elif message.text == 'IELTS':
		bot.send_message(message.chat.id, "- IELTS (International English Language Testing System) — это самый популярный международный тест на знание английского языка как иностранного, входящий в так называемые «кембриджские» экзамены.\n- *В нашей школе курс по подготовке к IELTS стоит - 40.000 тенге*", parse_mode="Markdown")
	elif message.text == 'НИШ, БИЛ, РФМШ':
		bot.send_message(message.chat.id, "- *В нашей школе курс по подготовки к НИШ, БИЛ, РФМШ стоит - 40.000 тенге*", parse_mode="Markdown")
	if message.text == 'Позвонить':
		bot.send_message(message.chat.id, '*+77058037757*', parse_mode="Markdown")
	elif message.text == 'Написать':
		bot.send_message(message.chat.id, '*https://wa.link/bjrgou*', parse_mode="Markdown")
	elif message.text == 'Адрес':
		bot.send_message(message.chat.id, 'БЦ TAYMAS , 3 этаж, 303 кабинет\nВремя работы:\n*ПН - 9:00 - 22:00\nВТ - 9:00 - 22:00\nСР - 9:00 - 22:00\nЧТ - 9:00 - 22:00\nПТ - 9:00 - 22:00\nСБ - 11:00 - 19:00\nВС - 12:00 - 15:00*', parse_mode="Markdown")
	if message.text == 'Оставить отзыв!':
		bot.send_message(message.chat.id, 'https://forms.gle/LSqscZwZxJuHkeGu8')






bot.polling(none_stop=True, interval=0)