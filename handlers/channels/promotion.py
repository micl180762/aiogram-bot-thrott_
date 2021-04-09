from aiogram.dispatcher.filters import Command
from filters.forvarded_message import IsForvarded
from keyboards.inline.subscription import check_button
from loader import dp, bot
from aiogram import types
from data.config import channels
from aiogram.types import CallbackQuery


# если канал закрытый - username нет, только ссылка по которой можно пригласить
@dp.message_handler(IsForvarded(), content_types=types.ContentType.ANY)
async def get_channel_info(message: types.Message):
    # await message.answer(f'Message from channel {message.forward_from_chat.title}\n'
    #                      f'username: @{message.forward_from_chat.full_name}\n'
    #                      f'ID: {message.forward_from_chat.id}')
    await message.answer(f'Message from channel {message.forward_from_chat.title}\n')


@dp.message_handler(Command('channels'))
async def show_channels(message: types.Message):
    channels_format = str()
    for channel_id_or_username in channels:
        chat = await bot.get_chat(channel_id_or_username)
        invite_link = await chat.export_invite_link()
        channels_format += f"canal <a href= '{invite_link}'>{chat.title}</a>\n"
    await message.answer(f"you can to suscr: \n"
                         f"{channels_format}",
                         reply_markup=check_button,
                         disable_web_page_preview=True, parse_mode=types.ParseMode.HTML)


@dp.callback_query_handler(text='check_subs')
async def checker(call: CallbackQuery):
    await call.answer()
