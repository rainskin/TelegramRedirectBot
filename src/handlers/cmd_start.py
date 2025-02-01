from aiogram import types
from aiogram.filters import CommandObject, CommandStart
from aiogram.utils.deep_linking import decode_payload

from db import users, service, ref_links
from loader import dp


@dp.message(CommandStart(deep_link=True))
async def _(msg: types.Message, command: CommandObject):
    args = command.args

    full_name = msg.from_user.full_name
    username = msg.from_user.username
    user_id = msg.from_user.id

    welcome_text = service.get_welcome_text()

    if not users.is_new(user_id):
        return

    if args:
        ref_links.register_or_create_tag(args)

    users.add(full_name, username, user_id)

    if welcome_text:
        await msg.answer(welcome_text)


@dp.message(CommandStart)
async def _(msg: types.Message):
    full_name = msg.from_user.full_name
    username = msg.from_user.username
    user_id = msg.from_user.id

    welcome_text = service.get_welcome_text()

    if not users.is_new(user_id):
        return

    users.add(full_name, username, user_id)

    if welcome_text:
        await msg.answer(welcome_text)
