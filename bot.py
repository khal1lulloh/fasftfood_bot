import logging
from config import API_TOKEN1
from buttons import *
from aiogram.types import CallbackQuery
from aiogram import Bot, Dispatcher, executor, types


# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN1)
w = Sql()
dp = Dispatcher(bot)
Admin = * 


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    w.baza()
    user_id = message.from_user.id
    username = message.from_user.username
    first_name = message.from_user.first_name
    data1 = w.id_user(user_id)
    if data1 is None:
        w.user_add(user_id,username,first_name)
        await message.reply(f"Assalomu aleykum, {message.from_user.first_name}")
        await message.answer(f"Ovqat botiga xush kelibsiz☺️",reply_markup=menu)
        await bot.send_message(Admin,f"✅ Ro'yhatga qo'shildi: \nusername: @{message.from_user.username}\nid: {message.from_user.id}\nIsmi: {message.from_user.first_name}")
    else:
        await message.answer(f"Ovqat botiga xush kelibsiz☺️",reply_markup=menu)

@dp.message_handler(text="🛍 Buyurtma berish")
async def send_welcome(message: types.Message):
    await message.reply(f"Bu menu📗\nMarxamat:",reply_markup=menu1)

""" Hammasi lavashshi ichi """

@dp.callback_query_handler(text="lav")
async def menu_choose(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/lav.jpg','rb'),
        caption="Hozirda bizda:",reply_markup=lavash)

@dp.callback_query_handler(text='back1')
async def menu_choose(call:CallbackQuery):
    await call.message.answer(f"Bu menu\nMarxamat:",reply_markup=menu1)

@dp.callback_query_handler(text="mollav")
async def menu_choose(call:CallbackQuery):
    await call.message.answer("Kategoriyani tanlang",reply_markup=menu2)
    await call.message.delete()

@dp.callback_query_handler(text="tovlav")
async def menu_choose(call:CallbackQuery):
    await call.message.answer("Kategoriyani tanlang",reply_markup=menu3)
    await call.message.delete()

@dp.callback_query_handler(text="mollavq")
async def menu_choose(call:CallbackQuery):
    await call.message.answer("Kategoriyani tanlang",reply_markup=menu4)
    await call.message.delete()

@dp.callback_query_handler(text="tovlavq")
async def menu_choose(call:CallbackQuery):
    await call.message.answer("Kategoriyani tanlang",reply_markup=menu5)
    await call.message.delete()

@dp.callback_query_handler(text="mollavp")
async def menu_choose(call:CallbackQuery):
    await call.message.answer("Kategoriyani tanlang",reply_markup=menu6)
    await call.message.delete()

@dp.callback_query_handler(text="tovlavp")
async def menu_choose(call:CallbackQuery):
    await call.message.answer("Kategoriyani tanlang",reply_markup=menu7)
    await call.message.delete()

@dp.callback_query_handler(text="back2")
async def menu_choose(call:CallbackQuery):
    await call.message.answer("Hozirda bizda:",reply_markup=lavash)

"""  Kategoriyadan keyin  """

@dp.callback_query_handler(text="lavmini")
async def menu_choose(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/lavashmol.jpg','rb'),
        caption="""Narxi:   18 000 so'm
Tarkibi: Xamir, go`sht, chips, pomidor, bodring, sous, mayonez
Miqdorini kiriting:""",reply_markup=menu8)
    await call.message.delete()

@dp.callback_query_handler(text="lavclas")
async def menu_choose(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/lavashmol.jpg','rb'),
        caption="""Narxi:  22  000 so'm
Tarkibi: Xamir, go`sht, chips, pomidor, bodring, sous, mayonez
Miqdorini kiriting:""",reply_markup=menu8)
    await call.message.delete()

