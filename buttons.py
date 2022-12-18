from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup,ReplyKeyboardMarkup,KeyboardButton
import sqlite3

class Sql:
	def __init__(self):
		self.connection = sqlite3.connect('trbot.db')
		self.cursor = self.connection.cursor()

	def baza(self):
		self.cursor.execute("""CREATE TABLE IF NOT EXISTS user(
			id integer,
			username varchar(60),
			first_name varchar(60)
			)""")

	def user_add(self,idi,username,first_name):
		self.cursor.execute("INSERT INTO user (id,username,first_name) VALUES (?,?,?)",(idi,username,first_name))
		return self.connection.commit()

	def id_user(self,idi):
		self.cursor.execute(f"SELECT id FROM user WHERE id = {idi}")
		data = self.cursor.fetchone()
		return data

	def userlar(self):
		self.cursor.execute(f"SELECT COUNT(id) FROM user")
		info = self.cursor.fetchall()
		r = None
		for i in info:
			r = i[0]
		return r
	def rec(self):
		self.cursor.execute(f"SELECT * FROM user")
		idila = self.cursor.fetchall()		
		return idila

menu = ReplyKeyboardMarkup(
	keyboard = [
	[
	KeyboardButton(text="🛍 Buyurtma berish"),
	],
		[
		KeyboardButton(text="⚙️ Sozlamalar"),
		KeyboardButton(text="📞 Biz bilan aloqa")
		],	
	],
	resize_keyboard=True
)
""" Bosh menu """
menu1 = InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton(text="Lavash🌯",callback_data="lav"),
    InlineKeyboardButton(text="Hot Dog🌭",callback_data="hot")
	],
	[
	InlineKeyboardButton(text="Sandwich🥪",callback_data="sand"),
	InlineKeyboardButton(text="Shaurma🥙",callback_data="shaur")
	],
	[
	InlineKeyboardButton(text="Burger🍔",callback_data="bur"),
	InlineKeyboardButton(text="Tacos🌮",callback_data="taco")
	],
	[
	InlineKeyboardButton(text="Qo'shimchalar🍟",callback_data="qosh"),
	InlineKeyboardButton(text="Pizza🍕",callback_data="pizza")
	],
		[
		InlineKeyboardButton(text="Desertlar🍩",callback_data="des"),
		InlineKeyboardButton(text="Ichimliklar🥤",callback_data="suv")
		],	
	],
)
""" Lavash - 1 """
lavash = InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton(text="Mol Go'shtli🥩",callback_data="mollav"),
	InlineKeyboardButton(text="Tovuq Go'shtli🍗",callback_data="tovlav")
	],
	[
	InlineKeyboardButton(text="Mol+qalampir🥩🌶",callback_data="mollavq"),
	InlineKeyboardButton(text="Tovuq+qalampir🍗🌶",callback_data="tovlavq")
	],
	[InlineKeyboardButton(text="Mol+pishloq🥩🧀",callback_data="mollavp"),
	InlineKeyboardButton(text="Tovuq+pishloq🍗🧀",callback_data="tovlavp")
	],
	[
	InlineKeyboardButton(text='Fitter🥬',callback_data='fit')
	],
	[
    InlineKeyboardButton(text='◀️ Ortga',callback_data='back1')
	],
	]
)	
menu2 = InlineKeyboardMarkup(
	inline_keyboard = [
    [
    InlineKeyboardButton(text='mini',callback_data='lavmini'),
    InlineKeyboardButton(text='classic',callback_data='lavclas')
	],
	[
	InlineKeyboardButton(text="◀️ Ortga",callback_data="back2")
	],
	]
)
menu3 = InlineKeyboardMarkup(
	inline_keyboard = [
    [
    InlineKeyboardButton(text='mini',callback_data='lavtmini'),
    InlineKeyboardButton(text='classic',callback_data='lavtclas')
	],
	[
	InlineKeyboardButton(text="◀️ Ortga",callback_data="back2")
	],
	]
)
menu4 = InlineKeyboardMarkup(
	inline_keyboard = [
    [
    InlineKeyboardButton(text='mini',callback_data='lavqmini'),
    InlineKeyboardButton(text='classic',callback_data='lavqclas')
	],
    [
	InlineKeyboardButton(text="◀️ Ortga",callback_data="back2")
	],
	]
)
menu5 = InlineKeyboardMarkup(
	inline_keyboard = [
    [
    InlineKeyboardButton(text='mini',callback_data='lavtqmini'),
    InlineKeyboardButton(text='classic',callback_data='lavtqclas')
	],
    [
	InlineKeyboardButton(text="◀️ Ortga",callback_data="back2")
	],
	]
)
menu6 = InlineKeyboardMarkup(
	inline_keyboard = [
    [
    InlineKeyboardButton(text='mini',callback_data='lavpmini'),
    InlineKeyboardButton(text='classic',callback_data='lavpclas')
	],
    [
	InlineKeyboardButton(text="◀️ Ortga",callback_data="back2")
	],
	]
)
menu7 = InlineKeyboardMarkup(
	inline_keyboard = [
    [
    InlineKeyboardButton(text='mini',callback_data='lavtpmini'),
    InlineKeyboardButton(text='classic',callback_data='lavtpclas')
	],
    [
	InlineKeyboardButton(text="◀️ Ortga",callback_data="back2")
	],
	]
)
menu8 = InlineKeyboardMarkup(
	inline_keyboard = [
    [
    InlineKeyboardButton(text='1️⃣',callback_data='1'),
    InlineKeyboardButton(text='2️⃣',callback_data='2'),
    InlineKeyboardButton(text='3️⃣',callback_data='3')
	],
	[
	InlineKeyboardButton(text='4️⃣',callback_data='4'),
    InlineKeyboardButton(text='5️⃣',callback_data='5'),
    InlineKeyboardButton(text='6️⃣',callback_data='6')
	],
	[
	InlineKeyboardButton(text='7️⃣',callback_data='7'),
    InlineKeyboardButton(text='8️⃣',callback_data='8'),
    InlineKeyboardButton(text='9️⃣',callback_data='9')
	],
	[
	InlineKeyboardButton(text="◀️ Ortga",callback_data="back3")
	],
	]
)
menu50 = InlineKeyboardMarkup(
	inline_keyboard = [
    [
    InlineKeyboardButton(text='1️⃣',callback_data='1'),
    InlineKeyboardButton(text='2️⃣',callback_data='2'),
    InlineKeyboardButton(text='3️⃣',callback_data='3')
	],
	[
	InlineKeyboardButton(text='4️⃣',callback_data='4'),
    InlineKeyboardButton(text='5️⃣',callback_data='5'),
    InlineKeyboardButton(text='6️⃣',callback_data='6')
	],
	[
	InlineKeyboardButton(text='7️⃣',callback_data='7'),
    InlineKeyboardButton(text='8️⃣',callback_data='8'),
    InlineKeyboardButton(text='9️⃣',callback_data='9')
	],
	[
	InlineKeyboardButton(text="◀️ Ortga",callback_data="back4")
	],
	]
)
menu51 = InlineKeyboardMarkup(
	inline_keyboard = [
    [
    InlineKeyboardButton(text='1️⃣',callback_data='1'),
    InlineKeyboardButton(text='2️⃣',callback_data='2'),
    InlineKeyboardButton(text='3️⃣',callback_data='3')
	],
	[
	InlineKeyboardButton(text='4️⃣',callback_data='4'),
    InlineKeyboardButton(text='5️⃣',callback_data='5'),
    InlineKeyboardButton(text='6️⃣',callback_data='6')
	],
	[
	InlineKeyboardButton(text='7️⃣',callback_data='7'),
    InlineKeyboardButton(text='8️⃣',callback_data='8'),
    InlineKeyboardButton(text='9️⃣',callback_data='9')
	],
	[
	InlineKeyboardButton(text="◀️ Ortga",callback_data="back5")
	],
	]
)
menu52 = InlineKeyboardMarkup(
	inline_keyboard = [
    [
    InlineKeyboardButton(text='1️⃣',callback_data='1'),
    InlineKeyboardButton(text='2️⃣',callback_data='2'),
    InlineKeyboardButton(text='3️⃣',callback_data='3')
	],
	[
	InlineKeyboardButton(text='4️⃣',callback_data='4'),
    InlineKeyboardButton(text='5️⃣',callback_data='5'),
    InlineKeyboardButton(text='6️⃣',callback_data='6')
	],
	[
	InlineKeyboardButton(text='7️⃣',callback_data='7'),
    InlineKeyboardButton(text='8️⃣',callback_data='8'),
    InlineKeyboardButton(text='9️⃣',callback_data='9')
	],
	[
	InlineKeyboardButton(text="◀️ Ortga",callback_data="back6")
	],
	]
)
menu53 = InlineKeyboardMarkup(
	inline_keyboard = [
    [
    InlineKeyboardButton(text='1️⃣',callback_data='1'),
    InlineKeyboardButton(text='2️⃣',callback_data='2'),
    InlineKeyboardButton(text='3️⃣',callback_data='3')
	],
	[
	InlineKeyboardButton(text='4️⃣',callback_data='4'),
    InlineKeyboardButton(text='5️⃣',callback_data='5'),
    InlineKeyboardButton(text='6️⃣',callback_data='6')
	],
	[
	InlineKeyboardButton(text='7️⃣',callback_data='7'),
    InlineKeyboardButton(text='8️⃣',callback_data='8'),
    InlineKeyboardButton(text='9️⃣',callback_data='9')
	],
	[
	InlineKeyboardButton(text="◀️ Ortga",callback_data="back7")
	],
	]
)
menu54 = InlineKeyboardMarkup(
	inline_keyboard = [
    [
    InlineKeyboardButton(text='1️⃣',callback_data='1'),
    InlineKeyboardButton(text='2️⃣',callback_data='2'),
    InlineKeyboardButton(text='3️⃣',callback_data='3')
	],
	[
	InlineKeyboardButton(text='4️⃣',callback_data='4'),
    InlineKeyboardButton(text='5️⃣',callback_data='5'),
    InlineKeyboardButton(text='6️⃣',callback_data='6')
	],
	[
	InlineKeyboardButton(text='7️⃣',callback_data='7'),
    InlineKeyboardButton(text='8️⃣',callback_data='8'),
    InlineKeyboardButton(text='9️⃣',callback_data='9')
	],
	[
	InlineKeyboardButton(text="◀️ Ortga",callback_data="back8")
	],
	]
)

