from telethon.tl import functions

from .. import sbb_b
from ..Config import Config
from ..core.managers import edit_delete, edit_or_reply
from ..utils.tools import create_supergroup


@sbb_b.ar_cmd(pattern="صنع (مجموعة خارقة|مجموعة عادية|قناة) ([\s\S]𓆘)")
async def _(event):
    type_of_group = event.pattern_match.group(1)
    group_name = event.pattern_match.group(2)
    if type_of_group == "قناة":
        descript = "تم صنع هذه القناة بواسطة سورس الفراعنة "
    else:
        descript = "تم صنع المجموعة باستخدام سورس الفراعنة "
    if type_of_group == "مجموعة عادية":
        try:
            result = await event.client(
                functions.messages.CreateChatRequest(
                    users=[Config.TG_BOT_USERNAME],
                    title=group_name,
                )
            )
            created_chat_id = result.chats[0].id
            result = await event.client(
                functions.messages.ExportChatInviteRequest(
                    peer=created_chat_id,
                )
            )
            await edit_or_reply(
                event, f"𓆘𓆘- المجموعة `{group_name}` تم بنجاح صنعها {result.link}𓆘𓆘"
            )
        except Exception as e:
            await edit_delete(event, f"𓆘𓆘Error:𓆘𓆘\n{str(e)}")
    elif type_of_group == "قناة":
        try:
            r = await event.client(
                functions.channels.CreateChannelRequest(
                    title=group_name,
                    about=descript,
                    megagroup=False,
                )
            )
            created_chat_id = r.chats[0].id
            result = await event.client(
                functions.messages.ExportChatInviteRequest(
                    peer=created_chat_id,
                )
            )
            await edit_or_reply(
                event, f"𓆘𓆘- القناة {group_name} تم بنجاح صنعها {result.link}𓆘𓆘"
            )
        except Exception as e:
            await edit_delete(event, f"𓆘𓆘Error:𓆘𓆘\n{e}")
    elif type_of_group == "مجموعة خارقة":
        answer = await create_supergroup(
            group_name, event.client, Config.TG_BOT_USERNAME, descript
        )
        if answer[0] != "error":
            await edit_or_reply(
                event,
                f"تم صنع المجموعة `{group_name}` بنجاح الرابط الرابط: {answer[0].link}",
            )
        else:
            await edit_delete(event, f"𓆘𓆘خطأ:𓆘𓆘\n{answer[1]}")
    else:
        await edit_delete(event, "استخدم الامر بشكل صحيح")