@dp.callback_query_handler(text="lavtmini")
async def menu_choose(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/lavashtovuq.jpg','rb'),
        caption="""Narxi:  20  000 so'm
Tarkibi: Xamir, tovuq go`shti, chips, pomidor, bodring, sous, mayonez
Miqdorini kiriting:""",reply_markup=menu50)
    await call.message.delete()

@dp.callback_query_handler(text="lavtclas")
async def menu_choose(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/lavashtovuq.jpg','rb'),
        caption="""Narxi:  22  000 so'm
Tarkibi: Xamir, tovuq go`shti, chips, pomidor, bodring, sous, mayonez
Miqdorini kiriting:""",reply_markup=menu50)
    await call.message.delete()

@dp.callback_query_handler(text="lavqmini")
async def menu_choose(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/lavashmolq.jpg','rb'),
        caption="""Narxi:  21  000 so'm
Tarkibi: Xamir, go`sht, garimdori, chips, pomidor, bodring, sous, mayonez
Miqdorini kiriting:""",reply_markup=menu51)
    await call.message.delete()

@dp.callback_query_handler(text="lavqclas")
async def menu_choose(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/lavashmolq.jpg','rb'),
        caption="""Narxi:  23  000 so'm
Tarkibi: Xamir, go`sht, garimdori, chips, pomidor, bodring, sous, mayonez
Miqdorini kiriting:""",reply_markup=menu51)
    await call.message.delete()

@dp.callback_query_handler(text="lavtqmini")
async def menu_choose(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/lavashtovuqq.jpg','rb'),
        caption="""Narxi:   21 000 so'm
Tarkibi: Xamir, tovuq go`shti, garimdori, chips, pomidor, bodring, sous, mayonez
Miqdorini tanlang:""",reply_markup=menu52)
    await call.message.delete()

@dp.callback_query_handler(text="lavtqclas")
async def menu_choose(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/lavashtovuqq.jpg','rb'),
        caption="""Narxi:   23 000 so'm
Tarkibi: Xamir, tovuq go`shti, garimdori, chips, pomidor, bodring, sous, mayonez
Miqdorini tanlang:""",reply_markup=menu52)
    await call.message.delete()

@dp.callback_query_handler(text="lavpmini")
async def menu_choose(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/lavashmolp.jpg','rb'),
        caption="""Narxi:   22 000 so'm
Tarkibi: Xamir, go`sht, pishloq, chips, pomidor, bodring, sous, mayonez
Miqdorini tanlang:""",reply_markup=menu53)
    await call.message.delete()

@dp.callback_query_handler(text="lavpclas")
async def menu_choose(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/lavashmolp.jpg','rb'),
        caption="""Narxi:   24 000 so'm
Tarkibi: Xamir, go`sht, pishloq, chips, pomidor, bodring, sous, mayonez
Miqdorini tanlang:""",reply_markup=menu53)
    await call.message.delete()

@dp.callback_query_handler(text="lavtpmini")
async def menu_choose(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/lavashtovuqp.jpg','rb'),
        caption="""Narxi:   22 000 so'm
Tarkibi: Xamir, tovuq go`shti, chips, pishloq, pomidor, bodring, sous, mayonez
Miqdorini tanlang:""",reply_markup=menu54)
    await call.message.delete()

@dp.callback_query_handler(text="lavtpclas")
async def menu_choose(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/lavashtovuqp.jpg','rb'),
        caption="""Narxi:   24 000 so'm
Tarkibi: Xamir, tovuq go`shti, chips, pishloq, pomidor, bodring, sous, mayonez
Miqdorini tanlang:""",reply_markup=menu54)
    await call.message.delete()

@dp.callback_query_handler(text="fit")
async def menu_choose(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/fitter.jpg','rb'),
        caption="""Narxi:   21 000 so'm
Tarkibi: Tovuq goʼshti, qarsildoq muztogʼ salati, yangi bodring va pomidorlar, fetaksa va bizning maxsus qaylamiz - barchasi yashil lavashga oʼralgan
Miqdorini tanlang:""",reply_markup=menu8)
    await call.message.delete()

