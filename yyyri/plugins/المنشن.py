from telethon.tl.types import ChannelParticipantsAdmins

from sbb_b import sbb_b

from ..helpers.utils import get_user_from_event, reply_id


@sbb_b.ar_cmd(pattern="(تاك للكل|للكل)(?:\s|$)([\s\S]𓆘)")
async def _(event):
    reply_to_id = await reply_id(event)
    input_str = event.pattern_match.group(2)
    mentions = input_str or "@all"
    chat = await event.get_input_chat()
    async for x in event.client.iter_participants(chat, 100):
        mentions += f" \n- [{x.first_name}](tg://user?id={x.id})"  # [\u2063]
    await event.client.send_message(event.chat_id, mentions, reply_to=reply_to_id)
    await event.delete()


@sbb_b.ar_cmd(pattern="تبليغ$")
async def _(event):
    mentions = "▿∲ انتباه الى المشرفين تم تبليغكم \n@admin"
    chat = await event.get_input_chat()
    reply_to_id = await reply_id(event)
    async for x in event.client.iter_participants(
        chat, filter=ChannelParticipantsAdmins
    ):
        if not x.bot:
            mentions += f"[\u2063](tg://user?id={x.id})"
    await event.client.send_message(event.chat_id, mentions, reply_to=reply_to_id)
    await event.delete()


@sbb_b.ar_cmd(pattern="منشن ([\s\S]𓆘)")
async def _(event):
    user, input_str = await get_user_from_event(event)
    if not user:
        return
    reply_to_id = await reply_id(event)
    await event.delete()
    await event.client.send_message(
        event.chat_id,
        f"<a href='tg://user?id={user.id}'>{input_str}</a>",
        parse_mode="HTML",
        reply_to=reply_to_id,
    )
