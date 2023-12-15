import re

from telethon.utils import get_display_name

from sbb_b import sbb_b

from ..core.managers import edit_or_reply
from ..sql_helper import blacklist_sql as sql
from ..utils import is_admin
from . import BOTLOG_CHATID


@sbb_b.ar_cmd(incoming=True, groups_only=True)
async def on_new_message(event):
    name = event.raw_text
    snips = sql.get_chat_blacklist(event.chat_id)
    jmthonadmin = await is_admin(event.client, event.chat_id, event.client.uid)
    if not jmthonadmin:
        return
    for snip in snips:
        pattern = f"( |^|[^\\w]){re.escape(snip)}( |$|[^\\w])"
        if re.search(pattern, name, flags=re.IGNORECASE):
            try:
                await event.delete()
            except Exception:
                await event.client.send_message(
                    BOTLOG_CHATID,
                    f"𓆘𓆘⌔∮ عذرًا ليست لدي صلاحية في {get_display_name(await event.get_chat())}.\nلذا سيتم إزالة الكلمات الممنوعة من هذه المجموعة𓆘𓆘",
                )
                for word in snips:
                    sql.rm_from_blacklist(event.chat_id, word.lower())
            break


@sbb_b.ar_cmd(
    pattern="منع(?:\s|$)([\s\S]𓆘)",
    require_admin=True,
)
async def _(event):
    text = event.pattern_match.group(1)
    to_blacklist = list(
        {trigger.strip() for trigger in text.split("\n") if trigger.strip()}
    )

    for trigger in to_blacklist:
        sql.add_to_blacklist(event.chat_id, trigger.lower())
    await edit_or_reply(
        event,
        f"𓆘𓆘- تم اضافة {len(to_blacklist)} الى قائمة المنع في هذه الدردشة𓆘𓆘",
    )


@sbb_b.ar_cmd(
    pattern="rmblacklist(?:\s|$)([\s\S]𓆘)",
    require_admin=True,
)
async def _(event):
    text = event.pattern_match.group(1)
    to_unblacklist = list(
        {trigger.strip() for trigger in text.split("\n") if trigger.strip()}
    )
    successful = sum(
        bool(sql.rm_from_blacklist(event.chat_id, trigger.lower()))
        for trigger in to_unblacklist
    )
    await edit_or_reply(
        event, f"تم حذف {successful} / {len(to_unblacklist)} من قائمة المنع"
    )


@sbb_b.ar_cmd(
    pattern="قائمة المنع$",
    require_admin=True,
)
async def _(event):
    all_blacklisted = sql.get_chat_blacklist(event.chat_id)
    OUT_STR = "قائمة المنع والكلمات الممنوعة في هذه الدردشة::\n"
    if len(all_blacklisted) > 0:
        for trigger in all_blacklisted:
            OUT_STR += f"- {trigger} \n"
    else:
        OUT_STR = "𓆘𓆘- يبدو انه لم يتم اضافة اي كلمات ممنوعة𓆘𓆘"
    await edit_or_reply(event, OUT_STR)