@dp.callback_query_handler(text="back3")
async def menu_choose(call:CallbackQuery):
    await call.message.answer("Kategoriyani tanlang",reply_markup=menu2)
    await call.message.delete()

@dp.callback_query_handler(text="back4")
async def menu_choose(call:CallbackQuery):
    await call.message.answer("Kategoriyani tanlang",reply_markup=menu3)
    await call.message.delete()

@dp.callback_query_handler(text="back5")
async def menu_choose(call:CallbackQuery):
    await call.message.answer("Kategoriyani tanlang",reply_markup=menu4)
    await call.message.delete()

@dp.callback_query_handler(text="back6")
async def menu_choose(call:CallbackQuery):
    await call.message.answer("Kategoriyani tanlang",reply_markup=menu5)
    await call.message.delete()

@dp.callback_query_handler(text="back7")
async def menu_choose(call:CallbackQuery):
    await call.message.answer("Kategoriyani tanlang",reply_markup=menu6)
    await call.message.delete()

@dp.callback_query_handler(text="back8")
async def menu_choose(call:CallbackQuery):
    await call.message.answer("Kategoriyani tanlang",reply_markup=menu7)
    await call.message.delete()

""" Xot doooooooooooog  """

@dp.callback_query_handler(text="hot")
async def menu_choose(call:CallbackQuery):
    await call.message.answer("Hozirda bizda:",reply_markup=dog)

@dp.callback_query_handler(text="dogclas")
async def menu_choose(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/hotdogclassic.jpg','rb'),
        caption="""Kulcha, sosiska, ketchup va xantal, qovurilgan piyoz. 
Narxi: 8 000 so'm.
Miqdorini tanlang:""",reply_markup=menu55)
    await call.message.delete()

@dp.callback_query_handler(text="dogkan")
async def menu_choose(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/canadskiy.jpg','rb'),
        caption="""Kulcha, kanadskiy sosiska, ketchup va xantal, qovurilgan piyoz. 
Narxi: 10 000 so'm.
Miqdorini tanlang:""",reply_markup=menu55)
    await call.message.delete()

@dp.callback_query_handler(text="dogt")
async def menu_choose(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/tovuqlihotdog.jpg','rb'),
        caption="""Kulcha, tovuq go'shti, ketchup va xantal, qovurilgan piyoz.
Narxi: 12 000 so'm.
Miqdorini tanlang:""",reply_markup=menu55)
    await call.message.delete()

@dp.callback_query_handler(text="dogkor")
async def menu_choose(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/corolevskiy.jpg','rb'),
        caption="""Kulcha, sosiska 2x, ketchup va xantal, qovurilgan piyoz. 
Narxi: 15 000 so'm.
Miqdorini tanlang:""",reply_markup=menu55)
    await call.message.delete()

@dp.callback_query_handler(text="back9")
async def menu_choose(call:CallbackQuery):
    await call.message.answer("Hozirda bizda:",reply_markup=dog)

"""  Sandwich club      """

@dp.callback_query_handler(text="sand")
async def menu_choose(call:CallbackQuery):
    await call.message.answer("Hozirda bizda:",reply_markup=sandwich)
    
@dp.callback_query_handler(text="sand1")
async def menu_choose(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/sandwicht.jpg','rb'),
        caption="""Kulcha, go'shti, pomidor, garimdori, sous,  piyoz. 
Narxi: 24 000 so'm.         
Miqdorini tanlang:""",reply_markup=menu56)
    await call.message.delete()

@dp.callback_query_handler(text="sand2")
async def menu_choose(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/sandwicht.jpg','rb'),
        caption="""Kulcha, tovuq go'shti, pomidor, sous,  piyoz. 
Narxi: 24 000 so'm.         
Miqdorini tanlang:""",reply_markup=menu56)
    await call.message.delete()

