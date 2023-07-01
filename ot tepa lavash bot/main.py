


import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

API_TOKEN = ''


logging.basicConfig(level=logging.INFO)


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)











bosh_menu = ReplyKeyboardMarkup(
      keyboard=[
          [
            KeyboardButton(text="harid kilish 🛒"),
            KeyboardButton(text="Oq tepa lavashqda✔")  
          ],
          [
              KeyboardButton(text="shirinliklar 🥞"),
              KeyboardButton(text="dostavka")
          ],
          [
              KeyboardButton(text="Ichimliklar 🍷"),
              KeyboardButton(text="Burgerlar🌭")
          ],

        #   [
        #       KeyboardButton(text="ortga")
        #   ]
         
      ],
      resize_keyboard=True

)
@dp.message_handler(commands=['start', 'menu'])
async def send_welcome(message: types.Message):

    await message.reply("Oq tepa lavash botiga hush kelibsiz", reply_markup=bosh_menu)

@dp.message_handler(text="orqaga")
async def echo(message: types.Message):
    await message.answer("Siz orqaga qayttiz", reply_markup=bosh_menu)


about = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="lokachiya📍"),
            KeyboardButton(text="contakt"),
            KeyboardButton(text="about us")

        ],
        [
            KeyboardButton(text="orqaga")
        ],
        
    ],
    resize_keyboard=True
)
@dp.message_handler(text="Oq tepa lavashqda✔")
async def send_welcome(message: types.Message):

    await message.reply("about", reply_markup=about)



@dp.message_handler(text="lokachiya📍")
async def send_welcome(message: types.Message):
      
    await message.answer_location(41.36582976886427, 69.28692548548665)


@dp.message_handler(text="contakt")
async def send_welcome(message: types.Message):
      
    await message.answer_contact(phone_number="+998 94 703 36 30", first_name="Sunnat")


@dp.message_handler(text="about us")
async def send_welcome(message: types.Message):
      
    await message.answer_contact(phone_number="+998 99 041 91 41", first_name="Nozima")





burger_menu = ReplyKeyboardMarkup(
    keyboard = [
        [
           KeyboardButton(text="tandir lavash🥪"),
           KeyboardButton(text=" lavash🥪"),
           KeyboardButton(text="tandir lavash s sirom🥪")
        ],
        [
           
           KeyboardButton(text=" lavash s garchitsoy🥪"),
           KeyboardButton(text="tandir lavash mini🥪"),
           KeyboardButton(text=" lavash  mini🥪")
        ],
        [
           KeyboardButton(text="chizburger🥪"),
           KeyboardButton(text=" clap🥪"),
           KeyboardButton(text="gamburger big")
        ],
        [
           
            KeyboardButton(text=" 5 ib 1 stack"), 
            KeyboardButton(text="orqaga ")
        ],
       
        [
            KeyboardButton(text="orqaga")
        ]
    ],
    resize_keyboard=True
)

@dp.message_handler(text="Burgerlar🌭")
async def send_welcome(message: types.Message):

    await message.reply("burgerlarni tanlang", reply_markup=burger_menu)











d_menu = ReplyKeyboardMarkup(
   keyboard= [
        [
          KeyboardButton(text="Tashkent🚩"),
          KeyboardButton(text="Tashkentski oblast🚩")
        ],
        [
          KeyboardButton(text="Buhara🚩"),
          KeyboardButton(text="Kashkadaryo🚩")
        ],
        [
          KeyboardButton(text="Samarkand🚩"),
          KeyboardButton(text="Fergana🚩"),
        ],
        [
            KeyboardButton(text="Jizax🚩"),
            KeyboardButton(text="Surhandarya🚩")
        ],
        [
            KeyboardButton(text="Termir🚩"),
            KeyboardButton(text="Navai🚩")
        ],
        [
            KeyboardButton(text="surhandarya🚩"),
            KeyboardButton(text="Andijan🚩")
        ],
        [
            KeyboardButton(text="orqaga")
        ]
    ],
    resize_keyboard=True
)
@dp.message_handler(text="dostavka")
async def echo(message: types.Message):
    await message.reply("manzilni tanlang", reply_markup=d_menu)








