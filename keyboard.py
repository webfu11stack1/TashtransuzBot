from aiogram.types.reply_keyboard import ReplyKeyboardMarkup
import json
def tuman_kb(tuman):
    with open("b.json","r") as f:
        raqamlar=json.load(f)
    buttons=[]
    for i in dict(raqamlar[tuman]).keys():
        buttons.append([i])
    key=ReplyKeyboardMarkup(buttons,resize_keyboard=True,row_width=1)
    return key