@dp.callback_query_handler(text="back10")
async def menu_choose(call:CallbackQuery):
    await call.message.answer("Hozirda bizda:",reply_markup=sandwich)

"""  SHAURMA   """

@dp.callback_query_handler(text="shaur")
async def menu_choose(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/shaur.jpg','rb'),
        caption="""Hozirda bizda:""",reply_markup=shaurma)

@dp.callback_query_handler(text="shaurm")
async def menu_choose(call:CallbackQuery):
    await call.message.answer("Kategoriyani tanlang:",reply_markup=menu9)
    await call.message.delete()
    
@dp.callback_query_handler(text="shaurt")
async def menu_choose(call:CallbackQuery):
    await call.message.answer("Kategoriyani tanlang:",reply_markup=menu10)
    await call.message.delete()

@dp.callback_query_handler(text="shaurq")
async def menu_choose(call:CallbackQuery):
    await call.message.answer("Kategoriyani tanlang:",reply_markup=menu11)
    await call.message.delete()

@dp.callback_query_handler(text="shaurtq")
async def menu_choose(call:CallbackQuery):
    await call.message.answer("Kategoriyani tanlang:",reply_markup=menu12)
    await call.message.delete()

@dp.callback_query_handler(text="shaurmini")
async def menu_choose(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/shaurma.jpg','rb'),
        caption="""Tarkibi: Yarimta non, piyoz, pomidor, mol go'shti, sous, mayonez.
Narxi: 18 000 so'm.
Miqdorini tanlang:""",reply_markup=menu57)
    await call.message.delete()

@dp.callback_query_handler(text="shaurclas")
async def menu_choose(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/shaurma.jpg','rb'),
        caption="""Tarkibi: Yarimta non, piyoz, pomidor, mol go'shti, sous, mayonez.
Narxi: 20 000 so'm.
Miqdorini tanlang:""",reply_markup=menu57)

@dp.callback_query_handler(text="shaurtmini")
async def menu_choose(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/shaurmat.jpg','rb'),
        caption="""Tarkibi: Yarimta non, piyoz, pomidor, tovuq go'shti, sous, mayonez.
Narxi: 18 000 so'm.
Miqdorini tanlang:""",reply_markup=menu58)
    await call.message.delete()

@dp.callback_query_handler(text="shaurtclas")
async def menu_choose(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/shaurmat.jpg','rb'),
        caption="""Tarkibi: Yarimta non, piyoz, pomidor, tovuq go'shti, sous, mayonez.
Narxi: 20 000 so'm.
Miqdorini tanlang:""",reply_markup=menu58)
    await call.message.delete()

@dp.callback_query_handler(text="shaurqmini")
async def menu_choose(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/shaurmaq.jpg','rb'),
        caption="""Tarkibi: Yarimta non, piyoz, pomidor, mol go'shti, sous, mayonez, qalampir.
Narxi: 19 000 so'm.
Miqdorini tanlang:""",reply_markup=menu59)
    await call.message.delete()

@dp.callback_query_handler(text="shaurqclas")
async def menu_choose(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/shaurmaq.jpg','rb'),
        caption="""Tarkibi: Yarimta non, piyoz, pomidor, mol go'shti, sous, mayonez, qalampir.
Narxi: 21 000 so'm.
Miqdorini tanlang:""",reply_markup=menu59)
    await call.message.delete()

@dp.callback_query_handler(text="shaurtqclas")
async def menu_choose(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/shaurmatq.jpg','rb'),
        caption="""Tarkibi: Yarimta non, piyoz, pomidor, tovuq go'shti, sous, mayonez.
Narxi: 21 000 so'm.
Miqdorini tanlang:""",reply_markup=menu60)
    await call.message.delete()