ichimliklar_menu = ReplyKeyboardMarkup(
   keyboard= [
        [
            KeyboardButton(text="pepsi🥤"),
            KeyboardButton(text="fanta🥃"),
            
        ],
        [
            KeyboardButton(text="cola🥤"),
            KeyboardButton(text="suv💧")
        ],
        [
            KeyboardButton(text="orqaga ")
        ]
    ],
    resize_keyboard=True
)
@dp.message_handler(text="Ichimliklar 🍷")
async def send_welcome(message: types.Message):
    await message.reply("burgerlarni tanlang", reply_markup=ichimliklar_menu)
    await message.answer_photo("https://trikky.ru/wp-content/blogs.dir/1/files/2023/03/22/1665870954-10-podacha-blud-com-p.jpg")
@dp.message_handler(text="fanta🥃")
async def send_welcome(message: types.Message):
    await message.answer_photo("http://shashlikcentr.ru/wp-content/uploads/2021/04/11766409_1920.jpg",
                               caption="""narhi- 7 000""")

@dp.message_handler(text="cola🥤")
async def send_welcome(message: types.Message):
    await message.answer_photo("https://mir-s3-cdn-cf.behance.net/project_modules/fs/7ebf1d11196997.587f3a1a2a06d.jpg",
                               caption="""narhi- 7 500""")

@dp.message_handler(text="suv💧")
async def send_welcome(message: types.Message):
    await message.answer_photo("https://kifa.by/upload/iblock/fc6/fc6948291b7e555a5073a0b84c5b130c.jpg",
                                caption="""narhi- 12 950""")

@dp.message_handler(text="pepsi🥤")
async def send_welcome(message: types.Message):
    await message.answer_photo("https://srokigodnosti.ru/wp-content/uploads/2022/07/Pepsi-cola-ice-cubes-drinks_2880x1800-2048x1280.jpg",
                               caption="""narhi 7 950""")









shirinliklar_menu = ReplyKeyboardMarkup(
    keyboard= [
        [
            KeyboardButton(text="cake🎂"),
            KeyboardButton(text="pahlava🍩")
        ],
        [
            KeyboardButton(text="napalyon🍪"),
            KeyboardButton(text="midovi🍰")
        ],
        [
            KeyboardButton(text="orqaga")
        ]
               ],
resize_keyboard=True

)
@dp.message_handler(text="midovi🍰")
async def send_welcome(message: types.Message):

    await message.answer_photo("https://lookw.ru/1/186/1380317275-tortiki-ch2--65.jpg",
                               caption="""narhi 45 000""")


@dp.message_handler(text="shirinliklar 🥞")
async def send_welcome(message: types.Message):

    await message.reply("konglingiz tusagan shirinlikni tanlang", reply_markup=shirinliklar_menu)


@dp.message_handler(text="cake🎂")
async def send_welcome(message: types.Message):

    await message.answer_photo("https://i.pinimg.com/originals/56/78/a9/5678a9dafcd29d915487929ef95795ed.jpg",
                               caption="""narhi- 56 000""")


@dp.message_handler(text="pahlava🍩")
async def send_welcome(message: types.Message):
    await message.answer_photo("https://mykaleidoscope.ru/uploads/posts/2021-09/1632388117_14-mykaleidoscope-ru-p-turetskie-sladosti-pakhlava-krasivo-foto-16.jpg",
                               caption="""narhi- 30 000""")


@dp.message_handler(text="napalyon🍪")
async def send_welcome(message: types.Message):
    await message.answer_photo("http://static.tildacdn.com/tild6265-6463-4835-a332-653031373265/valentines-cakes-gro.jpg",
                               caption="""narxi- 29 000""")
    # await message.answer_location(41.365606771426336, 69.28818608644262)
    # await message.answer_contact(phone_number="+998947033630", first_name="Sunnat")












@dp.message_handler()
async def echo(message: types.Message):
    await message.answer("ertyu")

    # await message.answer(message.text)




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)













@dp.message_handler(text="vidionote")
async def send_welcome(message: types.Message):
      
    await message.answer_video_note("https://telesco.pe/tannus8002/2")



@dp.message_handler(text="Gif")
async def send_welcome(message: types.Message):
      
    await message.answer_animation("https://t.me/tannus8002/3")



@dp.message_handler(text="vidionote")
async def send_welcome(message: types.Message):
      
    await message.answer_video("")



















