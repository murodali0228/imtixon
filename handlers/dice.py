from aiogram import types,Router

rt = Router()

@rt.message()
async def dice(msg: types.Message):
    if msg.dice:
        if msg.dice.emoji == "🎲":
            n = "tosh qiymati:"
            n+= f"{msg.dice.value} tushadi !!!"
            await msg.answer(n)

        elif msg.dice.emoji == "🎳":
            n = "shuncha bovling :"
            n += f"{msg.dice.value} yiqiladi !!!"
            await msg.answer(n)
        elif msg.dice.emoji == "🎯":
            n = f"{msg.dice.value} ga tushadi !!!"
            await msg.answer(n)