@dp.callback_query_handler(text="shaurtqmini")
async def menu_choose(call:CallbackQuery):
    await call.message.nswer_photo(
        photo=open('images/shaurmatq.jpg','rb'),
        caption="""Tarkibi: Yarimta non, piyoz, pomidor, tovuq go'shti, sous, mayonez.
Narxi: 19 000 so'm.
Miqdorini tanlang:""",reply_markup=menu60)
    await call.message.delete()

@dp.callback_query_handler(text="back11")
async def menu_choose(call:CallbackQuery):
    await call.message.answer("Hozirda bizda:",reply_markup=shaurma)

@dp.callback_query_handler(text="back12")
async def menu_choose(call:CallbackQuery):
    await call.message.answer("Kategoriyani tanlang:",reply_markup=menu9)
    await call.message.delete()

@dp.callback_query_handler(text="back13")
async def menu_choose(call:CallbackQuery):
    await call.message.answer("Kategoriyani tanlang:",reply_markup=menu10)
    await call.message.delete()

@dp.callback_query_handler(text="back14")
async def menu_choose(call:CallbackQuery):
    await call.message.answer("Kategoriyani tanlang:",reply_markup=menu11)
    await call.message.delete()

@dp.callback_query_handler(text="back15")
async def menu_choose(call:CallbackQuery):
    await call.message.answer("Kategoriyani tanlang:",reply_markup=menu12)
    await call.message.delete()

"""   BURGER    """

@dp.callback_query_handler(text="bur")
async def menu_choose(call:CallbackQuery):
    await call.message.answer("Hozirda bizda:",reply_markup=burger)

@dp.callback_query_handler(text="gamb")
async def menu_choose(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/gamburger.jpg','rb'),
        caption="""Tarkibi: Bulochka, pomidor, koklet, sous, mayonez.
Narxi: 17 000 so'm.
Miqdorini tanlang:""",reply_markup=menu61)
    await call.message.delete()

@dp.callback_query_handler(text="cheese")
async def menu_choose(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/cheeseburger.jpg','rb'),
        caption="""Tarkibi: Bulochka, pomidor, koklet, sous, mayonez.
Narxi: 19 000 so'm.
Miqdorini tanlang:""",reply_markup=menu61)
    await call.message.delete()

@dp.callback_query_handler(text="back16")
async def menu_choose(call:CallbackQuery):
    await call.message.answer("Hozirda bizda:",reply_markup=burger)

"""   DONAR - 1    """

@dp.callback_query_handler(text="taco")
async def menu_choose(call:CallbackQuery):
    await call.message.answer("Hozirda bizda:",reply_markup=tacos)

@dp.callback_query_handler(text="tacs")
async def menu_choose(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/tacos.jpg','rb'),
        caption="""Tarkibi: Bulochka, pomidor, mol go'shti, mayonez, salat.
Narxi: 20 000 so'm.
Miqdorini tanlang:""",reply_markup=menu62)
    await call.message.delete()

@dp.callback_query_handler(text="tacsq")
async def menu_choose(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/tacosq.jpg','rb'),
        caption="""Tarkibi: Bulochka, pomidor, mol go'shti, mayonez, salat, qalampir.
Narxi: 22 000 so'm.
Miqdorini tanlang:""",reply_markup=menu62)
    await call.message.delete()

@dp.callback_query_handler(text="back17")
async def menu_choose(call:CallbackQuery):
    await call.message.answer("Hozirda bizda:",reply_markup=tacos)

"""   QO'SHIMCHALAR    """

@dp.callback_query_handler(text="qosh")
async def menu_choose(call:CallbackQuery):
    await call.message.answer("Hozirda bizda:",reply_markup=qoshimcha)

@dp.callback_query_handler(text="fri")
async def menu_choose(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/fri.jpg','rb'),
        caption="""Kartoshka fri.
Narxi: 10 000 so'm.
Miqdorini tanlang:""",reply_markup=menu99)
    await call.message.delete()

