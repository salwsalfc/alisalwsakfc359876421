import asyncio

from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChatBannedRights

from ..sql_helper import antiflood_sql as sql
from ..utils import is_admin
from . import edit_or_reply, sbb_b

CHAT_FLOOD = sql.__load_flood_settings()

ANTI_FLOOD_WARN_MODE = ChatBannedRights(
    until_date=None, view_messages=None, send_messages=True
)


@sbb_b.ar_cmd(incoming=True, groups_only=True)
async def _(event):
    if not CHAT_FLOOD:
        return
    jmthonadmin = await is_admin(event.client, event.chat_id, event.client.uid)
    if not jmthonadmin:
        return
    if str(event.chat_id) not in CHAT_FLOOD:
        return
    should_ban = sql.update_flood(event.chat_id, event.message.sender_id)
    if not should_ban:
        return
    try:
        await event.client(
            EditBannedRequest(
                event.chat_id, event.message.sender_id, ANTI_FLOOD_WARN_MODE
            )
        )
    except Exception as e:
        no_admin_privilege_message = await event.client.send_message(
            entity=event.chat_id,
            message=f"𓆘𓆘⌔∮ تنبيه التكرار للادمنية ⚠️𓆘𓆘\n\n𓆘𓆘▾∮ الى𓆘𓆘 @admin 𓆘𓆘المجموعة!𓆘𓆘\n𓆘𓆘▾∮ قام↫𓆘𓆘 [المستخدم](tg://user?id={event.message.sender_id})\n𓆘𓆘▾∮بتكرار رسائله في المجموعة𓆘𓆘\x1f`{e}`",
            reply_to=event.message.id,
        )

        await asyncio.sleep(4)
        await no_admin_privilege_message.edit(
            "𓆘𓆘⌔∮هذا هو الشخص الذي قام بالتكرار \n توقف لكي لا تًطرد 📵𓆘𓆘"
        )
    else:
        await event.client.send_message(
            entity=event.chat_id,
            message=f"𓆘𓆘⌔∮ عملية التقيد التلقائي للتكرار ⚠️𓆘𓆘\n\n𓆘𓆘▾ قام ↫𓆘𓆘[المستخدم ](tg://user?id={event.message.sender_id})\n𓆘𓆘▾∮تم تقييده تلقائيًا بسبب عبوره حد السماح بالتكرار في هذه المجموعة𓆘𓆘",
            reply_to=event.message.id,
        )


@sbb_b.ar_cmd(
    pattern="ضع التكرار(?:\s|$)([\s\S]𓆘)",
    groups_only=True,
    require_admin=True,
)
async def _(event):
    input_str = event.pattern_match.group(1)
    event = await edit_or_reply(event, "𓆘𓆘▿∲ تم بنجاح تحديث عدد التكرار𓆘𓆘")
    await asyncio.sleep(2)
    try:
        sql.set_flood(event.chat_id, input_str)
        sql.__load_flood_settings()
        await event.edit(f"𓆘𓆘▿∲ تم تحديث التكرار الى {input_str} في الدردشة الحالية𓆘𓆘")
    except Exception as e:
        await event.edit(str(e))
