import json
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types.inline_keyboard import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import Message
from aiogram.types.reply_keyboard import ReplyKeyboardMarkup,ReplyKeyboardRemove
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram import types
import urllib.parse
from keyboard import *



logging.basicConfig(level=logging.INFO)

bot_token = ""
bot = Bot(token=bot_token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands=["start"],state="*")
@dp.message_handler(text="<<Ortga",state="tuman")
async def process_location(message: types.Message, state: FSMContext):

    til_kb=ReplyKeyboardMarkup(
        keyboard=[
           ["🇺🇿Uzb","🇷🇺Rus"]
           
        ],
        resize_keyboard=True
    )
    # await message.answer(f"Sizning manzilingiz: {address.address}")
    await message.answer("Assalomu alaykum, Botga Xush kelibsiz! \n\n⬇️Kerakli tilni tanlang⬇️",reply_markup=til_kb)
    await state.set_state("tuman")

    
@dp.message_handler(text="🇺🇿Uzb",state="*")
async def uzbtil(message:Message,state:FSMContext):
    rp_kb=ReplyKeyboardMarkup(
        keyboard=[
           ["🔍Tumanlar bo'yicha qidirish"],
           ["🔍Yo'nalishlar bo'yicha qidirish"],
           ["Ortga"]
        ],
        resize_keyboard=True
    )
    await message.answer("⬇️Kerakli xizmatlarni tanlang⬇️",reply_markup=rp_kb)
    await state.set_state("uzb")

@dp.message_handler(text="Ortga",state="*")
async def ort(message:Message,state:FSMContext):
    til_kb=ReplyKeyboardMarkup(
        keyboard=[
           ["🇺🇿Uzb","🇷🇺Rus"]
           
        ],
        resize_keyboard=True
    )
    await message.answer("Ortga",reply_markup=til_kb)

@dp.message_handler(text="🇷🇺Rus",state="*")
async def uzbtil(message:Message,state:FSMContext):
    rp_kb=ReplyKeyboardMarkup(
        keyboard=[
           ["🔍Поиск по направлениям"],
           ["Назад"]
        ],
        resize_keyboard=True
    )
    await message.answer("⬇️Kerakli xizmatlarni tanlang⬇️",reply_markup=rp_kb)
    await state.set_state("til")
   
@dp.message_handler(text="Назад",state="*")
async def rustil(message:Message,state:FSMContext):
    til_kb=ReplyKeyboardMarkup(
        keyboard=[
           ["🇺🇿Uzb","🇷🇺Rus"]
           
        ],
        resize_keyboard=True
    )
    await message.answer("Назад",reply_markup=til_kb)

@dp.message_handler(text="🔍Поиск по направлениям",state="*")
async def process_textt(message: types.Message, state: FSMContext):
        inl = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="🔍Поиск", switch_inline_query_current_chat="")]
        ], row_width=2)

        await message.answer(f"Нажмите кнопку\n<b>Поиск</b> для поиска автобусных маршрутов⬇️",
                             reply_markup=inl, parse_mode='HTML')
        await state.set_state("rus")
        




with open('r.json', "rb") as file:
    data = json.load(file)

async def search_data(query):
    results = []
    for district, routes in data.items():
        for route_name, route_details in routes.items():
            if query.lower() in route_name.lower():
                route_details_text = "\n".join(route_details)
                results.append(f"{route_name}\n\n{route_details_text}")
    return results

@dp.inline_handler(state="rus")
async def inline_query_handler(query: types.InlineQuery):
    query_text = query.query
    results = await search_data(query_text)

    inline_results = [
        types.InlineQueryResultArticle(
            id=str(index),
            title=result.split('\n\n')[0],
            input_message_content=types.InputTextMessageContent(result),
        )
        for index, result in enumerate(results)
    ]

    await bot.answer_inline_query(query.id, inline_results)