@dp.callback_query_handler(text="frider")
async def menu_choose(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/derevenskiy.jpg','rb'),
        caption="""Kartoshka fri (po derevenskiy)
Narxi: 11 000 so'm.
Miqdorini tanlang:""",reply_markup=menu99)
    await call.message.delete()

@dp.callback_query_handler(text="gk")
async def menu_choose(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/guruch.jpg','rb'),
        caption="""Guruch (kichik)
Narxi: 8 000 so'm.
Miqdorini tanlang:""",reply_markup=menu99)
    await call.message.delete()

@dp.callback_query_handler(text="gkk")
async def menu_choose(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/guruch.jpg','rb'),
        caption="""Guruch (katta)
Narxi: 12 000 so'm.
Miqdorini tanlang:""",reply_markup=menu99)
    await call.message.delete()

@dp.callback_query_handler(text="back18")
async def menu_choose(call:CallbackQuery):
    await call.message.answer("Hozirda bizda:",reply_markup=qoshimcha)

"""  ICHIMLIKLAR    """

@dp.callback_query_handler(text="suv")
async def menu_choose(call:CallbackQuery):
    await call.message.answer("Hozirda bizda:",reply_markup=ichish)

@dp.callback_query_handler(text="cof")
async def menu_choose(call:CallbackQuery):
    await call.message.answer('Kategoriyadan bittasini tanlang:',reply_markup=menu13)
    await call.message.delete()

@dp.callback_query_handler(text="freeze")
async def menu_choose(call:CallbackQuery):
    await call.message.answer('Kategoriyadan bittasini tanlang:',reply_markup=menu14)
    await call.message.delete()

@dp.callback_query_handler(text="soklar")
async def menu_choose(call:CallbackQuery):
    await call.message.answer('Kategoriyadan bittasini tanlang:',reply_markup=menu15)
    await call.message.delete()

@dp.callback_query_handler(text="choylar")
async def menu_choose(call:CallbackQuery):
    await call.message.answer('Kategoriyadan bittasini tanlang:',reply_markup=menu16)
    await call.message.delete()

@dp.callback_query_handler(text="coffee")
async def menu_choose(call:CallbackQuery):
    await call.message.answer('Kategoriyadan bittasini tanlang:',reply_markup=menu17)
    await call.message.delete()

@dp.callback_query_handler(text="bliss")
async def menu_choose(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/bliss.jpg','rb'),
        caption="""Bliss 1L
Narxi 13 000 so'm.
Miqdorini tanlang:""",reply_markup=menu68)
    await call.message.delete()

@dp.callback_query_handler(text="olma")
async def menu_choose(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/sabzi.jpg','rb'),
        caption="""Sabzi + olma sharbati
Narxi 15 000 so'm.
Miqdorini tanlang:""",reply_markup=menu68)
    await call.message.delete()

@dp.callback_query_handler(text="back19")
async def menu_choose(call:CallbackQuery):
    await call.message.answer("Hozirda bizda:",reply_markup=ichish)

@dp.callback_query_handler(text="back20")
async def menu_choose(call:CallbackQuery):
    await call.message.answer('Kategoriyadan bittasini tanlang:',reply_markup=menu13)
    await call.message.delete()

@dp.callback_query_handler(text="back21")
async def menu_choose(call:CallbackQuery):
    await call.message.answer('Kategoriyadan bittasini tanlang:',reply_markup=menu17)
    await call.message.delete()

@dp.callback_query_handler(text="back22")
async def menu_choose(call:CallbackQuery):
    await call.message.answer('Kategoriyadan bittasini tanlang:',reply_markup=menu18)
    await call.message.delete()

@dp.callback_query_handler(text="back23")
async def menu_choose(call:CallbackQuery):
    await call.message.answer('Kategoriyadan bittasini tanlang:',reply_markup=menu19)
    await call.message.delete()

@dp.callback_query_handler(text="back24")
async def menu_choose(call:CallbackQuery):
    await call.message.answer('Kategoriyadan bittasini tanlang:',reply_markup=menu16)
    await call.message.delete()