""" Hot DOG - 1 """
dog = InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton(text="Classic Hot Dog",callback_data="dogclas"),
	InlineKeyboardButton(text="Kanadskiy Hot Dog",callback_data="dogkan")
	],
	[
	InlineKeyboardButton(text="Tovuqli Hot Dog",callback_data="dogt"),
	InlineKeyboardButton(text="Karalevskiy Hot Dog",callback_data="dogkor")
	],
	[
	InlineKeyboardButton(text="◀️ Ortga",callback_data="back1")
	],	
	]
)
menu55 = InlineKeyboardMarkup(
	inline_keyboard = [
    [
    InlineKeyboardButton(text='1️⃣',callback_data='1'),
    InlineKeyboardButton(text='2️⃣',callback_data='2'),
    InlineKeyboardButton(text='3️⃣',callback_data='3')
	],
	[
	InlineKeyboardButton(text='4️⃣',callback_data='4'),
    InlineKeyboardButton(text='5️⃣',callback_data='5'),
    InlineKeyboardButton(text='6️⃣',callback_data='6')
	],
	[
	InlineKeyboardButton(text='7️⃣',callback_data='7'),
    InlineKeyboardButton(text='8️⃣',callback_data='8'),
    InlineKeyboardButton(text='9️⃣',callback_data='9')
	],
	[
	InlineKeyboardButton(text="◀️ Ortga",callback_data="back9")
	],
	]
)
""" Sandwich club - 1 """
sandwich = InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton(text="Classic Sandwich",callback_data="sand1"),
	InlineKeyboardButton(text="Tovuqli Sandwich",callback_data="sand2")
	],
	[
	InlineKeyboardButton(text="◀️ Ortga",callback_data="back1")
	],		
	]
)
menu56 = InlineKeyboardMarkup(
	inline_keyboard = [
    [
    InlineKeyboardButton(text='1️⃣',callback_data='1'),
    InlineKeyboardButton(text='2️⃣',callback_data='2'),
    InlineKeyboardButton(text='3️⃣',callback_data='3')
	],
	[
	InlineKeyboardButton(text='4️⃣',callback_data='4'),
    InlineKeyboardButton(text='5️⃣',callback_data='5'),
    InlineKeyboardButton(text='6️⃣',callback_data='6')
	],
	[
	InlineKeyboardButton(text='7️⃣',callback_data='7'),
    InlineKeyboardButton(text='8️⃣',callback_data='8'),
    InlineKeyboardButton(text='9️⃣',callback_data='9')
	],
	[
	InlineKeyboardButton(text="◀️ Ortga",callback_data="back10")
	],
	]
)	
"""  SHAURMA - 1 """
shaurma = InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton(text="Classic 🥙",callback_data="shaurm"),
	InlineKeyboardButton(text="Tovuqli 🥙",callback_data="shaurt")
	],
	[
	InlineKeyboardButton(text="Qalampirli 🥙+🌶",callback_data="shaurq"),
	InlineKeyboardButton(text="Tovuqli 🥙+🌶",callback_data="shaurtq")
	],
	[
	InlineKeyboardButton(text="◀️ Ortga",callback_data="back1")
	],	
	]
)	
menu9 = InlineKeyboardMarkup(
	inline_keyboard = [
    [
    InlineKeyboardButton(text='mini',callback_data='shaurmini'),
    InlineKeyboardButton(text='classic',callback_data='shaurclas')
	],
    [
    InlineKeyboardButton(text="◀️ Ortga",callback_data="back11")
    ],
	]
)
menu10 = InlineKeyboardMarkup(
	inline_keyboard = [
    [
    InlineKeyboardButton(text='mini',callback_data='shaurtmini'),
    InlineKeyboardButton(text='classic',callback_data='shaurtclas')
	],
    [
    InlineKeyboardButton(text="◀️ Ortga",callback_data="back11")
    ],
	]
)
menu11 = InlineKeyboardMarkup(
	inline_keyboard = [
    [
    InlineKeyboardButton(text='mini',callback_data='shaurqmini'),
    InlineKeyboardButton(text='classic',callback_data='shaurqclas')
	],
    [
    InlineKeyboardButton(text="◀️ Ortga",callback_data="back11")
    ],
	]
)
menu12 = InlineKeyboardMarkup(
	inline_keyboard = [
    [
    InlineKeyboardButton(text='mini',callback_data='shaurtqmini'),
    InlineKeyboardButton(text='classic',callback_data='shaurtqclas')
	],
    [
    InlineKeyboardButton(text="◀️ Ortga",callback_data="back11")
    ],
	]
)
menu57 = InlineKeyboardMarkup(
	inline_keyboard = [
    [
    InlineKeyboardButton(text='1️⃣',callback_data='1'),
    InlineKeyboardButton(text='2️⃣',callback_data='2'),
    InlineKeyboardButton(text='3️⃣',callback_data='3')
	],
	[
	InlineKeyboardButton(text='4️⃣',callback_data='4'),
    InlineKeyboardButton(text='5️⃣',callback_data='5'),
    InlineKeyboardButton(text='6️⃣',callback_data='6')
	],
	[
	InlineKeyboardButton(text='7️⃣',callback_data='7'),
    InlineKeyboardButton(text='8️⃣',callback_data='8'),
    InlineKeyboardButton(text='9️⃣',callback_data='9')
	],
	[
	InlineKeyboardButton(text="◀️ Ortga",callback_data="back12")
	],
	]
)
menu58 = InlineKeyboardMarkup(
	inline_keyboard = [
    [
    InlineKeyboardButton(text='1️⃣',callback_data='1'),
    InlineKeyboardButton(text='2️⃣',callback_data='2'),
    InlineKeyboardButton(text='3️⃣',callback_data='3')
	],
	[
	InlineKeyboardButton(text='4️⃣',callback_data='4'),
    InlineKeyboardButton(text='5️⃣',callback_data='5'),
    InlineKeyboardButton(text='6️⃣',callback_data='6')
	],
	[
	InlineKeyboardButton(text='7️⃣',callback_data='7'),
    InlineKeyboardButton(text='8️⃣',callback_data='8'),
    InlineKeyboardButton(text='9️⃣',callback_data='9')
	],
	[
	InlineKeyboardButton(text="◀️ Ortga",callback_data="back13")
	],
	]
)
menu59 = InlineKeyboardMarkup(
	inline_keyboard = [
    [
    InlineKeyboardButton(text='1️⃣',callback_data='1'),
    InlineKeyboardButton(text='2️⃣',callback_data='2'),
    InlineKeyboardButton(text='3️⃣',callback_data='3')
	],
	[
	InlineKeyboardButton(text='4️⃣',callback_data='4'),
    InlineKeyboardButton(text='5️⃣',callback_data='5'),
    InlineKeyboardButton(text='6️⃣',callback_data='6')
	],
	[
	InlineKeyboardButton(text='7️⃣',callback_data='7'),
    InlineKeyboardButton(text='8️⃣',callback_data='8'),
    InlineKeyboardButton(text='9️⃣',callback_data='9')
	],
	[
	InlineKeyboardButton(text="◀️ Ortga",callback_data="back14")
	],
	]
)
menu60 = InlineKeyboardMarkup(
	inline_keyboard = [
    [
    InlineKeyboardButton(text='1️⃣',callback_data='1'),
    InlineKeyboardButton(text='2️⃣',callback_data='2'),
    InlineKeyboardButton(text='3️⃣',callback_data='3')
	],
	[
	InlineKeyboardButton(text='4️⃣',callback_data='4'),
    InlineKeyboardButton(text='5️⃣',callback_data='5'),
    InlineKeyboardButton(text='6️⃣',callback_data='6')
	],
	[
	InlineKeyboardButton(text='7️⃣',callback_data='7'),
    InlineKeyboardButton(text='8️⃣',callback_data='8'),
    InlineKeyboardButton(text='9️⃣',callback_data='9')
	],
	[
	InlineKeyboardButton(text="◀️ Ortga",callback_data="back15")
	],
	]
)
"""    BURGER  - 1   """
burger = InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton(text="Gamburger",callback_data="gamb"),
	InlineKeyboardButton(text="Chizburger",callback_data="cheese")
	],
	[
	InlineKeyboardButton(text="◀️ Ortga",callback_data="back1")
	],		
	]
)
menu61 = InlineKeyboardMarkup(
	inline_keyboard = [
    [
    InlineKeyboardButton(text='1️⃣',callback_data='1'),
    InlineKeyboardButton(text='2️⃣',callback_data='2'),
    InlineKeyboardButton(text='3️⃣',callback_data='3')
	],
	[
	InlineKeyboardButton(text='4️⃣',callback_data='4'),
    InlineKeyboardButton(text='5️⃣',callback_data='5'),
    InlineKeyboardButton(text='6️⃣',callback_data='6')
	],
	[
	InlineKeyboardButton(text='7️⃣',callback_data='7'),
    InlineKeyboardButton(text='8️⃣',callback_data='8'),
    InlineKeyboardButton(text='9️⃣',callback_data='9')
	],
	[
	InlineKeyboardButton(text="◀️ Ortga",callback_data="back16")
	],
	]
)	
"""   DONAR - 1    """
tacos = InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton(text="Go'shtli taco",callback_data="tacs"),
	InlineKeyboardButton(text="Go'shtli taco + 🌶",callback_data="tacsq")
	],
	[
	InlineKeyboardButton(text="◀️ Ortga",callback_data="back1")
	],		
	]
)
menu62 = InlineKeyboardMarkup(
	inline_keyboard = [
    [
    InlineKeyboardButton(text='1️⃣',callback_data='1'),
    InlineKeyboardButton(text='2️⃣',callback_data='2'),
    InlineKeyboardButton(text='3️⃣',callback_data='3')
	],
	[
	InlineKeyboardButton(text='4️⃣',callback_data='4'),
    InlineKeyboardButton(text='5️⃣',callback_data='5'),
    InlineKeyboardButton(text='6️⃣',callback_data='6')
	],
	[
	InlineKeyboardButton(text='7️⃣',callback_data='7'),
    InlineKeyboardButton(text='8️⃣',callback_data='8'),
    InlineKeyboardButton(text='9️⃣',callback_data='9')
	],
	[
	InlineKeyboardButton(text="◀️ Ortga",callback_data="back17")
	],
	]
)
"""  Qo'shimchalar - 1  """
qoshimcha = InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton(text="Kartoshka fri🍟",callback_data="fri"),
	InlineKeyboardButton(text="Fri po Derevenskiy",callback_data="frider")
	],
	[
	InlineKeyboardButton(text="Guruch (250mg)",callback_data="gk"),
	InlineKeyboardButton(text="Guruch (500mg)",callback_data="gkk")
	],
	[
	InlineKeyboardButton(text="◀️ Ortga",callback_data="back1")
	],	
	]
)
menu99 = InlineKeyboardMarkup(
	inline_keyboard = [
    [
    InlineKeyboardButton(text='1️⃣',callback_data='1'),
    InlineKeyboardButton(text='2️⃣',callback_data='2'),
    InlineKeyboardButton(text='3️⃣',callback_data='3')
	],
	[
	InlineKeyboardButton(text='4️⃣',callback_data='4'),
    InlineKeyboardButton(text='5️⃣',callback_data='5'),
    InlineKeyboardButton(text='6️⃣',callback_data='6')
	],
	[
	InlineKeyboardButton(text='7️⃣',callback_data='7'),
    InlineKeyboardButton(text='8️⃣',callback_data='8'),
    InlineKeyboardButton(text='9️⃣',callback_data='9')
	],
	[
	InlineKeyboardButton(text="◀️ Ortga",callback_data="back18")
	],
	]
)
"""  ICHIMLIKLAR - 1   """
ichish = InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton(text="Choy va Kofe☕️",callback_data="cof"),
	InlineKeyboardButton(text="Sovuq Ichimliklar🥤",callback_data="freeze")
	],
	[
	InlineKeyboardButton(text="Tabiiy soklar🧃",callback_data="soklar")
	],
	[
	InlineKeyboardButton(text="◀️ Ortga",callback_data="back1")
	],	
	]
)
menu13 = InlineKeyboardMarkup(
	inline_keyboard = [
    [
    InlineKeyboardButton(text='Choylar🫖',callback_data='choylar'),
    InlineKeyboardButton(text='Coffee☕️',callback_data='coffee')
	],
    [
    InlineKeyboardButton(text="◀️ Ortga",callback_data="back19")
    ],
	]
)
menu14 = InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton(text="Fanta 0.5",callback_data="fanta"),
	InlineKeyboardButton(text="Sprite 0.5",callback_data="sprite")
	],
	[
	InlineKeyboardButton(text="Coca Cola 0.5",callback_data="cola"),
	InlineKeyboardButton(text="Ays 0.5",callback_data="ice")
	],
	[
    InlineKeyboardButton(text="◀️ Ortga",callback_data="back19")
    ],	
	]
)
menu15 = InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton(text="Bliss 1L",callback_data="bliss"),
	InlineKeyboardButton(text="Olma va sabzi soki",callback_data="olma")
	],
	[
    InlineKeyboardButton(text="◀️ Ortga",callback_data="back19")
    ],		
	]
)
menu16 = InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton(text="Qora choy",callback_data="qora"),
	InlineKeyboardButton(text="Ko'k choy",callback_data="ko'k")
	],
	[
	InlineKeyboardButton(text="Limon choy🍋",callback_data="lemon")
	],
	[
    InlineKeyboardButton(text="◀️ Ortga",callback_data="back20")
    ],	
	]
)
menu17 = InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton(text="Amerikano☕️",callback_data="amer"),
	InlineKeyboardButton(text="Cappuccino🧋",callback_data="cap")
	],
	[
	InlineKeyboardButton(text="coffee 3 in 1☕️",callback_data="coffee3"),
	InlineKeyboardButton(text="Latte🧋",callback_data="lat")
	],
	[
    InlineKeyboardButton(text="◀️ Ortga",callback_data="back20")
    ],	
	]
)
menu18 = InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton(text="Cappuccino small",callback_data="capk"),
	InlineKeyboardButton(text="Cappuccino katta",callback_data="capkk")
	],
	[
    InlineKeyboardButton(text="◀️ Ortga",callback_data="back21")
    ],		
	]
)
menu19 = InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton(text="Latte small",callback_data="latk"),
	InlineKeyboardButton(text="Latte katta",callback_data="latkk")
	],
	[
    InlineKeyboardButton(text="◀️ Ortga",callback_data="back21")
    ],		
	]
)
menu63 = InlineKeyboardMarkup(
	inline_keyboard = [
    [
    InlineKeyboardButton(text='1️⃣',callback_data='1'),
    InlineKeyboardButton(text='2️⃣',callback_data='2'),
    InlineKeyboardButton(text='3️⃣',callback_data='3')
	],
	[
	InlineKeyboardButton(text='4️⃣',callback_data='4'),
    InlineKeyboardButton(text='5️⃣',callback_data='5'),
    InlineKeyboardButton(text='6️⃣',callback_data='6')
	],
	[
	InlineKeyboardButton(text='7️⃣',callback_data='7'),
    InlineKeyboardButton(text='8️⃣',callback_data='8'),
    InlineKeyboardButton(text='9️⃣',callback_data='9')
	],
	[
	InlineKeyboardButton(text="◀️ Ortga",callback_data="back21")
	],
	]
)
menu64 = InlineKeyboardMarkup(
	inline_keyboard = [
    [
    InlineKeyboardButton(text='1️⃣',callback_data='1'),
    InlineKeyboardButton(text='2️⃣',callback_data='2'),
    InlineKeyboardButton(text='3️⃣',callback_data='3')
	],
	[
	InlineKeyboardButton(text='4️⃣',callback_data='4'),
    InlineKeyboardButton(text='5️⃣',callback_data='5'),
    InlineKeyboardButton(text='6️⃣',callback_data='6')
	],
	[
	InlineKeyboardButton(text='7️⃣',callback_data='7'),
    InlineKeyboardButton(text='8️⃣',callback_data='8'),
    InlineKeyboardButton(text='9️⃣',callback_data='9')
	],
	[
	InlineKeyboardButton(text="◀️ Ortga",callback_data="back22")
	],
	]
)
menu65 = InlineKeyboardMarkup(
	inline_keyboard = [
    [
    InlineKeyboardButton(text='1️⃣',callback_data='1'),
    InlineKeyboardButton(text='2️⃣',callback_data='2'),
    InlineKeyboardButton(text='3️⃣',callback_data='3')
	],
	[
	InlineKeyboardButton(text='4️⃣',callback_data='4'),
    InlineKeyboardButton(text='5️⃣',callback_data='5'),
    InlineKeyboardButton(text='6️⃣',callback_data='6')
	],
	[
	InlineKeyboardButton(text='7️⃣',callback_data='7'),
    InlineKeyboardButton(text='8️⃣',callback_data='8'),
    InlineKeyboardButton(text='9️⃣',callback_data='9')
	],
	[
	InlineKeyboardButton(text="◀️ Ortga",callback_data="back23")
	],
	]
)
menu66 = InlineKeyboardMarkup(
	inline_keyboard = [
    [
    InlineKeyboardButton(text='1️⃣',callback_data='1'),
    InlineKeyboardButton(text='2️⃣',callback_data='2'),
    InlineKeyboardButton(text='3️⃣',callback_data='3')
	],
	[
	InlineKeyboardButton(text='4️⃣',callback_data='4'),
    InlineKeyboardButton(text='5️⃣',callback_data='5'),
    InlineKeyboardButton(text='6️⃣',callback_data='6')
	],
	[
	InlineKeyboardButton(text='7️⃣',callback_data='7'),
    InlineKeyboardButton(text='8️⃣',callback_data='8'),
    InlineKeyboardButton(text='9️⃣',callback_data='9')
	],
	[
	InlineKeyboardButton(text="◀️ Ortga",callback_data="back24")
	],
	]
)
menu67 = InlineKeyboardMarkup(
	inline_keyboard = [
    [
    InlineKeyboardButton(text='1️⃣',callback_data='1'),
    InlineKeyboardButton(text='2️⃣',callback_data='2'),
    InlineKeyboardButton(text='3️⃣',callback_data='3')
	],
	[
	InlineKeyboardButton(text='4️⃣',callback_data='4'),
    InlineKeyboardButton(text='5️⃣',callback_data='5'),
    InlineKeyboardButton(text='6️⃣',callback_data='6')
	],
	[
	InlineKeyboardButton(text='7️⃣',callback_data='7'),
    InlineKeyboardButton(text='8️⃣',callback_data='8'),
    InlineKeyboardButton(text='9️⃣',callback_data='9')
	],
	[
	InlineKeyboardButton(text="◀️ Ortga",callback_data="back25")
	],
	]
)
menu68 = InlineKeyboardMarkup(
	inline_keyboard = [
    [
    InlineKeyboardButton(text='1️⃣',callback_data='1'),
    InlineKeyboardButton(text='2️⃣',callback_data='2'),
    InlineKeyboardButton(text='3️⃣',callback_data='3')
	],
	[
	InlineKeyboardButton(text='4️⃣',callback_data='4'),
    InlineKeyboardButton(text='5️⃣',callback_data='5'),
    InlineKeyboardButton(text='6️⃣',callback_data='6')
	],
	[
	InlineKeyboardButton(text='7️⃣',callback_data='7'),
    InlineKeyboardButton(text='8️⃣',callback_data='8'),
    InlineKeyboardButton(text='9️⃣',callback_data='9')
	],
	[
	InlineKeyboardButton(text="◀️ Ortga",callback_data="back26")
	],
	]
)
"""   DESSERTLAR - 1    """
dessert = InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton(text="Assalim",callback_data="assal"),
	InlineKeyboardButton(text="Choco",callback_data="choco")
	],
	[
	InlineKeyboardButton(text="Qulupnay",callback_data="qul")
	],
	[
	InlineKeyboardButton(text="◀️ Ortga",callback_data="back1")
	],
	]
)
menu69 = InlineKeyboardMarkup(
	inline_keyboard = [
    [
    InlineKeyboardButton(text='1️⃣',callback_data='1'),
    InlineKeyboardButton(text='2️⃣',callback_data='2'),
    InlineKeyboardButton(text='3️⃣',callback_data='3')
	],
	[
	InlineKeyboardButton(text='4️⃣',callback_data='4'),
    InlineKeyboardButton(text='5️⃣',callback_data='5'),
    InlineKeyboardButton(text='6️⃣',callback_data='6')
	],
	[
	InlineKeyboardButton(text='7️⃣',callback_data='7'),
    InlineKeyboardButton(text='8️⃣',callback_data='8'),
    InlineKeyboardButton(text='9️⃣',callback_data='9')
	],
	[
	InlineKeyboardButton(text="◀️ Ortga",callback_data="back27")
	],
	]
)
"""   PIZZA - 1  """
pizzala = InlineKeyboardMarkup(
	inline_keyboard = [
	[
	InlineKeyboardButton(text="Pepperoni",callback_data="pep"),
	InlineKeyboardButton(text="Margarita",callback_data="marg")
	],
	[
	InlineKeyboardButton(text="Ananasli",callback_data="ananas")
	],
	[
	InlineKeyboardButton(text="◀️ Ortga",callback_data="back1")
	],
	]
)
menu70 = InlineKeyboardMarkup(
	inline_keyboard = [
    [
    InlineKeyboardButton(text='1️⃣',callback_data='1'),
    InlineKeyboardButton(text='2️⃣',callback_data='2'),
    InlineKeyboardButton(text='3️⃣',callback_data='3')
	],
	[
	InlineKeyboardButton(text='4️⃣',callback_data='4'),
    InlineKeyboardButton(text='5️⃣',callback_data='5'),
    InlineKeyboardButton(text='6️⃣',callback_data='6')
	],
	[
	InlineKeyboardButton(text='7️⃣',callback_data='7'),
    InlineKeyboardButton(text='8️⃣',callback_data='8'),
    InlineKeyboardButton(text='9️⃣',callback_data='9')
	],
	[
	InlineKeyboardButton(text="◀️ Ortga",callback_data="back28")
	],
	]
)



# menu4 = InlineKeyboardMarkup(
# 	inline_keyboard = [
# 		[
# 		InlineKeyboardButton(text="Xa",callback_data="x"),
# 		InlineKeyboardButton(text="Yoq",callback_data="y")
# 		],	
# 	],
# )
# menu5 = InlineKeyboardMarkup(
# 	inline_keyboard = [
# 		[
# 		InlineKeyboardButton(text="Да",callback_data="r"),
# 		InlineKeyboardButton(text="Нет",callback_data="w")
# 		],	
# 	],
# )