@dp.message_handler(text="🔍Tumanlar bo'yicha qidirish",state="*")
async def process_text(message: types.Message, state: FSMContext):
    
        inline = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="1️⃣-Tuman", callback_data="1-tuman"),
                 InlineKeyboardButton(text="2️⃣-Tuman", callback_data="2-tuman"),
                 InlineKeyboardButton(text="3️⃣-Tuman", callback_data="3-tuman")],

                [InlineKeyboardButton(text="4️⃣-Tuman", callback_data="4-tuman"),
                 InlineKeyboardButton(text="5️⃣-Tuman", callback_data="5-tuman"),
                 InlineKeyboardButton(text="6️⃣-Tuman", callback_data="6-tuman")],

                [InlineKeyboardButton(text="7️⃣-Tuman", callback_data="7-tuman"),
                 InlineKeyboardButton(text="8️⃣-Tuman", callback_data="8-tuman")]

                
            ],
            row_width=2
        )
        await state.set_state("tuman")
        await message.answer("👇Kerakli tugmani tanlang👇", reply_markup=inline)


@dp.message_handler(text="🔍Yo'nalishlar bo'yicha qidirish",state="*")
async def process_textt(message: types.Message, state: FSMContext):
        inl = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="🔍Qidirish", switch_inline_query_current_chat="")]
        ], row_width=2)

        await message.answer(f"Avtobus yonalishlarini qidirish uchun\n<b>Qidirish</b> tugmasini bosing⬇️",
                             reply_markup=inl, parse_mode='HTML')
        await state.set_state("start")
        




with open('c.json', "rb") as file:
    data = json.load(file)

async def search_data(query):
    results = []
    for district, routes in data.items():
        for route_name, route_details in routes.items():
            if query.lower() in route_name.lower():
                route_details_text = "\n".join(route_details)
                results.append(f"{route_name}\n\n{route_details_text}")
    return results

@dp.inline_handler(state="start")
async def inline_query_handler(query: types.InlineQuery):
    query_text = query.query
    results = await search_data(query_text)

    inline_results = [
        types.InlineQueryResultArticle(
            id=str(index),
            title=result.split('\n\n')[0],
            input_message_content=types.InputTextMessageContent(result),
        )
        for index, result in enumerate(results)
    ]

    await bot.answer_inline_query(query.id, inline_results)


@dp.callback_query_handler(state="*")
async def tuman_callback_handler1(query: types.CallbackQuery, state: FSMContext):
    await query.message.answer("👇Avtobuslar raqamini bilish uchun kerakli yonalishni tanlang👇", reply_markup=tuman_kb(query.data))
    await state.set_state("tuman")
    await state.update_data(bulim=query.data)

@dp.message_handler(state="*")
async def bolim_info(message:Message,state:FSMContext):
    
    
    text=message.text
    data=await state.get_data()
    bulim=data["bulim"]
    with open("b.json","r") as f:
        info=json.load(f)
    if text in info[bulim].keys():
        global malumot
        malumot=info[bulim][text]
        if text in ["Tibbiyot Akademiyasi-Xamza tizimi. kollej", "TTZ -Yangiobod massivi", "'Chorsu' savdo markazi -'Food City' bozori", "4-metro bekati -Xonobod ko'chasi", "Do'stlik-2 massivi -'Food City' bozori", "O'rikzor bozori -Food City bozori", "Sergeli-10 massivi -Sp. Zangiota klinikasi", "Olmazor metrosi -Yangiyo'l (dehqon bozori)", "Kuylyuk-1 massivi -Binokor posyolkasi"]:

            await message.answer(malumot[0])

        elif text in ["<<Ortga"]:
            rl_kb = ReplyKeyboardMarkup(
        keyboard=[
            ["🔍Tumanlar bo'yicha qidirish"],
            ["🔍Yo'nalishlar bo'yicha qidirish"],
            # ["Tilni o'zgatirish"]
        ],
        resize_keyboard=True
    )

            await message.answer("⬇️Kerakli xizmatlarni tanlang⬇️", reply_markup=rl_kb) 
        else:
            await message.answer_photo(photo=malumot[1],caption=malumot[0]) 
            
        location_url = info[bulim][text][2]
        decoded_url = urllib.parse.unquote(location_url)
        inline_kuzatish=InlineKeyboardMarkup(
        inline_keyboard=[
           [InlineKeyboardButton(text="Avtobus harakatini kuzatish👀",url=decoded_url)]
       ],
        row_width=2
   )
        
        await message.answer("⬇️ Avtobus harakatini kuzatish uchun tugmani bosing ⬇️", reply_markup=inline_kuzatish)
        await state.set_state("yonal")



async def start_bot():
    await dp.start_polling()

if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    loop.create_task(start_bot())
    loop.run_forever()