@dp.callback_query_handler(text="back25")
async def menu_choose(call:CallbackQuery):
    await call.message.answer('Kategoriyadan bittasini tanlang:',reply_markup=menu14)
    await call.message.delete()

@dp.callback_query_handler(text="back26")
async def menu_choose(call:CallbackQuery):
    await call.message.answer('Kategoriyadan bittasini tanlang:',reply_markup=menu15)
    await call.message.delete()

"""  COFFEE """

@dp.callback_query_handler(text="amer")
async def menu_choose(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/amerikano.jpg','rb'),
        caption="""Amerikano☕️
Narxi 10 000 so'm.
Miqdorini tanlang:""",reply_markup=menu63)
    await call.message.delete()

@dp.callback_query_handler(text="coffee3")
async def menu_choose(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/3v1.jpg','rb'),
        caption="""Coffee 3 in 1☕️
Narxi 5 000 so'm.
Miqdorini tanlang:""",reply_markup=menu63)
    await call.message.delete()

@dp.callback_query_handler(text="cap")
async def menu_choose(call:CallbackQuery):
    await call.message.answer('Kategoriyadan bittasini tanlang:',reply_markup=menu18)
    await call.message.delete()

@dp.callback_query_handler(text="lat")
async def menu_choose(call:CallbackQuery):
    await call.message.answer('Kategoriyadan bittasini tanlang:',reply_markup=menu19)
    await call.message.delete()

@dp.callback_query_handler(text="capk")
async def menu_choose(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/cappuccino.jpg','rb'),
        caption="""Cappuccino small 80mg
Narxi: 8 000 so'm.
Miqdorini tanlang:""",reply_markup=menu64)
    await call.message.delete(
        )
@dp.callback_query_handler(text="capkk")
async def menu_choose(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/cappuccino.jpg','rb'),
        caption="""Cappuccino katta 120mg
Narxi: 12 000 so'm.
Miqdorini tanlang:""",reply_markup=menu64)
    await call.message.delete()

@dp.callback_query_handler(text="latk")
async def menu_choose(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/latte.jpg','rb'),
        caption="""Latte small 80mg
Narxi: 10 000 so'm.
Miqdorini tanlang:""",reply_markup=menu65)
    await call.message.delete()

@dp.callback_query_handler(text="latkk")
async def menu_choose(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/latte.jpg','rb'),
        caption="""Latte katta 120mg
Narxi: 14 000 so'm.
Miqdorini tanlang:""",reply_markup=menu65)
    await call.message.delete()

@dp.callback_query_handler(text="qora")
async def menu_choose(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/qorachoy.jpg','rb'),
        caption="""Qora choy
Narxi: 3 000 so'm.
Miqdorini tanlang:""",reply_markup=menu66)
    await call.message.delete()

@dp.callback_query_handler(text="ko'k")
async def menu_choose(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/qorachoy.jpg','rb'),
        caption="""Ko'k choy
Narxi: 3 000 so'm.
Miqdorini tanlang:""",reply_markup=menu66)
    await call.message.delete()

@dp.callback_query_handler(text="lemon")
async def menu_choose(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/limon.jpg','rb'),
        caption="""Limon choy
Narxi: 5 000 so'm.
Miqdorini tanlang:""",reply_markup=menu66)
    await call.message.delete()

@dp.callback_query_handler(text="fanta")
async def menu_choose(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/fanta.jpg','rb'),
        caption="""Fanta 500mg
Narxi: 6 000 so'm.
Miqdorini tanlang:""",reply_markup=menu67)
    await call.message.delete()

@dp.callback_query_handler(text="sprite")
async def menu_choose(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/sprite.jpg','rb'),
        caption="""Sprite 500mg
Narxi: 6 500 so'm.
Miqdorini tanlang:""",reply_markup=menu67)
    await call.message.delete()

