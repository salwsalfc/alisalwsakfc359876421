# ported from paperplaneExtended by avinashreddy3108 for media support
from telethon import events
from telethon.utils import get_display_name

from sbb_b import sbb_b
from sbb_b.core.logger import logging

from ..core.managers import edit_or_reply
from ..sql_helper.globals import gvarstatus
from ..sql_helper.welcome_sql import (
    add_welcome_setting,
    get_current_welcome_settings,
    rm_welcome_setting,
    update_previous_welcome,
)
from . import BOTLOG_CHATID

LOGS = logging.getLogger(__name__)


@sbb_b.on(events.ChatAction)
async def _(event):  # sourcery no-metrics  # sourcery skip: low-code-quality
    cws = get_current_welcome_settings(event.chat_id)
    if (
        cws
        and (event.user_joined or event.user_added)
        and not (await event.get_user()).bot
    ):
        if gvarstatus("clean_welcome") is None:
            try:
                await event.client.delete_messages(event.chat_id, cws.previous_welcome)
            except Exception as e:
                LOGS.warn(str(e))
        a_user = await event.get_user()
        chat = await event.get_chat()
        me = await event.client.get_me()
        title = get_display_name(await event.get_chat()) or "هذه الدردشة"
        participants = await event.client.get_participants(chat)
        count = len(participants)
        mention = f"<a href='tg://user?id={a_user.id}'>{a_user.first_name}</a>"
        my_mention = f"<a href='tg://user?id={me.id}'>{me.first_name}</a>"
        first = a_user.first_name
        last = a_user.last_name
        fullname = f"{first} {last}" if last else first
        username = f"@{a_user.username}" if a_user.username else mention
        userid = a_user.id
        my_first = me.first_name
        my_last = me.last_name
        my_fullname = f"{my_first} {my_last}" if my_last else my_first
        my_username = f"@{me.username}" if me.username else my_mention
        file_media = None
        current_saved_welcome_message = None
        if cws:
            if cws.f_mesg_id:
                msg_o = await event.client.get_messages(
                    entity=BOTLOG_CHATID, ids=int(cws.f_mesg_id)
                )
                file_media = msg_o.media
                current_saved_welcome_message = msg_o.message
                link_preview = True
            elif cws.reply:
                current_saved_welcome_message = cws.reply
                link_preview = False
        current_message = await event.reply(
            current_saved_welcome_message.format(
                mention=mention,
                title=title,
                count=count,
                first=first,
                last=last,
                fullname=fullname,
                username=username,
                userid=userid,
                my_first=my_first,
                my_last=my_last,
                my_fullname=my_fullname,
                my_username=my_username,
                my_mention=my_mention,
            ),
            file=file_media,
            parse_mode="html",
            link_preview=link_preview,
        )
        update_previous_welcome(event.chat_id, current_message.id)


@sbb_b.ar_cmd(pattern="ترحيب(?:\s|$)([\s\S]𓆘)")
async def save_welcome(event):
    msg = await event.get_reply_message()
    string = "".join(event.text.split(maxsplit=1)[1:])
    msg_id = None
    if msg and msg.media and not string:
        if BOTLOG_CHATID:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"اضافة ترحيب:\
                \nايدي الدردشة: {event.chat_id}\
                \nالترحيب التالي تم حفظه الى الدردشة : {get_display_name(await event.get_chat())} لا تحذف هذه الرسالة نهائيا !!",
            )
            msg_o = await event.client.forward_messages(
                entity=BOTLOG_CHATID, messages=msg, from_peer=event.chat_id, silent=True
            )
            msg_id = msg_o.id
        else:
            return await edit_or_reply(
                event,
                "يجب عليك تعيين فار كروب الحفظ اولا ",
            )
    elif event.reply_to_msg_id and not string:
        rep_msg = await event.get_reply_message()
        string = rep_msg.text
    success = "𓆘𓆘- تم بنجاح {} لهذه المجموعة𓆘𓆘"
    if add_welcome_setting(event.chat_id, 0, string, msg_id) is True:
        return await edit_or_reply(event, success.format("حفظ الترحيب"))
    rm_welcome_setting(event.chat_id)
    if add_welcome_setting(event.chat_id, 0, string, msg_id) is True:
        return await edit_or_reply(event, success.format("تحديث الترحيب"))
    await edit_or_reply("- لقد حدث خطأ اثناء وضع الترحيب لهذه الدردشة")


@sbb_b.ar_cmd(pattern="حذف الترحيبات$")
async def del_welcome(event):
    if rm_welcome_setting(event.chat_id) is True:
        await edit_or_reply(event, "𓆘𓆘- تم حذف جميع رسائل الترحيب المضافة𓆘𓆘")
    else:
        await edit_or_reply(event, "𓆘𓆘- ليس لديك اي رسائل ترحيب هن بالاصل𓆘𓆘")


@sbb_b.ar_cmd(pattern="الترحيبات$")
async def show_welcome(event):
    cws = get_current_welcome_settings(event.chat_id)
    if not cws:
        return await edit_or_reply(event, "𓆘𓆘- لا توجد اي رسائل ترحيب هنا اصلا𓆘𓆘")
    if cws.f_mesg_id:
        msg_o = await event.client.get_messages(
            entity=BOTLOG_CHATID, ids=int(cws.f_mesg_id)
        )
        await edit_or_reply(event, "𓆘𓆘- رسالة الترحيب الحالية هي:𓆘𓆘")
        await event.reply(msg_o.message, file=msg_o.media)
    elif cws.reply:
        await edit_or_reply(event, "𓆘𓆘- رسالة الترحيب الحالية هي:𓆘𓆘")
        await event.reply(cws.reply, link_preview=False)
