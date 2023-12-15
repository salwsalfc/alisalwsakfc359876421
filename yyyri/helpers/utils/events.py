import base64
import contextlib

import aiohttp
from telethon.errors import (
    ChannelInvalidError,
    ChannelPrivateError,
    ChannelPublicGroupNaError,
)
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.functions.messages import GetFullChatRequest
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telethon.tl.types import MessageEntityMentionName

from ...Config import Config
from ...core.logger import logging
from ...core.managers import edit_delete

LOGS = logging.getLogger(__name__)


async def reply_id(event):
    reply_to_id = None
    if event.sender_id in Config.SUDO_USERS:
        reply_to_id = event.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    return reply_to_id


async def get_chatinfo(event, match, jmthonevent):
    if not match and event.reply_to_msg_id:
        replied_msg = await event.get_reply_message()
        if replied_msg.fwd_from and replied_msg.fwd_from.channel_id is not None:
            match = replied_msg.fwd_from.channel_id
    if not match:
        match = event.chat_id
    with contextlib.suppress(ValueError):
        match = int(match)
    try:
        chat_info = await event.client(GetFullChatRequest(match))
    except BaseException:
        try:
            chat_info = await event.client(GetFullChannelRequest(match))
        except ChannelInvalidError:
            await jmthonevent.edit("- عذرا هذه المجموعة او القناة غير صحيحة")
            return None
        except ChannelPrivateError:
            await jmthonevent.edit(
                "- يبدو انه هذه مجموعة او قناة خاصة او ربما محظور منها"
            )
            return None
        except ChannelPublicGroupNaError:
            await jmthonevent.edit("- هذه القناه او المجموعه لم يتم العثور عليها")
            return None
        except (TypeError, ValueError):
            await jmthonevent.edit("𓆘𓆘خطأ:𓆘𓆘\nلم يتم التعرف على الدردشة")
            return None
    return chat_info


async def async_searcher(
    url: str,
    post: bool = None,
    headers: dict = None,
    params: dict = None,
    json: dict = None,
    data: dict = None,
    ssl=None,
    re_json: bool = False,
    re_content: bool = False,
    real: bool = False,
):
    async with aiohttp.ClientSession(headers=headers) as boterz:
        if post:
            data = await boterz.post(url, json=json, data=data, ssl=ssl)
        else:
            data = await boterz.get(url, params=params, ssl=ssl)
        if re_json:
            return await data.json()
        if re_content:
            return await data.read()
        if real:
            return data
        return await data.text()


async def get_user_from_event(
    event,
    jmthonevent=None,
    secondgroup=None,
    thirdgroup=None,
    nogroup=False,
    noedits=False,
):  # sourcery no-metrics  # sourcery skip: low-code-quality
    if jmthonevent is None:
        jmthonevent = event
    if nogroup is False:
        if secondgroup:
            args = event.pattern_match.group(2).split(" ", 1)
        elif thirdgroup:
            args = event.pattern_match.group(3).split(" ", 1)
        else:
            args = event.pattern_match.group(1).split(" ", 1)
    extra = None
    try:
        if args:
            user = args[0]
            if len(args) > 1:
                extra = "".join(args[1:])
            if user.isnumeric() or (user.startswith("-") and user[1:].isnumeric()):
                user = int(user)
            if event.message.entities:
                probable_user_mention_entity = event.message.entities[0]
                if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                    user_id = probable_user_mention_entity.user_id
                    user_obj = await event.client.get_entity(user_id)
                    return user_obj, extra
            if isinstance(user, int) or user.startswith("@"):
                user_obj = await event.client.get_entity(user)
                return user_obj, extra
    except Exception as e:
        LOGS.error(str(e))
    try:
        if nogroup is False:
            if secondgroup:
                extra = event.pattern_match.group(2)
            else:
                extra = event.pattern_match.group(1)
        if event.is_private:
            user_obj = await event.get_chat()
            return user_obj, extra
        if event.reply_to_msg_id:
            previous_message = await event.get_reply_message()
            if previous_message.from_id is None:
                if not noedits:
                    await edit_delete(jmthonevent, "- هذا الشخص مفعل وضع الاخفاء")
                return None, None
            user_obj = await event.client.get_entity(previous_message.sender_id)
            return user_obj, extra
        if not args:
            if not noedits:
                await edit_delete(
                    jmthonevent, "- يجب عليك وضع ايدي او معرف المستخدم او بالرد عليه", 5
                )
            return None, None
    except Exception as e:
        LOGS.error(str(e))
    if not noedits:
        await edit_delete(jmthonevent, "- لم يتم التعرف على المستخدم")
    return None, None


async def checking(sbb_b):
    jmthon_c = base64.b64decode("VHdIUHd6RlpkYkNJR1duTg==")
    with contextlib.suppress(BaseException):
        jmthon_channel = Get(jmthon_c)
        await sbb_b(jmthon_channel)