@dp.callback_query_handler(text="cola")
async def menu_choose(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/coca-cola.jpg','rb'),
        caption="""Coca-Cola 500mg
Narxi: 6 000 so'm.
Miqdorini tanlang:""",reply_markup=menu67)
    await call.message.delete()

@dp.callback_query_handler(text="ice")
async def menu_choose(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/ays.jpg','rb'),
        caption="""Ays 500mg
Narxi: 2 000 so'm.
Miqdorini tanlang:""",reply_markup=menu67)
    await call.message.delete()

"""   DESSERTLAR   """

@dp.callback_query_handler(text="des")
async def menu_choose(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/dessert.jpg','rb'),
        caption="""Hozirda bizda:""",reply_markup=dessert)

@dp.callback_query_handler(text="assal")
async def menu_choose(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/assalim.jpg','rb'),
        caption="""An'anaviy ta'm - asal asosidagi biskvit
Narxi: 14 000 so'm.
Miqdorini tanlang:""",reply_markup=menu69)
    await call.message.delete()

@dp.callback_query_handler(text="choco")
async def menu_choose(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/choco.jpg','rb'),
        caption="""An'anaviy ta'm - shokolad asosidagi biskvit
Narxi: 14 000 so'm.
Miqdorini tanlang:""",reply_markup=menu69)
    await call.message.delete()

@dp.callback_query_handler(text="qul")
async def menu_choose(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/qulupnay.jpg','rb'),
        caption="""Qulupnayli Muss
Narxi: 14 000 so'm.
Miqdorini tanlang:""",reply_markup=menu69)
    await call.message.delete()

@dp.callback_query_handler(text="back27")
async def menu_choose(call:CallbackQuery):
    await call.message.answer("Hozirda bizda:",reply_markup=dessert)

"""  PIZZALAAAAAAR  """

@dp.callback_query_handler(text="pizza")
async def menu_choose(call:CallbackQuery):
    await call.message.answer("Hozirda bizda:",reply_markup=pizzala)

@dp.callback_query_handler(text="pep")
async def menu_choose(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/pepperoni.jpg','rb'),
        caption="""Pizza 'Pepperoni'
33 sm
Tomat sousi
Pishloq 100gr
Kolbasa
Narxi: 65 000 so'm.""",reply_markup=menu70)
    await call.message.delete()

@dp.callback_query_handler(text="marg")
async def menu_choose(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/margarita.jpg','rb'),
        caption="""Pizza 'Margarita'
33 sm
Tomat sousi
Pishloq 100gr
Pomidor
Narxi: 53 000 so'm.""",reply_markup=menu70)
    await call.message.delete()

@dp.callback_query_handler(text="ananas")
async def menu_choose(call:CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/ananas.jpg','rb'),
        caption="""Ananasli pizza
33 sm
Tomat sousi
Pishloq 100gr
3 hil kolbasa
Jo'xori
Qo'ziqorin
Ananas
Narxi: 70 000 so'm.""",reply_markup=menu70)
    await call.message.delete()

@dp.callback_query_handler(text="back28")
async def menu_choose(call:CallbackQuery):
    await call.message.answer("Hozirda bizda:",reply_markup=pizzala)



@dp.message_handler(text="📞 Biz bilan aloqa")
async def send_welcome(message: types.Message):
    await message.reply(f"Murojaat uchun telefon: +998998755975\nID:@khal1lulloh\nTaklif va shikoyatlar uchun👆👆👆")

@dp.message_handler(commands=['allusers'])
async def send_welcome(message: types.Message):
    p = w.userlar()
    await bot.send_message(Admin,f"Botimizda foydalanuvchilar soni {p} ta")

@dp.message_handler(commands=['ads'],user_id=692799479)
async def send_welcome(message: types.Message):
    q = w.rec()
    e = message.text[5::]
    for k in q:
        data2 = k[0]
        await bot.send_message(chat_id=data2,text=e)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)